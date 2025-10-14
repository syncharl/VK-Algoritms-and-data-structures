def scoundrels(array: list) -> list:
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] == 0:
            array[left], array[right] = array[right], array[left]
            right -= 1
        else:
            left += 1

    return array

if __name__ == '__main__':
    print(scoundrels(list(map(int, input().split()))))