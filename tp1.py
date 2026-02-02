#Exercice 1
def message(nom):
    message = "bienvenue " + nom + " !"
    print(message)
#message(input("Veuillez indiquez votre nom"))

#Exercice2
def multiplication(table,nombre):
    i = 0
    while i<=nombre:
        print(f"{table} * {i} = {table*i}")
        i += 1
#multiplication(int(input()),int(input()))

#Exercice3
def diviseur():
    numerateur = int(input("Choissiez un nombre supérieur à 1 "))
    if numerateur <= 1 :
        int(input("Choissisez un nombre supérieur à 1 !!! "))
    res = []
    i = 2
    while i<numerateur:
        if numerateur%i==0 :
            res.append(i)
        i += 1
    if len(res) == 0 :
        print(f"{numerateur} est un nombre premier")
    print(res)
#diviseur()

#Exercice4
def nb_premier():
    tab = [2]
    i = 3
    while len(tab)<=100:
        nb_premier = True

        for premier in tab:
            if i % premier == 0 :
                premier = False
                break
        if premier :
            tab.append(i)
        i += 1
    print(tab)
#nb_premier()


#Exercice5
def fibonnacci(n):
    mul_1 = 0
    mul_2 = 1
    res = 0
    i = 0
    while i<n :
        res = mul_1 + mul_2
        print(res)
        mul_1 = mul_2
        mul_2 = res
        i += 1
#fibonnacci(5)

#Exercice6
def phare(nb_marche,hauteur_phare):
    total_marche = nb_marche*hauteur_phare*2*5*7
    total_parcourue = total_marche/100
    print("pour ", nb_marche, " et de ",hauteur_phare, " il parcours total_parcourue {:.2f}".format(total_parcourue), "par semaine")
#phare(200,10)


#Exercice7
def valide(ch_adn):
    cond_adn = "atgc"
    i = 0
    while i < len(ch_adn):
        if ch_adn[i] not in cond_adn:
            return False
        i += 1
    return True

#print(valide(input("Entrez une séquence : ")))


def saisie_valide():
    texte = input("Entrez votre séquence")
    while not valide(texte):
        texte = input("Entrez votre sequence")
    return print(texte)
#saisie_valide()

def proportion(chaine, sequence):
    nb_occurrences = chaine.count(sequence)

    if len(chaine) == 0:
        return 0

    prop = (nb_occurrences * len(sequence) / len(chaine)) * 100
    return prop

def saisie():
    chaine = input("chaîne : ")
    sequence = input("séquence : ")
    return chaine, sequence

chaine_utilisateur, sequence_utilisateur = saisie()
resultat = proportion(chaine_utilisateur, sequence_utilisateur)

print(f'Il y a {resultat:.2f} % de "{sequence_utilisateur}" dans votre chaîne.')
