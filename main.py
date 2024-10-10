# main.py
"""
Os alunos devem criar um RPG onde heróis enfrentam monstros em batalhas. Cada tipo de herói tem suas próprias habilidades e cada monstro reage de maneira diferente aos ataques.

Conceitos:

Herança: Uma classe Personagem que serve de base para Heroi e Monstro.
Polimorfismo: Heróis e monstros têm habilidades e comportamentos diferentes ao atacar e defender.
Instruções:

Crie uma classe base Personagem com atributos: nome, vida e ataque.
Crie uma classe Heroi com subclasses: Guerreiro e Mago, onde cada um ataca de maneira diferente (por exemplo, Guerreiro usa espada, Mago usa magia).
Crie uma classe Monstro com subclasses: Ogro e Dragao, onde cada um tem uma resistência ou fraqueza diferente.
Crie um sistema de batalha onde o herói enfrenta o monstro até que um dos dois perca toda a vida.    
    
    """
#este ficheiro representa a lógica da batalha utilizando os dados do ficheiro dados.py
    
# main.py

# main.py

from dados import herois, monstros
from model import Personagem

def exibir_menu_personagens(personagens, tipo_personagem):
    print(f"Escolha um {tipo_personagem}:")
    for i, personagem in enumerate(personagens):
        print(f"{i + 1}. {personagem.nome} (Vida: {personagem.vida}, Ataque: {personagem.ataque})")
    escolha = int(input(f"Digite o número do {tipo_personagem} escolhido: ")) - 1
    return personagens[escolha]

def batalha(heroi, monstro):
    print("A batalha começa!")
    heroi.exibir_informacoes()
    monstro.exibir_informacoes()

    while heroi.vida > 0 and monstro.vida > 0:
        heroi.atacar(monstro)
        if monstro.vida > 0:
            monstro.atacar(heroi)
        
        print("\n--- Próximo turno ---\n")
    
    if heroi.vida > 0:
        print(f"{heroi.nome} venceu a batalha!")
    else:
        print(f"{monstro.nome} venceu a batalha!")

def menu_inicial():
    print("Bem-vindo ao RPG de Batalhas!")
    print("============================")
    print("1. Iniciar a batalha")
    print("2. Sair do jogo")
    escolha = input("Escolha uma opção: ")

    return escolha

if __name__ == "__main__":
    while True:
        escolha_menu = menu_inicial()
        
        if escolha_menu == "1":
            # Exibe o menu para o jogador escolher o herói
            heroi_escolhido = exibir_menu_personagens(herois, "herói")
            
            # Exibe o menu para o jogador escolher o monstro
            monstro_escolhido = exibir_menu_personagens(monstros, "monstro")
            
            # Inicia a batalha entre o herói escolhido e o monstro escolhido
            batalha(heroi_escolhido, monstro_escolhido)
        
        elif escolha_menu == "2":
            print("Obrigado por jogar! Até a próxima!")
            break
        
        else:
            print("Opção inválida! Por favor, escolha novamente.")

