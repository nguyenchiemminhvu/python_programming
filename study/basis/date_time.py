import datetime as dt

now = dt.datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
print(now.strftime("%Y-%m-%d %H:%M:%S:%f"))

print()

tomorrow = now + dt.timedelta(days=1)
print(tomorrow.strftime("%Y-%m-%d %H:%M:%S"))

yesterday = now - dt.timedelta(days=1)
print(yesterday.strftime("%Y-%m-%d %H:%M:%S"))

print()

custom_datetime = dt.datetime(2023, 10, 1, 12, 30, 45, 123456)
print(custom_datetime.strftime("%Y-%m-%d %H:%M:%S:%f"))