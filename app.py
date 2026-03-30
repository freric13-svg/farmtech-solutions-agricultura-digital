#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FarmTech Solutions - Agricultura Digital
Projeto acadêmico com duas culturas:
1. Cogumelo Shitake
2. Horticultura / Olericultura

Requisitos atendidos:
- dados em vetores
- menu com inserção, listagem, atualização e remoção
- uso de loop e decisão
- exportação para CSV
"""

import csv

# Vetores paralelos
culturas = []
tipos_area = []
medida_1 = []
medida_2 = []
areas_m2 = []
insumos = []
dosagens = []
quantidades = []
observacoes = []


def linha():
    print("-" * 70)


def ler_float(msg):
    while True:
        try:
            valor = float(input(msg).replace(",", "."))
            if valor < 0:
                print("Digite um valor não negativo.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


def ler_int(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor < 0:
                print("Digite um valor não negativo.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


def pausar():
    input("\nPressione ENTER para continuar...")


def calcular_area_shitake():
    print("\n[Shitake] Área de produção em estufa/barracão")
    largura = ler_float("Informe a largura da estufa (m): ")
    comprimento = ler_float("Informe o comprimento da estufa (m): ")
    area = largura * comprimento
    obs = (
        "Microclima controlado: alta umidade relativa e temperatura ideal "
        "entre 18°C e 25°C para incubação/frutificação."
    )
    return "Retangular", largura, comprimento, area, obs


def calcular_area_horticultura():
    print("\n[Horticultura] Área de cultivo em canteiro/horta")
    largura = ler_float("Informe a largura do canteiro/área (m): ")
    comprimento = ler_float("Informe o comprimento do canteiro/área (m): ")
    area = largura * comprimento
    obs = (
        "Produção de hortaliças e legumes em pequena ou média escala. "
        "A área pode variar desde hortas comerciais menores até produções rurais."
    )
    return "Retangular", largura, comprimento, area, obs


def calcular_insumo_shitake(area):
    print("\nEscolha o manejo de insumo para Shitake:")
    print("1 - Água para irrigação/umidificação (litros por m²)")
    print("2 - Substrato (kg por m²)")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        dosagem = ler_float("Informe a dosagem de água (L/m²): ")
        total = dosagem * area
        return "Água", dosagem, total
    elif opcao == "2":
        dosagem = ler_float("Informe a dosagem de substrato (kg/m²): ")
        total = dosagem * area
        return "Substrato", dosagem, total
    else:
        print("Opção inválida. Será usado o padrão Água.")
        dosagem = ler_float("Informe a dosagem de água (L/m²): ")
        total = dosagem * area
        return "Água", dosagem, total


def calcular_insumo_horticultura(area):
    print("\nEscolha o manejo de insumo para Horticultura:")
    print("1 - Fertilizante (kg por m²)")
    print("2 - Pulverização (mL por metro)")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        dosagem = ler_float("Informe a dosagem do fertilizante (kg/m²): ")
        total = dosagem * area
        return "Fertilizante", dosagem, total
    elif opcao == "2":
        ruas = ler_int("Quantas ruas/canteiros a lavoura possui? ")
        metros = ler_float("Qual o comprimento médio de cada rua/canteiro (m)? ")
        dosagem = ler_float("Informe a dosagem da pulverização (mL/metro): ")
        total_ml = ruas * metros * dosagem
        total_litros = total_ml / 1000
        return "Pulverização", dosagem, total_litros
    else:
        print("Opção inválida. Será usado o padrão Fertilizante.")
        dosagem = ler_float("Informe a dosagem do fertilizante (kg/m²): ")
        total = dosagem * area
        return "Fertilizante", dosagem, total


def inserir_registro():
    linha()
    print("CADASTRO DE CULTURA")
    print("1 - Cogumelo Shitake")
    print("2 - Horticultura / Olericultura")
    opcao = input("Escolha a cultura: ").strip()

    if opcao == "1":
        cultura = "Shitake"
        tipo_area, m1, m2, area, obs = calcular_area_shitake()
        insumo, dosagem, quantidade = calcular_insumo_shitake(area)
    elif opcao == "2":
        cultura = "Horticultura"
        tipo_area, m1, m2, area, obs = calcular_area_horticultura()
        insumo, dosagem, quantidade = calcular_insumo_horticultura(area)
    else:
        print("Opção inválida.")
        return

    culturas.append(cultura)
    tipos_area.append(tipo_area)
    medida_1.append(m1)
    medida_2.append(m2)
    areas_m2.append(area)
    insumos.append(insumo)
    dosagens.append(dosagem)
    quantidades.append(quantidade)
    observacoes.append(obs)

    print("\nRegistro inserido com sucesso!")
    print(f"Cultura: {cultura}")
    print(f"Área calculada: {area:.2f} m²")
    if insumo == "Pulverização":
        print(f"Quantidade total: {quantidade:.2f} litros")
    else:
        unidade = "litros" if insumo == "Água" else "kg"
        print(f"Quantidade total: {quantidade:.2f} {unidade}")


def listar_registros():
    linha()
    print("LISTAGEM DE REGISTROS")
    if not culturas:
        print("Nenhum registro cadastrado.")
        return

    for i in range(len(culturas)):
        print(f"\nÍndice: {i}")
        print(f"Cultura: {culturas[i]}")
        print(f"Tipo de área: {tipos_area[i]}")
        print(f"Largura (m): {medida_1[i]:.2f}")
        print(f"Comprimento (m): {medida_2[i]:.2f}")
        print(f"Área total (m²): {areas_m2[i]:.2f}")
        print(f"Insumo: {insumos[i]}")
        print(f"Dosagem informada: {dosagens[i]:.2f}")
        if insumos[i] == "Pulverização":
            print(f"Quantidade total: {quantidades[i]:.2f} litros")
        elif insumos[i] == "Água":
            print(f"Quantidade total: {quantidades[i]:.2f} litros")
        else:
            print(f"Quantidade total: {quantidades[i]:.2f} kg")
        print(f"Observações: {observacoes[i]}")


def atualizar_registro():
    linha()
    print("ATUALIZAÇÃO DE REGISTRO")
    if not culturas:
        print("Nenhum registro cadastrado.")
        return

    listar_registros()
    indice = ler_int("\nInforme o índice que deseja atualizar: ")

    if indice < 0 or indice >= len(culturas):
        print("Índice inválido.")
        return

    print("\nRedigite todos os dados do registro:")
    print("1 - Cogumelo Shitake")
    print("2 - Horticultura / Olericultura")
    opcao = input("Escolha a cultura: ").strip()

    if opcao == "1":
        cultura = "Shitake"
        tipo_area, m1, m2, area, obs = calcular_area_shitake()
        insumo, dosagem, quantidade = calcular_insumo_shitake(area)
    elif opcao == "2":
        cultura = "Horticultura"
        tipo_area, m1, m2, area, obs = calcular_area_horticultura()
        insumo, dosagem, quantidade = calcular_insumo_horticultura(area)
    else:
        print("Opção inválida.")
        return

    culturas[indice] = cultura
    tipos_area[indice] = tipo_area
    medida_1[indice] = m1
    medida_2[indice] = m2
    areas_m2[indice] = area
    insumos[indice] = insumo
    dosagens[indice] = dosagem
    quantidades[indice] = quantidade
    observacoes[indice] = obs

    print("Registro atualizado com sucesso!")


def excluir_registro():
    linha()
    print("EXCLUSÃO DE REGISTRO")
    if not culturas:
        print("Nenhum registro cadastrado.")
        return

    listar_registros()
    indice = ler_int("\nInforme o índice que deseja excluir: ")

    if indice < 0 or indice >= len(culturas):
        print("Índice inválido.")
        return

    culturas.pop(indice)
    tipos_area.pop(indice)
    medida_1.pop(indice)
    medida_2.pop(indice)
    areas_m2.pop(indice)
    insumos.pop(indice)
    dosagens.pop(indice)
    quantidades.pop(indice)
    observacoes.pop(indice)

    print("Registro excluído com sucesso!")


def exportar_csv(nome_arquivo="dados_agricolas.csv"):
    linha()
    print("EXPORTAÇÃO DE DADOS")
    if not culturas:
        print("Não há dados para exportar.")
        return

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow([
            "cultura",
            "tipo_area",
            "largura_m",
            "comprimento_m",
            "area_m2",
            "insumo",
            "dosagem",
            "quantidade_total",
            "observacoes"
        ])

        for i in range(len(culturas)):
            escritor.writerow([
                culturas[i],
                tipos_area[i],
                f"{medida_1[i]:.2f}",
                f"{medida_2[i]:.2f}",
                f"{areas_m2[i]:.2f}",
                insumos[i],
                f"{dosagens[i]:.2f}",
                f"{quantidades[i]:.2f}",
                observacoes[i]
            ])

    print(f"Arquivo '{nome_arquivo}' exportado com sucesso!")


def menu():
    while True:
        linha()
        print("FARMTECH SOLUTIONS - AGRICULTURA DIGITAL")
        print("1 - Entrada de dados")
        print("2 - Saída/Listagem de dados")
        print("3 - Atualizar dado em uma posição do vetor")
        print("4 - Deletar dado do vetor")
        print("5 - Exportar dados para CSV")
        print("0 - Sair do programa")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            inserir_registro()
            pausar()
        elif opcao == "2":
            listar_registros()
            pausar()
        elif opcao == "3":
            atualizar_registro()
            pausar()
        elif opcao == "4":
            excluir_registro()
            pausar()
        elif opcao == "5":
            exportar_csv()
            pausar()
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")
            pausar()


if __name__ == "__main__":
    menu()
