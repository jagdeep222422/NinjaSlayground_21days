from typing import List

def printNos(x: int) -> List[int]: 
    # Write your code here
    if (x==0):
        return []
    else:
        arr=printNos(x-1)
        arr.append(x)
        return arr    
   
