import string
import sys


class Solution:
    def longestPalindrome(self, str: string, n:int) -> str:
        table = [[0 for x in range(n)] for y in range(n)]
        maxLength=1
        i=0
        while(i<n):
          table[i][i]=True
          i=i+1
        start = 0
        i = 0
        while i < n - 1 :
            if (str[i] == str[i + 1]) :
                table[i][i + 1] = True
                start = i
                maxLength = 2
            i = i + 1
        k = 3
        while k <= n :
          i=0
          while i<(n-k+1):
            j = i + k - 1
            if (table[i + 1][j - 1] and
                      str[i] == str[j]) :
                table[i][j] = True
     
                if (k > maxLength) :
                    start = i
                    maxLength = k
            i=i+1
          k=k+1
        print ("Longest palindrome substring is: ")
        print (printSubStr(str, start,start + maxLength - 1))
        return maxLength
def printSubStr(st, low, high) :
    sys.stdout.write(st[low : high + 1])
    sys.stdout.flush()
    return ''

s=Solution()
st = "abacdgfdcaba"
l = s.longestPalindrome(st,12)
print ("Length is:", l)