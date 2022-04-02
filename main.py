from datetime import datetime as dt
import pandas as pd
import random
import smtplib


# Email account credentials from where you want to send wishes
MY_EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"

today = dt.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

birthday_people = data.loc[
    (data["day"] == today_tuple[1]) & (data["month"] == today_tuple[0])
]
# print(birthday_people)

if birthday_people.empty:
    print("There are no birthdays defined in birthdays.csv file for today")
else:
    for idx in birthday_people.index:
        name = birthday_people['name'][idx]
        email = birthday_people['email'][idx]
        number = random.randint(1, 3)
        # print(number)
        file_name = f"letter_templates/letter_{number}.txt"
        # print(file_name)
        with open(file_name) as file:
            text_data = file.read()
            final_data = text_data.replace("[NAME]", name)
            # print(final_data)

            try:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=email,
                        msg=f"Subject:Happy Birthday!\n\n{final_data}",
                    )
            except smtplib.SMTPAuthenticationError as err:
                print(err)
