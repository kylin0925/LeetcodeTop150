"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        node_list = []
        tmp = head
        node_map = {}
        idx = 0
        cp_node = Node(0)
        new_head = cp_node
        while tmp !=None:
            cp_node.val =  tmp.val
            if tmp.next!=None:
                cp_node.next = Node(0)

            node_list.append(tmp)
            node_map[tmp] = idx
            tmp = tmp.next
            cp_node = cp_node.next
            idx+=1
        
        cp_node = None
        #print(node_list)
        #print(node_map)
        
        rand_idx = []
        for n in node_list:
            r = n.random
            if r == None:
                rand_idx.append(-1)
            else:
                idx = node_map[r]
                rand_idx.append(idx)
        #print(rand_idx)

        new_list = []
        tmp = new_head
        while tmp!=None:
            new_list.append(tmp)
            tmp = tmp.next
        #print(new_list)
        for i in range(len(rand_idx)):
            if rand_idx[i] != -1:
                idx = rand_idx[i]
                new_list[i].random = new_list[idx]
        return new_head


