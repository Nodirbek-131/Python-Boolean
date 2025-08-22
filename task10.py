from getpass import getpass

entered = input("Xabar:")
secret = getpass("Yashirin habar:")

result = entered == secret

print(result)