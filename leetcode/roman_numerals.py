"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """

def roman_to_integer(rs):
    total = 0
    my_dict = {
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000
    }
    if len(rs) == 1:
        return my_dict[rs[0]]
    my_list = []
    previous = 0

    for i in range(len(rs)):
        my_list.append(rs[i])

    while len(my_list) > 0:
        val = my_dict[my_list.pop()]
        if val > previous:
            total += val
        else:
            total -= val

        previous = val

    return total

def antother_solution(rs):
    total = 0
    my_dict = {
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000
    }

    if len(rs) == 1:
        return my_dict[rs[0]]

    my_list = []
    previous = 0
    ls = len(rs) # 3
    for i in range(ls): # III
        j = ls - i - 1 #2 
        val = my_dict[rs[j]] # I
        if val >= previous:
            total += val
        else:
            total -= val

        previous = val

    return total


# s = "III"
# print(roman_to_integer(s))

# s = "LVIII"
# print(roman_to_integer(s))

# s = "MCMXCIV"

# print(roman_to_integer(s))

# -------------------

print("END----------")

s = "III"
print(antother_solution(s))

s = "LVIII"
print(antother_solution(s))

s = "MCMXCIV"

print(antother_solution(s))



