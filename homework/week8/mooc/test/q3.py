def q3(n):
    if n <= 4:
        return 1
    else:
        return q3(n-1)+q3(n-2)+q3(n-3)+q3(n-4)



if __name__ == '__main__':
    print(q3(6))