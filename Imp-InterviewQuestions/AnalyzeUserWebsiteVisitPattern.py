# https://leetcode.com/problems/analyze-user-website-visit-pattern/
#
# You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].
#
# A pattern is a list of three websites (not necessarily distinct).
#
# For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
# The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.
#
# For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
# Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
# Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
# Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.
#
# Example 2:
#
# Input: username = ["ua", "ua", "ua", "ub", "ub", "ub"], timestamp = [1, 2, 3, 4, 5, 6], website = ["a", "b", "a", "a","b", "c"]
# Output: ["a", "b", "a"]
#
# Example 1:
#
# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation: The tuples in this example are:
# ["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
# The pattern ("home", "about", "career") has score 2 (joe and mary).
# The pattern ("home", "cart", "maps") has score 1 (james).
# The pattern ("home", "cart", "home") has score 1 (james).
# The pattern ("home", "maps", "home") has score 1 (james).
# The pattern ("cart", "maps", "home") has score 1 (james).
# The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
from collections import defaultdict, Counter
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        '''
        Create tuples as shown in description
        The timestamps may not always be pre-ordered (one of the testcases)
        Sort first based on user, then time (grouping by user)
        This also helps to maintain order of websites visited in the later part of the solution
        '''
        users = defaultdict(list)
        '''
        Iterate over the set of username, timestamp, website and which is sorted with key as username and timestamp.
        The order of sorting should remain the same.
        and store the website approriately to the users dictionary for that user.
        '''
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[user].append(site)
        print(users)
        pattern = Counter()
        '''
            1. first get all possible 3-sequences combinations(sites, 3)
            2. then, count each one once (set)
            3. finally, count the number of times we've seen the 3-sequence for every user (patterns.update(Counter)) 
            - updating a dictionary will update the value for existing keys accordingly (int in this case)
        '''
        for user, site in users.items():
            user_site_cominations = combinations(site, 3)
            unique_user_site_combinations = set(user_site_cominations)
            # print("set combinations=", unique_user_site_combinations)
            # counting number of patterns
            unique_user_site_combinations = Counter(unique_user_site_combinations)
            # print("unique counter=",unique_user_site_combinations)
            pattern.update(unique_user_site_combinations)
            # print("pattern final = ",pattern)
            # print("max counter=",max(sorted(pattern),key=pattern.get))
            # get most frequent 3-sequence sorted lexicographically)
        return max(sorted(pattern), key=pattern.get)


s = Solution()
username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
s.mostVisitedPattern(username, timestamp, website)
