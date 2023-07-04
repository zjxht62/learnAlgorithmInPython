from pythonds.basic.deque import Deque


def palchecker(a_str):
    str_queue = Deque()
    for s in a_str:
        str_queue.addRear(s)

    still_ok = True
    while str_queue.size() > 1 and still_ok:
        first = str_queue.removeFront()
        last = str_queue.removeRear()
        if first != last:
            still_ok = False

    return still_ok


if __name__ == '__main__':
    print(palchecker("北京输油管油输京北"))
    print(palchecker("safasdfadf"))
