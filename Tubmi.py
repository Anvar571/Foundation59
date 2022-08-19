 def Tubmi(son):
 2     if son<2:
 3         return False
 4     for i in range(2,son//2):
 5         if not son%i:
 6             return False
 7     return True
 8     
