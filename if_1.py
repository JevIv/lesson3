age = int(input("Hello my darling!\nPlease type your age!: "))
reply = ("I am guessing, that you")


def guess(age):
    if age < 6:
        return(f"{reply} study in kindergarten!")
    elif 6 <= age < 16:
        return(f"{reply} study at school!")
    elif 16 <= age < 21:
        return(f"{reply} study in University!")
    else:
        return(f"{reply} you are employed!")

result = (guess(age))
print(result)

if __name__ == "__main__":
    guess(age)
