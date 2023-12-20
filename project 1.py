#banking application
ac_no=0
branch_code=" "
mobile= 0
bal =0
def createAccounts():
    global cus_name
    global branch_code
    global mobile
    global bal
    ac_no= int(input("enter account number :"))
    cus_name=input("enter your name :")
    branch_code=int(input("enter brach code :"))
    mobile=int(input("enter mobile number :"))
    bal=int(input("enter current balence : "))
def showacdetails():
    print("account NO:",ac_no )
    print("costomer_name:",cus_name)
    print("branch_code:",branch_code)
    print("mobile no:",mobile)
def deposite(amount):
    global bal
    bal=bal+amount
    check_balence()
def withdraw(amount):
    global bal
    bal=bal - amount
    check_balence()
def check_balence():
    print("current balence:",bal)

#main
choice1='y'
while(choice1=='y'):
    welcome = input("welcome to our banking appilication.please press ENTER to continue")
    print("1.accounts\n 2.withdraw\n 3.deposite\n 4.check_balence")
    choice=int(input("select any option:"))
    if choice==1:
        createAccounts()
    elif choice==2:
        amount=int(input("enter amount to withdraw"))
        withdraw(amount)
    elif choice==3:
        amount=int(input("enter amount to deposit"))
        deposite(amount)
    elif choice==4:
        check_balence()
    else:
        print("please select any 4 options above")
    print("do you want to continue...press y")
    choice1=input()