"""
470. Implement Rand10() Using Rand7()

Given the API rand7() that generates a uniform random integer in the range [1, 7],
 write a function rand10() that generates a uniform random integer in the range [1, 10].
 You can only call the API rand7(), and you shouldn't call any other API.
 Please do not use a language's built-in random API.

Each test case will have one internal argument n,
the number of times that your implemented function rand10() will be called while testing.
Note that this is not an argument passed to rand10().

Example 1:
Input: n = 1
Output: [2]

Example 2:
Input: n = 2
Output: [2,8]

Example 3:
Input: n = 3
Output: [3,8,10]
"""

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def formula(self):
        """
        Method called "Rejection Sampling"
        get random number from [1,7] twice and use formula
        to get result which will be uniformly distributed between [1, 49]
        Multiplying won't get uniformly distributed result, because
        some numbers are more probable, ex. 12 (4*3 and 3*4)
        """
        c = 49
        while c >= 40:
            a = rand7()
            b = rand7()
            c = (a - 1) * 7 + b - 1

        return (c % 10) + 1

    def twice(self):
        """
        1. get a in [1, 2, 3, 4, 5, 6] - as bin flag
        2. get b in [1, 2, 3, 4, 5] as number
        3. if flag is odd return b, esle return b + 5
        """
        a = 7
        while a > 6:
            a = rand7()

        b = 7
        while b > 5:
            b = rand7()

        if a % 2 == 0:
            return b
        return b + 5

    def rand10(self):
        """
        :rtype: int
        """
        # return self.formula()
        return self.twice()
