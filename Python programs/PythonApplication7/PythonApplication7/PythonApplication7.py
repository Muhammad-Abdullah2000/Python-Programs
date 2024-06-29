
m1 = input("Enter 1st number")
m1 = int(m1)

m2 = input("Enter 2nd number")
m2 = int(m2)

m3 = input("Enter 3rd number")
m3 = int(m2)

m4 = input("Enter 4th number")
m4 = int(m4)


if(m1 > m2):

    f1 = m1

else:
    f1 = m2

    if (m3 > m4):
        f2 = m3

    else:
        f2 = m4

if(f1 > f2):

        print(str(f1) + " is greatest")
else:

        print(str(f2) + " is greatest")




