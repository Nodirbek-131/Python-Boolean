from getpass import getpass

pasword = getpass("Parol:")
confirm = getpass("Parol qiymati:")

result = pasword == confirm

print(result)