# Arquivo: cadastro.py

class Cliente:
    def __init__(self, nome, cpf, endereco, cep, telefone):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._cep = cep
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, cep):
        self._cep = cep

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone


class Cadastro:
    def __init__(self):
        self.clientes = []  
    def cadastrar(self, cliente):
        if not self.verifica_cadastro(cliente.cpf):
            self.clientes.append(cliente)
            print(f"Cliente {cliente.nome} cadastrado com sucesso.")
        else:
            print(f"Cliente com CPF {cliente.cpf} já está cadastrado.")

    def get_total(self):
        return len(self.clientes)

    def verifica_cadastro(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return True
        return False

if __name__ == "__main__":
    cadastro = Cadastro()

    cliente1 = Cliente("Walison Weudes", "12345678900", "Rua A, 123", "64000000", "8899998888")
    cliente2 = Cliente("Maria Silva", "09876543211", "Rua B, 456", "64000001", "8899998887")

    cadastro.cadastrar(cliente1)
    cadastro.cadastrar(cliente2)


