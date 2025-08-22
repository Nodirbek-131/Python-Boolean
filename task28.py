from getpass import getpass


pasword = getpass("Parol kiriting: ")

parol1 = '\"\"'
parol2 = 'secret'

result = pasword != parol1 or pasword != parol2
print(result)