

import random

def GameWin(Computer, Abdullah):
    if Computer == Abdullah:
        return None
    elif Computer == 'R':
        if Abdullah == 'S':
            return False
        elif Abdullah == 'P':
            return True
        elif Computer == 'S':
            if Abdullah == 'P':
                return False
            elif Abdullah == 'R':
                return True
            elif Computer == 'P':
                if Abdullah == 'R':
                    return False
                elif Abdullah == 'S':
                    return True

print("Computer Turn : Rock(R) , Paper(P) , Scissor(S)")

randNo = random.randint(1, 3)

if randNo == 1:
    Computer = 'R'
if randNo == 2:
    Computer = 'P'
if randNo == 3:
    Computer = 'S'

Abdullah = input("Your turn : Rock(R) , Paper(P) , Scissor(S)")

a = (Computer, Abdullah)

print(f"Computer choose {Computer}")
print(f"You choose {Abdullah}")

if a == None:
    print("Game is Tie")

elif a == True:
    print("You won")
else:
    print("You Loose")
