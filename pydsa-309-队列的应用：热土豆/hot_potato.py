from pythonds.basic.queue import Queue
def hot_potato(name_list, num):
    game_queue = Queue()
    for name in name_list:
        game_queue.enqueue(name)

    while game_queue.size() > 1:
        for i in range(num):
            game_queue.enqueue(game_queue.dequeue())
        game_queue.dequeue()

    return game_queue.dequeue()

if __name__ == '__main__':
    name_list = ['wjp', 'zjx', 'yd', 'dxy', 'ckx', 'zs', 'wl']
    print(hot_potato(name_list, 6))
