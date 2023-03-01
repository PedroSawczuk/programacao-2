# 27 - método de instancia
"""
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 6999
    
    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente + contador +1
        self.__limite = limite
        self.__saldo  = saldo
        ContaCorrente.contador = self.__numero 


class Produto:

    contador = 0

    def __init__(self,  nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id    


class Usuario:

    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha


# 28 - Exercício

class Produto:

    contador = 0

    def __init__(self,  nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id    

    def desconto(self, porcentagem):
        return (self.__valor * ( 100 -porcentagem) / 100)


# 29 - Exercício
produto_1  = Produto('Notebook Gamer', 'I7 16 RAM HD 1TB', 8598.52)
print(produto_1.desconto(25))

print()

produto_2  = Produto('Camisa do Grêmio', 'Camisa da temporada 2023 do Grêmio', 250.52)
print(produto_2.desconto(25))


# 30 - Exercício
class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo_senha(self):
        return f'Nome......: {self.__nome} {self.__sobrenome} - Senha: {self.__senha}'

    def mostrar_email_senha(self):
        return f'Email: {self.__email} | Senha: {self.__senha}'
# 31 - Exercício
usuario_um = Usuario('Gnomica', 'Cristófina','Gnomica@gmail.com', '654321')
usuario_dois = Usuario('Gertrudez','Sancré','Gertrudez@gmail.com', '01010101')
usuario_tres = Usuario('Genoveva','Agnóstica','Genoveva@gmail.com', '4503215')

print(usuario_um.nome_completo_senha())
print(usuario_dois.nome_completo_senha())
print(usuario_tres.nome_completo_senha())

print()

print(usuario_um.mostrar_email_senha())
print(usuario_dois.mostrar_email_senha())
print(usuario_tres.mostrar_email_senha())


# - Feita a instalação - importe a biblioteca passlib para seu código:  

from passlib.hash import pbkdf2_sha512 as cryptografa

# - Para criptografar a senha a sintaxe é:  
from passlib.hash import pbkdf2_sha512 as cryptografa


# 32 - Refatore a classe Usuario para receber o atributo senha criptografada, depois
          # desenvolva um método na mesma classe que retorne o nome completo e a
          # senha criptografada.
          
class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryptografa.hash(senha, salt_size = 32, rounds = 12000)

    def nome_completo_senha(self):
        return f'Nome......: {self.__nome} {self.__sobrenome} - Senha: {self.__senha}'

usuario_um = Usuario('Gnomica', 'Cristófina','Gnomica@gmail.com', '654321')
usuario_dois = Usuario('Gertrudez','Sancré','Gertrudez@gmail.com', '01010101')
usuario_tres = Usuario('Genoveva','Agnóstica','Genoveva@gmail.com', '4503215')

print('\n',usuario_um.nome_completo_senha(),'\n')
print(usuario_dois.nome_completo_senha(),'\n')
print(usuario_tres.nome_completo_senha())

# 33 - Aplicando métodos de Classe 
from passlib.hash import pbkdf2_sha512 as cryptografa

class Usuario:

    controle = 0

    @classmethod
    def qtd_usuario(cls):
        print(f'\nTotal de usuários cadastrados no sistema: {cls.controle}')
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.controle + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryptografa.hash(senha, salt_size = 32, rounds = 12000)
        Usuario.controle = self.__id
   
usuario_um = Usuario('Gnomica', 'Cristófina','Gnomica@gmail.com', '654321')
usuario_um.qtd_usuario()


# 34 - Métodos de classe privados

from passlib.hash import pbkdf2_sha512 as cryptografa

class Usuario:

    controle = 0

    @classmethod
    def qtd_usuario(cls):
        print(f'\nTotal de usuários cadastrados no sistema: {cls.controle}')

    @classmethod
    def Disciplina(cls):
        print('Estrutura de Dados')
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.controle + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryptografa.hash(senha, salt_size = 32, rounds = 12000)
        Usuario.controle = self.__id
        print(f'\nNome do e-mail capturado: {self.__captura_nome_email()} \n')

    def nome_completo_senha(self):
        return f'Nome......: {self.__nome} {self.__sobrenome} - Senha: {self.__senha}'

    def __captura_nome_email(self): # métodode classe privado
        return self.__email.split('@')[0]

usuario_dois = Usuario('Gertrudez','Sancré','Gertrudez@gmail.com', '01010101')


# 35 - Métodos de classe estático

from passlib.hash import pbkdf2_sha512 as cryptografa

class Usuario:

    controle = 0

    @classmethod
    def qtd_usuario(cls):
        print(f'\nTotal de usuários cadastrados no sistema: {cls.controle}')

    @classmethod
    def disciplina(cls):
        print('Estrutura de Dados')

    @staticmethod
    def instituicao():
        return 'Instituto Federal de Rondônia - Campus Ariquemes - 2023'    
    
    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.controle + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryptografa.hash(senha, salt_size = 32, rounds = 12000)
        Usuario.controle = self.__id
        print(f'\nNome do e-mail capturado: {self.__captura_nome_email()} \n')

    def nome_completo_senha(self):
        return f'Nome......: {self.__nome} {self.__sobrenome} - Senha: {self.__senha}'

    def __captura_nome_email(self): # métodode classe privado
        return self.__email.split('@')[0]

Usuario.qtd_usuario()

Usuario.disciplina()

print(Usuario.instituicao())

usuario_dois = Usuario('Gertrudez','Sancré','Gertrudez@gmail.com', '01010101')

# 36 – Refatore a classe televisão seus atributos

import time

class Televisao:
    def __init__(self):
        self.marca = marca
        self.modelo = modelo
        self.tamanho_tela = tamanho_tela
        self.tipo_tecnologia = tipo_tecnologia
        self.voltagem = voltagem
        self.nr_serie = nr_serie
        self.codigo_barras = cod_barras
        self.preco =  preco
        self.ligada = False  
        self.conectada = False
        self.canais = 1

    # 37 - Métodos - ou ações que podemos executar com a classe televisão     
    def verifica_tv_ligada(self):
        return self.ligada

    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False # se tiver ligada = desliga a tv
        else:
            self.ligada = True # se tiver desligada = liga a tv
    
    def verifica_conexao(self):
        return self.conectada

    def conecta_tv(self):
        if self.conectada:
            self.conectada = False # se estiver desconectada irá conectar
        else:
            self.conectada = True # se estiver desconectda = irá conectar
        

# 38 – Entrada de dados simples – função input() – Entrada em estoque na loja 
print()
print('>>> Dados da Televisão - na loja <<<')
print()
marca                = input('Marca.........................................: ')
modelo              = input('Modelo........................................: ')
tamanho_tela    = input('Tamanho da tela em polegadas : ')
tipo_tecnologia = input('Tipo de tecnologia......................:  ')
voltagem           = input('Voltagem.....................................: ')
nr_serie             = input('Numero de série.........................: ')
cod_barras        = input('Código de Barras........................: ')
preco                 = input('Preço de venda R$.....................: ')


# 39 - Instanciando objeto a partir dos dados coletados da função input()
tv_1 = Televisao()  # instancia todos os atributos da televisão


# 40 - Executando métodos  
print()
print(f'A TV: {tv_1.marca} - {tipo_tecnologia} - modelo: {tv_1.modelo} - está ligada? {tv_1.verifica_tv_ligada()}')
print()
print('Aguarde enquanto sua TV está sendo ligada!!!' )
time.sleep(1)
tv_1.ligar_desligar() 
print()
print('         - Utilizando sua Televisão -')
print()
print(f'>>> Bem vindo a sua televisão: {tv_1.marca} - {tipo_tecnologia} - modelo: {tv_1.modelo} <<<')
print()
print(f'         - Você está no menu principal do cliente - canal: {tv_1.canais} ')
print()
print(input('>>> Escolha uma  opção para aproveitar todos os recursos de nossa tecnologia <<<'))
print()                                                                                                                                                                                 
# Consolidando - revendo alguns objetos

# 41 - Classe lâmpada
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    # Métodos ou ações que o objeto pode realizar
    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


# 42 -  instanciando o objeto lampada_1
lampada_1 = Lampada('amarela', 220, 1200)
 
# 43 - executando um método do objeto lampada_1
print(f'A lampada  está ligada? {lampada_1.checa_lampada()}')
 
# 44 - Executando outro método do objeto lampada_1
lampada_1.ligar_desligar()
print(f'A lampada  está ligada? {lampada_1.checa_lampada()}')


# 45 - classe cliente
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf


# 46 - classe ContaCorrente
class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'\nO cliente é: {self.__cliente._Cliente__nome}')

    def mostra_saldo(self):
        print(f'\nO cliente é: {self.__cliente._Cliente__nome} possui um saldo total (saldo + limite) de: {self.__saldo + self.__limite}')


# 47 - instanciando o Objeto cliente
cliente_1 = Cliente('Gertrudez Gnomica', '145.738.444-89')

# 48 - instanciando o Objeto conta
conta = ContaCorrente(2565, 4500, cliente_1)
 
# 49 - executando um método dos objetos conta e cliente_1
conta.mostra_cliente()
 
# 50 - executando outro método dos objetos conta e cliente_1
conta.mostra_saldo()

# Abstração e encapsulamento - exemplo

# 51 - classe Conta

class Conta:

    contador = 700

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'\nSaldo de {self.__saldo} do titular {self.__titular}, com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('\nO valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('\nSaldo insuficiente')
        else:
            print('\nO valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor  # remove valor da conta 
        self.__saldo -= 10 # taxa de tranferencia paga por quem realizou a transferencia
        conta_destino.__saldo += valor  # 2 adiciona valor na conta destino


# 52 - Movimentando as contas

conta_1 = Conta('Getrudez Gnomica', 100, 500)
conta_2 = Conta('Gastronildo Soares', 1000, 450)

conta_1.extrato()
conta_2.extrato()

print('\nTransferido 100 reais da conta_2 para a conta_1 - o novo saldo das contas são:')
input('')
conta_2.transferir(100, conta_1)

conta_1.extrato()
conta_2.extrato()

print('\nTentando sacar  R$ 1.500,00 da conta_1: Gertrudez')
input('')

conta_1.sacar(1500)

#53 – Define a classe televisão seus atributos

import time

class Televisao:
    def __init__(self):
        self.marca = marca
        self.modelo = modelo
        self.tamanho_tela = tamanho_tela
        self.tipo_tecnologia = tipo_tecnologia
        self.voltagem = voltagem
        self.nr_serie = nr_serie
        self.codigo_barras = cod_barras
        self.preco =  preco
        self.ligada = False  
        self.conectada = False
        self.canais = 1

    # 54 – Métodos que podemos executar com o objeto televisão     
    def verifica_tv_ligada(self):
        return self.ligada

    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False # se tiver ligada = desliga a tv
        else:
            self.ligada = True # se tiver desligada = liga a tv
    
    def verifica_conexao(self):
        return self.conectada

    def conecta_tv(self):
        if self.conectada:
            self.conectada = False # se estiver desconectada irá conectar
        else:
            self.conectada = True # se estiver desconectda = irá conectar
        

# 55 – Entrada de dados simples – função input() – Entrada em estoque na loja 
print()
print('>>> Dados da Televisão - na loja <<<')
print()
marca                = input('Marca.........................................: ')
modelo              = input('Modelo........................................: ')
tamanho_tela    = input('Tamanho da tela em polegadas : ')
tipo_tecnologia = input('Tipo de tecnologia......................:  ')
voltagem           = input('Voltagem.....................................: ')
nr_serie             = input('Numero de série.........................: ')
cod_barras        = input('Código de Barras........................: ')
preco                 = input('Preço de venda R$.....................: ')


# 56 - Instanciando objeto a partir dos dados coletados da função input()
tv_1 = Televisao()  # instancia todos os atributos da televisão


# 57 - Executando métodos  
print()
print(f'A TV: {tv_1.marca} - {tipo_tecnologia} - modelo: {tv_1.modelo} - está ligada? {tv_1.verifica_tv_ligada()}')
print()
print('Aguarde enquanto sua TV está sendo ligada!!!' )
time.sleep(1)
tv_1.ligar_desligar() 
print()
print('         - Utilizando sua Televisão -')
print()
print(f'>>> Bem vindo a sua televisão: {tv_1.marca} - {tipo_tecnologia} - modelo: {tv_1.modelo} <<<')
print()
print(f'         - Você está no menu principal do cliente - canal: {tv_1.canais} ')
print()
print(input('>>> Escolha uma  opção para aproveitar todos os recursos de nossa tecnologia <<<'))
print()                                                             

# 70 - classe Clientes
class Clientes: 
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

# 71 - classe Funcionarios
class Funcionarios:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

# 72 - Testando:
cliente_1 = Clientes('Genoveva', 'Gnomica', '999.888.777-66', 2000)

funcionario_1 = Funcionarios('Festronildo', 'Gerundio', '555.4444.333-222', 430125)

print(f'\nCliente: {cliente_1.nome_completo()}')
print(f'\nCliente: {cliente_1.nome_completo()}')

print(f'\nFuncionário: {funcionario_1.nome_completo()}')"""


