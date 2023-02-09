print("Seja muito bem vindo ao quiz!")
answer_user = input("Quer começar? s/n ")

if answer_user !="s":
    quit()
    
score = 0
print("Começando...")
print("Quem desenvolveu o jogo GTA? \n (A) Rockstar Games \n (B) Ubisoft")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score+= 1
else:
    print("Incorreto!")
    
print(f"A sua pontuação : {score}")
