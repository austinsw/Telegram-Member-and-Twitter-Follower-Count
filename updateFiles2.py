#pip install openpyxl
#pip install schedule
############# Twitter Part #############
import tweepy

consumer_key = "****************"
consumer_secret = "************************************************"
access_token = "************************************************"
access_token_secret = "************************************************"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

listTwitter = ["elonmusk","unclebobmartin"]

############# Telegram Part #############
import json
from urllib.request import urlopen

BOT_TOKEN = "************************************************" #numCounter_bot in the group

def getCount(chat_id):
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/getChatMembersCount?chat_id=@" + chat_id
    with urlopen(url) as f:
        resp = json.load(f)
    return resp['result']

listTelegram = ["GroupUsername1","GroupUsername2"]

############# Write into csv & scheduler & convert to Excel #############
import schedule #pip install schedule
import time
from datetime import datetime
import csv
import pandas as pd

twitterFile = '../../Dropbox/Dashboard/twitter.csv'
telegramFile = '../../Dropbox/Dashboard/telegram.csv'

def job():
    date = datetime.today().strftime("%Y-%m-%d")
    #date = "2021-07-07"
    print(date)
    with open(twitterFile, 'a', newline='') as csv_file:
        fieldnames = ["Date"]
        fieldnames = fieldnames + listTwitter
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        content = {
            "Date": date
        }
        for page in listTwitter:
            user = api.get_user(page)
            content[page] = user.followers_count
        csv_writer.writerow(content)
        print("Content: ", content)
    with open(telegramFile, 'a', newline='') as csv_file:
        fieldnames = ["Date"]
        fieldnames = fieldnames + listTelegram
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        content = {
            "Date": date
        }
        for channel in listTelegram:
            content[channel] = getCount(channel)
        csv_writer.writerow(content)
        print(content)
    read_fileTwi = pd.read_csv(r'C:\Users\User\Dropbox\Dashboard\twitter.csv')  ###pip install openpyxl
    read_fileTwi.to_excel(r'C:\Users\User\Dropbox\Dashboard\twitter.xlsx', index=None, header=True)
    read_fileTel = pd.read_csv(r'C:\Users\User\Dropbox\Dashboard\telegram.csv')
    read_fileTel.to_excel(r'C:\Users\User\Dropbox\Dashboard\telegram.xlsx', index=None, header=True)
    return

schedule.every().day.at("15:35").do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