class Conta:
    
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        Conta.contador += 1

    def extrato(self):
        return f'    {self.__saldo} - Cliente: {self.__titular}'

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.__saldo -= valor
        destino.__valor += valor

# 80 - Testando a  super classe Conta

#                             Titular         Saldo      limite
conta_1 = Conta('Festronildo', 4780.15, 200.35)
conta_2 = Conta('Gertrudez  ', 3852.35, 308.15)

print(f'\nSaldo da conta_1: {conta_1.extrato()}')
print(f'Saldo da conta_2: {conta_2.extrato()}')


# 81 - Refatorando a super classe Conta - get()

class Conta:
    
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        Conta.contador += 1

    def extrato(self):
        return f'    {self.__saldo} - Cliente: {self.__titular}'

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.__saldo -= valor
        destino.__valor += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite


# 82 - Testando a  super classe Conta refatorada

#                             Titular         Saldo      limite
conta_1 = Conta('Festronildo', 4780.15, 200.35)
conta_2 = Conta('Gertrudez  ', 3852.35, 308.15)

print(f'\nSaldo da conta_1: {conta_1.extrato()}')
print(f'Saldo da conta_2: {conta_2.extrato()}')

soma = conta_1.get_saldo() + conta_2.get_saldo()
print('                               --------------')
print(f'A soma dos saldos é: {soma}')        


# 83 - Refatorando a super classe Conta e seus métodos
         # get() e set()

class Conta:
    
    contador = 0
    
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'    {self.__saldo} - Cliente: {self.__titular}'          

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.__saldo -= valor
        destino.__valor += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


# 84 - Testando a  super classe Conta refatorada
        #  get() e set()

#                             Titular         Saldo      limite
conta_1 = Conta('Festronildo', 4780.15, 200.35)
conta_2 = Conta('Gertrudez  ', 3852.35, 308.15)

print(f'\nLimite anterior da conta_1 = R$: {conta_1.get_limite()}')

conta_1.set_limite(500)

print(f'\nLimite ATUAL da conta_1 = R$: {conta_1.get_limite()}')

print(f'\nSaldo da conta_1: {conta_1.extrato()}')
print(f'Saldo da conta_2: {conta_2.extrato()}')

soma = conta_1.get_saldo() + conta_2.get_saldo()
print('                               --------------')
print(f'A soma dos saldos é: {soma}')        
 
