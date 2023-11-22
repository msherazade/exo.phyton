#creer un programme qui verifie si un mot est un palindrome exemple entree :radar sortie true

#def printResult
mot = "bonjour" # bonjour != ruobnob si different de
array = list(mot)
print(array)
count = len(array)
print(count)
est_palindrome = True
result = ''
for i in range(count):
    result = result + array[count-(i+1)] #attention al ordre de positionnement des element car il s agit de 2 string QUI SE CONCATENE

if mot == result :
    print(True)
else :
    print(False)     




    #boucle foreach 2éme méthode
#result=""
#for i in array:
#      result = i + result
#print(printResult(mot, result))



    
    






