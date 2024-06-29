
Sub1 = input("Enter first marks")
Sub1 = int(Sub1)

Sub2 = input("Enter second marks")
Sub2 = int(Sub2)

Sub3 = input("Enter third marks")
Sub3 = int(Sub3)

if(Sub1 < 33 or Sub2 < 33 or Sub3 < 33):

   print("You failed the exam")


if(Sub1 + Sub2 + Sub3)/3 < 40:

    print("You failed")

else:
    print("You passed the exam")





