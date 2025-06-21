
#    *
#   * *
#  * * *
# * * * *
rows=int(input("enter rows: "))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" " )
         
    print()              
        


# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *

row=int(input("Enter number of rows: "))

for i in range(rows):
    if (i>0):
        for j in range(i):
            print(" ",end="")
    for k in range(rows-i):
        print("* ",end="")
    print()        

