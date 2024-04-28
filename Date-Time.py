import datetime
today_date=datetime.date.today()
current_time=datetime.datetime.now().time()
today_day=today_date.strftime("%A")
print("Today's date:",today_date)
print("Current time:",current_time)
print("Today's day:",today_day)
