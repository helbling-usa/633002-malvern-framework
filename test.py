import time

start_time = time.time()

cur_time = time.time()
while (cur_time - start_time < 10):
    print(cur_time - start_time)
    cur_time  = time.time()