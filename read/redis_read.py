from redis import StrictRedis
import time
from datetime import datetime

r = StrictRedis()
start = time.time() * 1000
for k in range(0, 100000):
    r.get("boo" + str(k))

print(time.time() * 1000 - start)
