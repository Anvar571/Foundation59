def Tubmi(son):
        if son < 2:
            return False
        for i in range(2, son//2):
            if not son % i:
                return False
        return True
