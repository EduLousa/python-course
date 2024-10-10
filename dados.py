  # dados.py
# Este arquivo contém a inicialização dos personagens e monstros com atributos como nome, vida e ataque

from model import Guerreiro, Mago, Ogro, Dragao

# Inicialização de heróis e monstros
guerreiro = Guerreiro("Marcos", 100, 20)
mago = Mago("Magnus", 80, 25)

ogro = Ogro("Shrek", 90, 15)
dragao = Dragao("Drakonar", 100, 30)

# Lista de heróis e monstros, útil para uma futura expansão
herois = [guerreiro, mago]
monstros = [ogro, dragao]
