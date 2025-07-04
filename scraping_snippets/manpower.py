import pandas as pd
import selenium
from bs4 import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import datetime
from selenium.webdriver.chrome.service import Service
import os
import pyodbc
from dotenv import dotenv_values
config = dotenv_values('.env')
SERVER = config['DB_SERVER_SGA']
DATABASE = config['DB_DATABASE_SGA_TIBDB']
USERNAME = config['DB_USERNAME_SGA']
PASSWORD = config['DB_PASSWORD_SGA']


HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
}
os.environ["HTTP_PROXY"] = "" 
os.environ["HTTPS_PROXY"] = ""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://is-ilanlari.manpower.com.tr/#/')
time.sleep(4)


job_count_parameter = driver.find_element(By.XPATH, "//div[@class='open-positions']/span").text.split(' ')[-1].replace('(','').replace(')','')
json_url = f'https://public-rest70.bullhornstaffing.com/rest-services/47YIPS/search/JobOrder?start=1&query=(isOpen:1)%20AND%20(isDeleted:0)%20AND%20(owner.departments.id:%221000005%22)&fields=id,title,publishedCategory(id,name),address(city,state,zip),employmentType,dateLastPublished,publicDescription,isOpen,isPublic,isDeleted,publishedZip,salary,salaryUnit&count={job_count_parameter}&sort=-dateLastPublished&showTotalMatched=true'
response = requests.get(json_url,headers=HEADERS)
response_json = response.json()


data = response_json['data']

temp_df = pd.DataFrame(data)



temp_df['JobLocation'] = temp_df['address'].apply(lambda x: x['state'])
temp_df['JobDetailUrl'] = temp_df['id'].apply(lambda x: 'https://is-ilanlari.manpower.com.tr/#/jobs/' + str(x))
temp_df['JobDefinition'] = temp_df['publicDescription'].str.replace(r'<[^<>]*>', '', regex=True)
temp_df['CompanyName'] = 'Manpower'
temp_df['JobArea'] = temp_df['publishedCategory'].apply(lambda x: x['name'].split(', ')[0])


df = temp_df[['id','title','JobDefinition','CompanyName','employmentType','JobDetailUrl','JobLocation','JobArea']]

df["JobDefinition"] = df["JobDefinition"].str.slice(0, 390, 1)



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
where s.siteId = 82 and convert(date,BaslangicZamani )= convert(date, getdate())) '''
cur.execute(qry)
cur.commit()
            
qry = ''' DECLARE @outputLastId INT EXEC InsertCrawlProcessInfo @siteId = 82, @lastId = @outputLastId OUTPUT SELECT @outputLastId AS LastId '''
cur.execute(qry)
cur.commit()
       
# Kayıtları eklyor
qry = '''INSERT INTO Manpower (JobNo,JobTitle,JobDefinition,CompanyName,Type,JobDetailURL,JobLocation,JobArea) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
       
for index, row in df.iterrows():    
    param_values = list(row.values)
    cur.execute(qry, param_values)
    cur.commit()
                

cur = conn.cursor()
qry = " Update [Manpower] SET LastApplyDate=PublishDate+90"
cur.execute(qry)
cur.commit() 

# Crawl için açılan kaydın idsini alıyor.
cur = conn.cursor()
qry = '''SELECT ProcesslerID  FROM Processler where siteId = 82 AND BitisZamani is NULL ORDER BY BaslangicZamani DESC'''
cur.execute(qry)
results = []
columns = [column[0] for column in cur.description]
for row in cur.fetchall():
    results.append(dict(zip(columns, row)))
processid = results[0]["ProcesslerID"]
       
# Bitiş ve toplam çekileni ekliyor
qry = 'EXEC UpdateCrawlProcessInfo @processId = ' + str(processid) + ', @totalRowsCount =' + str(job_count_parameter)
cur.execute(qry)
cur.commit()
       

cur = conn.cursor()
qry = 'EXEC TransferCrawlSiteData 82'
cur.execute(qry)
cur.commit()                


       
#Bağlantıyı kapıyor.
cur.close()
conn.close()
        

driver.quit()

print('Df Aktarldı !')