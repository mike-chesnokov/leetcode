"""
1996. The Number of Weak Characters in the Game

You are playing a game that contains multiple characters,
and each of the characters has two main properties: attack and defense.
You are given a 2D integer array properties where properties[i] = [attack[i], defense[i]]
represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels
strictly greater than this character's attack and defense levels.
More formally, a character i is said to be weak
if there exists another character j where attack[j] > attack[i] and defense[j] > defense[i].

Return the number of weak characters.

Example 1:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
"""
from typing import List


class Solution:
    def bruteForce(self, properties: List[List[int]]) -> int:

        cnt_weak = 0
        properties_sorted = sorted(properties, key=lambda x: x[0])

        len_prop = len(properties_sorted)

        for userA_ind in range(len_prop):
            for userB_ind in range(userA_ind + 1, len_prop):

                if properties_sorted[userA_ind][0] < properties_sorted[userB_ind][0] \
                        and properties_sorted[userA_ind][1] < properties_sorted[userB_ind][1]:
                    cnt_weak += 1
                    break

        return cnt_weak

    def groups(self, properties: List[List[int]]) -> int:
        cnt_weak = 0
        prop_sorted = sorted(properties, key=lambda x: x[0])
        len_prop = len(prop_sorted)
        # print(prop_sorted)
        # create groups of users
        # stack = [prop_sorted[0]]  # for current user group
        # stack_len = 0

        gr_next_gr_start_ind = {}

        for ind_A in range(1, len_prop):
            if prop_sorted[ind_A][0] == prop_sorted[ind_A - 1][0]:
                gr_next_gr_start_ind[prop_sorted[ind_A][0]] = None
                # stack.append(prop_sorted[ind_A])
                # stack_len += 1
            else:
                gr_next_gr_start_ind[prop_sorted[ind_A - 1][0]] = ind_A
            # print(gr_next_gr_start_ind)

        gr_next_gr_start_ind[prop_sorted[len_prop - 1][0]] = None
        # print(gr_next_gr_start_ind)

        for userA_ind in range(len_prop):
            next_gr_start_ind = gr_next_gr_start_ind[prop_sorted[userA_ind][0]]

            if next_gr_start_ind:
                for userB_ind in range(next_gr_start_ind, len_prop):

                    if prop_sorted[userA_ind][1] < prop_sorted[userB_ind][1]:
                        cnt_weak += 1
                        break
        return cnt_weak

    def sort_stack(self, properties: List[List[int]]) -> int:
        # sort attack in ascending order and defence in descending order
        prop_sorted = sorted(properties, key=lambda x: (x[0], -x[1]))
        # print(prop_sorted)
        stack = []
        cnt_weak = 0

        for a, d in prop_sorted:
            # print(stack)
            while stack and stack[-1] < d:
                stack.pop()
                cnt_weak += 1
            stack.append(d)
            # print(stack)
        return cnt_weak

    def sort_max(self, properties: List[List[int]]) -> int:
        # sort attack in descending order and defence in ascending order
        prop_sorted = sorted(properties, key=lambda x: (-x[0], x[1]))
        # print(prop_sorted)
        max_val = -1
        cnt_weak = 0

        for a, d in prop_sorted:
            if d < max_val:
                cnt_weak += 1
            else:
                max_val = d
        return cnt_weak

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # return self.bruteForce(properties)  # time limit
        # return self.groups(properties)  # time limit
        # return self.sort_stack(properties)  # passes tests
        return self.sort_max(properties)  # passes tests
