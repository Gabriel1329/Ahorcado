import random

lista=["electrocardiograma","blusa","lapicero","boton","billetera","calor","jueves","avion","bus","ventana","python","electronica","japones","idioma","raiz","capullo","disco","celular","programa","television","radio","cuerda","raton","perro","sierra","casa","gato","bebe","cola","tarjeta","shampoo","violin","guitarra","ahorcado","puntual","responsabilidad","hiperventilacion","rayo","necesidad","cooperacion","columna","sobrexplotacion","inteligencia","interdinamismo","unicelular","bipolaridad","arroz","saturado","cerebro","corrupcion","uva","reto","locutor","espectaculo","ovario","estuche","carpeta","candela","fosforo","carisma","bolsa","camaleon","arena","humanoide","contemporaneo","romantisismo","teatro","moderno","salvaje","ingenuidad","infidelidad","amorio","limite","postal","enagua","medalla","pila","brazalete","pollo","medicina","ingenieria","psicologia","cartografo","ciencia","oeste","este","sur","norte","occidente","alumno","escuela","tanques","luciernaga","inodoro","anteojos","cabellera","constelacion","particula","galaxia","espectaculo","rinoceronte","cachalote","delfin","hipopotamo","jirafa","espada","armadura","dama","caballo","caballero","chancleta","oportunidad","surrealismo","cortar","reciclar","director","razon","no","error","media","crema","computadora","cielo","noche","luna","formato","letra","palabra","teclado","profesor","agresion","interlocutor","regreso","camaron","pintura","arte","sensacion","escritura","ambiente","celda","restriccion","equis","tabla","cocina","acuario","actualidad","sembrar","retener","programar","destruir","estrella","requisito","actualidad","papel","llave","cortina","libro","informacion","interprete","exterminar","cajero","plato","comida","gustos","audifonos","reproductor","renovar","inventar","amor","repetir","lazo","ojo","paisaje","hermoso","novia","procesador","lenguaje","circuitos","ritmo","melodia","armonia","llevar","descargar","presente","futuro","pasado","atardecer","luz","felicidad","oscuridad","ficcion","realidad","complejo","simple","melon","rama","carroceria","bincha","juego","tecnologico","computacion","cancion","metal","musica","clasico","mesa","silla","brazo"]
palabra=random.choice(lista)

def juego():
    intentosF=0
    print("solo puede fallar 7 veces")
    c=0
    x=""
    while len(palabra)>c:
        if palabra[c]==" ":
            x+=" "
            c+=1
        else:
            x+="-"
            c+=1
    return adivinar(0,x,intentosF)

def adivinar(c,x,intentosF):
    if intentosF==7:
        print("PERDISTES")
        print("la palabra era: "+str(palabra))
        input("")
    elif "-" not in x:
        print(x)
        print("GANASTES")
        input("")
    else:
        print("")
        print(x)
        print("")
        letra=input("ingrese una letra: ")
        if letra in palabra:
            return poscicion(letra,x,0,intentosF)
        else:
            print("")
            print("la letra no esta")
            print("")
            print("intentos fallidos: "+str(intentosF+1))
            return adivinar(c,x,intentosF+1)
        


def poscicion(letra,x,c,intentosF):
    if c==len(palabra):
        return adivinar(0,x,intentosF)
    elif letra==palabra[c]:
        return poscicion(letra,x[:c]+str(letra)+x[c+1:],c+1,intentosF)
    else:
        return poscicion(letra,x,c+1,intentosF)

juego()
