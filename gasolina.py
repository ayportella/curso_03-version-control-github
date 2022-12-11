import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv")

grafico = sns.lineplot(data=df, x="dia", y="venda", palette="colorblind")
grafico.set_title("Variação do Preço da Gasolina por Dia", fontsize=20, fontweight="bold")
grafico.set(xlabel="Dia", ylabel="Preço")
grafico.figure.set_size_inches(15,10) 

plt.savefig('gasolina.png')