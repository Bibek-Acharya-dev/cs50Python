import math

n=int(input("enter n: "))
leftSum=0
rightSum=0
for i in range(n):
    num=int(input("numbers"))
    if(i+1<=n/2):
        
        leftSum=leftSum+num
    else:
        rightSum=rightSum+num

if math.fabs(rightSum-leftSum)==0:
    print("yes, sum= ",leftSum+rightSum)
else:
    print("no, difference= ",leftSum-rightSum)    
