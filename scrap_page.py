import json
from bs4 import BeautifulSoup

row_selector = "table>tbody>tr"
column_selector = "td"
header_selector = "thead>tr>th"

with open('get_data.html', 'rb') as file:
    page = file.read()

soup = BeautifulSoup(page, 'html.parser')
rows = soup.select(row_selector)

head_elements = soup.select(header_selector)
header = [elem.text for elem in head_elements]

# header.pop(0)  # eliminate the # sign

all_data = []
for row in rows:
    columns = row.findAll(column_selector)
    all_data.append(dict(zip(header, [column.text for column in columns])))

# print(all_data)
with open('scrapped-data.json', 'w') as json_data:
    json.dump(all_data, json_data, indent=2)

print("File saved -> scrapped_data.json")