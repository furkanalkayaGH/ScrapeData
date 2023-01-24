from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://rcdb.com/r.htm?ot=2')


roller_coasters = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[2]")
amusement_park = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[3]")
type = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[4]")
design = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[5]")
status = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[6]")
opened = driver.find_elements("xpath", "//div[@class='stdtbl rer']/table/tbody/tr/td[7]")

result=[]

for i in range(len(type)):
    temp_data={'Roller Coaster': roller_coasters[i].text,
               'Type': type[i].text,
               'Design': design[i].text,
               'Status': status[i].text,
               'Opened': opened[i].text}
    result.append(temp_data)

df_data=pd.DataFrame(result)
print(df_data)





