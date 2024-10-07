import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, 
                             QDialog, QInputDialog)
from cadastro import Cliente, Cadastro

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.cadastro = Cadastro()  
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sistema de Cadastro de Clientes')
        
        layout = QVBoxLayout()

        btn_buscar = QPushButton('Buscar Cliente')
        btn_alterar = QPushButton('Alterar Cliente')
        btn_mostrar_todos = QPushButton('Mostrar Todos')

        btn_buscar.clicked.connect(self.tela_buscar_cliente)
        btn_alterar.clicked.connect(self.tela_alterar_cliente)
        btn_mostrar_todos.clicked.connect(self.mostrar_todos)

        layout.addWidget(btn_buscar)
        layout.addWidget(btn_alterar)
        layout.addWidget(btn_mostrar_todos)

        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def tela_buscar_cliente(self):
        buscar_dialog = QDialog(self)
        buscar_dialog.setWindowTitle("Buscar Cliente")
        
        layout = QVBoxLayout(buscar_dialog)

        self.cpf_input = QLineEdit()
        self.cpf_input.setPlaceholderText('Digite o CPF do cliente')
        
        btn_confirmar_busca = QPushButton('Buscar')
        btn_confirmar_busca.clicked.connect(lambda: self.buscar_cliente(buscar_dialog))

        layout.addWidget(QLabel("Buscar Cliente"))
        layout.addWidget(self.cpf_input)
        layout.addWidget(btn_confirmar_busca)

        buscar_dialog.setLayout(layout)
        buscar_dialog.exec_()  # Exibe o diálogo

    def buscar_cliente(self, dialog):
        cpf = self.cpf_input.text()
        if self.cadastro.verifica_cadastro(cpf):
            cliente = next(c for c in self.cadastro.clientes if c.cpf == cpf)
            QMessageBox.information(self, 'Cliente Encontrado', 
                                    f'Nome: {cliente.nome}\nEndereço: {cliente.endereco}\nCEP: {cliente.cep}\nTelefone: {cliente.telefone}')
        else:
            QMessageBox.warning(self, 'Erro', 'Cliente não encontrado!')

        dialog.close()  # Fecha o diálogo após a busca

    def tela_alterar_cliente(self):
        alterar_dialog = QDialog(self)
        alterar_dialog.setWindowTitle("Alterar Cliente")
        
        layout = QVBoxLayout(alterar_dialog)

        self.cpf_input_alterar = QLineEdit()
        self.cpf_input_alterar.setPlaceholderText('Digite o CPF do cliente que deseja alterar')

        btn_confirmar_alteracao = QPushButton('Alterar')
        btn_confirmar_alteracao.clicked.connect(lambda: self.alterar_cliente(alterar_dialog))

        layout.addWidget(QLabel("Alterar Cliente"))
        layout.addWidget(self.cpf_input_alterar)
        layout.addWidget(btn_confirmar_alteracao)

        alterar_dialog.setLayout(layout)
        alterar_dialog.exec_()  # Exibe o diálogo

    def alterar_cliente(self, dialog):
        cpf = self.cpf_input_alterar.text()
        if self.cadastro.verifica_cadastro(cpf):
            cliente = next(c for c in self.cadastro.clientes if c.cpf == cpf)

            novo_nome, ok = QInputDialog.getText(self, 'Alterar Cliente', f'Digite o novo nome para {cliente.nome}:')
            if ok and novo_nome:
                cliente.nome = novo_nome
                QMessageBox.information(self, 'Sucesso', f'O nome foi alterado para {cliente.nome}.')
            else:
                QMessageBox.warning(self, 'Erro', 'Nenhum nome foi fornecido.')
        else:
            QMessageBox.warning(self, 'Erro', 'Cliente não encontrado!')

        dialog.close()  # Fecha o diálogo após a alteração

    def mostrar_todos(self):
        self.tabela = QTableWidget()
        self.tabela.setRowCount(len(self.cadastro.clientes))
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(['Nome', 'CPF', 'Endereço', 'CEP', 'Telefone'])

        for i, cliente in enumerate(self.cadastro.clientes):
            self.tabela.setItem(i, 0, QTableWidgetItem(cliente.nome))
            self.tabela.setItem(i, 1, QTableWidgetItem(cliente.cpf))
            self.tabela.setItem(i, 2, QTableWidgetItem(cliente.endereco))
            self.tabela.setItem(i, 3, QTableWidgetItem(cliente.cep))
            self.tabela.setItem(i, 4, QTableWidgetItem(cliente.telefone))

        layout = QVBoxLayout()
        layout.addWidget(self.tabela)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
