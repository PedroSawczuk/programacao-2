"""
#1 - Definindo a classe Animal
class Animal:
    def __init__(self, tipo, tamanho = None, peso = None, idade = None):
        self.tipo = tipo
        self.tamanho = tamanho
        self.peso = peso
        self.idade = idade


    def comer(self): # 1.1 - Definindo o método comer da classe Animal
        return print('O ', self.tipo, ' está comendo!')

    
# 2lamp – Instanciando (criando)  o objeto Animal, chamado elefante e passando seus argumentos
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



# 07 -  Conta corrente
class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo  = saldo


# 08 -  Produto 
class Produto:

    def __init__(self,  nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


# 09 -  Usuário 

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# 10 - Definindo atributos de instância privados de uma classe
class LoginIntranet:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha


# 11 - tentando acessar um atributo de instância privado de fora da classe
usuario = LoginIntranet('teste@gmail.com', '123456') # instanciando o objeto
print(usuario._email)
print(usuario._senha)



# 12 - verificando as classes que estão relacionadas ao objeto usuario instanciado
# print(dir(usuario))


# 13 – Apresentando o valor de um atributo de instancia privado - Name Mangling
print(f'\n O e-mail do objeto usuário é: {usuario._LoginIntranet__email}')
print(f'\n A senha do objeto usuário é: {usuario._LoginIntranet__senha}')
 

# 14 - Definindo uma classe e métodos para acessar seus atributos de instância público
          # ou privado de fora da classe 
class LoginIntranetDois:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self):
        print()
        print(self.email)
        print(f'O e-mail do objeto usuário_dois é: {self.email}')
        
    def mostra_senha(self):
        print()
        print(self.__senha)
        print(f'A senha do objeto usuário_dois é: {self.__senha}')

 
# 15 - Acessando atributos de instância público e privado de fora da classe
usuario_dois = LoginIntranetDois('Gnomica@gmail.com', '654321') 
usuario_dois.mostra_email()
usuario_dois.mostra_senha()

# 16 – Definindo objetos a partir de uma classe (molde)
usuario_tres = LoginIntranetDois('Gnomica@gmail.com', '654321')
usuario_quatro = LoginIntranetDois('Gertrudez@gmail.com', '01010101')
usuario_cinco = LoginIntranetDois('Genoveva@gmail.com', '4503215')
usuario_seis = LoginIntranetDois('Gerimunda@gmail.com', '987654')


# 17 – Acessando atributos de instância público e privado de fora da
        # classe dos objetos criados a partir da classe modelo
usuario_tres.mostra_email()
usuario_quatro.mostra_email()
usuario_cinco.mostra_email()
usuario_seis.mostra_email()
"""

# 18 – Acessando um atributo de classe
#print(Produto.imposto)


# 19 - Atributo de classe  - loja de venda de computadores
class Produto:

    imposto = 1.08  #  imposto sobre o valor de venda

    def __init__(self, descricao,cor,marca,tela,valor):
        self.descricao = descricao
        self.cor = cor
        self.marca = marca
        self.tela = tela
        self.valor = (valor * Produto.imposto)
    
    def mostra_na_tela(self):
        print(self.descricao)
        print(self.cor)
        print(self.marca)
        print(self.tela)
        print(self.valor)


# 20 – Acessando atributos dos objetos criados a partir da classe modelo com o valor acrescido de 8%
produto_1  = Produto('Notebook Gamer', 'Preto','Dell', 'Monitor 15', 13542.25)
produto_2 = Produto('Magic Mouse 2 A1657', 'Branco','Apple', '2,16 X 5,71 cm', 675.00)
produto_1.mostra_na_tela()
print()
produto_2.mostra_na_tela()


# 21 - Atributo de classe  - loja de venda de computadores - outro exemplo

class Produto:

    imposto = 1.12  #  imposto - atributo de classe
    contator = 0  # atributo de classe

    def __init__(self, descricao,cor,marca,tela,valor):
        self.id = Produto.contator + 1
        self.descricao = descricao
        self.cor = cor
        self.marca = marca
        self.tela = tela
        self.valor = (valor * Produto.imposto)
        Produto.contator = self.id # atributo de classe
    
    def mostra_na_tela(self):
        print(self.id)
        print(self.descricao)
        print(self.cor)
        print(self.marca)
        print(self.tela)
        print(self.valor)


# 22 – Acessando atributos dos objetos criados a partir da classe modelo com o valor acrescido de 8%
        # com contador de produtos   
produto_1  = Produto('Notebook Gamer', 'Preto','Dell', 'Monitor 15', 13542.25)
produto_2 = Produto('Magic Mouse 2 A1657', 'Branco','Apple', '2,16 X 5,71 cm', 675.00)
#produto_1.mostra_na_tela()
#print()
#produto_2.mostra_na_tela()


