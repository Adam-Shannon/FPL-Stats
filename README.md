# WebScraperExample

# Simple Web Scraping with Python

This guide will provide a step by step walkthrough of a simple python web scraping script which will go to the premier league website click on some dropdown menus and grab some player data from the resulting table.

# Prerequisites

- Python 3.9 or greater [available here](https://www.python.org/downloads/release/python-390/)
  
- Chrome Driver  [available here](https://chromedriver.chromium.org/downloads)
  - Download the newest version and place it somewhere easy to find
  
- Python packages Selenium and Beautiful Soup and Pandas, installed using pip which should be bundled with python
  - "pip install beautifulsoup4"
  - "pip install Selenium"
  - "pip install pandas"
  

# Explanantion

## Setup

As with any python project this is probably best used within a virtual environment, but I wont describe how to create one here. The chrome driver can be installed Inline but for a script like this it can be worth it to have a local version and just update the version by installing the new driver when needed.

## Code Walkthrough

#### Service defintion - Selenium

After importing the necessary packages the code begins by creating an instance of the Service class with the path to the local web driver downloaded in the setup steps.

The code then defines an options instance which can be used to pass additional parameters to the Webdriver, in this case options is used to suppress warnings about licensing.

Finally we create the driver which will open a browser capable of being acted on automatically by our python script, we direct the browser to fetch the statistics page of the Fantasy premier league website.

#### Interactivity - Selenium

The next section of code interacts with the dropdown menus on the statisitcs page to filter the stats table to show defenders.

Using the inspector "ctrl + shift + i " we can see that the dropdown has the id "filter" which enables selenium to find it, the code then selects defneders which has the value "et_2" also visible in the inspector.

#### Parsing the table - beautiful soup (bs4)

We define a custom function "specific_table_parse" to actually retrive the data from the websites table into a usable format.

Initially we create a variable named soup which loads the beautiful soup parser using the driver from earlier which has been passed as an argument to the function to retrive the html for the webpage.

Next we use the bs4 "Soup.find()" method to get the table element from the webpages html which we've just parsed. Finally we use the pandas librabry to parse the table into a dataframe object which we then perform some example specific formatting steps on to remove teh 0th column and apply a function on each element in the player column.

#### More Interaction - Selenium

Using the same methods we used earlier to filter for defenders the script will next interact with the sort dropdown menu to order the table of defenders by goals scored, assists and cleansheets. Each time the list is re-ordered the script will run our specific_table_parse function to collect the data shown in the table so we can write it to a xlsx file, to look at the other lists add print(list_name) to the script or copy the code used for the assiters table to output to an excel file.

Finally the webdriver is proprely closed down to exit the script and tidy everything up.

# Running the code
open a command promptand use the "cd" command to move to the folder where the Scrape.py file is. In the same command prompt type "Python Scrape.py"
