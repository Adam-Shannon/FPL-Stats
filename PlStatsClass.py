from distutils.command.clean import clean
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class StatsGetter:
    def __init__(self):
        self.driver = webdriver.Chrome("C:/Users/adams/Desktop/code/dependencies/chromedriver.exe")
        self.driver.get("https://fantasy.premierleague.com/statistics")
        #get and setup element for the position filter
        position_filter_element = self.driver.find_element(By.ID, "filter")
        self.position_filter = Select(position_filter_element) 
        #get and setup element for the sorting criteria
        sorting_filter_element = self.driver.find_element(By.ID, "sort")
        self.sorting_filter = Select(sorting_filter_element)

    def get_table(self,position,sortCriteria):
        #set filters according to user input
        self.position_filter.select_by_value(position)
        self.sorting_filter.select_by_value(sortCriteria)

        #use filters to construct array containing rows of the table
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        table = soup.find("table")
        rows =  [i.split(",") for i in table.get_text(",", strip=True).split(",View player information,")[1:]]
        return rows

    def finish(self):
        #function which should always be called to close the automated browser
        self.driver.close()
        self.driver.quit()

#usage demonstration
""" 
provider = StatsGetter()
table = provider.get_table('et_2','goals_scored')
provider.finish()
print(table) 
"""