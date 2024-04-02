import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as file:
    content = file.readlines()
    selected_quote = random.choice(content)
    print(selected_quote)


my_email = "jadhavmihir143@gmail.com"
my_password = "coronavirus"
with smtplib.SMTP("smtp.gmail.com") as connection:
    # Below line is to make our connection secure.
    connection.starttls()

    # Logged in to your email provider.
    connection.login(user=my_email, password=my_password)

    connection.sendmail(
        from_addr=my_email,
        to_addrs="jadhavmihir0225@gmail.com",
        msg=f"Subject:Sunday Quote\n\n{selected_quote}",
    )
