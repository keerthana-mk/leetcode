# https://leetcode.com/problems/min-cost-climbing-stairs/
#
# MinCostClimbingStairs
#
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
'''
Approach 1: Bottom-Up Dynamic Programming (Tabulation)
Intuition

Bottom-up dynamic programming is also known as tabulation and is done iteratively. Dynamic programming is based on the concept of overlapping subproblems and optimal substructure. This is when the solution to a problem can be constructed from solutions to similar and smaller subproblems. Solving a smaller version of the problem can be easier and faster, thus if we break up the problem into smaller subproblems, solving them can lead us to the final solution easier and faster.

Let's look at an example costs = [0,1,2,3,4,5]. Since we can take 1 or 2 steps at a time, we need to reach either step 4 or step 5 (0-indexed), and then pay the respective cost to reach the top. For this example, to reach step 4 optimally would cost 2 by taking path 0 --> 2 --> 4 (we're not counting the cost of step 4 yet since we are only talking about reaching the step right now). To reach step 5 optimally would cost 4 by taking path 1 --> 3 --> 5.

Now, imagine that before we started the problem, somebody came up to us and said "to optimally reach step 4 costs 2 and to optimally reach step 5 costs 4." Well,
then the problem is trivial - the answer is the minimum of 2 + cost[4] = 6 and 4 + cost[5] = 9. The only reason this was so easy was because we already knew the cost to
reach steps 4 and 5.
So how do we find the minimum cost to reach step 4 or step 5? Well, you might notice that it's the exact same problem, just with a smaller input.
For example, finding the minimum cost to reach step 4 is like solving the original problem with input [0,1,2,3] (step 4 is the "top of the floor" now).
To solve this subproblem, we need to find the minimum cost to reach steps 2 and 3, which requires us to answer the original problem for inputs [0,1] and [0,1,2].

This pattern is known as a recurrence relation, and in this case, the minimum cost to reach the i^{th}i
th
  step is equal to minimumCost[i] = min(minimumCost[i - 1] + cost[i - 1], minimumCost[i - 2] + cost[i - 2]). As you can see, we get the solution for the i^{th}i
th
  step by using solutions from earlier steps. So, when does the sequence terminate? For this question, the base cases are given in the problem description - we are allowed to start at either step 0 or step 1, so minimumCost[0] and minimumCost[1] are both 0.

Algorithm

With our base cases and recurrence relation, we can now easily solve this problem.

Define an array minimumCost, where minimumCost[i] represents the minimum cost of reaching the i^{th}
  step. The array should be one element longer than costs and start with all elements set to 0.

The reason the array should contain one additional element is because we will treat the top floor as the step to reach.
Iterate over the array starting at the 2nd index. The problem statement says we are allowed to start at the 0 th
or 1st step, so we know the minimum cost to reach those steps is 0.

For each step, apply the recurrence relation - minimumCost[i] = min(minimumCost[i - 1] + cost[i - 1], minimumCost[i - 2] + cost[i - 2]).

Algorithm 2 Top-down approach
As you can see, as we populate minimumCost, it becomes possible to solve future subproblems. For example, before solving the 5th and 6th steps we are required to solve the 4th step.

At the end, return the final element of minimumCost. Remember, we are treating this "step" as the top floor that we need to reach.

As you can see, there are a ton of repeat computations. When there are only 5 stairs, it might not seem that bad. However, imagine if there were 6 stairs instead. This entire image would be one child of the root. As n increases, the amount of computations required grows exponentially. So, how do we resolve this issue? If we calculate, say, minimumCost(3), then why should we calculate it again? Instead of going through the entire subtree every time we want to calculate minimumCost(3), let's just store the value of minimumCost(3) after calculating it the first time, and refer to that instead.

This is what memoization is - caching "expensive" function calls to avoid duplicate computations. Imagine what the recursion tree would look like for a call to minimumCost(10000), and how expensive calls like minimumCost(9998) would be to compute multiple times. We can use a hash map for the memoization, where each key will have the value minimumCost(key).

Algorithm

Define a hash map memo, where memo[i] represents the minimum cost of reaching the i^{th}i th step.
Define a function minimumCost, where minimumCost(i) will determine the minimum cost to reach the i^{th}ith  step.

In our function minimumCost, first check the base cases: return 0 when i == 0 or i == 1.
Next, check if the argument i has already been calculated and stored in our hash map memo. If so, return memo[i].
Otherwise, use the recurrence relation to calculate memo[i], and then return memo[i].

Simply call and return minimumCost(cost.length). Once again, we can make use of the trick from approach 1 where we treat the top floor as an extra "step".
Since cost is 0-indexed, cost.length will be an index 1 step above the last element of cost.
'''


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        minCost =[0 for i in range(len(cost)+1)]
        minCost[0] = 0
        minCost[1]= 0
        for i in range(2, len(cost)+1):
            minCost[i] = min(minCost[i-1]+cost[i-1],minCost[i-2]+cost[i-2])
        return minCost[len(cost)]

s = Solution()
cost = [10,15,20]
cost1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(s.minCostClimbingStairs(cost))
print(s.minCostClimbingStairs(cost1))