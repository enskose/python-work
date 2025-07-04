import pandas as pd
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from lxml import etree
import os
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)
import datetime
from dateutil import parser
from urllib.parse import urlparse
import re
import numpy as np
import pyodbc
from dotenv import dotenv_values
from datetime import datetime, timedelta
import urllib.parse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
config = dotenv_values('.env')
SERVER = config['DB_SERVER_SGA']
DATABASE = config['DB_DATABASE_SGA_TIBDB']
USERNAME = config['DB_USERNAME_SGA']
PASSWORD = config['DB_PASSWORD_SGA']
TOKEN = config['SCRAPE_DO_TOKEN']


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br"
}

base_url = f"https://www.iyibiris.com/is-ilanlari/&p="

succesful_req_count = 0
failed_req_count = 0
#Scrape do parametreleri
geoCode="tr"
superParam = "true"
customHeaders = "true"
render="true"

def get_joblinks():
    session = requests.Session()

    paging = True
    page = 1
    job_link_list = []

    while paging:
        page_url = f"https://www.iyibiris.com/is-ilanlari/&p={page}"
        print(f"Scrape ediliyor... {page_url}")
        final_url = base_url+str(page)
        encoded_full_url = urllib.parse.quote(final_url)
        api_url = f"http://api.scrape.do/?token={TOKEN}&url={encoded_full_url}&render={render}"

        max_retries = 3
        retry_count = 0
        success = False

        while retry_count < max_retries and not success:
            try:
                response = session.get(api_url, headers=HEADERS, timeout=60)
                response.raise_for_status()  # 4xx veya 5xx hata varsa Exception fırlatır

                success = True

                soup = BeautifulSoup(response.content, "lxml")
                dom = etree.HTML(str(soup))

                links_per_page = dom.xpath("//*[@id='resumes-content']/div/ul/li/a/@href")
                job_link_list.extend(links_per_page)

                last_page_xpath = dom.xpath("//*[@id='resumes-content']/div/div/nav/ul/li/span")[0].text
                last_page = last_page_xpath.split('/')[1]

            except requests.exceptions.RequestException as e:
                retry_count += 1
                print(f"[Deneme {retry_count}/{max_retries}] Hata alındı: {e}")
                if retry_count == max_retries:
                    print(f"Sayfa {page} için {max_retries} kez denendi, başarısız oldu. Atlanıyor...")
                continue

        if success:
            if page == int(last_page):
                paging = False
        else:

            pass

        page += 1

    return job_link_list

