from selenium import webdriver
import pandas as pd

with open('job_scraping.csv', 'w', encoding='utf8',newline="") as file:
    file.write("Roller Coasters; Type; Design; Status; Opened \n")

driver = webdriver.Chrome()
driver.get('https://rcdb.com/r.htm?ot=2')


roller_coasters = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[2]")
amusement_park = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[3]")
type = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[4]")
design = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[5]")
status = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[6]")
opened = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[7]")

result=[]

with open('job_scraping.csv', 'a', encoding='utf8',newline="") as file:
    for i in range(len(type)):
      file.write(roller_coasters[i].text + ";" +
                   type[i].text + ";" +
                    design[i].text + ";" +
                    status[i].text + ";" +
                    opened[i].text + "\n")