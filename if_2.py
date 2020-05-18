#first=input("Please type something:")
#second=input("Please type something again:")
first="l"
second="learn"

def check_strings(first, second):
    if type(first) != str or type(second) != str:
        return 0
    else:
        if first == second:
            return 1
        if first != second and len(first) > len(second):
            return 2
        if first != second and second == "learn":
            return 3
        else:
            return 4


print(check_strings(first, second))
