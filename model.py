# este ficheiro representa Contém as definições de classes para heróis e monstros, seguindo o conceito de herança e polimorfismo.

# model.py



class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}")
    
    def atacar(self, outro_personagem):
        print(f"{self.nome} ataca {outro_personagem.nome} causando {self.ataque} de dano.")
        outro_personagem.receber_dano(self.ataque)
    
    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

class Heroi(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

class Guerreiro(Heroi):
    def atacar(self, outro_personagem):
        print(f"{self.nome} usa a espada contra {outro_personagem.nome} causando {self.ataque} de dano.")
        outro_personagem.receber_dano(self.ataque)

class Mago(Heroi):
    def atacar(self, outro_personagem):
        print(f"{self.nome} lança uma magia em {outro_personagem.nome} causando {self.ataque} de dano mágico.")
        outro_personagem.receber_dano(self.ataque)

class Monstro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)

class Ogro(Monstro):
    def receber_dano(self, dano):
        dano_reduzido = dano // 2
        print(f"{self.nome} é resistente e só recebe {dano_reduzido} de dano.")
        super().receber_dano(dano_reduzido)

class Dragao(Monstro):
    def receber_dano(self, dano):
        dano_ampliado = dano * 2
        print(f"{self.nome} é vulnerável à magia e recebe {dano_ampliado} de dano.")
        super().receber_dano(dano_ampliado)
