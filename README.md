# Telegram-Member-and-Twitter-Follower-Count
Using Telegram API and Twitter API to scrape the number of members and followers into excel, made in 2021

The project was originally created to log the follower count and group no. count onto excel everyday. The information was then incorporated with free dashboard making website to create a dashboard for showing the statistics that updated everyday.

## Run
The code is run on Python 3. If Python 3 is not your default interpreter (say Python 2.7), you will probably need `pip3 install`, and `python3` command to install the packages and run the .py file.

If the packages are not already installed, run the code to install the package: E.g. `pip install openpyxl`, `pip install openpyxl`

`python updateFiles2.py` to run the file: It was originally created on PyCharm, and used on a local Windows machine.

## Set up the basics
Change the following codes accordinly:
- `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret` Input the values accordingly (register for Twitter Developer and follow the steps to create app)
- `listTwitter` Input the Twiiter username(s)
- `BOT_TOKEN` Input the bot token for the Telegram bot
- `listTelegram` Input the Telegram group username(s)
- `twitterFile` & `telegramFile` Replace the file paths for writing the scrapped information onto the csv files. 
- `read_fileTwi`, `read_fileTwi.to_excel(...)`, `read_fileTel`, `read_fileTel.to_excel(...)` Replace the file paths for the csv files and the excel files generated. 
- `schedule.every().day.at("15:35").do(job)` Change the scheduler to another point of time in the day as you wish
