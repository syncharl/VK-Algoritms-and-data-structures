def reverse_array(array: list) -> list:
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
        
    return array

def reverse_part(array: list, k: int) -> list:
    reversed = reverse_array(array)
    return reverse_array(reversed[:k]) + reverse_array(reversed[k:])

if __name__ == '__main__':
    print(reverse_part(list(map(int, input().split())), int(input())))