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
"""


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




