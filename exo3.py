#ecrire un script qui trove le plus grand nombre dans 1 liste exemple: entree[3,58,11,21] sortie:58


array = [3,58,11,21]
maxvalue = array[0]
for var in range(len(array)):
    if array[var] > maxvalue:
        maxvalue = array[var]
print(maxvalue)  

maxvalue = 0
for var in array :
    if var > maxvalue:     #maxvalue peut aussi s appeler sortie
        maxvalue = var
print(maxvalue)

    
    













