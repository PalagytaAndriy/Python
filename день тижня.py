from datetime import datetime

week = ['понеділок', 'вівторок', 'середа', 'четверг', 'пятниця', 'субота', 'неділя']

now = datetime.today()
p = datetime.weekday(now)
print(week[p])
