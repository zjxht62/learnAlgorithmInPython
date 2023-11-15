isBadVersion = 'lambda n:n>=30'

versions = [i for i in range(50)]
print(versions)

bad_versions = list(filter(eval(isBadVersion), versions))
print(bad_versions)


def binary_search(versions, lambda_exp):
    start = 0
    end = len(versions) - 1
    while start <= end:
        mid = (start + end) // 2
        if lambda_exp == versions[mid]:
            return True
        elif lambda_exp < mid:
            end = mid - 1
        else:
            start = mid + 1
    return False


if __name__ == '__main__':
    print(binary_search([1,2,3,4,6,7,8,9],4))


