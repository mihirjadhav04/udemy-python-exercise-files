# # How to send Emails using python
# import smtplib

# my_email = "jadhavmihir143@gmail.com"
# my_password = "coronavirus"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Below line is to make our connection secure.
#     connection.starttls()

#     # Logged in to your email provider.
#     connection.login(user=my_email, password=my_password)

#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="jadhavmihir0225@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email.",
#     )


# # connection.close() - Instead of using this and closing it manually, we will use with keyword like file opening.

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week)
# print(now)
# print(year)
# print(month)

date_of_birth = dt.datetime(year=2000, month=8, day=2)
print(date_of_birth)
