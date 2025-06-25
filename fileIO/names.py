# writing on a file 

# name=input("Whats your name? ")

# with open("names.txt","a") as file:
#     file.write(f"{name}\n")



# reading from a file
# with open("names.txt","r") as file:
#     lines=file.readlines()
# for line in lines:
#     print("hello, ", line.rstrip())    

# or

with open("names.txt","r") as file:
    for line in file:
        print("hello, ",line.rstrip())



