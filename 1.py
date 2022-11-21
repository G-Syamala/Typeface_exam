class Problem1:
   def solution(self, n):
      sign = '-' if n<0 else ''
      n = abs(n)
      if n < 3:
         return str(n)
      s = ''
      while n != 0:
         s = str(n%3) + s
         n = n//3
      return sign+s
ob = Problem1()
print(ob.solution(10))
