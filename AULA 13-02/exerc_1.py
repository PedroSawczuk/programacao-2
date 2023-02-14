#1 - Definindo a classe Animal
class Animal:
    def __init__(self, tipo, tamanho = None, peso = None, idade = None):
        self.tipo = tipo
        self.tamanho = tamanho
        self.peso = peso
        self.idade = idade


    def comer(self): # 1.1 - Definindo o método comer da classe Animal
        return print('O ', self.tipo, ' está comendo!')

    
# 2 – Instanciando (criando)  o objeto Animal, chamado elefante e passando seus argumentos
elefante = Animal('Elefante', 3, 2700, 30)

# 3 – Apresentando na tela os atributos do objeto elefante recebidos da classe Animal 
print('\nTipo do animal: ', elefante.tipo)
print('Tamanho: ',elefante.tamanho, ' metros de altura')
print('Peso: ',elefante.peso, '  quilos')
print('Idade: ',elefante.idade, ' anos ')
print(f'Ele é da classe {type(elefante)}')

