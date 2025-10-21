class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push(self, val):
        new_node= Node(val)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def pop(self):
        if self.head.next == self.tail:
            return None        
        pop_result = self.tail.prev
        self.tail.prev = pop_result.prev
        pop_result.prev.next = self.tail
        self.size -= 1
        return pop_result.data
    
    def peek(self):
        if self.head.next == self.tail:
            return None
        return self.tail.prev.data
    
class Stack:
    def __init__(self):
        self.top = Node()

    def push(self, val):
        new_node = Node(val)
        new_node.prev = self.top
        self.top = new_node
    
    def pop(self):
        if self.top.data is None:
            return None
        pop_result = self.top
        self.top = self.top.prev
        pop_result.prev = None
        return pop_result.data

def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next

    while slow != fast:
        if fast == None or slow == None:
            return False
        
        slow = slow.next
        fast = fast.next.next

    return True

def reverse_linked_list(head: Node) -> Node:
    if not head:
        return None 
       
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def find_middle(head: Node) -> Node:
    if not head or not head.next:
        return head
    
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def remove_elem(head: Node, val: int) -> Node:
    dummy = Node()
    dummy.next = head
    current = dummy  

    while current and current.next:
        if current.next.data == val:
            current.next = current.next.next
        else:
            current = current.next    

    return dummy.next

def is_subsequence_by_queue(substring: str, fullstring: str) -> bool:
    q = Queue()

    for el in substring:
        q.push(el) 

    for el in fullstring:
        if q.peek() and el == q.peek():
            q.pop()

    return q.size == 0

def is_subsequence_by_index(s: str, t: str) -> bool:
    if not s:
        return True
    
    left = 0
    right = len(t) - 1

    while left <= right and s:
        if t[left] == s[0]:
            s = s[1:]  
            left += 1      
        elif s and t[right] == s[-1]:
            s = s[:-1]
            right -= 1
        else:
            left += 1
            right -= 1

    return not s

def is_palindrome_by_stack(s: str) -> bool:
    stack = Stack()

    for el in s:
        stack.push(el)    
    for el in s:
        popped = stack.pop()
        if popped and popped != el:
            return False 
           
    return True

def is_palindrome_by_index(s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        a = 0
        b = len(s) - 1
        while a <= b:
            if s[a] == s[b]:
                a +=1
                b -= 1
                continue                
            return False
        return True

def merge_linked_lists(first_list: LinkedList, second_list: LinkedList) -> LinkedList:
    if not first_list.head:
        return second_list
    if not second_list.head:
        return first_list
    
    if first_list.head.data <= second_list.head.data:
        main = first_list.head
        other = second_list.head
        result_list = first_list
    else:
        main = second_list.head
        other = first_list.head
        result_list = second_list
    
    prev_main = None
    
    while main and other:
        if main.data <= other.data:
            prev_main = main
            main = main.next
        else:
            next_other = other.next
            if prev_main:
                prev_main.next = other
            else:
                result_list.head = other
            other.next = main
            prev_main = other
            other = next_other
    
    if other:
        prev_main.next = other
    
    return result_list