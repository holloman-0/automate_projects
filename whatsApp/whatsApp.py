import pywhatkit
from datetime import date, datetime

now = datetime.now()
current_time = now.strftime("%H:%M")

hour = int(current_time[:2])
min = int(current_time[3:]) + 1

pywhatkit.sendwhatmsg("+4407481279180" , "Hi Andrea ,\nIt's Jack here interested in a video tour of Ad Ad ref# 16347981 as i am interested in putting down a deposit. \n" , hour , min , wait_time= 43)


