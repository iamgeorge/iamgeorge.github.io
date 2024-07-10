import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import os
import re

# 配置Selenium
chrome_service = Service('/usr/local/bin/chromedriver')  # 请替换为你ChromeDriver的路径
driver = webdriver.Chrome(service=chrome_service)


def load_existing_data(filename="contractors_info.csv"):
    if not os.path.exists(filename):
        return []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过头行
        existing_data = [row[:2] for row in reader]  # 只提取前两个值
    return existing_data


def extract_emails_from_website(url, name):
    visited = set()
    emails = set()

    def extract_emails_from_page(page_url):
        if page_url in visited:
            return
        visited.add(page_url)

        try:
            driver.get(page_url)
            time.sleep(3)  # 等待页面加载
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # 查找所有可能的邮件链接
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if "mailto:" in href:
                    email = href.split(":")[1]
                    if is_valid_email(email):
                        emails.add(email)
                        save_email_to_file(name, url, email)
                        return  # 找到一个邮箱就返回

            # 查找所有可能的邮件文本
            text = soup.get_text()
            for email in re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
                if is_valid_email(email):
                    emails.add(email)
                    save_email_to_file(name, url, email)
                    return  # 找到一个邮箱就返回

        except Exception as e:
            print(f"Error fetching website {page_url}: {e}")

    extract_emails_from_page(url)

    # 如果首页没有找到Email，尝试访问"About Us"、"Contact"等页面
    if not emails:
        possible_paths = ["/about", "/about-us", "/contact",
                          "/contact-us", "/info", "/information"]
        for path in possible_paths:
            full_url = url.rstrip('/') + path
            extract_emails_from_page(full_url)
            if emails:
                break

    return emails


def is_valid_email(email):
    # 使用正则表达式检查Email格式
    regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return re.match(regex, email) is not None


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


def save_email_to_file(name, website, email, filename="contractors_emails.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Business Name", "Website", "Email"])
        writer.writerow([name, website, email])


def main():
    companies = load_existing_data("contractors_info.csv")

    for name, website in companies:
        print(f"Extracting emails from {website} ...")
        extract_emails_from_website(website, name)

    print("Emails extracted and saved to file successfully.")


if __name__ == "__main__":
    main()
    driver.quit()
