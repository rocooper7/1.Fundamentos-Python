#Eejemplo 1
def my_gen():     #Return corta en el primer argumento terminando la funcion , no regresa lo demas 
    a = 1
    yield a       #Yield hace un return parcial, no corta la funcion  

    a = 2
    yield a

    a = 3
    yield a


my_first_gen = my_gen()    #Esto se convierte en un iterador 

print(next(my_first_gen))
print(next(my_first_gen))
print(next(my_first_gen))
print(next(my_first_gen))


#Ejemplo 2
# def my_gen():
#     for i in range(1, 201):
#         if i % 2 == 0:
#             yield i

# my_first_gen = my_gen()

# for i in range(100):
#     print(next(my_first_gen))

#Es lo mismo que hacer 
# for i in range(1, 201):
#     if i % 2 == 0:
#         print(i)