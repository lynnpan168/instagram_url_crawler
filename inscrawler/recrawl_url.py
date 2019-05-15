from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import urllib.request
from itertools import chain

# open chorme driver
driver = webdriver.Chrome(executable_path="C:/Users/Lynn/Desktop/SOA/chromedriver")

# read in the output file that we get from instagrame-craler-master hashtage mode service
df = pd.read_json('output')

def crawler(row):
    try:
        driver.get(row['key'])
        time.sleep(2)
        # Collect data
        igSource = driver.page_source
        soup = BeautifulSoup(igSource, "html.parser")
        # poster name
        poster_name = soup.find('a',{"class":"FPmhX notranslate nJAzx"}).text
        row['poster_name'] = poster_name
        # content + hashtag
        All_content = soup.find_all('div',{"class":"C4VMK"})
        try:
            if All_content[1].find_all('a')[0].text == poster_name:
                    new_content = All_content[0:2]
            else:
                new_content = All_content[0:1]
        except:
            new_content = All_content[0:1]
        try:
            span = new_content.find('span')
            hashtag=[]
            hashtag_soup = span.find_all('a')
            for h in hashtag_soup:
                hashtag.append(h.text)
            content = span.get_text(separator=u' ')
        except:
            span = [n.find_all('span') for n in new_content]
            span = list(chain.from_iterable(span))
            content = ''
            hashtag=[]
            for n in span:
                hashtag_soup = n.find_all('a')
                for h in hashtag_soup:
                    hashtag.append(h.text)
            for n in span:
                content = content + n.get_text(separator=u' ')
        row['hashtag'] = hashtag
        row['content'] = content
        # likes
        row['likes'] = soup.find('a',{"class":"zV_Nj"}).text.split()[0]  # split the Num + 個讚 ,only get the number
        # datetime
        row['datetime'] = soup.find('time',{"class":"_1o9PC Nzb55"}).attrs['title']
        # img description and img href
        row['img_desc'] = soup.find('img',{"class":"FFVAD"}).attrs['alt']
        row['img_url'] = soup.find('img',{"class":"FFVAD"}).attrs['src']
    except:
        pass
    return row

df = df.apply(crawler,axis=1)

df.to_csv('output_df.csv')