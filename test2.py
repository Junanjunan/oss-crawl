from datetime import datetime, timedelta

now = datetime.now()
one_day = timedelta(days=1)
yesterday = now - one_day
print(now-one_day)