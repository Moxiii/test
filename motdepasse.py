import secrets
#definition des caractère a utilisé 
minuscule = [chr(i)for i in range(97,123)]
majuscule = [chr(i) for i in range (65,91)]
chiffres = [chr(i) for i in range (48,58)]
caracteres_speciaux = [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']
all = minuscule + majuscule + chiffres + caracteres_speciaux
print('Nous allons généré un mot de passe  ')
def generate():
    #si le nombre de mot de passe n'est pas définit il est par défaut a 12
    try: 
        nombre_mdp = int(input('Combien de mot de passe voulez-vous ? \n'))
    except ValueError : 
        print('le nombre de mot de passe est 12\n')
        nombre_mdp = 12 
    #si la taille n'est pas définit la taille par défaut a 20
    try:
        taille = int(input('\nEntrer la taille souhaité : \n'))
    except  ValueError:
        print('la taille par défaut est 20 charactère\n')
        taille = 20
    while nombre_mdp > 0 : 
        password = ''.join(secrets.choice(all) for i in range(taille))
        print(password)
        nombre_mdp = nombre_mdp-1 
generate()
print('Voulez-vous regénéré des mot de passe ? ')
def choix():
    global c
    c = int(input('1.OUI\n2.NON\n>'))
    return c

choix()
while c == 1:
    generate()
    choix()
