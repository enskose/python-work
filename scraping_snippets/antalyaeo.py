import pandas as pd
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from lxml import etree
import os
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
import datetime
import time
from dateutil import parser
import numpy as np
import pyodbc
from dotenv import dotenv_values
config = dotenv_values('.env')
SERVER = config['DB_SERVER_SGA']
DATABASE = config['DB_DATABASE_SGA_TIBDB']
USERNAME = config['DB_USERNAME_SGA']
PASSWORD = config['DB_PASSWORD_SGA']


HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  "sec-ch-ua-platform": "Windows",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "no-cors",
  "sec-fetch-site": "same-origin",
}

succesful_req_count = 0
failed_req_count = 0

def get_joblinks():
    paging = True
    page = 1
    job_link_list = []
    while paging:
        page_url = f"https://www.antalyaeo.org.tr/tr/ilanlar?kID=4&sID={page}"
        print(f"scrape ediliyor... {page_url}")
        try:
            response = requests.get(page_url, headers = HEADERS,timeout=40)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)
            continue
        job_link_list.extend({page_url})
        last_page=6
        if page > last_page:
            paging = False
            continue
        page+=1        
    return job_link_list

job_links = get_joblinks()

print(job_links)

def get_data(links):
    global data
    global succesful_req_count
    global failed_req_count
    df=pd.DataFrame(columns=("JobTitle","Position","JobNo","PublishDate","CompanyName", "Phone", "JobLocation", "JobDefinition","JobDetailURL"))
    id = 0
    for url in links:
        is_request_failed = True
        while is_request_failed:
            try:
                response = requests.get(url, headers = HEADERS,timeout=40)
                soup = BeautifulSoup(response.content, "lxml")
                dom = etree.HTML(str(soup))
                is_request_failed = False
                succesful_req_count += 1
                if succesful_req_count % 100 == 0:
                    print(f"{succesful_req_count} th Successful request!")
            except requests.exceptions.ConnectionError:
                failed_req_count += 1
                print('connection error!')
                time.sleep(3)
                continue
            except requests.exceptions.RequestException as e:
                failed_req_count += 1
                print('Request Exception',e)
                time.sleep(3)
                continue
        elements=soup.select("body > div.content.eo-content > div > div > div > div.haber > div")       
        for element in elements[1:]:
            try:
                JobTitle = "Eleman"
            except:
                JobTitle = ""
            try:
                Position = "Eleman"
            except:
                Position = ""             
            try:
                div_element = element.find('div', class_='col-md-6')
                JobNo = div_element.get_text(strip=True).split('İlan No:')[1].strip()
            except:
                JobNo = ""
            try:
                div_element = element.find('strong', string='İlan Tarihi:')
                PublishDate = div_element.find_next_sibling(string=True).strip()
                parsed_date = parser.parse(PublishDate, dayfirst=True)
                formatted_date = parsed_date.strftime('%Y-%m-%d %H:%M:%S.000')
                PublishDate = formatted_date
            except:
                PublishDate = ""
            try:
                CompanyName = element.find('strong', string='Adı Soyadı:')
                CompanyName = CompanyName.find_next_sibling(string=True).strip()
            except:
                CompanyName = ""
            try:
                Phone = element.find('strong', string='Telefon:')
                Phone=Phone.find_next_sibling(string=True).strip()
                Phone= Phone.replace('(','').replace(')','').replace(' ','').lstrip('0').replace('-','')
                if Phone.startswith('90'):
                    Phone=Phone.replace('90', '', 1) 
                if len(Phone) !=10:
                    Phone=None
            except:
                Phone = ""
            try:
              """   MailAdress = element.select_one('body > div.content.eo-content > div > div > div > div.haber > div > div > div:nth-child(3)')
                MailAdress = MailAdress.get_text(strip=True)
                print(MailAdress) """
            except:
                MailAdress = ""
            try:
                JobLocation = "Antalya"
            except:
                JobLocation = ""
            try:
                JobDefinition = element.select_one('body > div.content.eo-content > div > div > div > div.haber > div > div > div > p')
                JobDefinition = JobDefinition.get_text()
                JobDefinition = JobDefinition[:4000] 
            except:
                JobDefinition = ""
            try:
                JobDetailURL = url
            except:
                JobDetailURL = ""
            df.loc[id] = (JobTitle,Position,JobNo,PublishDate,CompanyName, Phone, JobLocation, JobDefinition,JobDetailURL)
            id += 1
    return df
df=get_data(job_links)

new_order = ['JobTitle','JobLocation','JobNo', 'JobDetailURL', 'Position', 'PublishDate','CompanyName','JobDefinition','Phone']
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
        where s.siteId = 71 and convert(date,BaslangicZamani )= convert(date, getdate())) '''
cur.execute(qry)
cur.commit()

qry = ''' DECLARE @outputLastId INT EXEC InsertCrawlProcessInfo @siteId = 71, @lastId = @outputLastId OUTPUT SELECT @outputLastId AS LastId '''
cur.execute(qry)
cur.commit()  

cur = conn.cursor()
qry = '''INSERT INTO AntalyaEczaciOdasi ([JobTitle],[JobLocation],[JobNo],[JobDetailURL],[Position],[PublishDate],[CompanyName],[JobDefinition],[Phone]) VALUES (?,?,?,?,?,?,?,?,?)'''
         
for index, row in df.iterrows():
    param_values = list(row.values)
    cur.execute(qry, param_values)
    cur.commit()


numofpost = len(df)

cur = conn.cursor()
qry = '''SELECT ProcesslerID  FROM Processler where siteId = 71 AND BitisZamani is NULL ORDER BY BaslangicZamani DESC'''
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

qry = 'EXEC TransferCrawlSiteData 71'
cur.execute(qry)
cur.commit()
print("Data insert done")