# Ask the user:
# "Do you want to continue? (yes/no): "
# Keep asking until the input is "yes" or "no".

while True:
    answer=input("Do you want to continue? (yes/no):")
    if answer=="yes" or answer=="no":
        print(f"your entered answer is {answer}")
        break
    else:
        print(f"invalid input !!!")