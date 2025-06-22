n=int(input("enter n: "))
summ=0
store=0

for i in range(n):
    num=int(input("enter number :"))
    summ+=num
    if num>store:
        store=num
    sum_of_rest=summ-store     
if(sum_of_rest==store):
    print("yes, ",sum_of_rest)
else:
    print("no, ",sum_of_rest-store)


       
