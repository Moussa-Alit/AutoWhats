import pywhatkit as pwt
from datetime import datetime

message = input("Enter:\n")
def send(message):
    now = datetime.now()
    nowlst = str(now).split()
    time = nowlst[1]
    timelst = time.split(":")
    hour = int(timelst[0])
    min = int(timelst[1])
    pwt.sendwhatmsg("+96170594811", message, hour, min+2)


send(message)