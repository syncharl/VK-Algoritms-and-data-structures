def netherlands(array: list) -> list:
    left = 0
    centre = 0
    right = len(array) - 1

    while centre <= right:
        if array[centre] == 0:
            array[centre], array[left] = array[left], array[centre]
            centre += 1
            left += 1      
        elif array[centre] == 1:
            centre += 1
        elif array[centre] == 2:
            array[centre], array[right] = array[right], array[centre]
            right -= 1        

    return array

if __name__ == '__main__':
    print(netherlands(list(map(int, input().split()))))
    