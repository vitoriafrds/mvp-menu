base_dados_onu_2019 = {
    "mes_ano_referencia" : "01-2022",
    "total_habitantes" : 5000,
    "total_obitos" : 1800
}

class ServiceONU():
    def __init__(self) -> None:
        self.dados_gerais = []

    def cadastrar_mes_referencia(self, mes_ano, total_habitantes, total_obitos):
        base_dados_onu = {}

        base_dados_onu['mes_ano_referencia'] = mes_ano
        base_dados_onu['total_habitantes'] = total_habitantes
        base_dados_onu['total_obitos'] = total_obitos
        self.dados_gerais.append(base_dados_onu)

        print('Cadastro realizado com sucesso')

    def exibir_dados_mes_referencia(self, mes) -> dict:
        for dado in self.dados_gerais:
            if dado.get('mes_ano_referencia') == mes:
                return dado
            else:
                print("mes-ano nao cadastrado")
                pass


    def gerar_relatorio_comparativo(self, ano):
        print('RELATÓRIO COMPARATIVO DE TAXA DE MORTALIDADE ANUAL')
        
        for dado in self.dados_gerais:
            ano_referencia = str(dado.get('mes_ano_referencia')).split('-')[1]

            if (ano_referencia == ano):
                total_habitantes = dado.get('total_habitantes') + base_dados_onu_2019.get('total_habitantes')
                total_obitos = dado.get('total_obitos') + base_dados_onu_2019.get('total_obitos')
                
                print(f'TOTAL HABITANTES:..... {total_habitantes}')
                print(f'TOTAL HABITANTES:..... {total_obitos}')
                print(f'TAXA POR 100K HABITANTES - 2019:..... {15}')

    def listar(self):
        for dado in self.dados_gerais:
            print(dado)
            
