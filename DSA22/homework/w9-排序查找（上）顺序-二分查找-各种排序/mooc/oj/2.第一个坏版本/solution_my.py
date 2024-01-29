def isBadVersion(n):
    if n > 9:
        return True
    else:
        return False

# versions = [i for i in range(50)]
# print(versions)
#
# bad_versions = list(filter(eval(isBadVersion), versions))
# print(bad_versions)


def first_bad_version(N):
    start = 1
    end = N
    while start < end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    return start


num = int(input())
isBadVersion = eval(input())
print(first_bad_version(num))

