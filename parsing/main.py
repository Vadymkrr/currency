import requests
import csv
from bs4 import BeautifulSoup
import sqlite3


#
#
# def get_page_content():
#     base_url = 'https://hophey.ua/ru/od/razlivnoe/pivo/'
#
#     response = requests.get(base_url)
#     response.raise_for_status()
#     return response.text
#
#
# def main():
#     page_content = get_page_content()
#
#     soup = BeautifulSoup(page_content, features="html.parser")
#
#     search_results = soup.find("div", {"id": "section-items-wrapper_148"})
#     single_items = search_results.find_all("div", {"class": "product"})
#
#     with open('beer_items.csv', 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Product ID', 'Item Link'])
#
#         for item in single_items:
#             item_details = item.find("a", {"class": "d-flex flex-auto product-picture"})
#             data_product_id = item['data-product_id']
#             item_link = item_details['href']
#
#
# if __name__ == '__main__':
#     main()


def get_page_content():
    base_url = 'https://hophey.ua/ru/od/razlivnoe/pivo/'

    response = requests.get(base_url)
    response.raise_for_status()
    return response.text


class CSVWriter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

        with open(self.filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)

    def write(self, row: list):
        with open(self.filename, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)


class SQLiteWriter:
    def __init__(self, db_name, table_name, columns):
        self.db_name = db_name
        self.table_name = table_name
        self.columns = columns

        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table_name} ({', '.join(self.columns)})"
        )

    def write(self, row: list):
        placeholders = ', '.join(['?'] * len(row))
        self.cursor.execute(
            f"INSERT INTO {self.table_name} VALUES ({placeholders})", row
        )
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()


def main():
    writers = {
        CSVWriter('beer.csv', ['product_id', 'product_link']),
        SQLiteWriter('beer.db', 'products', ['product_id TEXT', 'product_link TEXT'])
    }
    page_content = get_page_content()

    soup = BeautifulSoup(page_content, features="html.parser")

    search_results = soup.find("div", {"id": "section-items-wrapper_148"})
    single_items = search_results.find_all("div", {"class": "product"})

    items_data = []

    for item in single_items:
        item_details = item.find("a", {"class": "d-flex flex-auto product-picture"})
        data_product_id = item['data-product_id']
        item_link = item_details['href']

        item_data = {
            'product_id': data_product_id,
            'product_link': item_link
        }

        items_data.append(item_data)

        for writer in writers:
            writer.write([item_data['product_id'], item_data['product_link']])


if __name__ == '__main__':
    main()
