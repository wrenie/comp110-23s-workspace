"""knock knock joke with conditionals"""

inter_cow: str = input("Do you want a silly little interrupting cow?")

if (inter_cow == "yes"):
    print("Knock Knock!")
    print("...who's there?")
    print("Interrupting cow :)")
    print("...interrupting cow wh--")
    print("MOOOOOOOOOOO!!!")
else:
    print("Oh... okay.. I guess")
    if (inter_cow == "you're not funny"):
        print("i'm under your bed right now")