import bs4 
import requests
import pandas as pd
import re
import sys

def get_and_write_url(url):
    print("Fetching : " + url)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url = url, headers = header)
    con = response.text
    return con

words = ["heart"]
main_df = pd.DataFrame()
main_df["url"] = main_df["text"] = main_df["article_date"] = ''
main_url = "https://cvshealth.com/search?keys="
links = []
for i in words:
    source = get_and_write_url(main_url, i.replace('', '+'))
    y = re.findall(r'href="(.*?)" rel="bookmark"',source)
    links = links + y
    page = page + 1
links = list(set(links))
