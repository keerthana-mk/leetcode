# Robot Bounded In Circle
# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
#
# The north direction is the positive direction of the y-axis.
# The south direction is the negative direction of the y-axis.
# The east direction is the positive direction of the x-axis.
# The west direction is the negative direction of the x-axis.
#
# The robot can receive one of three instructions:
#
# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
# Example 1:
#
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
# "G": move one step. Position: (0, 1). Direction: South.
# "G": move one step. Position: (0, 0). Direction: South.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
# Based on that, we return true.
'''
0 = north, 1 = east, 2 = south, 3 = west
With a move (G) in any direction, you will go 1 unit.
So you need to add 1 unit with x or y depending on
which direction you are going. For example,
if you go north from (x,y), then new position would be
(x, y+1) which is you get by x = x+0, y = y+1.
Now think about how you can get new position for other direction
So creating a dictionary with directions as keys and the
amount we need to add with x and y while we go for 1 unit
as value.
Now the idea is if after executing the instructions, if you
get your final position at (0,0) or if you are not facing north
direction, that means you will be in circle. Not facing north
direction means, as you can repeat the instructions, if you are
not facing north after 1st execution of the instructions, just
repeat 3 more times of the same instructions, you will see
yourself at the origin. Think about with 'GL' or 'GR'
instructions as an example. With instruction 'GLGR', you
can't be back at origin, no matter how many times you repeat.
'''


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        direction = 0  # north direction
        possible_directions = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
        print(instructions)
        for instruction in instructions:
            if instruction == 'L':
                direction = (direction + 3) % 4
            elif instruction == 'R':
                direction = (direction + 1) % 4
            else:
                x = x + possible_directions[direction][0]
                y = y + possible_directions[direction][1]
        # Finally, if you get your final position at (0,0) or if you
        # are not facing north direction, that means you will be
        # in circle.
        return (x ==0 and y ==0) or direction!=0


s = Solution()
instructions = "GGLLGG"
print(s.isRobotBounded(instructions))
