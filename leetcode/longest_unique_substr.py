"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def longest_substr(s):
    my_dict = {}
    longest = 0

    for i in range(len(s)):
        j = i# 0,1
        while j < len(s):
            if my_dict.get(s[j], False): #false:a,false:b,false:c,true:a|false:p,false:w,true:w, 
                if len(my_dict) > longest: # true| true
                    longest = len(my_dict) # 3,| 2
                    my_dict = {}
                    my_dict[s[j]] = repr(j)
                    break
            else:
                    my_dict[s[j]] = repr(j) # {a=1, b=2, c=3}
            j +=1 # 1,2

    # in case it's all unique str
    if len(my_dict) > longest:
        longest = len(my_dict)
    return longest

s = "abcabcbb"
print(longest_substr(s))

s = "bbbbbb"
print(longest_substr(s))

s = "pwwkew"
print(longest_substr(s))

s = " "
print(longest_substr(s))

s = "au"
print(longest_substr(s))

s = "bwf"

print(longest_substr(s))
