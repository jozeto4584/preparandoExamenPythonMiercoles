bandas=[]


opcion=100
while(opcion != 5):
    
    print("*****FESTIVAL ALTAVOZ*****")
    print("**************************")
    print("1.Regitrar Banda ")
    print("2.Cartel Festival")
    print("3.Buscar Banda")
    print("4.Modificar UNa Banda")
    print("5.Finalizar")
        
    opcion= int(input("Digita una opcion :"))
    banda={}
    
    if opcion==1:
        
        ## SE llena el objeto de banda
        banda["id"]=int(input("Digita el id: "))
        banda["nombre"]=input(" Nombre: ")
        banda["genero"]=input("Genero: ")
        banda["costo"]=int(input("Costo: "))
        
        ## como agrego un diccionario a una lista 
        bandas.append(banda)
         
    elif opcion==2:
        #Recorriendo una lista para imprimir sus elementos 
        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar["id"]}--{bandaAuxiliar["nombre"]}")
        
        
    elif opcion==3:
        # Buscando un elemento de una lista 
        bandaBuscada=input("Digita la banda que quiere buscar :")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]==bandaBuscada:
                print("oe la encontre") 
            else:
                print("No lo encontro")    
        
      
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        print("Opcion Invalida")
    
    
    
    

    