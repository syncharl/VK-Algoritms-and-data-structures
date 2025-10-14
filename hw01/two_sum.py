def two_sum(array: list, target: int) -> int:
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] + array[right] > target:
            right -= 1
        elif array[left] + array[right] < target:
            left += 1
        else:
            return left, right
    
if __name__ == '__main__':
    print(two_sum(list(map(int, input().split())), int(input())))