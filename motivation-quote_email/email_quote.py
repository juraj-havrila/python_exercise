import datetime as dt
import calendar
import random
import smtplib
my_email = "my_mail@gmail.com"
my_password = "my_password"


with open("quotes.txt","r") as f:
    quotes = f.readlines()
now = dt.datetime.now()
year = now.year
day_of_the_week = calendar.day_name[now.weekday()]
#print(day_of_the_week)
#date_of_birth = dt.datetime(year=1900,month=1,day=1)
#print(date_of_birth)

if day_of_the_week == "Sunday":
    random_quote = random.choice(quotes)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="my_recipient@gmail.com",
            msg=f"Subject:Happy {day_of_the_week}\n\n{random_quote}"
        )
