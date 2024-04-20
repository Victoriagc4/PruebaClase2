"""closet = ["Pantalon" , "Camisa" , "Harina pan"]
#closet =     0      ,     1    ,     2              (Indices de la lista)

print(closet[0])"""


netflix = ["Batman","Simon","Ley de los audaces"]

running = True

while running:

    print("1.Agregar\n2.Ver lista\n3.Borrar elemento\n4.Salir\n")
    
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        pelicula = input("Agrega una pelicula: ")
        netflix.append(pelicula)

    if opcion == 2:
        print(netflix)

    if opcion == 3:
        indice = int(input("Ingrese el numero que desea borrar: "))
        netflix.pop(indice)
        #Para pasar un string se agrega un remove, es decir, netflix.remove(indice) y se elimina el int debajo de if opcion == 3

    if opcion == 4:
        print("Vuelva pronto :)")
        running = False
    
    print("\n")