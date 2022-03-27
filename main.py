from datetime import datetime as dt
import pandas
import random
import smtplib


# Email account credentials from where you want to send wishes
my_email = "YOUR_EMAIL"
password = "YOUR_PASSWORD"


today = dt.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_person = data.loc[
    (data["day"] == today_tuple[1]) & (data["month"] == today_tuple[0])
]
name = birthday_person.iloc[0]["name"]
email = birthday_person.iloc[0]["email"]


if not birthday_person.empty:
    number = random.randint(1, 3)
    # print(number)
    file_name = f"letter_templates/letter_{number}.txt"
    # print(file_name)
    with open(file_name) as file:
        text_data = file.read()
        final_data = text_data.replace("[NAME]", name)
        # print(final_data)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{final_data}",
            )
