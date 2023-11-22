#compteur de mot :ecrire un script qui compte le nombre de mots dans une phrase (exemple: entree: "le test logiciel est essentiel" sortie: 5)

phrase = "j ai 2 boutons"
compteur = 1
for i in phrase:
    if i == " ":
       compteur =compteur + 1 #ou noter compteur +=1
print(compteur)

#facon split
entree ="le test logiciel est logiciel"
nombre_de_mot = 0
for mot in entree.split():
    nombre_de_mot = nombre_de_mot + 1
print(nombre_de_mot)    


