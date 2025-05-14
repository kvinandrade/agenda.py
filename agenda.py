from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Conectar ao banco de dados MySQL
DB_URL = "mysql+pymysql://usuario:senha123@localhost/agenda_db"
engine = create_engine(DB_URL, echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Contato(Base):
    __tablename__ = 'contatos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)

Base.metadata.create_all(engine)  # Criar tabela se não existir

class AgendaDeContatos:
    def __init__(self):
        self.session = SessionLocal()

    def adicionar(self):
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        email = input('Email: ')
        contato = Contato(nome=nome, telefone=telefone, email=email)
        self.session.add(contato)
        self.session.commit()
        print(f'Contato adicionado! ID: {contato.id}')

    def alterar(self):
        try:
            id_contato = int(input('Digite o ID do contato a alterar: '))
        except ValueError:
            print('ID inválido.')
            return
        
        contato = self.session.query(Contato).filter_by(id=id_contato).first()
        if not contato:
            print('Contato não encontrado.')
            return
        
        nome = input(f'Novo nome [{contato.nome}]: ') or contato.nome
        telefone = input(f'Novo telefone [{contato.telefone}]: ') or contato.telefone
        email = input(f'Novo email [{contato.email}]: ') or contato.email
        
        contato.nome = nome
        contato.telefone = telefone
        contato.email = email
        self.session.commit()
        print('Contato alterado!')

    def apagar(self):
        try:
            id_contato = int(input('Digite o ID do contato a apagar: '))
        except ValueError:
            print('ID inválido.')
            return
        
        contato = self.session.query(Contato).filter_by(id=id_contato).first()
        if contato:
            self.session.delete(contato)
            self.session.commit()
            print('Contato apagado!')
        else:
            print('Contato não encontrado.')

    def listar(self):
        contatos = self.session.query(Contato).all()
        if not contatos:
            print('Agenda vazia.')
            return
        for contato in contatos:
            print(f'ID: {contato.id} | Nome: {contato.nome} | Telefone: {contato.telefone} | Email: {contato.email}')

def menu():
    agenda = AgendaDeContatos()
    while True:
        print('\n--- Agenda de Contatos ---')
        print('1. Adicionar contato')
        print('2. Alterar contato')
        print('3. Apagar contato')
        print('4. Listar contatos')
        print('0. Sair')
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            agenda.adicionar()
        elif opcao == '2':
            agenda.alterar()
        elif opcao == '3':
            agenda.apagar()
        elif opcao == '4':
            agenda.listar()
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    menu()