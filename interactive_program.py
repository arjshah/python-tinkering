# Using inputs to collect user data
voting_age = input("How old are you? ")
voting_age = int(voting_age)

if voting_age >= 18:
    print("\nYou are old enough to vote!")
else:
    print(f"\nAt {voting_age}, you are not yet old enough to vote")

# Playing with while loop and flags
prompt = "\nSay something and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
