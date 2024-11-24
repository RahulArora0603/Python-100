from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

req = requests.get(url)

soup = BeautifulSoup(req.text, features="lxml")

table = soup.find('table',
    class_ = 'wikitable sortable mw-datatable sticky-header static-row-numbers sort-under col1left col5left col6left')
headings = table.find_all('th')
all_headings = [heading.text.strip() for heading in headings]
t_body = table.find('tbody')
table_rows = t_body.find_all('tr')

df = pd.DataFrame(columns=all_headings)
for row in table_rows[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

print(df.head())

