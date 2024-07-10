import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import re
import os

# 配置Selenium
chrome_service = Service('/usr/local/bin/chromedriver')  # 请替换为你ChromeDriver的路径
driver = webdriver.Chrome(service=chrome_service)


def search_on_google(query="local contractor"):
    driver.get("https://www.google.com/search?tbm=lcl&q=" + query)
    time.sleep(3)


def click_next_page():
    try:
        # 查找并点击分页按钮
        next_button = driver.find_element(By.ID, "pnnext")
        if next_button.is_enabled():
            next_button.click()
            time.sleep(5)  # 等待新页面加载
            return True
        return False
    except Exception as e:
        print(f"Error clicking next page button: {e}")
        return False


def extract_business_info():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    business_cards = soup.find_all('div', class_='VkpGBb')

    business_info_list = []
    for card in business_cards:
        try:
            name = card.find('div', class_='dbg0pd').text
            website_button = card.find('a', href=True)
            phone = card.find('span', class_='rllt__details lqhpac')
            phone_number = phone.text if phone else None
            website = None
            if website_button:
                website = website_button['href']
                if is_valid_url(website):
                    business_info_list.append((name, website, phone_number))
        except Exception as e:
            print(f"Error extracting business info: {e}")

    return business_info_list


def is_valid_url(url):
    # 使用正则表达式检查URL格式
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// 或 https://
        # 域名
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # 本地服务器
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4地址
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6地址
        r'(?::\d+)?'  # 可选端口
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def save_to_file(data, filename="contractors_info.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Business Name", "Website", "Phone"])
        for row in data:
            writer.writerow(row)


def load_existing_data(filename="contractors_info.csv"):
    if not os.path.exists(filename):
        return []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过头行
        existing_data = [tuple(row) for row in reader]
    return existing_data


def main():
    queries = [
        "local contractor",
        "building contractor",
        "construction contractor",
        "home improvement contractor",
        "renovation contractor",
        "general contractor",
        "remodeling contractor",
        "roofing contractor",
        "electrical contractor",
        "plumbing contractor",
        "HVAC contractor",
        "painting contractor",
        "landscaping contractor",
        "masonry contractor",
        "carpentry contractor"
    ]
    all_business_info = []

    for query in queries:
        search_on_google(query)
        while True:
            business_info_list = extract_business_info()
            all_business_info.extend(business_info_list)
            if not click_next_page():
                break

    existing_data = load_existing_data()
    existing_data_set = set(existing_data)

    unique_business_info = []
    for business in all_business_info:
        if business not in existing_data_set:
            unique_business_info.append(business)
            existing_data_set.add(business)

    # 对unique_business_info按公司名称排序
    unique_business_info.sort(key=lambda x: x[0])

    save_to_file(unique_business_info)
    print("Data saved to file successfully.")


if __name__ == "__main__":
    main()
    driver.quit()
