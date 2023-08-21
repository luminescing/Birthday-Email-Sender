import smtplib
from datetime import datetime
import random
import pandas

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "testpassword"
SENDER_NAME = "Sender"


today_month = datetime.now().month
today_day = datetime.now().day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        birthday_person = birthdays_dict[today]
        contents = letter_file.read()
        updated_contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"From: \"{SENDER_NAME}\" <{MY_EMAIL}>\n"
                f"To: {birthday_person['name']} {birthday_person['email']}\n"
                f"Subject:Happy Birthday!\n\n{updated_contents}"
        )


