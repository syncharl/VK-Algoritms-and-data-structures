def ones_and_zeros(array: list) -> list:
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] == 0:
            left += 1
        else:
            if array[left] == 1 and array[right] == 0:
                array[left], array[right] = array[right], array[left]
                left += 1
            right -= 1

    return array

if __name__ == '__main__':
    print(ones_and_zeros(list(map(int, input().split()))))