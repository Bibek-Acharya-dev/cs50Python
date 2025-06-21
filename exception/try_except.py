# while True:
#     try:
#          x= int( input( " Whats's x?"))
#     except ValueError:
#          print("x is not an integer")    
#     else:    
#          if x>=0:
#             print(" x is positive")
#             break
#          else:
#             print("x is negative")
#             break 


# another approach

while True:
    try:
        x = int(input("What's x? "))
        print("x is positive" if x >= 0 else "x is negative")
        break  # break only if input is valid
    except ValueError:
        print("x is not an integer")

    