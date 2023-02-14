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

# 4 - Exercício

class Lampada:
    def __init__(self, tipo, vol = None, cor = None, tec = None, lum = None, sta = None):
        self.tipo = tipo
        self.vol = vol
        self.cor = cor
        self.tec = tec
        self.lum = lum
        self.sta = sta

# lâmpada da sala 
lampada_sl = Lampada('Lâmpada da sala', 'Bivolt', 'Branca', 'Led', 1800, 'Desligada')

print('\nTipo do objeto..: ', lampada_sl.tipo)
print('Voltagem..........: ', lampada_sl.vol)
print('Cor...................: ',lampada_sl.cor)
print('Tecnologia........: ',lampada_sl.tec)
print('Luminosidade..: ',lampada_sl.lum, ' lumens')
print('Status...............: ',lampada_sl.sta)


# lâmpada da quarto
lampada_qt = Lampada('Lâmpada do quarto', '110', 'Amarelo', 'Filamento', 100, 'Ligada')

print('\nTipo do objeto..: ', lampada_qt.tipo)
print('Voltagem..........: ', lampada_qt.vol)
print('Cor...................: ',lampada_qt.cor)
print('Tecnologia........: ',lampada_qt.tec)
print('Luminosidade..: ',lampada_qt.lum, ' lumens')
print('Status...............: ',lampada_qt.sta)


# lâmpada da cozinha
lampada_cz = Lampada('Lâmpada da cozinha', '220', 'Branca', 'Florescente', 3000, 'Ligada')

print('\nTipo do objeto..: ', lampada_cz.tipo)
print('Voltagem..........: ', lampada_cz.vol)
print('Cor...................: ',lampada_cz.cor)
print('Tecnologia........: ',lampada_cz.tec)
print('Luminosidade..: ',lampada_cz.lum, ' lumens')
print('Status...............: ',lampada_cz.sta)

