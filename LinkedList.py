class Node:
    def __init__(self, value = 0, address = None):
        self.data = value
        self.next = address

def ArraytoLL(NodeClass, arr, n):
    if n == 0 or not arr:
        return None
    head = NodeClass(arr[0])
    curr = head
    for i in range(1, n):
        temp = NodeClass(arr[i])
        curr.next = temp
        curr = curr.next
    return head

def printallLL(head):
    temp = head
    while temp != None:
        print(temp.data, end= " ")
        temp = temp.next
        
def FindLength(head):
    temp = head
    count = 0
    while temp != None:
        count += 1
        temp = temp.next
    return count

def FindElement(head, k):
    temp = head
    while temp != None:
        if(temp.data == k):
            return True
        temp = temp.next
    return False

arr = list(map(int, input().split()))
n = len(arr)
k = int(input())

head = ArraytoLL(Node, arr, n)
print("Head: " + str(head.data))

printallLL(head)

length = FindLength(head)
print("\nLength : " + str(length))

element = FindElement(head, k)
print("No Element" if not element else "Element exits")