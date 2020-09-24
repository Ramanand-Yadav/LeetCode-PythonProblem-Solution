/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL){
            return l2;
        }
        if (l2 == NULL){
            return l1;
        }
        ListNode* s;
        ListNode* new_head;
        ListNode* q;
        ListNode* p;
        p = l1;
        q = l2;
        if (p->val >= q->val){
            s = q;
            q = q->next;
        }
        else{
           s = p;
            p = p->next;
        }
        new_head = s;
        while (p && q){
            if (p->val >= q->val){
                s->next = q;
                s = q;
                q = q->next;
            }
            else {
                s->next = p;
                s = p;
                p = p->next;
            }
        }
        if (p == NULL){
            s->next = q;
        }
        if (q==NULL){
            s->next = p;
        }
        return new_head;
    }
};
