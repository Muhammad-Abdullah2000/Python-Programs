
Letter = ''' Dear |<NAME>|
I am very happy to inform you that you are eligible for this job and you are also selected for this \n
job. Hope that you will work hard

you are selecred
Have a great day ahead!

Date: |<DATE>|'''

name = input("Enter your name \n")
date = input("Enter date \n")

Letter = Letter.replace("|<NAME>|",name)
Letter = Letter.replace("|<DATE>|",date)

print(Letter)