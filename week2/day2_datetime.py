import datetime

# 3-1-2015

day = datetime.datetime(year=2004, month=3, day=1)
print(day - datetime.timedelta(hours=12))

now = datetime.datetime.now()
print(now)
now_formatted = now.strftime("%A, %B, %-d %Y %H:%M:%S")
print(now_formatted)

now_obj = datetime.datetime.strptime(now_formatted, "%A, %B, %d %Y %H:%M:%S")
print(now_obj)

now_encoded = now.strftime("%A||||||||| %B,(441@94) ffss%-d %Y 34%H:614%M:41%S")
print(now_encoded)
print("DECODING TIME")
import time
time.sleep(10)
print(datetime.datetime.strptime(now_encoded, "%A||||||||| %B,(441@94) ffss%d %Y 34%H:614%M:41%S"))


d

#workflow of game
#draw board, matrix
#promp, choose row, then choose column
#board gets drawn again, with new X or O
#promp asking for O
