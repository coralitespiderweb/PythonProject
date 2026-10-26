import smtplib
import datetime as dt
import random

my_email = "wenxin.zhou@warriorlife.net"
password = "hwuyzfpltveykgzq"
now = dt.datetime.now()

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

if now.weekday() == 5:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jenniferzhou3413@gmail.com",
            msg=f"Subject:Hello\n\n{random.choice(quotes)}"
        )

#year = now.year
#month = now.month
#day_of_week = now.weekday()
#print(day_of_week)

#date_of_birth = dt.datetime(year= 1995, month= 12, day= 15, hour=4)
#print(date_of_birth)
