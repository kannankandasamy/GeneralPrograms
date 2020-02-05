"""Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make 
it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string st

A string consisting of lowercase English letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

[output] string
"""

def buildPalindrome(st):
    stk, s, n = [], list(st), len(st)
    for i in range(n):
        if s==s[::-1]:
            break
        else:
            stk.append(s[0])
            del s[0]
    while stk:
        i = stk.pop()
        s.insert(0,i)
        s.append(i)
    return "".join(s)  
