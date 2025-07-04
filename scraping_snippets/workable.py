import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from dateutil.relativedelta import relativedelta
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import dotenv_values
import pyodbc
import os
from datetime import datetime, time as datetime_time
from selenium.common.exceptions import TimeoutException
config = dotenv_values('.env')
SERVER = config['DB_SERVER_SGA']
DATABASE = config['DB_DATABASE_SGA_TIBDB']
USERNAME = config['DB_USERNAME_SGA']
PASSWORD = config['DB_PASSWORD_SGA']


options = Options()
#options.add_experimental_option('prefs', prefs)
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

path = "https://jobs.workable.com/search?location=Turkey&remote=false"


os.environ["HTTP_PROXY"] = "" 
os.environ["HTTPS_PROXY"] = ""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.maximize_window()
driver.get(path)
wait = WebDriverWait(driver, 10)

try:
    decline_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept all')]")))
    decline_button.click()
    print("Butona tıklama başarılı.")
except Exception as e:
    print(f"Hata: {e}")


time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

scrolling = True
while scrolling:    
    count_jobs_before = len(driver.find_elements(by=By.XPATH,value="/html/body/div/main/div/div/div/div/div/div/div/div/ul/li/div/div[2]/div[1]/h2"))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    count_jobs_last = len(driver.find_elements(by=By.XPATH,value="/html/body/div/main/div/div/div/div/div/div/div/div/ul/li/div/div[2]/div[1]/h2"))
    if count_jobs_before == count_jobs_last:
        print("scrolling has done!")
        scrolling = False




def format_date(date: str) -> str:
    date = date.lower().strip()


    if "today" in date:
        today = datetime.today().date()
        dt = datetime.combine(today, datetime_time(0, 0, 0))
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    
    if ("over" in date) or ("about" in date):
        parts = date.split()
        if len(parts) >= 4:
            time_diff = int(parts[2])
            unit = parts[3]
        else:
            return date
    else:
        parts = date.split()
        if len(parts) >= 3:
            time_diff = int(parts[1])
            unit = parts[2]
        else:
            return date

    today = datetime.today()

    if "day" in unit:
        result = today - relativedelta(days=time_diff)
    elif "month" in unit:
        result = today - relativedelta(months=time_diff)
    elif "year" in unit:
        result = today - relativedelta(years=time_diff)
    else:
        return date  

    result = datetime.combine(result.date(), datetime_time(0, 0, 0))
    return result.strftime("%Y-%m-%d %H:%M:%S")


job_items = driver.find_elements("xpath","//li[@data-ui='job-item']")

data_dict = {}
job_detailurl = driver.find_elements("xpath","//h2[@data-ui='job-card-title']//a")
job_detailurl_list = [detail.get_attribute("href") for detail in job_detailurl]
driver.execute_script("window.scrollTo(0,0)")

