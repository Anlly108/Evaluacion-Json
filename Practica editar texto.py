import json
datos = {}
print ("Ferreteria\n")

print("--------------------")
print("* Menú de opciones *")
print("--------------------")

print("1. Agregar productos")
print("2. Ver productos")
print("3. Editar productos")

numero = int(input("Introduce la opción deseada:"))

if numero == 1:
    datos = {}

    nombre = input("Ingresa el Nombre del producto: ")                           
    precio = int(input("Ingresa el precio: "))   
    descrip = input("Ingresa la descripcion: ")       
        
    datos['productos']= []
    datos = ['productos'].append({                                             
        "nombre": nombre,                                         
        "precio": precio,
        "descrip": descrip
                        })  
    with open('productos.json', 'w') as file:   
            json.dump(datos, file, indent=4)                                         

elif numero == 2:
    with open("productos.json", "r") as readfile:
        productlist = json.load(readfile)
         
    buscar = str(input('Escriba el nombre del producto que desea buscar en la BD :'))     

    for prod in productlist():
        if prod'nombre' == buscar:                                                 
            print('Se ha encontrado el Producto : ',prod'nombre')                                                  
            print('Precio: ',prod'precio')   
            print('Descripcion: ', prod'descrip') 
        else
            print("Fallo en buscar el producto.")    

    
elif numero == 3:        
    buscar = str(input('Escriba el nombre del producto que desea buscar en la BD :'))  
    with open('productos.json', 'w') as file:
    for prod in productlist'productos':
        if prod'nombre' == buscar:                                                 
            print('Se ha encontrado el Producto : ',prod'nombre')                                                  
            print('Precio: Rs.',prod'precio')   
            print('Descripcion: ', prod'descrip') 
        else
            print("Fallo en buscar el producto.")        

    nombre = input("Ingresa el nombre del producto: ")                           
    precio = int(input("Ingresa el precio: "))   
    descrip = input("Ingresa la descripcion: ")       

    with open('productos.json', 'w') as file:
        datos = json.load(file)({                                             
            "nombre": nombre,                                         
            "precio": precio,
            "descrip": descrip
                    })  

        json.dump(datos, file, indent=4)                                           
else:
    print("La opción elegida no existe, vuelve a intentar.")
