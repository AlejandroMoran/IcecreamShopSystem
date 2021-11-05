from Orders import Helado
Ordenes=[]
y=int(0)
temporal=int(0)
numeroOrdenes=int(0)
def Cuenta(Ordenes, atributo):
    Cantidad=dict()
    for o in Ordenes:
        codigo= []
        if atributo==2:
            for topping in toppings:
                if topping not in Cantidad:
                    Cantidad[topping]=0
            y=0
            for n in o.toppings:
                if o.toppings[y] in Cantidad:
                    Cantidad[o.toppings[y]]+=1
                y +=1
        elif atributo==3:
            for e in envase:
                if e not in Cantidad:
                    Cantidad[e]=0
            y=0
            if o.envase in Cantidad:
                Cantidad[o.envase]+=1
        elif atributo==1:
            for tip in tipo:
                if tip not in Cantidad:
                    Cantidad[tip]=0
            if o.tipo in Cantidad:
                Cantidad[o.tipo]+=1
    return Cantidad
def Ordenamiento(aordenar):
    
    diccionario=Cuenta(Ordenes, aordenar)
    Cantidador=dict()
    valoror=list(diccionario.values())
    Ordenamiento2(valoror)
    for v in valoror:
        for key in diccionario:
            if diccionario[key]==v:
                Cantidador[key]=v
    return Cantidador
def Ordenamiento2(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        Ordenamiento2(L)
        Ordenamiento2(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
tipo = {
    1: "Yogurt",
    2: "Cremoso",
    3:"Cremoso especial"
}
sabor = [
        {1: "Fresa",2: "Vainilla",3: "Chocolate"},
        {1: "Fresa",2: "Vainilla",3: "Chocolate",4: "Rompope",5: "Oreo con chocolate"},
        {1: "Amareto",2: "Crema irlandés",3: "Chocolate Belga",4: "Mora Azul",5: "Cajeta",6: "Tequila",7: "Menta con chocolate",8: "Capuchino",9: "Chocolate Amargo"}
]
toppings = {
    1: "Mango",
    2: "Zarzamora",
    3: "Fresa",
    4: "Chispas de chocolate",
    5: "Granola",
    6: "Chocolate liquido",
    7: "Rompope",
    8: "Cajeta",
    9: "Licor de cereza",
}
envase = { 
    1: "Vaso",
    2: "Cono",
    3: "Canastilla"
}
o=Helado()
o.numeroOrden=-1
Ordenes.append(o)
while True:
    x=int
    while True:
            try:
                x=int(input(" Que quiere hacer?\n Levantar una orden(1)\n Ver todas las ordenes(2)\n Calcular el helado mas popular(3)\n Calcular el helado menos popular(4)\n Consultar la lista del consumo de los helados(5)\n Salir(0)\n\n"))
            except ValueError:
                print("Lo siento, no entendi tu respuesta\n\n")
                continue
            if x < 0 or x > 5:
                print("Tu valor debe de ser un numero entre el 0 y el 5\n\n")
                continue
            else:
                break
    if x==0:
        break
    elif x==1:
        o=Helado()
        o.leerHelado(numeroOrdenes)
        Ordenes.append(o)
        while True:
            try:
                y=int(input("Quiere agregar otro helado a su orden? Si(1), No(2)\n\n"))
            except ValueError:
                print("Lo siento, no entendi tu respuesta\n\n")
                continue
            if y < 1 or y > 2:
                print("Tu valor debe de ser un numero entre el 1 y el 2\n\n")
                continue
            elif y==1:
                o=Helado()
                o.leerHelado(numeroOrdenes)
                Ordenes.append(o)
            elif y==2:
                break
        numeroOrdenes += 1
    elif x==2:
        print(chr(27) + "[2J")
        contador=0
        for o in range(len(Ordenes)-1):
            if Ordenes[contador].numeroOrden != Ordenes[contador+1].numeroOrden:
                if temporal!=0:
                    print("Precio total:",temporal,"\n")
                    temporal=0
                print("\n")
                print("Orden [",Ordenes[contador+1].numeroOrden,"]:")
            temporal=temporal+Ordenes[contador+1].precio
            print(" Tipo:",tipo[Ordenes[contador+1].tipo],"\n Sabor:")
            y=0
            for z in Ordenes[contador+1].sabor:
                print("  ",sabor[Ordenes[contador+1].tipo-1][Ordenes[contador+1].sabor[y]])
                y +=1
            print(" Toppings:")
            y=0
            if Ordenes[contador+1].toppings[0]==0:
                print("   Ninguno")
            else:
                for c in Ordenes[contador+1].toppings:
                    if Ordenes[contador+1].toppings[y] != 0:
                        print("  ",toppings[Ordenes[contador+1].toppings[y]])
                    y +=1
            print(" Precio:",Ordenes[contador+1].precio,"\n")
            contador+=1
            if contador+2>len(Ordenes):
                print("Precio total:",temporal,"\n")
                temporal=0
        print("Helados vendidos vendidos:")
        contador=1
        p=list(Ordenamiento(1).values())
        for h in tipo:
            print("  ",tipo[int(((list(Ordenamiento(1)))[3-contador]))],":",p[3-h])
            contador+=1
        print("\nEnvases vendidos:")
        contador=1
        p=list(Ordenamiento(3).values())
        for e in envase:
            print("  ",envase[int(((list(Ordenamiento(3)))[3-contador]))],":",p[3-e])
            contador+=1
        print("Toppings vendidos:")
        contador=1
        p=list(Ordenamiento(2).values())
        for t in toppings:
            print("  ",toppings[int(((list(Ordenamiento(2)))[9-contador]))],":",p[9-t])
            contador+=1
    elif x==3:
        print(chr(27) + "[2J")
        if len(Ordenes)==1:
            print("No hay ordenes")
        else:
            print(chr(27) + "[2J")
            print("Helado/s mas popular/es:\n")
            p=list(Ordenamiento(1).values())
            print(tipo[int(((list(Ordenamiento(1)))[len(list(Ordenamiento(1)))-1]))],",lo han comprado",p[len(p)-1],"veces\n")
            contador=1
            while (len(p)-(contador+1))>=0 and p[len(p)-contador]==p[len(p)-(contador+1)]:
                print(tipo[int(((list(Ordenamiento(1)))[len(list(Ordenamiento(1)))-(1+contador)]))],"lo han comprado",p[len(p)-contador],"veces\n")
                contador+=1
        
    elif x==4:
        print(chr(27) + "[2J")
        if len(Ordenes)==1:
            print("No hay ordenes")
        else:
            print(chr(27) + "[2J")
            print("Helado/os menos popular:\n")
            p=list(Ordenamiento(1).values())
            print(tipo[int((list(Ordenamiento(1)))[0])],",lo han comprado",p[0],"veces\n")
            contador=0
            while (contador+1)<len(p) and p[contador]==p[(contador+1)]:
                print(tipo[int((list(Ordenamiento(1)))[contador+1])],",lo han comprado",p[contador+1],"veces\n")
                contador+=1
    elif x==5:
        print(chr(27) + "[2J")
        p=list(Ordenamiento(1).values())
        contador=0
        for helado in Ordenamiento(1):
                print(tipo[int(((list(Ordenamiento(1)))[len(list(Ordenamiento(1)))-(1+contador)]))],"lo han comprado",p[len(p)-(1+contador)],"veces")
                contador+=1
