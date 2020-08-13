class login(Exception):
    pass
def signup():
    m=input("how many ids ur using:")
    count=1
    while count<=int(m):
        a = input("enter the username:")
        b = input("enter the password:")
        count+=1

        SpecialSymbol = ['$', '@', '&', '#', '*']
        if len(b) < 5:
            raise login("password should contain morethan 5 characters")
        if len(b) > 15:
            raise login("password should contain lessthan 5 characters")
        if not any(char.isdigit() for char in b):
            raise login("password should contain atleast one numerical character")
        if not any(char.isupper() for char in b):
            raise login("password should contain atleast one uppercase character")
        if not any(char.islower() for char in b):
            raise login("password should contain atleast one lowercase character")
        if not any(char in SpecialSymbol for char in b):
            raise login("password should contain atleast one special character")
        print('-' * 25)
        print("signup done successfully")
        print('-' * 25)
    x = input("enter the username:")
    y = input("enter the password:")
    if b or b==y:
        print('-' * 25)
        print("login done suceessfully...")
        print('-' * 25)
        print('*'*25)
        print("WELCOME...",x)
        print('*'*25)

    else:
        raise login("invalid password!!,,,,,Trt Again")
signup()


