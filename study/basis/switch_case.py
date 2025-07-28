val = 2
match val:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case 3:
        print("Value is 3")
    case _:
        print("Value is something else")

# combine values in a case
val = 3
match val:
    case 1 | 2:
        print("Value is either 1 or 2")
    case 3 | 4:
        print("Value is either 3 or 4")
    case _:
        print("Value is something else")

# if statement as guard
locker = True
val = 5
match val:
    case 1 if locker:
        print("Value is 1 and locker is open")
    case 2 if not locker:
        print("Value is 2 and locker is closed")
    case _:
        print("Value is something else")
