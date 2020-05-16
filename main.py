import random
import screen

menu = {1:'piedra',2:'papel',3:'tijera'}
loop = False
#Ranking
userV = 0
aiV = 0
empate = 0 

#Loop de repeticion
while not loop:
    
    #Hacer un input de opciones:
    user = int(input(" 1: Piedra\n 2:Papel \n 3:Tijera\n 0: Salir\n"))
    screen.clear()
       
    #AI calculo
    ai = random.randint(1, 3)
    print("AI elige:",menu[ai])

    #Definir quien gana
    # 1 gana a 3 / 1 pierde vs 2
    if user == 1 and ai == 1:
        empate += 1
        print("Empate")
    elif user == 1 and ai ==2:
        print("User win")
        userV +=1
    elif user == 1 and ai ==3:
        print("AI Wins")
        aiV +=1
        
    # 2 gana a 1 / 2 pierde vs 3
    if user == 2 and ai == 1:
        print("User Win")
        userV +=1
    elif user == 2 and ai ==2:
        print("Empate")
        empate += 1
    elif user == 2 and ai ==3:
        print("AI Wins")
        aiV +=1

    # 3 gana a 2 / 3 pierde vs 1
    if user == 3 and ai == 3:
        print("Empate")
        empate += 1
    elif user == 3 and ai ==2:
        print("User win")
        userV +=1
    elif user == 3 and ai ==1:
        print("AI Wins")
        aiV +=1
    if user == 0:
        loop = True

print("-- RANKING FINAL --\n User: {}\nAI: {}\nEmpates: {}".format(userV,aiV,empate))
#imprimir resultado
#print("Usuario: {} \n VS \n AI: {}".format(user_m, ai))