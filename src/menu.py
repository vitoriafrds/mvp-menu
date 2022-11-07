import sys
from service import ServiceONU

def exibir():
    print(
        '[1] – Cadastrar mês de referência',
        '\n[2] – Exibir dados do mês de referência [pesquisa por mês]',
        '\n[3] – Relatório comparativo – Referência 2019',
        '\n[4] – Listar todos os meses cadastrados',
        '\n[5]- Sair'
        )

def capturar_opcao():
    return int(input('Escolha a opção desejada: '))

def executar():
    service = ServiceONU()
    exibir()
    
    opcao = capturar_opcao()

    while opcao != 5:
        if opcao == 1:
            mes_ano = str(input('Digite o mes e o ano de referencia (padrão mm-yyyy: '))
            total_habitantes = int(input('Digite o total de habitantes: '))
            total_obitos = int(input('Digite o total de óbitos: '))
            service.cadastrar_mes_referencia(mes_ano, total_habitantes, total_obitos)
            pass
        elif opcao == 2:
            mes_ano = str(input('Digite o mes-ano referencia que gostaria de consultar: '))
            dados = service.exibir_dados_mes_referencia(mes_ano)
            print(dados)
            pass
        elif opcao == 3:
            ano = str(input('Digite o ano a ser comparado: '))
            service.gerar_relatorio_comparativo(ano)
            pass
        elif opcao == 4:
            service.listar()
            pass
        elif opcao == 5:
            sys.exit()
        else:
            print('Opção invalida')

        exibir()
        opcao = capturar_opcao()
    
if __name__ == '__main__':
    executar()