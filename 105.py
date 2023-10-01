import datetime

now = str(datetime.datetime.now()).split()
time = now[1]
print(time[:5])
