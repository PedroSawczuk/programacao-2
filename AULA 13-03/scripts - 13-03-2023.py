"""
Pedro Henrique Sawczuk Monteiro - UTF8 - pt-br - 13-03-2023
Programação II

# MÉTODO super(): 

# 72 - Implementando o método super():
class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self._especie = especie


    def som(self, som):
        print(f'\nO som que o {self.__nome} faz chama-se: {som}')

class Elefante(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)  
        super().som('bramido')
        self.__raca = raca


class Girafa(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)  
        self.__raca = raca


# 73 - testando o método super():
dumbo = Elefante('Elefante','Africano', 'Loxodonta africana')
gisela = Girafa('Girafa','Africana',' Giraffidae')

gisela.som('Zumbido')

# 74 - A herança múltipla em Python - implementação:
class Animal:
    def __init__(self, nome):
        self.__nome = nome


    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Terrestre(Animal): # Herança direta
    def __init__(self, nome):
        super().__init__(nome)


    def andar(self):
        return f'Olá eu sou {self._Animal__nome} e estou andando pela mata'


    def cumprimentar(self): # sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo em florestas tropicais!'


class Aquatico(Animal): # Herança direta
    def __init__(self, nome):
        super().__init__(nome)


    def nadar(self):
        return f'O {self._Animal__nome} nada'


    def cumprimentar(self): # sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo em agua doce!'

# Testando herança múltipla - direta
tatu = Terrestre('Tatu Bola')  # herança direta
print(f'\n{tatu.andar()}')
print('\n',tatu.cumprimentar())


# Analisando qual instância pertence o tatu:
print(f'\ntatu Bola é instância de Tatu?: {isinstance(tatu, Terrestre)}')


# Testando herança múltipla - direta
peixe = Aquatico('Tambaqui') # herança direta
print('\n',peixe.nadar())
print('\n',peixe.cumprimentar())


# Analisando qual instância pertence o tambaqui:
print(f'\nTambaqui é instância de peixe?: {isinstance(peixe, Aquatico)}')

# Classe multi derivada direta
class Ornitorrinco(Terrestre, Aquatico): # classe multi deverivada direta

    def __init__(self, nome):
        super().__init__(nome)


    def cumprimentar(self): # sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo na terra e na agua doce!'


# 75 - Testando a classe multi derivada direta
perry = Ornitorrinco('Perry')
print('\n',perry.andar())
print('\n',perry.nadar())
print('\n',perry.cumprimentar()) 

# 76 -  classe multidevirada indireta
class Pinguim(Ornitorrinco): # classe multi deverivada indireta
    def __init__(self, nome):
        super().__init__(nome)


    def cumprimentar(self): # sobrescrição do método da classe super()
        return f'Eu sou {self._Animal__nome} e vivo na terra e na agua salgada!'


# 77 - Testando classe multiderivada indireta
pinguim = Pinguim('Picolino')
print()
print(pinguim.nadar())
print()
print(pinguim.cumprimentar())


# Analisando qual instância pertence o pinguim:
print()
print(f'Pinguim Picolino é  da instância pinguin?: {isinstance(pinguim, Pinguim)}')


# 78 - Entendendo a ordem de execução de uma classe multi derivada
print()
perry = Ornitorrinco('Perry')
print(perry.cumprimentar())  # -  Metodo Resolution Order ou MRO

print(help(Ornitorrinco))

"""

# 79 - O overrinding é a melhor representação do polimorfismo
          # - POO - Polimorfismo ou Poli: muitas / Morfis: formas
class Animal(object):
    def __init__(self, nome):
        self.__nome = nome


    def emite_som(self):
        raise NotImplementedError('A classe filha precisa implementar o método falar')


    def come(self):
        print(f'Self {self.__nome} está comendo')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)


    def emite_som(self):
        print(f'{self._Animal__nome} faz o som: au au')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)


    def emite_som(self):
        print(f'{self._Animal__nome} faz o som miau miau')


