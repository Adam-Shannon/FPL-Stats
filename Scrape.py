from distutils.command.clean import clean
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd
import numpy as np

# Create Test version of chrome
service = Service(executable_path="C:/Users/adams/Desktop/code/dependencies/chromedriver.exe")

# Setup options to disable warnings
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Define browser and load Website of choice
driver = webdriver.Chrome(options=options, service=service)
driver.get("https://fantasy.premierleague.com/statistics")

# Click on View Dropdown and select defenders
position_filter_element = driver.find_element(By.ID, "filter")
position_filter = Select(position_filter_element) 
position_filter.select_by_value('et_2')

# Click on Sorted By dropdown
sorting_filter_element = driver.find_element(By.ID, "sort")
sorting_filter = Select(sorting_filter_element)

# Define what to sort by
attributes = ["goals_scored", "assists", "clean_sheets"] 

# Function to get data from table and return it in nice format
def specific_table_parse(drvr):
    soup = BeautifulSoup(drvr.page_source, "html.parser")
    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    # Tidy up parsed table
    # remove unwanted first column
    df.drop(df.columns[[0]], axis=1, inplace=True)
    # tidy up player name (put commas in between so its "name,team,position")
    df["Player"] = df["Player"].map(lambda player: f"{player[:-6]},{player[-6:-3]},{player[-3:]}")
    return df
    

# Sort by Goals, Assists and Clean Sheets and read the stats from the table for each
sorting_filter.select_by_value(attributes[0])
goalscorers = specific_table_parse(driver)

sorting_filter.select_by_value(attributes[1])
assisters = specific_table_parse(driver)

sorting_filter.select_by_value(attributes[2])
cleanSheetBest = specific_table_parse(driver)

## Write the assiters to an xlsx file (all stats)
assisters.to_excel("assiters.xlsx")

# Close scraping browser and utilities
driver.close()
driver.quit()