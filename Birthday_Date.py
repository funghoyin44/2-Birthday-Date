questions = ("day", "month", "year")
birthday = []

def question():
    for i in questions:
        answer = input("What is your birthday %s?" % (i))
        answer = int(float(answer))
        birthday.append(answer)

print("Hello, please tell me your birthday detail!\nI will help you to summerize it")
question()
print("Your birthday is %02d - %02d - %04d." % (birthday[0], birthday[1], birthday[2]))