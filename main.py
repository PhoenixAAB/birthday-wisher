import smtplib
import pandas
import random
import datetime as dt
import os
from dotenv import load_dotenv

# 1. Read the birthdays CSV
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient='records')

# 2. Check today's date
now = dt.datetime.now()
month = now.month
day = now.day

# 3. Check if anyone's birthday matches today
birthday_person = None
for row in data_dict:
    if row["month"] == month and row["day"] == day:
        birthday_person = row
        break

# 4. If yes, choose a random letter and personalize it
if birthday_person:
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    chosen_letter = random.choice(letters)

    with open(f"letter_templates/{chosen_letter}", encoding="utf-8") as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    # 5. Send the email
    load_dotenv()
    my_gmail = os.getenv("MY_EMAIL")
    password = os.getenv("MY_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )
else:
    print("It's not anyone's birthday today 🎂")
