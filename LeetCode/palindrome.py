'''
TimeComplexity = O(1)
Name: Bishal jaiswal    
'''

def isPalindrome(x:int) ->bool:
    my_str = str(x)
    if x<0:
        return False
    
    if my_str == my_str[::-1]:
        return True
        

    else:
        return False
        
print(isPalindrome(1010101))