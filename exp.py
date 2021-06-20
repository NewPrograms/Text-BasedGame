def undeadmon_att_succ():
        # This is for zombie and skeleton who are undead!
        
        val = []        
        ans = 0.6
        print(division(4, 1))

def division(a, b):
    val = []
    if a < b:
        return a
    else:
        ans =  0.125 + division(a - b, b)
        print(ans)
        return ans
    

undeadmon_att_succ()