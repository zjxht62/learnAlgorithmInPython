import random
from pythonds.basic.queue import Queue

class Printer:
    def __init__(self, ppm):
        # 初始化打印速度、当前任务、以及任务倒计时
        self.print_speed = ppm
        self.current_task = None
        self.countdown = 0

    # 打印当前任务
    def tick(self):
        if self.current_task is not None:
            self.countdown -= 1
            if self.countdown <= 0:
                self.current_task = None

    def is_busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next_task(self, new_task):
        self.current_task = new_task
        # 根据打印速度及页数计算所需打印时间
        self.countdown = new_task.get_pages() * 60 / self.print_speed


class Task:
    def __init__(self, time):
        self.create_timestamp = time
        self.pages = random.randrange(1, 21)

    def get_create_time(self):
        return self.create_timestamp

    def get_pages(self):
        return self.pages

    # 根据创建时间以及停止时间计算等待时间
    def get_waiting_time(self, time):
        return time - self.create_timestamp

# 根据1/180的概率生成任务
def create_new_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def simulate(num_seconds, pages_per_minute):
    task_queue = Queue()
    printer = Printer(pages_per_minute)
    waiting_times = []
    for current_second in range(num_seconds):
        # 创建新任务，入队
        if create_new_task():
            task = Task(current_second)
            task_queue.enqueue(task)
        # 打印机空闲，从队列取任务
        if (not printer.is_busy()) and (not task_queue.isEmpty()):
            next_task = task_queue.dequeue()
            waiting_times.append(next_task.get_waiting_time(current_second))
            printer.start_next_task(next_task)
        printer.tick()

    average_wait = sum(waiting_times)/len(waiting_times)

    print('Average Wait %6.2f secs %3d tasks remaining.' %(average_wait, task_queue.size()))

for i in range(10):
    simulate(3600, 10)
