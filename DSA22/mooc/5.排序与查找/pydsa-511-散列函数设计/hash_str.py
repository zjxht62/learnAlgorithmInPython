def hash(str, table_size):
    sum = 0
    for pos in range(len(str)):
        sum += ord(str[pos])

    return sum % table_size
if __name__ == '__main__':
    print(hash('cat',11))