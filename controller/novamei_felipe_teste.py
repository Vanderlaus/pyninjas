from db.database import engine
from datetime import datetime
from models.model import Nova_mei, Ocupacao, RelacaoOcupacaoXNovaMEI
from sqlmodel import Session


# Função Criar Mei
def createMei(cpf: str, objetivo_viabilidade: str, inscricao_endereco: str, tipo_endereco: str, endereco: str, nr_endereco: str, relacao_ocupacoes: list[RelacaoOcupacaoXNovaMEI]):   # Criação da Instancia no Banco de Dados
    with Session(engine) as session:
        nova_mei = Nova_mei(
            cpf=cpf,
            objetivo_viabilidade=objetivo_viabilidade,
            inscricao_endereco=inscricao_endereco,
            tipo_endereco=tipo_endereco,
            endereco=endereco,
            nr_endereco=nr_endereco,
            relacao_ocupacoes=relacao_ocupacoes
        )
        
        session.add(nova_mei)
        session.commit()
        session.refresh(nova_mei)
        
   
        
        
        return nova_mei

# Inseridendo dados e cadastrando no banco de dados
with Session(engine) as session:
    nova_mei = Nova_mei(cpf="12345678900",  objetivo_viabilidade="teste",
                        inscricao_endereco="123", tipo_endereco="Rua", endereco="Rua Teste",
                        nr_endereco="123")
    ocupacao = Ocupacao(descricao="Teste", cnae="123")
    relacao_ocupacao = RelacaoOcupacaoXNovaMEI(nova_mei=nova_mei, ocupacao=ocupacao, is_primario=True)


    session.add(nova_mei)
    session.add(ocupacao)
    session.commit()

    print(nova_mei)
    print(ocupacao)