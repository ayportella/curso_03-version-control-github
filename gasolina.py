import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv")

grafico = sns.lineplot(data=df, x="dia", y="venda", palette="pastel")
grafico.set_title("Variação do preço da gasolina por dia", fontsize=14, fontweight="bold")
grafico.set(xlabel="Dia", ylabel="Preço")
grafico.figure.set_size_inches(10,6) 

plt.savefig('gasolina.png')