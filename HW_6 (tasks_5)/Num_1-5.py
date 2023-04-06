class DLNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# формирующие из списка [a_1,a_2,...a_n] двусвязанный список с соответствующими значениями
def create_doubly_linked_list(numbers: list) -> DLNode:
    head = None
    current = head

    if numbers:
        current = DLNode(numbers[0])
        head = current

        for item in numbers[1:]:
            prev = current
            current.next = DLNode(item, prev)
            current = current.next

    return head


def get_values_from_doubly_linked_list(head: DLNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result


#  функцию удаляющую нод по порядковому номеру (возвращает нод)
def remove_node(head: DLNode, nodenum: int) -> DLNode:
    current = head
    index = 0

    if head == None:
        return head

    if nodenum == 0:
        head = head.next

    while current and current.next:
        if index + 1 == nodenum:
            if current.next and current.next.next != None:
                current.next = current.next.next
                current.next.prev = current
                current = current.next
            else:
                current.next = None

        else:
            current = current.next

        index += 1

    return head


# функцию добавляющую нод по порядковому номеру
def add_node(head: DLNode, nodenum: int) -> DLNode:
    index = 0
    current = head

    if nodenum == 0:
        nxt = head
        head = DLNode(nodenum)
        head.next = nxt
        head.next.prev = head
        return  head

    while current and current.next:
        if index + 1 == nodenum:
            nxt = current.next
            current.next = DLNode(nodenum)
            current.next.prev = current
            current = current.next

            current.next = nxt
            current.next.prev = current

        else:
            current = current.next
        index += 1

    if index + 1 == nodenum:
        current.next = DLNode(nodenum)
        current.next.prev = current

    return head


# функцию разворачивающую список
def inverse_list(head: DLNode) -> DLNode:
    prev = None
    current = head

    while current:
        prev = current.prev
        nxt = current.next
        current.next = prev
        current.prev = nxt
        current = nxt
    return prev.prev







list1 = [1, 2, 3, 4, 5]

chain = create_doubly_linked_list(list1)
chain1 = inverse_list(chain)
print(get_values_from_doubly_linked_list(chain1))
