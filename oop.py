# in python everything is an object
#   heritage in python:
#   class str(object) <-- heritage 

class Pessoa:
    # constructor:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def imprimir_nome(self):
        print(self.nome)

p = Pessoa('Camila', 23)
p.imprimir_nome()

class Conta:

    def __init__(self, cliente, numero):
        self.cliente = cliente
        self.numero = numero

class ContaEspecial(Conta):

    def __init__(self, cliente, numero, limite = 0):
            Conta.__init__(self, cliente, numero)
            self.limite = limite

conta = ContaEspecial('Camila Z', '7526', 100)
print(conta.limite)