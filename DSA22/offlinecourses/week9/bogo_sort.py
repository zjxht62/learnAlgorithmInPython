from random import shuffle


def inorder(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def bogo(x):
    while not inorder(x):
        shuffle(x)
    return x


l = bogo([1, 3, 2, 4, 5])
print(l)
