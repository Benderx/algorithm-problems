# https://leetcode.com/problems/add-two-numbers/?tab=Description
# COMPLETED

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2
        trace1 = []
        trace2 = []

        while(curr1 != None):
            if curr2 != None:
                trace1.append(curr1.val)
                trace2.append(curr2.val)
                curr1 = curr1.next
                curr2 = curr2.next
            else:
                trace1.append(curr1.val)
                curr1 = curr1.next

        while(curr2 != None):
            trace2.append(curr2.val)
            curr2 = curr2.next

        m = max(len(trace1), len(trace2))
        new = [0]*(m+1)

        for i in range(0, m):
            if i <= len(trace1)-1 and i <= len(trace2)-1:
                temp = trace1[i] + trace2[i] + new[i]
            elif i <= len(trace1)-1:
                temp = trace1[i] + new[i]
            else:
                temp = trace2[i] + new[i]

            carry = 0
            if temp >= 10:
                carry = 1
                temp = temp % 10
                print(i)
            new[i] = temp
            new[(i+1)] = carry

        if len(new) == 1 & new[0] == 0:
            return None


        root = ListNode(new[0])
        curr = root
        for i in range(1, len(new)):
            if i == len(new)-1:
                if new[i] == 0:
                    break

            new_node = ListNode(new[i])
            curr.next = new_node
            curr = new_node

        return root