import pandas as pd

csv = pd.read_csv('https://pastebin.com/raw/8HL2hdq5', sep=';')

csv = csv.dropna()


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

csv['Tipo'] = le.fit_transform(csv['Tipo'])

dados = csv.values

entrada = dados[:, :5]

comentarios = dados[:, 5]

like = dados[:, 6]

compartilhamentos = dados[:, 7]

from sklearn.linear_model import LinearRegression

modeloA = LinearRegression()
modeloA.fit(entrada, comentarios)

modeloB = LinearRegression()
modeloB.fit(entrada, like)

modeloC = LinearRegression()
modeloC.fit(entrada, compartilhamentos)

novosValores = []
novosValores.append(int(input('Informe o número do tipo da postagem: Foto[0]|Link[1]|Status[2]|Video[3]')))
novosValores.append(int(input('Mês: ')))
novosValores.append(int(input('Dia da semana: D[1]|S[2]|T[3]|Q[4]|Q[5]|S[6]|S[7]')))
novosValores.append(int(input('Hora:')))
novosValores.append(int(input('Pago: SIM[1]|NÃO[0]')))

qtLikes = modeloB.predict([novosValores])
qtComentarios = modeloA.predict([novosValores])
qtCompartilhamentos = modeloC.predict([novosValores])

print('Média de Likes: ', int(qtLikes[0]))
print('Média de Compartilhamento: ', int(qtCompartilhamentos[0]))
print('Média de Comentários: ', int(qtComentarios[0]))
