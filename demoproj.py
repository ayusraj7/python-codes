print('create account now ')
username=input('Enter username:')
password=input('Enter password:')
print('your account has been created successfully')
print('Login now')
username2=input('Enter username:')
password2=input('Enter password:')

if username==username2 and password==password2:
    print("logged in successfully")
else:
    print("incorrect credentials")