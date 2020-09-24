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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL){
            return head;
        }
        ListNode *p,*new_start,*q,*temp;
        p = head;
        new_start = p->next;
        while (1){
            q = p->next;
            temp = q->next;
            q->next = p;
            if (temp == NULL || temp->next == NULL){
                p->next = temp;
                break;
            }
            p->next = temp->next;
            p = temp;
        }
        return new_start;
    }
};
