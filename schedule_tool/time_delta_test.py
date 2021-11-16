import time
from datetime import datetime
from dateutil.relativedelta import relativedelta


now = datetime.now()
time.sleep(60)


print(relativedelta(datetime.now(), now).minutes)
print(relativedelta(now, datetime.now()))
