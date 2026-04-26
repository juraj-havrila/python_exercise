#MY_EMAIL = "XXX"
#MY_PASSWORD = "XXX"

import pandas
import datetime as dt
import calendar
import os
import random
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
my_contacts={row['name']:row['email'] for (index,row) in data.iterrows()}
my_birthdays={row['name']:str(row['month'])+'-'+str(row['day']) for (index, row) in data.iterrows()}
#my_birthdays={str(row['month'])+'-'+str(row['day']):row['name'] for (index, row) in data.iterrows()} ##good idea but works only for one person per day if several have same birthday
my_ages={row['name']:now.year-row['year'] for (index,row) in data.iterrows()}
#date_today = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
date_today = str(now.month)+'-'+str(now.day)
#print(date_today)
day_of_the_week = calendar.day_name[now.weekday()]

for my_name in my_birthdays.keys():
    if my_birthdays[my_name] == date_today:
        my_email=my_contacts[my_name]
        my_age=my_ages[my_name]
        my_template_file = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{my_template_file}") as file:
            my_email_text = file.read()
            my_email_text = my_email_text.replace("[NAME]", my_name)
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=my_email,
                msg=f"Subject:Hello {my_name}, Happy {my_age}th birthday!\n\n{my_email_text}"
            )
