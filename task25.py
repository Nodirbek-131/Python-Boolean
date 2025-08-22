from getpass import getpass

pasword = getpass("Parol kiriting:")
kiritilgan_parol = 'secret123'

result = pasword == kiritilgan_parol
print(result)