print()
feliz = Gato('Felix')
feliz.come()
feliz.emite_som()

print()
gerinaldo = Cachorro('Gerinaldo')
gerinaldo.come()
gerinaldo.emite_som()
"""


# MÉTODOS MÁGICOS
# 80 - aplicando métodos mágicos
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas


    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'
  

# 81 - Testando
livro_1 = Livros('Python: Guia Prático do Básico ao Avançado', 'Rafael F. V. C. Santos', 225)
livro_2 = Livros('Programação Funcional para Leigos', ' Jhon Paul Mueller', 481)

print(f'\n Livro: {livro_1}')
print(f'\n Livro: {livro_2}')


# 82 – Refatorando e testando a classe Livros com __repr__(self)
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas


    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor} - nº páginas: {self.__paginas}'
  

# - Testando
livro_1 = Livros('Python: Guia Prático do Básico ao Avançado', 'Rafael F. V. C. Santos', 225)
livro_2 = Livros('Programação Funcional para Leigos', ' Jhon Paul Mueller', 481)

print(f'\n Livro: {livro_1}')
print(f'\n Livro: {livro_2}')


# 83 – Tornando a informação representativa para o usuário final __str__(self)
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas


    def __str__(self):
        return f'{self.__titulo} escrito por {self.__autor} - nº páginas: {self.__paginas}'
  

# - Testando
livro_1 = Livros('Python: Guia Prático do Básico ao Avançado', 'Rafael F. V. C. Santos', 225)
livro_2 = Livros('Programação Funcional para Leigos', ' Jhon Paul Mueller', 481)

print(f'\n Livro: {livro_1}')
print(f'\n Livro: {livro_2}')
 

# 84 – Verificando o tamanho de um atributo usando - __len__(self)
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas


    def __len__(self):
        return len(self.__titulo) 
    
   
# - Testando
livro_1 = Livros('Python: Guia Prático do Básico ao Avançado', 'Rafael F. V. C. Santos', 225)
livro_2 = Livros('Programação Funcional para Leigos', ' Jhon Paul Mueller', 481)

print('\nO tamanho do título do  Livro_1 é:', livro_1)
print('\nO tamanho do título do  Livro_2 é:', len(livro_2))


# 85 – Apagando objetos da memória
del livro_1
del livro_2


# 86 – Apagando objetos da memória e retornando uma mensagem
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas


    def __del__(self):
        print(f'\nO objeto do tipo livro foi apagado da memória')
    
   
# - Testando
livro_1 = Livros('Python: Guia Prático do Básico ao Avançado', 'Rafael F. V. C. Santos', 225)
livro_2 = Livros('Programação Funcional para Leigos', ' Jhon Paul Mueller', 481)

del livro_1
del livro_2


# 87 - Concatenando objetos __add__(self)
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas


    def __str__(self):
        return self.__titulo


    def __add__(self, segundo_objeto):
        return f'Título livro_1: {self} - Título livro_2: {segundo_objeto}'
        
  
# - Testando
livro_1 = Livros('Python: Guia Prático do Básico ao Avançado', 'Rafael F. V. C. Santos', 225)
livro_2 = Livros('Programação Funcional para Leigos', ' Jhon Paul Mueller', 481)

print('\n', livro_1 + livro_2)


 # 88 - Multiplicando o  valor do atributo de um objeto por um número (self, numero)
class Livros:
    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas


    def __str__(self):
        return self.__titulo


    def __mul__(self, numero):
        if isinstance(numero, int):
            mensagem = ' '
            for n in range(numero):
                mensagem += ' - ' + str(self)
            return mensagem
        return 'Não foi possível multiplicar'

        
# - Testando
livro_1 = Livros('Python: Guia Prático do Básico ao Avançado', 'Rafael F. V. C. Santos', 225)

print('\n', livro_1 * 3)
print('\n', livro_1 * 'abc')
"""