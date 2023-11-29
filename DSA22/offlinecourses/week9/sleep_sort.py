import threading
from time import sleep

items = [6, 2, 5, 3, 1, 7]


def sleep_sort(i):
    sleep(i)
    print(i)


threads = [threading.Thread(target=sleep_sort,args=(i,))for i in items]
# 启动所有线程
for t in threads:
    t.start()
# 等待所有线程执行结束
for thread in threads:
    thread.join()