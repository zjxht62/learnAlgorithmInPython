# 判断是否是素数
# n = int(input())

def is_prime(num):
    # if num == 1 or num ==2:
    #     print('yes')
    #     return
    for i in range(2, num):
        if num % i == 0:
            print('no')
            break
    else:
        print('yes')

# is_prime(n)

print(list(range(2,1)))
