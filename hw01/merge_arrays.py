def merge_arrays(array_1: list, array_2:list) -> list:
    first = 0
    second = 0
    result = []

    while first < len(array_1) and second < len(array_2):
        if array_1[first] <= array_2[second]:
            result.append(array_1[first])
            first += 1
        else:
            result.append(array_2[second])
            second += 1

    return result + array_1[first:] + array_2[second:]

if __name__ == '__main__':
    print(merge_arrays(list(map(int, input().split())), list(map(int, input().split()))))


