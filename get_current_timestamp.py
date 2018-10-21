import datetime
import time

print ("timestamp1: ", time.time())
print ("timestamp2: ", 
    (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime("%Y%m%d%H%M%S"))
