import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Escolha uma pasta:")

lista_arquivos = os.listdir(caminho)

diretorio = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Músicas": [".mp3", ".wav", ".mp4"],
    "Planilhas": [".xls", ".xlsx"],
    "Arquivos Diversos": [".pdf", ".word", ".txt", ".doc", ".pptx"],
    "Arquivos CSV": [".csv"],
    "Arquivos ZIP": [".zip", ".exe", ".msi", ".rar"]
}

for arquivo in lista_arquivos:

    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in diretorio:
        if extensao in diretorio[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

