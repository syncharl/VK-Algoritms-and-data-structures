def switch_even(array: list) -> list:
    even = 0
    odd = 0

    while even < len(array):
        if array[even] % 2 == 0:
            array[even], array[odd] = array[odd], array[even]
            even += 1
            odd += 1
        else:
            even += 1
    
    return array

if __name__ == '__main__':
    print(switch_even(list(map(int, input().split()))))