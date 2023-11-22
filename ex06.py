#compteur de mot :ecrire un script qui compte le nombre de mots dans une phrase (exemple: entree: "le test logiciel est essentiel" sortie: 5)

phrase = "j ai 2 boutons"
compteur = 1
for i in phrase:
    if i == " ":
       compteur =compteur + 1 #ou noter compteur +=1
print(compteur)

#facon split
entree ="p l m"
nombre_de_mot = 0
for mot in entree.split():
    nombre_de_mot = nombre_de_mot + 1
print(nombre_de_mot)    

#autre facon
chaine = "moi loo nous vous a demain"
def compter_mots(chaine):
    return len(chaine.split())
print(len(chaine.split()))

#autre methode par tom methode foreach
prompt = "le test"
array = []
space = False
var = ""
for i in prompt:
    if i == "":
        space = True
    else :#concatenation
         space = False  
    if space :
        array.append(var) #ajouter un element au tableau
        var = ""       
    else :
        var = var + i    
if i != "":
     array.append(var)     


result = 0
for i in array :     
    result = result + 1
print(result)    


