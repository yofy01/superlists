# -*- coding:utf-8 -*-
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# 定义url地址
url = 'http://localhost:8000/'

# 定义Firefox地址
geckodriver_path = Service('G:\Python39\geckodriver.exe')

# 创建浏览器操作对象 
browser = webdriver.Firefox(service = geckodriver_path)
browser.get(url)