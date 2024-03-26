class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        list1=[]
        list2=[]
        tmp=head
        while head:
            y=head.val
            if y<x:
                list1.append(y)
            else:
                list2.append(y)
            head=head.next
        tmp1=tmp
        head=tmp
        i=0
        l=len(list1)
        while i<l:
            tmp=ListNode()
            tmp.val=list1[i]
            head.next=tmp
            head=head.next
            i+=1
        
        i=0
        l=len(list2)
        while i<l:
            tmp=ListNode()
            tmp.val=list2[i]
            head.next=tmp
            head=head.next
            i+=1
        return tmp1.next
