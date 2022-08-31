from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print('Now: ', now)

now = now + relativedelta(months=1, weeks=1, hour=10)
print('Now: ', now)