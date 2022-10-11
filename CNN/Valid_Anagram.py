class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      a={}
      b={}
      for i in s:
        if i in a:
          a[i]+=1
        else:
          a[i]=1
      for i in t:
        if i in b:
          b[i]+=1
        else:
          b[i]=1
      if a==b:
        return True
      else:
        return False
      
s=Solution()
s1 = "anagram"
t1 = "nagaram"
print(s.isAnagram(s1,t1))
s2 ="rat"
t2="car"
print(s.isAnagram(s2,t2))