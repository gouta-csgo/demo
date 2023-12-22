def recursive(x, ans):
    if x == 0:
        return 
    recursive(x-1, ans)
    
    ans.append(x)
    
def print(x):
    ans = []
    
    recursive(x, ans)
    
    return ans

print(print(x= 5))