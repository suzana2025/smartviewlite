import pandas as pd
import matplotlib.pyplot as plt

PRODUCAO = "../data/producao.csv"
OPERADORES = "../data/operadores.csv"

def carregar_dados():
    producao = pd.read_csv(PRODUCAO)
    operadores = pd.read_csv(OPERADORES)
    return producao, operadores

def calcular_metricas(df):
    df["percentual_meta"] = (df["quantidade_produzida"] / df["meta_diaria"]) * 100
    return df

def gerar_relatorio(df):
    print("\n===== RELATÓRIO DE PRODUÇÃO =====")
    for _, row in df.iterrows():
        print(
            f"Data: {row['data']} | Linha: {row['linha']} | "
            f"Produção: {row['quantidade_produzida']} kg | "
            f"Meta: {row['meta_diaria']} kg | "
            f"Atingimento: {row['percentual_meta']:.2f}%"
        )

def gerar_grafico(df):
    plt.figure(figsize=(10, 5))
    plt.title("Atingimento de Meta por Dia")
    plt.plot(df["data"], df["percentual_meta"], marker="o")
    plt.xlabel("Data")
    plt.ylabel("% da Meta Atingida")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    producao, operadores = carregar_dados()
    producao = calcular_metricas(producao)
    gerar_relatorio(producao)
    gerar_grafico(producao)

if __name__ == "__main__":
    main()
