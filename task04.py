from getpass import getpass

password = getpass("password: ")

result = len(password) >= 8
print(result)
