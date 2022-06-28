#starter program
#script one/dictornary
print("Helli, World!")
print ("dictonary")

def Zombies():
    Zombies = {"Zombie ID":"Script Value",
           "001":"script01.py",
           "002":"script02.py",
           "003":"Script03.py",
           "004":"Script03.py"}
    print(Zombies)
def Form():
    name = input("Enter username:")
    print("Username is: " + name)
    age= input("Enter age:")

    txt = "Your name is {1}. {1} is {0} years old."
    print(txt.format(age, name))

#print out numbers 1-100 by 2 numbers at a time or every even number
def Numbers():
    print(list(range( 1,100)))
def 
def main():
    Zombies()
    Form()
    Numbers()
main()
