import requests
import pandas as pd 
import time
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import random
from dateutil.relativedelta import relativedelta
import datetime
from bs4 import BeautifulSoup 
from lxml import etree
import pyodbc
from dotenv import dotenv_values
import urllib.parse

config = dotenv_values('.env')
SERVER = config['DB_SERVER_SGA']
DATABASE = config['DB_DATABASE_SGA_TIBDB']
USERNAME = config['DB_USERNAME_SGA']
PASSWORD = config['DB_PASSWORD_SGA']
TOKEN = config['SCRAPE_DO_TOKEN']

#PAGE = 1
BASE_URL = "https://modhotel.com/personel.asp?page="


HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
}

company_list =[]
position_list =[]
publish_date_list = []
job_location_list = []
clean_publish_date = []


for page in range(1,90):
  print(f"{page}. Sayfayı geziyor. ")
  url = BASE_URL + str(page)
  encoded_full_url = urllib.parse.quote(url)
  api_url = f"http://api.scrape.do/?token={TOKEN}&url={encoded_full_url}"

  try:
      response = requests.request('GET', api_url, headers=HEADERS, timeout=70)
  except:
    continue
  soup = BeautifulSoup(response.content, 'lxml')
  dom = etree.HTML(str(soup))
  try:
    company_name_temp = dom.xpath("//div[@class='trow jobrow']//div[@data-title = 'İşletme Adı']/text()")
    company_list.extend(company_name_temp)
  except:
    _company_name = ''
    company_name_temp = [_company_name for i in range(0,25)]
    company_list.extend(company_name_temp)
  try:
    position_temp = dom.xpath("//div[@class='trow jobrow']//div[@data-title = 'Pozisyon']/text()")
    position_list.extend(position_temp)
  except:
    _position_name = ''
    position_temp = [_position_name for i in range(0,25)]
    position_list.extend(position_temp)
  try:
    job_location_temp = dom.xpath("//div[@class='trow jobrow']//div[@data-title = 'Yer']/text()")
    job_location_list.extend(job_location_temp)

  except:
    _job_name = ''
    job_location_temp = [_job_name for i in range(0,25)]
    job_location_list.extend(job_location_temp)

  try:
    publish_date_temp = dom.xpath("//div[@class='trow jobrow']//div[@data-title = 'Tarih']/text()")
    publish_date_list.extend(publish_date_temp)
  except:
    publish_date_temp = ['' for i in range(0,25)]
    publish_date_list.extend(publish_date_temp)
  



def date_cleaner(arr):
  if arr == "Bugün":
    pubdate = datetime.datetime.today().strftime("%Y-%m-%d")
    return pubdate
  elif len(arr) == 0:
    pubdate = arr
    return pubdate
  else:
    date = arr.split(".")
    day=date[0]
    year=date[2]
    month = date[1]
    pubdate=year+'-'+month+'-'+day
    return pubdate




def DataCleaner(data_list):
  clean_data_list = []
  for data in data_list:
      corrected = data.replace("\r\n","").strip()
      clean_data_list.append(corrected)
  return clean_data_list


company_list = DataCleaner(company_list)
position_list = DataCleaner(position_list)
job_location_list = DataCleaner(job_location_list)
clean_publish_date = [date_cleaner(date) for date in DataCleaner(publish_date_list)]

job_dict = {
    "CompanyName":company_list,
    "Position":position_list,
    "JobLocation":job_location_list,
    "PublishDate":clean_publish_date,
}



# dataframe dönüştürme konusunda hata aldığımız için aşağıdaki blok ile çözüm bulduk.
# #############################################################
def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if  ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list
# #############################################################

job_dict_corrected = pad_dict_list(job_dict,'')


df = pd.DataFrame().from_dict(job_dict_corrected)
df_unneccessary_values = df[ df['Position'] == '' ] # Step 1
df = df.drop(df_unneccessary_values.index, axis=0) # Step 2

df = df[df["PublishDate"] !='']

df["JobDefinition"] = ''
df["JobNo"] =  df['CompanyName'].str[:4] + df['Position'].str[:4] + df['JobLocation'].str[:4]
df["JobDetailUrl"] = BASE_URL



conn_str = f"Driver={'{SQL Server}'};Server={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
conn = pyodbc.connect(conn_str)
        
numofpost = len(df)
            
# Crawl başlangıç kaydı atıyor
cur = conn.cursor()
qry = ''' DELETE FROM Processler WHERE ProcesslerID 
IN
(SELECT  p.ProcesslerID FROM Processler p
LEFT JOIN ProcessInfos i on p.ProcesslerID = i.ProcessID
JOIN Siteler s on p.SiteId = s.SiteID
where s.siteId = 173 and convert(date,BaslangicZamani )= convert(date, getdate())) '''
cur.execute(qry)
cur.commit()
            
qry = ''' DECLARE @outputLastId INT EXEC InsertCrawlProcessInfo @siteId = 173, @lastId = @outputLastId OUTPUT SELECT @outputLastId AS LastId '''
cur.execute(qry)
cur.commit()
       
# Kayıtları eklyor
qry = '''INSERT INTO [modhotelcom] (CompanyName,Position,JobLocation,PublishDate,JobDefinition,JobNo,JobDetailURL) VALUES(?, ?, ?, ?, ?, ?, ?)'''
       
for index, row in df.iterrows():    
    param_values = list(row.values)
    cur.execute(qry, param_values)
    cur.commit()
                

cur = conn.cursor()
qry = " Update [modhotelcom] SET LastApplyDate=PublishDate+60, Jobtitle = Position"
cur.execute(qry)
cur.commit() 

# Crawl için açılan kaydın idsini alıyor.
cur = conn.cursor()
qry = '''SELECT ProcesslerID  FROM Processler where siteId = 173 AND BitisZamani is NULL ORDER BY BaslangicZamani DESC'''
cur.execute(qry)
results = []
columns = [column[0] for column in cur.description]
for row in cur.fetchall():
    results.append(dict(zip(columns, row)))
processid = results[0]["ProcesslerID"]
       
# Bitiş ve toplam çekileni ekliyor
qry = 'EXEC UpdateCrawlProcessInfo @processId = ' + str(processid) + ', @totalRowsCount =' + str(numofpost)
cur.execute(qry)
cur.commit()
       

cur = conn.cursor()
qry = 'EXEC TransferCrawlSiteData 173'
cur.execute(qry)
cur.commit()                


       
#Bağlantıyı kapıyor.
cur.close()
conn.close()
        

today = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
print(f"Df Aktarıldı !! - Tarih: {today}")



