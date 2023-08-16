# Automatizar um processo com a linguagem Python:
# Instalar e utilizar bibliotecas
# Buscar dados de ações automaticamente
# Gerar algumas estatísticas com esses dados
# Gerar um gráfico simples de linha
# Automatizar o controle do teclado e mouse com o pyautogui Utilizar strings de múltiplas linhas
# Enviar e-mails de forma automática

# Projeto da aula:
# Você trabalha em uma empresa de investimentos e todos os dias precisa enviar um e-mail com o valor da cotação de algumas ações. O e-mail precisa conter as informações dos últimos seis meses:
# Cotação mínima da ação 
# Cotação máxima da ação 
# Cotação do dia

# O que é o Yahoo Finanças?
# Site que fornece notícias sobre finanças, incluindo cotações de ações. 
# Link: https://br.financas.yahoo.com/

# Instalacao das bibliotecas no python
# !pip install yfinance
# !pip install pyautogui

# importar biblioteca
import yfinance

# Buscando as cotacoes de uma Acao
ticker = input('Digite o codigo da açao: ')
dados = yfinance.Ticker(ticker)
dados.history()

# Configurando o periodo historico
# Ano:y
# Mes:mo
# Dia: d

tabela = dados.history("6mo")
tabela 
#DICA: comando print para mostrar na tela!
# print(tabela)

# Selecionando apenas a coluna de Fechamento (Close)
# Para selecionar a coluna desejada, basta colocar o nome dela entre colchetes na frente da variável que está armazenando os dados

fechamento = tabela.Close
fechamento

# Gerando um Grafico de Linha
# Vamos gerar um grafico muito simples, apenas utilizando o metodo .plot()

# fechamento.plot()

#Gerando as estatísticas
#Gerar estatísticas no Python é muito simples, pois já temos os métodos prontos para serem aplicados!
#cotação máxima: max()
#votação mínima: min()
#cotação atual: é a última linha!Para acessá-la basta colocar [-1]

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

print(maxima)
print(minima)
print(atual)

# Enviando e-mail de forma automática
# Processo de enviar um e-mail passo a passo:
# abrir uma nova aba no navegador (clicar em + ou CTRL + T)
# digitar o endereço do gmail (www.gmail.com) e digitar ENTER
# clicar em Escrever
# digitar o endereço de e-mail do destinatário
# mudar para o campo Assunto (clicar no campo ou digitar tab)
# digitar o Assunto
# mudar para campo principal do e-mail (clicar no campo ou digitar tab) escrever a mensagem
# clicar em Enviar

# Instalando as bibliotecas
# !pip install pyautogui
# !pip install pyperclip

# Importando biblioteca
import pyautogui
import pyperclip

# Criando o e-mail que vamos enviar
destinatario = "seu_email@gmail.com"
assunto = "Analise diaria"

mensagem = f"""
Bom dia,

Segue abaixo as analises de acao {ticker} dos ultimos seis meses:

Cotacao maxima: R${round(maxima,2)}
Cotacao minima: R${round(minima,2)}
Cotacao atual: R${round(atual,2)}

Atenciosamente,
Seu nome
"""

print(destinatario)
print(assunto)
print(mensagem)


# Automatizando o envio
# Configurar uma pausa entre as acoes de pyautogui
pyautogui.PAUSE = 6

# Abrir uma nova aba
pyautogui.hotkey("command", "t")

# copiar o endereco de email para o clipboard
pyperclip.copy("www.gmail.com")

# colar o endereco do gmail e dar um ENTER
 pyautogui.hotkey("command", "v")
 pyautogui.press("enter")
 
 # Clicando no botao Escrever
 pyautogui.click(x=2030, y=210)
 
 # Preenchendo o destinatario
 pyautogui.copy(destinatario)
 pyautogui.hotkey("ctrl", "v")
 pyautogui.press("tab")
 
 # preenchendo o assunto
 pyperclip.copy(assunto)
 pyautogui.hotkey("ctrl", "v")
 pyautogui.press("tab")
 
 # preenchendo a mensagem
 pyperclip.copy(mensagem)
 pyautogui.hotkey("crtl", "v")
 
 # Clicar no botao Enviar
 pyautogui.click(x=3107, y=975)
 
 # Fechar a aba do gmail
 pyautogui.hotkey("crtl", "f4")
 
 # Imprimir mensagem de enviar com sucesso
 print('E-mail enviado com sucesso!')
 
 
    