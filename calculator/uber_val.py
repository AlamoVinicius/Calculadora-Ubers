def conv_real(x=float, moeda='R$ '):
    """
    ==> Converta o resultado de uma str para uma moeda predeterminada (BRl),
    :param x: Valor a ser convertido
    :param moeda: Cifrão da moeda local
    :return: F'string da representação da moeda
    """
    return f'{moeda}{x:.2f}'.replace('.', ',')

def calculo_total(preco_gas=float, autonomia_carro=float, valor_corrida=float, km_corrida=float):
    while True:
        try:
            valkm_corrida = valor_corrida / km_corrida
            porc_manut = 20.0
            gasto_km = (preco_gas / autonomia_carro) + (valkm_corrida * porc_manut / 100)
            por_despesatotal = gasto_km * 100 / valkm_corrida
            lucro_total = valor_corrida - (valor_corrida * por_despesatotal / 100)
            gasto_gasolina = (km_corrida / autonomia_carro) * preco_gas
            porc_gasolina = gasto_gasolina * 100 / valor_corrida
        except ValueError:
            print('\033[91merro, Valor inválido\033[m')
        else:
            break
    # Saida formatada tabela simples
    lista = []
    lista.append(valor_corrida)   #0
    lista.append(gasto_gasolina)  #1
    lista.append(porc_gasolina)   #2
    lista.append(porc_manut)      #3
    lista.append(por_despesatotal)   #4
    lista.append(valkm_corrida)   #5
    lista.append(gasto_km)   #6
    lista.append(lucro_total)   #7
    return lista
    

def minha_tabela(lista):
    return f'''
GANHO BRUTO................: {conv_real(lista[0])}
GASTO COMBUSTIVEL..........: {conv_real(lista[1])}
GASTO COMBUSTIVEL EM %.....: {lista[2]:.2f} %
DESPESAS OUTROS APROX EM %.: {lista[3]:.2f} %
DESPESA TOTAL APROX EM %...: {lista[4]:.2f} %
GANHO POR KM...............: {conv_real(lista[5])}
DESPESA APROX/KM...........: {conv_real(lista[6])}
GANHO LIQUIDO..............: {conv_real(lista[7])}
obs: Outros ==> Manutenção, Financiamento ou aluguel,
seguros, impostos, alimentação, etc.
'''


def leia_dinheiro(txt):
    """
    ==> Essa função irá validar número em formatos de dinheiro (BRL)
    :param txt: valor que irá ser formatado.
    :return:  float de txt.
    """
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO:\"{entrada}\"valor inválido.\033[m')
        else:
            valido = True
            return float(entrada)

