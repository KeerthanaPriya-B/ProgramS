import datetime
import calendar
date=input()
born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
print(calendar.day_name[born].upper())