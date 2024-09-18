email = input('Insira o seu email: ')

index = email.index('@')

username = email[:index]
dominio = email[index:]

print(f" seu username é {username} e seu dominio é {dominio}")