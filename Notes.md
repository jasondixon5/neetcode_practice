## Arrays & Hashing

### Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

Approach 1:
Compare each item in the array to the items in the rest of the array to find a duplicate
Time O(n2)
Space O(1) (if not counting original memory for input)

Approach 2:
Sort the array first. Only have to iterate through the array once and compare two neighbors in the array and checking if they're duplicates.
Time O(n) + O(nlogn) for sorting, so  O(nlogn)
Space O(1) 

Approach 3:
Use a hash set. If an item does not exist in our hash set, add it. If it does, then we've found a duplicate
Time O(n)
Space O(n)

### Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Pre-Approach Notes:
To call t an anagram of s, each string has the same characters and the same number of those characters. This means the two strings are of equal length.

Approach 1:

Use two hash maps, one for each string.
Build each hash map with the characters in the string as the keys and the count of those characters as the values.
Iterate through the first hash map and compare the counts.
If a count is different or a character in the first hash map is not found in the second, then the hash maps are not equal.

Time O(s + t) - have to iterate through each string
Memory O(s + t) - hash maps are size of s and size of t

Approach 2:

Do same approach but using Counter class. 
return Counter(s) == Counter(t)
Same time and space complexity

Approach 3:

Sort the characters in each string & then do an == oper on 

Sort could be time n2 for bad algos or at best nlogn
Space complexity might use O(n) but sometimes could run on constant extra memory, i.e., O(1). Many interviewers think sorting doesn't take extra space.

Memory O(1)


### Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Pre-Approach Notes:
If trying to find a sum target, then looking for an integer that satisifes target - number

Approach 1
Start with first integer. Check each remaining item and see if it and the first integer equal target. Repeat with second integer. (Note: Don't have to repeat first integer in array in this case because already checked that combiantion.)
Time O(n2)

Approach 2
Make hash map of every item in the array. The key is the item, the value is the index. But when start iterating throough array, will hit first item in array and it will be in hash map when we check it. But that's the element that's in the hash map so we can't use it. So not clear this appraoch works.

Approach 3
Start with empty hashmap. Iterate through array. For each element , subtract from target and check if item is in hash map. If not, add the item (item is key, index is value).

Time O(n)
Memory O(n) (potentially will add every item to the hash map)

### Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Approach 1:

Take each string
Sort them
But time complexity is nlogn * m (where m is length of input list)

Approach 2:

Constraint says each character is lower-case a to z so at most have 26 characters
Create array count
From each string, count chars a - z (e.g., eat has 1 e, 1 a, 1 t)
Use hash map - key is the count, value is the list of anagrams, i.e., which strings have the pattern in the key

O(m * n * 26) where m is the total # of input strings given and n is the avg length of a string (because have to iterate over string to count number of times for each character) - * 26 because that's length of the count array but it reduces so actual time complexity is O(m * n)

Note that array count will have to be initialized to have a 0 in each idx
Then when iterating over string, have to have some way of putting new count in right idx. 
One approach is to use ord() funct to get ASCII value of the character and then subtract ord("a") from that (e.g., ord(c) - ord("a")); for "a" result is zero, for "z" result is 25, thus giving correct idx.

Another trick is to use a default dict for the hash map where the default val is a list i.e., defaultdict(list)

One noteable detail is that an array can't actually be a dict key, so need to wrap the array in a tuple() call when appending the count array 
i.e., res[tuple(count)].append(s)

### Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Pre-Approach Notes:

Approach 1:

Count the number of occurrences of each value
Sort by the counts in asc order
Return the values with the highest counts
O(nlogn)

Approach 2:

Use a heap and heap sort
Pop from heap k times
Each pop takes log n, do this k times, so O(klogn)

Appraoch 3:
O(n) time and O(n) memory

Use modified algorithm bucket sort
Let the index be the count and the values be a sublist of the input items that appear that many times

input [1, 1, 1, 2, 2, 100]
0  1      2     3    4   5    6
[] [100] [2]    [1]  []  []   []

With this approach the new array is bounded by the size of the input array
e.g., an input array of size 6 will only need to store 



Encode and Decode Strings

#659 on Leetcode
Lintcode - solve for free
Premium on Leetcode

Design an algorithm to encode a list of strings to a [single] string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

Approach 1:

For each string in the array, count the length of it
In the intermediate output (the encoded string), will put the char count and another character like a # as a delimiter.

e.g., ["neet", "co#de"] becomes "4#neet5#co#de"
Then can decode by reading 4 and #, then the next 4 characters _even if one ofo the next 4 is an integer or the delimiter char_
