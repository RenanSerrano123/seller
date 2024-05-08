def calcular_comissao(salario_fixo, total_vendas):
    comissao = 0.2 * total_vendas
    meta_vendas = 0.5 * salario_fixo
    atingiu_meta = comissao >= meta_vendas
    return comissao, atingiu_meta
def main():
    salario_fixo = float(input())
    total_vendas = float(input())
    comissao, atingiu_meta = calcular_comissao(salario_fixo, total_vendas)
    print(f"{comissao:.2f}")
    if atingiu_meta:
        print("Atingiu meta de vendas")
    else:
        print("Nao atingiu meta de vendas")
main()