from distutils.command.clean import clean
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:/Users/adams/Desktop/code/dependencies/chromedriver.exe")
driver.get("https://fantasy.premierleague.com/statistics")

position_filter_element = driver.find_element(By.ID, "filter")
position_filter = Select(position_filter_element) 
position_filter.select_by_value('et_2')

sorting_filter_element = driver.find_element(By.ID, "sort")
sorting_filter = Select(sorting_filter_element)

attributes = ["goals_scored", "assists", "clean_sheets"] 

def specific_table_parse(drvr):
    soup = BeautifulSoup(drvr.page_source, "html.parser")
    table = soup.find("table")
    rows =  [i.split(",") for i in table.get_text(",", strip=True).split(",View player information,")[1:]]
    return rows
    

sorting_filter.select_by_value(attributes[0])
goalscorers = specific_table_parse(driver)

sorting_filter.select_by_value(attributes[1])
assisters = specific_table_parse(driver)

sorting_filter.select_by_value(attributes[2])
cleanSheetBest = specific_table_parse(driver)

print("Goalscorers:")
for i in goalscorers:
    print(f"{i[0]} has scored {i[7]}") 


driver.close()
driver.quit()