class Helado:
    def __init__(self):
        self.tipo = int
        self.numeroOrden = int
        self.precio = int
        self.sabor = []
        self.bolas = int
        self.toppings = []
        self.envase = int
        self.next = next
    def leerHelado(self, norden):
        x=int
        self.numeroOrden = norden
        self.precio=0
        while True:
            try:
                self.tipo=int(input("Que tipo de helado quiere? Yougurt(1), Cremoso(2), Cremoso especial(3)\n"))
            except ValueError:
                print("Lo siento, no entendi tu respuesta\n\n")
                continue
            if self.tipo < 1 or self.tipo > 3:
                print("Tu valor debe de ser un numero entre el 1 y el 3\n\n")
                continue
            else:
                break
        if self.tipo == int(1):
            self.bolas=1 
            while True:
                try:
                    self.sabor.append(int(input("De que sabor quiere su helado? Fresa(1), Vainilla(2), Chocolate(3)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.sabor[len(self.sabor)-1] < 1 or self.sabor[len(self.sabor)-1] > 3:
                    print("Tu valor debe de ser un numero entre el 1 y el 3\n\n")
                    self.sabor.pop()
                    continue
                else:
                    break
            while True:
                try:
                    self.toppings.append(int(input("Que toppings desea agregarle a su helado(puede agregar hasta 4)? Mango(1), Zarzamora(2), Fresa(3), Chispas de chocolate(4), Granola(5), Chocolate liquido(6), Rompope(7), Cajeta(8), Licor de cereza(9), Ninguno(0)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.toppings[len(self.toppings)-1] < 0 or self.toppings[len(self.toppings)-1] > 9:
                    print("Tu valor debe de ser un numero entre el 0 y el 9\n\n")
                    self.toppings.pop()
                    continue
                else:
                    if self.toppings[len(self.toppings)-1] == 0:
                        self.precio=-10
                        break
                    elif len(self.toppings)<4:
                        print("Quiere agregar otro topping(todavia puede agregar ",4-len(self.toppings),")? Si(1), No(2)")
                        try:
                            x=int(input())
                        except ValueError:
                            print("Lo siento, no entendi tu respuesta\n\n")
                            continue
                        if x < 1 or x > 2:
                            print("Tu valor debe de ser un numero entre el 0 y el 9\n\n")
                            continue
                        if x==2:
                            break
                    else:
                        break
            while True:
                try:
                    self.envase=(int(input("Quiere su helado en vaso(1), cono(2) o canastilla(3)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.envase < 1 or self.envase > 3:
                    print("Tu valor debe de ser un numero entre el 1 y el 3\n\n")
                    continue
                else:
                   break
            if self.envase==1:
                self.precio=self.precio+(self.bolas*50)+((len(self.toppings))*10)+0
            elif self.envase==2:
                self.precio=self.precio+(self.bolas*50)+((len(self.toppings))*10)+15
            elif self.envase==3:
                self.precio=self.precio+(self.bolas*50)+((len(self.toppings))*10)+30
        if self.tipo == int(2):
            while True:
                try:
                    self.bolas=(int(input("De cuantas bolas quiere su helado una(1), dos(2) o tres(3)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.bolas < 1 or self.bolas > 3:
                    print("Tu valor debe de ser un numero entre el 1 y el 3\n\n")
                    continue
                else:
                   break
            while True:
                try:
                    print("De que sabor quiere su bola numero", len(self.sabor)+1,"(le quedan",self.bolas-len(self.sabor),") ? Fresa(1), Vainilla(2), Chocolate(3), Rompope(4), Oreo con chocolate(5)")
                    self.sabor.append(int(input()))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.sabor[len(self.sabor)-1] < 1 or self.sabor[len(self.sabor)-1] > 5:
                    print("Tu valor debe de ser un numero entre el 1 y el 5\n\n")
                    self.sabor.pop()
                    continue
                else:
                    if len(self.sabor)==self.bolas:
                        break
            while True:
                try:
                    self.toppings.append(int(input("Que toppings desea agregarle a su yougurt(puede agregar hasta 4)? Mango(1), Zarzamora(2), Fresa(3), Chispas de chocolate(4), Granola(5), Chocolate liquido(6), Rompope(7), Cajeta(8), Licor de cereza(9), Ninguno(0)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.toppings[len(self.toppings)-1] < 0 or self.toppings[len(self.toppings)-1] > 9:
                    print("Tu valor debe de ser un numero entre el 0 y el 9\n\n")
                    self.toppings.pop()
                    continue
                else:
                    if self.toppings[len(self.toppings)-1] == 0:
                        self.precio=-10
                        break
                    elif len(self.toppings)<4:
                        print("Quiere agregar otro topping(todavia puede agregar ",4-len(self.toppings),")? Si(1), No(2)")
                        try:
                            x=int(input())
                        except ValueError:
                            print("Lo siento, no entendi tu respuesta\n\n")
                            continue
                        if x < 1 or x > 2:
                            print("Tu valor debe de ser un numero entre el 0 y el 9\n\n")
                            continue
                        if x==2:
                            break
                    else:
                        break
            while True:
                try:
                    self.envase=(int(input("Quiere su helado en vaso(1), cono(2) o canastilla(3)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.envase < 1 or self.envase > 3:
                    print("Tu valor debe de ser un numero entre el 1 y el 3\n\n")
                    continue
                else:
                   break
            if self.envase==1:
                self.precio=self.precio+(self.bolas*40)+((len(self.toppings))*10)+0
            elif self.envase==2:
                self.precio=self.precio+(self.bolas*40)+((len(self.toppings))*10)+15
            elif self.envase==3:
                self.precio=self.precio+(self.bolas*40)+((len(self.toppings))*10)+30
                
        if self.tipo == int(3):
            while True:
                try:
                    self.bolas=(int(input("De cuantas bolas quiere su helado una(1), dos(2) o tres(3)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.bolas < 1 or self.bolas > 3:
                    print("Tu valor debe de ser un numero entre el 1 y el 3\n\n")
                    continue
                else:
                   break
            while True:
                try:
                    print("De que sabor quiere su bola numero", len(self.sabor)+1,"(le quedan",self.bolas-len(self.sabor),") ? Amareto(1), Crema irlandés(2), Chocolate Belga(3), Mora Azul(4), Cajeta(5), Tequila(6), Menta con chocolate(7), Capuchino(8), Chocolate Amargo(9)")
                    self.sabor.append(int(input()))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.sabor[len(self.sabor)-1] < 1 or self.sabor[len(self.sabor)-1] > 9:
                    print("Tu valor debe de ser un numero entre el 1 y el 9\n\n")
                    self.sabor.pop()
                    continue
                else:
                    if len(self.sabor)==self.bolas:
                        break
            while True:
                try:
                    self.toppings.append(int(input("Que toppings desea agregarle a su yougurt(puede agregar hasta 4)? Mango(1), Zarzamora(2), Fresa(3), Chispas de chocolate(4), Granola(5), Chocolate liquido(6), Rompope(7), Cajeta(8), Licor de cereza(9), Ninguno(0)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.toppings[len(self.toppings)-1] < 0 or self.toppings[len(self.toppings)-1] > 9:
                    print("Tu valor debe de ser un numero entre el 0 y el 9\n\n")
                    self.toppings.pop()
                    continue
                else:
                    if self.toppings[len(self.toppings)-1] == 0: 
                        if len(self.toppings)>2:
                            self.precio=-10
                        break
                    elif len(self.toppings)<4:
                        print("Quiere agregar otro topping(todavia puede agregar ",4-len(self.toppings),")? Si(1), No(2)")
                        try:
                            x=int(input())
                        except ValueError:
                            print("Lo siento, no entendi tu respuesta\n\n")
                            continue
                        if x < 1 or x > 2:
                            print("Tu valor debe de ser un numero entre el 0 y el 9\n\n")
                            continue
                        if x==2:
                            break
                    else:
                        break
            while True:
                try:
                    self.envase=(int(input("Quiere su helado en vaso(1), cono(2) o canastilla(3)\n")))
                except ValueError:
                    print("Lo siento, no entendi tu respuesta\n\n")
                    continue
                if self.envase < 1 or self.envase > 3:
                    print("Tu valor debe de ser un numero entre el 1 y el 3\n\n")
                    continue
                else:
                   break
            if len(self.toppings) == 0:
                if self.envase==1:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings))*10)+0
                elif self.envase==2:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings))*10)+15
                elif self.envase==3:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings))*10)+30   
            elif len(self.toppings) ==1:
                if self.envase==1:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings)-1)*10)+0
                elif self.envase==2:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings)-1)*10)+15
                elif self.envase==3:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings)-1)*10)+30
            else:
                if self.envase==1:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings)-2)*10)+0
                elif self.envase==2:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings)-2)*10)+15
                elif self.envase==3:
                    self.precio=self.precio+(self.bolas*70)+((len(self.toppings)-2)*10)+30 
