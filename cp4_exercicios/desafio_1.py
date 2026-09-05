email = input('Digite os e-mails: ')
email = email.split(',')

#print(email)
usernames = []
dominios = []


for i in email:
    username, dominio = i.split('@')
    usernames.append(username)
    dominios.append(dominio)

def count_letters(dominios):
    d = dict()
    for c in dominios:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print("Relatório:")
print("Quantide de e-mails por domínio")
print(count_letters(dominios))
print(f"lista de usuários{usernames}")

usernames[0], usernames[-1] = usernames[-1], usernames[0]

print(f"Após troca de posições{usernames}")

tupla = tuple(usernames)


