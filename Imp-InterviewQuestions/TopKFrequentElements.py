# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]

'''
Explanation:

find the first k most reoccuring elements in the dictionary

* Find the frequency using hashmap/dictionary using counting freq
* sort the dictionary based on dictionary values/ frequencies in descending order
* return the top most k key elements from the dictionms

* PS : find a bettter solution than O(nlogn)
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict ={}
        order_freq = {}
        result =[]
        final_result =[]
        for i in nums:
            if i not in dict:
                dict[i] =1
            else:
                dict[i]+=1
        print(dict)
        for k,v in dict.items():
            if v not in order_freq:
                order_freq[v] = [k]
            else:
                order_freq[v].append(k)

        print("ordered freq=", order_freq)
        arr =[]
        for x in (range(len(nums), 0, -1)):
            if x in order_freq:

                for i in order_freq[x]:
                    arr.append(i)
        print(arr)
        return [arr[x] for x in range(0, k)]

        # sorted_dict= sorted(dict.items(), key= lambda x:x[1], reverse=True)
        # print("Sorted dict = ",sorted_dict)
        # print("result =",result)
        # for i in range(0,k):
        #     final_result.append(sorted_dict[i][0])
        # print(final_result)
        # return final_result


s = Solution()
nums = [4,1,-1,2,-1,2,3]
k = 2
nums1 = [1]
k1 = 1
print("result =",s.topKFrequent(nums, k))
print("result ",s.topKFrequent(nums1, k1))