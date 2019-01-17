import bs4
import pandas as pd
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#webpage for 2018-2019 season 
stat_page = 'https://stats.nba.com/players/advanced/?sort=PLAYER_NAME&dir=-1'

#opening the stats page in chrome
nba_driver = webdriver.Chrome()
nba_driver.get(stat_page)

# modifying the webpage so that the table is set to "All" instead of '1'
combobox = nba_driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/nba-stat-table/div/div/div/select")
table_all = Select(combobox)
table_all.select_by_visible_text('All')

# downloading the html file for parsing
nba_html = nba_driver.page_source

# closing the browser
nba_driver.close()


