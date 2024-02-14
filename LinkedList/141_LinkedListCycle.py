/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *tot,*hare;
        tot = head;
        hare = head;
        while(tot!=NULL && hare!=NULL){
            
            tot = tot->next;
            hare = hare->next;
            if(hare == NULL)
                break;
            hare = hare->next;
            if(hare!=NULL && tot == hare){
                cout << tot->val<<"\n";
                cout << hare->val<<"\n";
                return true;
            }
        }
        return false;
    }
};