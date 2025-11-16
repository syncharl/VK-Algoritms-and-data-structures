def binary_search_sqrt(target):
    l, r = 0, target
    while l < r:
        middle = (l + r) // 2
        if middle ** 2 > target:
            r = middle - 1
            continue
        if middle ** 2 < target:
            l = middle + 1
            continue
        return middle
    return r

def copy_time(n, x, y):
    l = 0
    r = (n - 1) * max(x, y)
    while l + 1 < r:
        mid = (r + l) // 2
        if mid // x + mid // y < n - 1:
            l = mid
        else:
            r = mid
    return r + min(x, y)

def feed_animals(animals, food):
    animals.sort()
    food.sort()
    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break
    return count

def extra_letter(a, b):
    hash_a = {}
    for i in a:
        hash_a[i] = hash_a.get(i, 0) + 1
    for i in b:
        if i in hash_a.keys():
            hash_a[i] = hash_a[i] - 1
            if hash_a[i] == 0:
                del hash_a[i]
                continue
            continue
        return i
    return None

def two_sum(data, target):
    cache = {}
    i = 0
    for d in data:
        cache[d] = i
        i += 1
    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache.keys():
            return [i, cache[diff]]
    return []

def shell_sort(arr):
    n = len(arr)
    gap = len(arr) // 2
    while gap > 0:
        cur = gap
        while cur < n:
            m_gap = cur
            while m_gap >= gap and arr[m_gap] < arr[m_gap - gap]:
                arr[m_gap], arr[m_gap - gap] = arr[m_gap - gap], arr[m_gap]
                m_gap -= gap
            cur += 1
        gap = gap // 2
    return arr

def anagramms(anagramms):

    def to_hash(anagramm):
        hash_a = {}
        for i in anagramm:
            hash_a[i] = hash_a.get(i, 0) + 1
        return hash_a
    
    out = []
    for anagramm in anagramms:
        out.append(to_hash(anagramm))

    final_out = []
    while anagramms:
        an_list = []
        left = 0
        right = len(anagramms) - 1
        while left < right:
            if out[left] == out[right]:
                an_list.append(anagramms.pop(right))
                out.pop(right)
            right -= 1
        else:
            print(out)
            an_list.append(anagramms.pop(right))
            out.pop(right)
        final_out.append(an_list)
        left += 1

    return final_out