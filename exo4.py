#developper une fonction qui calcule la factorielle  d' un nombre exemple entréé:5 et sortie:120 car( 5!=5*4*3*2*1) fact peut aussi se nommer valeur ou result ect....



nbr = 5
fact = 1
for i in range(1, nbr+1):

    fact = fact * i
print (fact)


def factorielle (num):
        result = 1
        i = 0
        for i in range(num):
              result = result *(num-1)
              i=i+1
print(result) 


#autre facon de faire par tom 
entree = 5
for var in range(entree - 1):
    var = var + 1             # mettre un print ici pour debugger et voir ce qui se passe
    entree = var * entree

      
