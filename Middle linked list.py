#class Solution:
#   def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#      stack=[]
#     while head:
#        stack.append(head)
#       head=head.next
#  tmp=len(stack)//2 +1
# return stack[tmp-1]

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow
