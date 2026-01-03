'''
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
class ListNode: 
    def __init__(self, val=0, next=None): 
        self.val = val 
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    length1 = 0
    currenthead1 = list1
    listItem = []
    while currenthead1:
        length1 = length1 + 1
        listItem.append(currenthead1.val)
        currenthead1 = currenthead1.next

    length2 = 0
    currenthead2 = list2
    while currenthead2:
        length2 = length2 + 1
        listItem.append(currenthead2.val)
        currenthead2 = currenthead2.next

    length = length1 + length2

    if length1 > 50 or length2 > 50: #len(list1) < 0 and len(list2) < 0 and 
        return None
    elif list1 == None and list2 == None: #len(list1) < 0 and len(list2) < 0 and 
        return None
    elif list1 == None and list2 != None:
        return list2
    elif list1 != None and list2 == None:
            return list1  
    '''
    dummy =  ListNode()
    combinedlst = dummy
    while list1:
        combinedlst.next = list1
        combinedlst = combinedlst.next
        list1 = list1.next
        
    while list2:
        combinedlst.next = list2
        combinedlst = combinedlst.next
        list2 = list2.next

    listItem = []
    while combinedlst:
        listItem.append(combinedlst.next)
    '''
    b = 0
    while b < len(listItem):
        for i in range(len(listItem)-1):
            current = listItem[i]
            next = listItem[i+1]
            if current > next:
                temp = current
                listItem[i] = next #[5,3,2,1] [3,2,1,5]
                listItem[i+1] = temp
        b = b + 1
    head = ListNode(listItem[0])
    currentNode = head
    for val in listItem[1:]:
        currentNode.next = ListNode(val)
        currentNode = currentNode.next
    return head

# Create nodes 
list1 = ListNode(1) 
list1.next = ListNode(2) 
list1.next.next = ListNode(4)

list2 = ListNode(1) 
list2.next = ListNode(3) 
list2.next.next = ListNode(4)
result = mergeTwoLists(list1,list2)
print(result)