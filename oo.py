class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.__test = "test"

    def correr(self, velocidade):
        print(f"{self.nome} correndo na velocidade {velocidade}")

    def falar(self):
        print("Falandoooo")

    def identificador(self):
        raise NotImplemented

    def __private_method(self):
        print("test private method")


class Animal:
    def especie(self):
        print("retornaria a especie do animal")

class PessoaFisica(Pessoa, Animal):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf

    def identificador(self):
        return self.cpf


class PessoaJuridica(Pessoa):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj

    def identificador(self):
        return self.cnpj


p = PessoaFisica("Tonho", "000.000.000-00")
p.especie()
# p.correr("Máxima")
# print(p.cpf)

# p => PessoaFisica => Pessoa
# p => Pessoa
print(isinstance(p, PessoaFisica))
print(isinstance(p, Pessoa))

def mensagem(pessoa: Pessoa) -> str:
    print(f"Bem vindo {pessoa.nome}")


p2 = PessoaJuridica("UNCISAL", "00000000000")
# p2.correr("Mínima")
# print(p2.cnpj)

# instância ou objeto da classe Pessoa
# p = Pessoa("Tonho da Lua", "Silva")
# print(p.nome)
#
# p2 = Pessoa("Zé de Nanan", "Santos")
# print(p2.nome)
#
# p.correr("Máxima")
# p2.correr("Mínima")
