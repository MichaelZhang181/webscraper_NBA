import bs4
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv



#webpage for 2018-2019 season 
stat_url = 'https://stats.nba.com/players/advanced/?sort=PLAYER_NAME&dir=-1'


#opening the stats page in chrome
nba_driver = webdriver.Chrome()
nba_driver.get(stat_url)


# make sure that proper page is loaded
assert "404" not in nba_driver.title
nba_driver.implicitly_wait(5)


# modifying the webpage so that the table is set to "All" instead of '1'
combobox = nba_driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/nba-stat-table/div/div/div/select")
stat_all = Select(combobox)
stat_all.select_by_visible_text('All')


#taking the webpage and making it into a soup object
stat_html = nba_driver.page_source
stat_soup = soup(stat_html, "html.parser")


# closing the browser
nba_driver.close()


# getting the headers and writing to csv
header_html = stat_soup.find_all('th')
headers = []
for x in range(1, len(header_html)):
    if header_html[x].string == 'FGM':
        break
    else:
        headers.append(header_html[x].string)


# getting the player stats
player_html = (stat_soup.find('tbody')).find_all('tr')
player_table = []
for i in player_html:
    column = i.find_all('td')
    p_stats = []
    for x in range(1, len(headers) + 1):
        p_stats.append(column[x].string)
    player_table.append(p_stats)


#fill in the csv file
with open('adv_stat.csv', 'w', newline='') as stat_file:
    stat_writer = csv.writer(stat_file, delimiter=',',
                      quotechar='|', quoting=csv.QUOTE_MINIMAL)
    stat_writer.writerow(headers)
    for x in player_table:
        stat_writer.writerow(x)
    



