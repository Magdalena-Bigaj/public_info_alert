#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
from datetime import date
import smtplib
import ssl

url= 'https://bip.dolnyslask.pl/o,2149,informacje-i-obwieszczenia.html?sort=13_&sort_dir=desc'
PATH= 'C:\Program Files (x86)\chromedriver.exe'
driver =  webdriver.Chrome(PATH)
driver.get(url)
time.sleep(5)
soup= BeautifulSoup(driver.page_source, 'html.parser')
soup


# In[10]:



date_bip= soup.find('td', {'class': 'sc-pAkoP iqlssu'})
today_date= date.today()
today_date= date.fromisoformat(str(today_date))
d= date.fromisoformat(date_bip.text)


# In[11]:


def send_email():   
    smtp_server= 'smtp.gmail.com'
    smtp_port= 587
    email_from= 'testowymailmmmb7943@gmail.com'
    email_to= 'magda.bigaj@wp.pl'
    pswd= 'jannivkjemramsfn'

    message= 'There are some BIP changes'
    simple_email_context = ssl.create_default_context()

    try:
        TIE_server= smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context= simple_email_context)
        TIE_server.login(email_from, pswd)
        print('Connecting to server...')
        print(f'Sending email to {email_to}')
        TIE_server.sendmail(email_from, email_to, message)
        print(f'Email succesfully sent to {email_to}')


    except Exception as e:
        print(e)
    finally:
        TIE_server.close()


if d== today_date:
    send_email()
else:
    print("no changes")


# In[5]:


# import requests
# import re
# from bs4 import BeautifulSoup
# import pandas as pd
# import smtplib
# from datetime import date
# import json
# import html5lib
# import urllib

#jann ivkj emra msfn

