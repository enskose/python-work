import requests
import pandas as pd
from lxml import html
from datetime import datetime
import re
from bs4 import BeautifulSoup
import pyodbc
from dotenv import load_dotenv
from dotenv import dotenv_values
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import numpy as np
load_dotenv()
config = dotenv_values('.env')

SERVER = config['DB_SERVER_SGA']
DATABASE = config['DB_DATABASE_SGA_TIBDB']
USERNAME = config['DB_USERNAME_SGA']
PASSWORD = config['DB_PASSWORD_SGA']

BASE_URL = "https://cvbenim.com/is-ilanlari-sayfa"
START_PAGE = 1
END_PAGE = 60  # Örnek olarak 5. sayfaya kadar crawl edilecek

# Sabit xpath değişkenleri
JOB_DETAIL_XPATH = "//a[@class='ilnBslk']/@href"  # Kullanıcı tarafından sağlanacak
DETAILS_PARENT_XPATH = "//ul[@class='kriterler']"
JOB_TITLE_SELECTOR = "div.ilanBilgi.ilanBilgi-reklam h1"
JOB_DEFINITION_SELECTOR = "div.ilanBilgi.ilanBilgi-reklam p"
COMPANY_NAME_SELECTOR = "p.firma-adi.nw"


# Tarihi uygun formatta stringe dönüştüren fonksiyon
def convert_to_yyyy_mm_dd(date_str):
    try:
        months = {
            'Ocak': '01', 'Şubat': '02', 'Mart': '03', 'Nisan': '04', 'Mayıs': '05', 'Haziran': '06',
            'Temmuz': '07', 'Ağustos': '08', 'Eylül': '09', 'Ekim': '10', 'Kasım': '11', 'Aralık': '12'
        }
        day, month, year = date_str.split()
        month_number = months.get(month, '00')
        return f"{year}-{month_number}-{day.zfill(2)}"
    except ValueError:
        return None


# İlan detay bilgilerini regex kullanarak alacak fonksiyon
def extract_job_details(job_page_content, job_detail_url):
    soup = BeautifulSoup(job_page_content, 'html.parser')
    details_parent = soup.select_one("ul.kriterler")
    if not details_parent:
        return {}

    # Temizlenmiş detay metni
    details_text = re.sub(r'\n+', '\n', details_parent.get_text(separator="\n")).strip()

    try:
        ilan_numarasi = re.search(r'İlan Numarası\s*:\s*(\d+)', details_text).group(1)
    except AttributeError:
        ilan_numarasi = None

    try:
        ilan_tarihi = convert_to_yyyy_mm_dd(
            re.search(r'İlan Tarihi\s*:\s*(\d{1,2}\s\w+\s\d{4})', details_text).group(1))
    except AttributeError:
        ilan_tarihi = None

    try:
        calisma_sekli = re.search(r'Çalışma Şekli\s*:\s*(.*?)\n', details_text).group(1).strip()
    except AttributeError:
        calisma_sekli = None

    try:
        calisma_yeri = re.search(r'Çalışma Yeri\s*:\s*(.*?)\n', details_text).group(1).strip()
    except AttributeError:
        calisma_yeri = None

    try:
        pozisyon = re.search(r'Pozisyon\s*:\s*(.*?)\n', details_text).group(1).strip().split(',')[0]
    except AttributeError:
        pozisyon = None

    try:
        sektor = re.search(r'Sektör\s*:\s*(.*?)\n', details_text).group(1).strip()
    except AttributeError:
        sektor = None

    try:
        kapanma_tarihi = convert_to_yyyy_mm_dd(
            re.search(r'Kapanma Tarihi\s*:\s*(\d{1,2}\s\w+\s\d{4})', details_text).group(1))
    except AttributeError:
        kapanma_tarihi = None

    try:
        job_title = soup.select_one(JOB_TITLE_SELECTOR).get_text().strip()
    except AttributeError:
        job_title = None

    try:
        job_definition = soup.select_one(JOB_DEFINITION_SELECTOR).get_text().strip()
    except AttributeError:
        job_definition = None

    try:
        company_name = soup.select_one(COMPANY_NAME_SELECTOR).get_text().strip()
    except AttributeError:
        company_name = None

    return {
        'JobDefinition': job_definition,
        'CompanyName': company_name,
        'JobDetailUrl': job_detail_url,
        'JobNo': ilan_numarasi,
        'PublishDate': ilan_tarihi,
        'Type': calisma_sekli,
        'JobLocation': calisma_yeri,
        'Position': pozisyon,
        'Sector': sektor,
        'JobTitle': job_title,
        'LastApplyDate': kapanma_tarihi
    }


# Pagination ve ilan detaylarını toplamak için fonksiyon
def crawl_job_listings(base_url, start_page, end_page):
    job_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
    session = requests.Session()
    # Retry yapılandırması
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
    )

    # Adapter'i ekleyin ve Session'a ekleyin
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)
    session.mount('http://', adapter)

    session.headers.update(headers)
    for page in range(start_page, end_page + 1):
        try:
            response = session.get(f"{base_url}-{page}")
            print(f"request for page--> {page}")
        except:
            continue

        if response.status_code != 200:
            continue
        tree = html.fromstring(response.content)
        job_links = tree.xpath(JOB_DETAIL_XPATH)
        job_links = ["https://cvbenim.com" + link for link in job_links]

        if not job_links:
            break

        for job_link in job_links:
            job_response = session.get(job_link)
            if job_response.status_code == 200:
                job_details = extract_job_details(job_response.text, job_link)
                job_list.append(job_details)

    return job_list


def write_to_database():
    conn_str = f"Driver={'{SQL Server}'};Server={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
    conn = pyodbc.connect(conn_str)
    numofpost = len(jobs_df)

    cursor = conn.cursor()
    cur = conn.cursor()

    qry = ''' DELETE FROM Processler WHERE ProcesslerID 
    IN
    (SELECT  p.ProcesslerID FROM Processler p
    LEFT JOIN ProcessInfos i on p.ProcesslerID = i.ProcessID
    JOIN Siteler s on p.SiteId = s.SiteID
    where s.siteId = 58 and convert(date,BaslangicZamani )= convert(date, getdate())) '''
    cur.execute(qry)
    cur.commit()

    qry = ''' DECLARE @outputLastId INT EXEC InsertCrawlProcessInfo @siteId = 58, @lastId = @outputLastId OUTPUT SELECT @outputLastId AS LastId '''
    cur.execute(qry)
    cur.commit()
    jobs_df.replace(np.nan, None, inplace=True)
    for index, row in jobs_df.iterrows():
        insert_query = '''
        INSERT INTO cvbenimcom (JobNo, JobLocation, Type, Position, CompanyName, JobDetailUrl, PublishDate, JobDefinition, Sector,JobTitle,LastApplyDate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?,?,?,?)'''
        cursor.execute(insert_query, row['JobNo'], row['JobLocation'], row['Type'], row['Position'], row['CompanyName'],
                       row['JobDetailUrl'], row['PublishDate'], row['JobDefinition'], row['Sector'], row['JobTitle'],
                       row['LastApplyDate'])

    conn.commit()

    cur = conn.cursor()
    qry = '''SELECT ProcesslerID  FROM Processler where siteId = 58 AND BitisZamani is NULL ORDER BY BaslangicZamani DESC'''
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
    qry = 'EXEC TransferCrawlSiteData 58'
    cur.execute(qry)
    cur.commit()


job_data = crawl_job_listings(BASE_URL, START_PAGE, END_PAGE)
jobs_df = pd.DataFrame(job_data)

write_to_database()
