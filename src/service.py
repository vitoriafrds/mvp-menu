dados_gerais = []

base_dados_onu = {
    "mes_ano_referencia" : "",
    "total_habitantes" : 0,
    "total_obitos" : 0
}

dados_gerais.append(base_dados_onu)

base_dados_onu_2019 = {
    "mes_ano_referencia" : "01-2022",
    "total_habitantes" : 5000,
    "total_obitos" : 1800
}

class ServiceONU():
    def __init__(self) -> None:
        self.dados_gerais = dados_gerais
        self.base_dados_onu = base_dados_onu

    def cadastrar_mes_referencia(self, mes_ano, total_habitantes, total_obitos):
        print('PROCESSO PARA CADASTRO DOS DADOS INICIADO...')

        self.base_dados_onu['mes_ano_referencia'] = mes_ano
        self.base_dados_onu['total_habitantes'] = total_habitantes
        self.base_dados_onu['total_obitos'] = total_obitos
        self.dados_gerais.append(self.base_dados_onu)

        print('DADOS CADASTRADOS COM SUCESSO')

    def exibir_dados_mes_referencia(self, mes) -> dict:
        for dado in self.dados_gerais:
            if dado.get('mes_ano_referencia') == mes:
                return dado
            else:
                print("mes-ano nao cadastrado")


    def gerar_relatorio_comparativo(self, ano):
        print('RELATÓRIO COMPARATIVO DE TAXA DE MORTALIDADE ANUAL')
        
    def listar(self):
        results = [dado for dado in self.dados_gerais]
        return results
