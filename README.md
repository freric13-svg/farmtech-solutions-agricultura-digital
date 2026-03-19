#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

# =========================
# VETORES PARA ARMAZENAMENTO
# =========================
culturas = []
tipos_area = []
larguras = []
comprimentos = []
areas_m2 = []
insumos = []
dosagens = []
quantidades_totais = []
observacoes = []


# =========================
# FUNÇÕES AUXILIARES
# =========================
def linha():
    print("-" * 70)


def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < 0:
                print("Digite um valor maior ou igual a zero.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


def ler_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Digite um valor maior ou igual a zero.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


def pausar():
    input("\nPressione ENTER para continuar...")


# =========================
# CÁLCULO DE ÁREA
# =========================
def calcular_area_shitake():
    print("\n[Shitake] Cálculo de área da estufa/barracão")
    largura = ler_float("Informe a largura da estufa (m): ")
    comprimento = ler_float("Informe o comprimento da estufa (m): ")
    area = largura * comprimento

    obs = (
        "Microclima controlado: alta umidade relativa e temperatura "
        "ideal entre 18°C e 25°C nas fases de incubação e frutificação."
    )

    return "Retangular", largura, comprimento, area, obs


def calcular_area_horticultura():
    print("\n[Horticultura] Cálculo de área do canteiro/horta")
    largura = ler_float("Informe a largura da área/canteiro (m): ")
    comprimento = ler_float("Informe o comprimento da área/canteiro (m): ")
    area = largura * comprimento

    obs = (
        "Produção de hortaliças, legumes e frutas em pequena ou média escala, "
        "com áreas que podem variar de hortas comerciais menores a produções rurais."
    )

    return "Retangular", largura, comprimento, area, obs


# =========================
# CÁLCULO DE INSUMOS
# =========================
def calcular_insumo_shitake(area):
    print("\nEscolha o manejo de insumo para Shitake:")
    print("1 - Água para irrigação/umidificação (L/m²)")
    print("2 - Substrato (kg/m²)")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        dosagem = ler_float("Informe a dosagem de água (L/m²): ")
        quantidade_total = dosagem * area
        return "Água", dosagem, quantidade_total

    if opcao == "2":
        dosagem = ler_float("Informe a dosagem de substrato (kg/m²): ")
        quantidade_total = dosagem * area
        return "Substrato", dosagem, quantidade_total

    print("Opção inválida. Será usado o padrão Água.")
    dosagem = ler_float("Informe a dosagem de água (L/m²): ")
    quantidade_total = dosagem * area
    return "Água", dosagem, quantidade_total


def calcular_insumo_horticultura(area):
    print("\nEscolha o manejo de insumo para Horticultura:")
    print("1 - Fertilizante (kg/m²)")
    print("2 - Pulverização (mL/metro)")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        dosagem = ler_float("Informe a dosagem do fertilizante (kg/m²): ")
        quantidade_total = dosagem * area
        return "Fertilizante", dosagem, quantidade_total

    if opcao == "2":
        ruas = ler_int("Quantas ruas/canteiros a lavoura possui? ")
        metros_por_rua = ler_float("Qual o comprimento médio de cada rua/canteiro (m)? ")
        dosagem = ler_float("Informe a dosagem da pulverização (mL/metro): ")

        total_ml = ruas * metros_por_rua * dosagem
        total_litros = total_ml / 1000
        return "Pulverização", dosagem, total_litros

    print("Opção inválida. Será usado o padrão Fertilizante.")
    dosagem = ler_float("Informe a dosagem do fertilizante (kg/m²): ")
    quantidade_total = dosagem * area
    return "Fertilizante", dosagem, quantidade_total


# =========================
# MENU - OPERAÇÕES
# =========================
def inserir_registro():
    linha()
    print("ENTRADA DE DADOS")
    print("1 - Cogumelo Shitake")
    print("2 - Horticultura / Olericultura")

    opcao = input("Escolha a cultura: ").strip()

    if opcao == "1":
        cultura = "Shitake"
        tipo_area, largura, comprimento, area, obs = calcular_area_shitake()
        insumo, dosagem, quantidade_total = calcular_insumo_shitake(area)

    elif opcao == "2":
        cultura = "Horticultura"
        tipo_area, largura, comprimento, area, obs = calcular_area_horticultura()
        insumo, dosagem, quantidade_total = calcular_insumo_horticultura(area)

    else:
        print("Opção inválida.")
        return

    culturas.append(cultura)
    tipos_area.append(tipo_area)
    larguras.append(largura)
    comprimentos.append(comprimento)
    areas_m2.append(area)
    insumos.append(insumo)
    dosagens.append(dosagem)
    quantidades_totais.append(quantidade_total)
    observacoes.append(obs)

    print("\nRegistro inserido com sucesso!")
    print(f"Cultura: {cultura}")
    print(f"Área: {area:.2f} m²")

    if insumo in ["Água", "Pulverização"]:
        print(f"Quantidade total do insumo: {quantidade_total:.2f} litros")
    else:
        print(f"Quantidade total do insumo: {quantidade_total:.2f} kg")


def listar_registros():
    linha()
    print("SAÍDA DE DADOS")

    if len(culturas) == 0:
        print("Nenhum registro cadastrado.")
        return

    for i in range(len(culturas)):
        print(f"\nÍndice: {i}")
        print(f"Cultura: {culturas[i]}")
        print(f"Tipo de área: {tipos_area[i]}")
        print(f"Largura: {larguras[i]:.2f} m")
        print(f"Comprimento: {comprimentos[i]:.2f} m")
        print(f"Área total: {areas_m2[i]:.2f} m²")
        print(f"Insumo: {insumos[i]}")
        print(f"Dosagem informada: {dosagens[i]:.2f}")

        if insumos[i] in ["Água", "Pulverização"]:
            print(f"Quantidade total: {quantidades_totais[i]:.2f} litros")
        else:
            print(f"Quantidade total: {quantidades_totais[i]:.2f} kg")

        print(f"Observações: {observacoes[i]}")


def atualizar_registro():
    linha()
    print("ATUALIZAÇÃO DE DADOS")

    if len(culturas) == 0:
        print("Nenhum registro cadastrado.")
        return

    listar_registros()
    indice = ler_int("\nInforme o índice que deseja atualizar: ")

    if indice < 0 or indice >= len(culturas):
        print("Índice inválido.")
        return

    print("\nDigite novamente os dados do registro.")
    print("1 - Cogumelo Shitake")
    print("2 - Horticultura / Olericultura")
    opcao = input("Escolha a cultura: ").strip()

    if opcao == "1":
        cultura = "Shitake"
        tipo_area, largura, comprimento, area, obs = calcular_area_shitake()
        insumo, dosagem, quantidade_total = calcular_insumo_shitake(area)

    elif opcao == "2":
        cultura = "Horticultura"
        tipo_area, largura, comprimento, area, obs = calcular_area_horticultura()
        insumo, dosagem, quantidade_total = calcular_insumo_horticultura(area)

    else:
        print("Opção inválida.")
        return

    culturas[indice] = cultura
    tipos_area[indice] = tipo_area
    larguras[indice] = largura
    comprimentos[indice] = comprimento
    areas_m2[indice] = area
    insumos[indice] = insumo
    dosagens[indice] = dosagem
    quantidades_totais[indice] = quantidade_total
    observacoes[indice] = obs

    print("Registro atualizado com sucesso!")


def excluir_registro():
    linha()
    print("DELEÇÃO DE DADOS")

    if len(culturas) == 0:
        print("Nenhum registro cadastrado.")
        return

    listar_registros()
    indice = ler_int("\nInforme o índice que deseja excluir: ")

    if indice < 0 or indice >= len(culturas):
        print("Índice inválido.")
        return

    culturas.pop(indice)
    tipos_area.pop(indice)
    larguras.pop(indice)
    comprimentos.pop(indice)
    areas_m2.pop(indice)
    insumos.pop(indice)
    dosagens.pop(indice)
    quantidades_totais.pop(indice)
    observacoes.pop(indice)

    print("Registro excluído com sucesso!")


def exportar_csv(nome_arquivo="dados_agricolas.csv"):
    linha()
    print("EXPORTAÇÃO PARA CSV")

    if len(culturas) == 0:
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
                f"{larguras[i]:.2f}",
                f"{comprimentos[i]:.2f}",
                f"{areas_m2[i]:.2f}",
                insumos[i],
                f"{dosagens[i]:.2f}",
                f"{quantidades_totais[i]:.2f}",
                observacoes[i]
            ])

    print(f"Arquivo '{nome_arquivo}' exportado com sucesso!")


# =========================
# MENU PRINCIPAL
# =========================
def menu_principal():
    while True:
        linha()
        print("FARMTECH SOLUTIONS - AGRICULTURA DIGITAL")
        print("1 - Entrada de dados")
        print("2 - Saída de dados")
        print("3 - Atualização de dados")
        print("4 - Deleção de dados")
        print("5 - Exportar CSV")
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
    menu_principal()