link_list = get_joblinks()
print(link_list)
print(len(link_list))
def get_data(links):
    global data
    global succesful_req_count
    global failed_req_count
    df=pd.DataFrame(columns=("JobTitle","Position","JobDefinition", "Qualifications", "Sector", "Type","JobLocation","PublishDate","CompanyName","JobDetailURL","JobNo","District"))
    id = 0
    for url in links:
        is_request_failed = True
        encoded_full_url = urllib.parse.quote(url)
        api_url = f"http://api.scrape.do/?token={TOKEN}&url={encoded_full_url}&render={render}"
        response = requests.get(api_url, headers=HEADERS, timeout=70)
        soup = BeautifulSoup(response.content, 'lxml')
        dom = etree.HTML(str(soup))
        try:
            JobTitle = dom.xpath("(//*[@id='content-area']/div/div[1]/h2/text())")
            JobTitle=' '.join(JobTitle).strip()
        except:
            JobTitle = ""
        try:
            label = soup.find('label', string='Pozisyon')
            if label:
                next_sibling = label.find_next_sibling('span')
                a_tag = next_sibling.find('a')
                Position=a_tag.text
            else:
                Position=None    
        except:
            Position = ""
        try:
          start_heading = soup.find('h4', string='İŞ TANIMI')

          if start_heading:
                content = []
                sibling = start_heading.find_next_sibling()
                while sibling and sibling.name != 'h4':
                    text = sibling.get_text(separator=' ', strip=True)
                    text=text.replace('*','')
                    text=text.replace('•','')
                    if text:
                        content.append(text)
                    sibling = sibling.find_next_sibling()
                result = ' '.join(content)
                JobDefinition = result
                
                if JobDefinition=='':
                    JobDefinition = None
                JobDefinition = JobDefinition[:4000] 
        except:
            JobDefinition = ""
        try:
         start_heading = soup.find('h4', string='ARANAN NİTELİKLER')

         if start_heading:
                content = []
                sibling = start_heading.find_next_sibling()
                while sibling and sibling.name != 'div':
                    text = sibling.get_text(separator=' ', strip=True)
                    text=text.replace('*','')
                    text=text.replace('•','')
                    if text:
                        content.append(text)
                    sibling = sibling.find_next_sibling()
                result = ' '.join(content)
                Qualifications = result
                
                if Qualifications=='':
                    Qualifications = None
                Qualifications = Qualifications[:4000] 
        except:
            Qualifications = ""

        try:
            label = soup.find('label', string='Sektör')
            if label:
                next_sibling = label.find_next_sibling('span')
                a_tag = next_sibling.find('a')
                Sector=a_tag.text
            else:
                Sector=None    
        except:
            Sector = "" 
        
        try:
            label = soup.find('label', string='Çalışma Şekli')
            if label:
                next_sibling = label.find_next_sibling('span')
                a_tag = next_sibling.find('a')
                Type=a_tag.text
            else:
                Type=None
        except:
            Type = ""
        try:
            label = soup.find('label', string='Çalışma Yeri')
            if label:
                next_sibling = label.find_next_sibling('span')
                a_tag = next_sibling.find('a')
                JobLocation=a_tag.text
                location_match = re.search(r' - (.+)', JobLocation)
                location = location_match.group(1).strip() 
                District = location
                JobLocation=JobLocation.split()[0]
            else:
                JobLocation=None     
        except:
            JobLocation = ""
        try:
            PublishDate = soup.select_one('#content-area > div > div.text-col > div.job_meta > strong.job_detail_dates')
            publish_date_text = PublishDate.get_text(strip=True)
            publish_date_text = publish_date_text.replace('\xa0', ' ')
            if publish_date_text == 'Bugün':
                parsed_date = datetime.now()
            elif publish_date_text == 'Dün':
                parsed_date = datetime.now() - timedelta(days=1)
            else:
                try:
                    parsed_date = parser.parse(publish_date_text, dayfirst=True)
                except ValueError as e:
                    parsed_date = None
            if parsed_date:
                formatted_date = parsed_date.strftime('%Y-%m-%d 00:00:00.000')
                PublishDate = formatted_date
        except:
            PublishDate = ""
        try:
            CompanyName = soup.select_one('#content-area > div > div.text-col > div.company_meta > span')
            CompanyName =CompanyName.find('a').text
        except:
            CompanyName = ""  
        try:
            JobDetailURL = url
        except:
            JobDetailURL = ""  
        try:
            path = urlparse(url).path
            segments = path.split('-')
            JobNo = segments[-1]
        except:
            JobNo = ""  
        df.loc[id] = (JobTitle,Position,JobDefinition,Qualifications, Sector, Type,JobLocation,PublishDate,CompanyName,JobDetailURL,JobNo,District)
        id += 1
    return df
df=get_data(link_list)
new_order = ['JobTitle', 'JobLocation', 'Qualifications','JobNo','JobDetailURL','Position','Type','PublishDate','CompanyName','JobDefinition','District','Sector']
df = df[new_order]

df.replace(np.nan, None, inplace=True)

conn_str = f"Driver={'{SQL Server}'};Server={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
conn = pyodbc.connect(conn_str)
 
cur = conn.cursor()
qry = ''' DELETE FROM Processler WHERE ProcesslerID 
        IN
        (SELECT  p.ProcesslerID FROM Processler p
        LEFT JOIN ProcessInfos i on p.ProcesslerID = i.ProcessID
        JOIN Siteler s on p.SiteId = s.SiteID
        where s.siteId = 86 and convert(date,BaslangicZamani )= convert(date, getdate())) '''
cur.execute(qry)
cur.commit()

qry = ''' DECLARE @outputLastId INT EXEC InsertCrawlProcessInfo @siteId = 86, @lastId = @outputLastId OUTPUT SELECT @outputLastId AS LastId '''
cur.execute(qry)
cur.commit()  

cur = conn.cursor()
qry = '''INSERT INTO iyibiris ([JobTitle],[JobLocation],[Qualifications],[JobNo],[JobDetailURL],[Position],[Type],[PublishDate],[CompanyName],[JobDefinition],[District],[Sector]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
         
for index, row in df.iterrows():
    param_values = list(row.values)
    cur.execute(qry, param_values)
    cur.commit()

cur = conn.cursor()
qry = " UPDATE [iyibiris] SET LastApplyDate = DATEADD(DAY, 30, PublishDate)"
cur.execute(qry)
cur.commit()  

numofpost = len(df)

cur = conn.cursor()
qry = '''SELECT ProcesslerID  FROM Processler where siteId = 86 AND BitisZamani is NULL ORDER BY BaslangicZamani DESC'''
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

qry = 'EXEC TransferCrawlSiteData 86'
cur.execute(qry)
cur.commit()