for i in range(len(job_items)):
    time.sleep(4)
    #print(job_detailurl_list[i])
    job_items[i].click()
    current_link = driver.current_url
    
    job_dict = {}
    job_dict["JobNo"] = current_link.split("JobId=")[1]
    try:
        title_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "h2[data-ui='overview-title'] strong"
        )))

        if title_element.is_displayed():
            job_title = title_element.text.strip()
        else:
            print("Element is not visible!")
        print(f"Element text: '{title_element.text.strip()}'")
        job_title = title_element.text.strip()
        print(job_title)
        job_dict["Title"] = job_title
    
    except:
        print("İlan başlığı elementi zamanında bulunamadı.")
        job_title = None
    try:
        company = driver.find_element("xpath","//h3[@data-ui='overview-company']").text[3:]
        job_dict["Company"] = company
    except:
        company = None
        job_dict["Company"] = company
    try:

        date = driver.find_element("xpath","//span[@class='jobOverview__text--2CN0j']").text
        if "year" in date:
            continue
        date = format_date(date)
        job_dict["Date"] = date
    except:
        date = None
        job_dict["Date"] = date
        
    try:
        description = driver.find_element("xpath", "//div[@class='jobBreakdown__job-breakdown--31MGR']").text
        description = description[12:4000]
        job_dict["Description"] = description
    except:
        description = None
        job_dict["Description"] = description
    try:
        location = driver.find_element("xpath","//span[@data-ui='overview-location']").text
        loc_list = location.split(", ")
        if len(loc_list) == 1:
            location = loc_list[0]
        elif len(loc_list) == 2:
            location = loc_list[1]
        else:
            location = loc_list[1]
            district = loc_list[0]
        job_dict["Location"] = location
        try:
            job_dict["District"] = district
        except:
            job_dict["District"] = None
    except:
        location = None
        job_dict["Location"] = None
    try:
        job_area = driver.find_element("xpath","//*[@id='cAB8KULLTX2oprJB'']/div/div/div/div/div[1]/span/span[3]").text
        job_dict["JobArea"] = job_area
    except:
        job_area = None
        job_dict["JobArea"] = None
    try:
        position = job_title
        job_dict["Position"] = position
    except:
        position = None
        job_dict["Position"] = None
    try:
        employment_type = driver.find_element("xpath","//span[@data-ui='overview-employment-type']").text
        job_dict["Type"] = employment_type
    except:
        employment_type = None
        job_dict["Type"] = None
    time.sleep(1)
    if not(job_dict["Date"]):
        pass
    data_dict[job_detailurl_list[i]] = job_dict
    ilan_kapa_tusu = driver.find_element("xpath","//div[@aria-label='Dismiss']")
    try:
        ilan_kapa_tusu.click()
        print(current_link)
    except:
        continue
        

main_df = pd.DataFrame(index=data_dict.keys(),data=data_dict.values())
main_df = main_df.reset_index()
main_df = main_df.rename(columns={"index":"JobDetailUrl"})
main_df['date_parsed'] = pd.to_datetime(main_df['Date'], format='%Y-%m-%d %H:%M:%S')
main_df['LastApplyDate'] = main_df['date_parsed'] + pd.to_timedelta(60, unit='days')
main_df['LastApplyDate'] = main_df['LastApplyDate'].dt.strftime('%Y-%m-%d %H:%M:%S')
main_df.drop(columns=['date_parsed'], inplace=True)

driver.quit()

main_df.replace(np.nan, None, inplace=True)

conn_str = f"Driver={'{SQL Server}'};Server={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
conn = pyodbc.connect(conn_str)

cur = conn.cursor()
qry = ''' DELETE FROM Processler WHERE ProcesslerID 
        IN
        (SELECT  p.ProcesslerID FROM Processler p
        LEFT JOIN ProcessInfos i on p.ProcesslerID = i.ProcessID
        JOIN Siteler s on p.SiteId = s.SiteID
        where s.siteId = 172 and convert(date,BaslangicZamani )= convert(date, getdate())) '''
cur.execute(qry)
cur.commit()

qry = ''' DECLARE @outputLastId INT EXEC InsertCrawlProcessInfo @siteId = 172, @lastId = @outputLastId OUTPUT SELECT @outputLastId AS LastId '''
cur.execute(qry)
cur.commit()

cur = conn.cursor()
qry = '''INSERT INTO workable
           ([jobdetailurl]
           ,[jobno]
           ,[jobtitle]
           ,[companyname]
           ,[publishdate]
           ,[jobdefinition]
           ,[joblocation]
           ,[district]
           ,[jobarea]
           ,[position]
           ,[type]
           ,[lastapplydate]
           )
     VALUES
           (?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           ,?
           )'''
          


for index, row in main_df.iterrows():
    param_values = list(row.values)
    print(len(param_values))
    cur.execute(qry, param_values)
    cur.commit()


qry = ''' update workable set siteID = 172 '''
cur.execute(qry)
cur.commit()


numofpost = len(main_df)

cur = conn.cursor()
qry = '''SELECT ProcesslerID  FROM Processler where siteId = 172 AND BitisZamani is NULL ORDER BY BaslangicZamani DESC'''
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

qry = 'EXEC TransferCrawlSiteData 172'
cur.execute(qry)
cur.commit()

