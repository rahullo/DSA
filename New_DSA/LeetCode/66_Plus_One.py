class Solution:
    def plusOne(self, digits):
      integer = 0
      for num in digits:
        integer = (integer*10) + num
      integer+=1
      ans = []
      while integer:
         ans.append(integer%10)
         integer = integer // 10
      ann = ans[::-1]
      return ann
    
    def plusOne_2(self, digits):
       for i in range(len(digits)-1, -1, -1):
          if digits[i] == 9:
             digits[i] = 0
          else:
             digits[i]  += 1
             return digits
       return [1] + digits

s = Solution()
print(s.plusOne_2([2, 4, 4, 9, 0, 9]))