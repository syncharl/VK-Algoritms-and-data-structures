def reverse_array(array: list) -> list:
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
        
    return array

if __name__ == '__main__':
    print(reverse_array(list(map(int, input().split()))))