welcome = input("მოგესალმებით სიმონ აგერ ზუკას ბანკში ძალიან მაგარი ბანკია და იცოდეთ: ")


#registeer
if welcome == "register":

    name = input("enter your name: ")
    email = input("Enter your email address: ")
    id = input("enter your id: ")
    phone = input("Enter your phone number: ")

    if len(phone) != 9:
        print("invalid phone number. Try again")
        input("enter phone number again: ")

    cvc = input("enter your cvc: ")

    if len(cvc) != 3:
        print("invalid cvc. Try again")
        input("enter cvc again: ")
    
    password = input("enter your password: ")

    if len(password) < 10:
        print("password must be at least 10 characters")
        input("enter your password: ")
        confrim = input("Confrim your password: ")

    if confrim != password:
        print("you entered wrong password")
        input("enter password again: ")

    print("--------end------------")
    print("you succesfully registered !!! Welcome to Goa Bank <3")
    print("""                                                                                                                                       

        """)


#login

if welcome == "login":
    name= input("enter your name: ")
    email = input("enter your email: ")
    password = input("enter your password forgot ? Y/N: ")
    if password == "Y" or password == "y":
        checkemail = input("enter your email: ")
        checkcode = input("enter your one time code: ")
        checkpassword = input("enter your new password: ")
        confrimPassword = input("confrim new password: ")

        if confrimPassword != checkpassword:
            print("you entered wrong password")
            input("enter password again: ")
        else:
            print("you succesfully changed your password")
            print("you succesfully logged in !!! მოგესალმებით აგერ სიმონ ზუკას ბანკში <3")
    else:
        input("enter your password: ")
        print("you succesfully logged in !!! მოგესალმებით აგერ სიმონ ზუკას ბანკში  <3")

#deposit

deposit = int(input("how much $ you want to deposit?: "))

if deposit == 0:
    print("you can't deposit 0$")
    input("how much $ you want to deposit?: ")

print("now on your bank account, you have " + str(deposit) + " $")
print("---------------------------")



#depos., with., tran.,

question = input("do you want to deposit again, withdraw or transfer ?: ")
if question == "deposit":
    newdeposit = int(input("how much $ you want to deposit"))
    deposit = deposit + newdeposit

print("now on your bank account, you have " + str(deposit) + " $")
print("""                                                                                                                                       

        """)
print("---------------------------")

#withdraw

if question == "withdraw":
    withdraw = int(input("how much $ you want to withdraw?: "))
    if withdraw > deposit:
        print("you can't withdraw more than you have")
        again = int(input("how much $ you want to withdraw?: "))

    print("now on your bank account, you have " + str(deposit - withdraw) + " $")
    print("---------------------------")




#transfer

if question == "transfer":
    transfer = input("do you want to transfer? (yes or no): ")
    
    if transfer == "yes":
        user_name = input("who you transfer to?: ")
        user_email = input("number of the person: ")
        transfer_to = int(input("how much he/she have?: "))
        user_id = input("id of the user: ")
        transfer_user = int(input("how much you want to transfer?: "))
        if transfer_user > deposit:
            print("you can't transfer more than you have")
            transfer_user = int(input("how much $ you want to transfer?: "))

        print("transfer succesfully  ")
        print("now you have " + str(deposit - transfer_user) + " $")
        print("now second acc have " + str(transfer_to + transfer_user) + " $")

#dellacc
def delete_account():
    delete = input("გინა წაშალო აქაუნტი ? კი/არა: ")
    if delete == "კი":
        print("შენი აქაუნტი არის წაშლილი")
        print("---------------------------")
        print("გეიხარე რომ ხმარობ ზუკა ბანკს <3")
        exit()
    else:
        print("შენი აქაუნტი არ წეიშალა")
        print("---------------------------")
        print("გეიხარე რო ხმარობ ზუკას ბანკს<3")
