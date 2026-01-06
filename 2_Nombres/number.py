# verification d'un type de nomnbre
type(33)

print(type)

type(2.0)

print(type)

# transtypage typecast
# addition de deux float

somme = 33.9 + 23.8

# affichage du resultat

print(somme)


type(somme)

## affichage du type
print(type)

## conversion du type en integer

somme = int(somme)

# affichage de la conversion
print(somme)

# c
type(somme)

## affichage 
print(type)

print(2/2)

print(2//2)

#mini projet horticole

#Demande de quntite et calcule des prix TTC
pot     = int(input('Combien de pot de fleurs ?: '))
graines = int(input('Combien de sac de graines ?: '))
terreau = int(input('Combien de sachet de terreau ?: '))

#prix unitaire hors taxe

prix_pot     = 4.00
prix_graines = 1.00
prix_terreau = 5.00

#Taxe TVA
Taux_taxe = 0.20

#Calcul du total hors taxe

Total_HT = (pot * prix_pot) + (graines * prix_graines) + (terreau * prix_terreau)

print(F"Total hors taxe est :  {Total_HT}")

#Calcul du montant TTC

Total_TTC = Total_HT + (Total_HT * Taux_taxe)
print(F"Montant net a payer: {Total_TTC}")
