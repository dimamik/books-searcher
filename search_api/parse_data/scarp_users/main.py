import csv
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.litmir.me/')

driver.find_element_by_class_name("lts39").click()

driver.find_element_by_id("username").send_keys(os.environ['USERNAME'])
# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(os.environ['PASSWORD'])
# click login button
driver.find_element_by_class_name("entry-button").click()

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
sleep(5)


# Writes to csv table where table is
# [[A, B, C], [D,E,F]]
# Data is APPENDED!!!


def write_to_csv(data_table):
    with open('out.csv', 'a', newline='\n', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data_table)


def parse_books(merged_tab, page):
    for index, (link, book_numbers) in enumerate(merged_tab):
        if (page == 17 and index <= 85):
            continue
        user_id = link.split('=')[1]
        link = link + '&o=100'
        driver.get(link)
        try:
            driver.find_element_by_class_name('xs_msg')
            print('No books found')
            continue
        except:
            pass
        hrefs = WebDriverWait(driver, 50).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".book_name [href]")))
        book_link_tab = [elem.get_attribute('href') for elem in hrefs]
        book_name_tab = [elem.text for elem in hrefs]
        tab_to_write_in_csv = [
            [user_id, book_name, book_link] for book_name, book_link in zip(book_name_tab, book_link_tab)
        ]
        write_to_csv(tab_to_write_in_csv)
        print(f'Page {page} number {index} is done')


def parse_users(page_from=2, page_to=31):
    for page in range(page_from, page_to):
        # Go to that page
        driver.get(
            f'https://www.litmir.me/UserLoadSearch?order=BookAddedDown&type=last_user&p={page}&o=100')
        # Write down all user names and their ids

        elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".desc2 [href]")))
        links = [elem.get_attribute('href') for index,
                                                elem in enumerate(elements) if index % 2 != 0]
        number_of_books = [elem.text for index,
                                         elem in enumerate(elements) if index % 2 != 0]
        merged_tab = [(link, book_number)
                      for link, book_number in zip(links, number_of_books)]
        parse_books(merged_tab, page)
        # Do the parsing there!
