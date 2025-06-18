name=input("enter your name").capitalize()
match name:
    case "Harry" | "Hermoine" |"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who? default")          
