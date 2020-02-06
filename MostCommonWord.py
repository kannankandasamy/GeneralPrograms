"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  
The answer is in lowercase.

Example:
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
"""
import string
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    dic, punc, p = dict(), ".!?',", paragraph
    for c in string.punctuation:
        p = p.lower().replace(c, " ")
    for i in p.split():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in sorted(dic.items(), key = lambda x:x[1], reverse= True):
        if i[0] not in banned:
            return i[0]
