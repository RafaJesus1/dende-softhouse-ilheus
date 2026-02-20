import os
import csv
from dende_statistics import Statistics

# 1. DEFINIÇÃO DA FUNÇÃO (Deve vir primeiro)
def carregarSpotify(caminhoArquivo):
    dataset = {}
    with open(caminhoArquivo, mode='r', encoding='utf-8') as ficheiro:
        leitor = csv.DictReader(ficheiro)
        for coluna in leitor.fieldnames:
            dataset[coluna] = []
        for linha in leitor:
            for coluna in leitor.fieldnames:
                valor = linha[coluna]
                try:
                    if '.' in valor:
                        dataset[coluna].append(float(valor))
                    else:
                        dataset[coluna].append(int(valor))
                except ValueError:
                    dataset[coluna].append(valor)
    return dataset

# 2. LÓGICA DO CAMINHO DINÂMICO
# Pega a pasta onde este arquivo main.py está salvo
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
# Junta o nome da pasta com o nome do arquivo CSV
caminho_csv = os.path.join(diretorio_do_script, 'spotify_data clean.csv')

# 3. CHAMADA DA FUNÇÃO (Agora ela existe e o caminho está correto)
dadosSpotify = carregarSpotify(caminho_csv)

# 4. RESTANTE DO CÓDIGO
stats = Statistics(dadosSpotify)

print("ANÁLISE EXPLORATÓRIA SPOTIFY")


colunaPop = "track_popularity"
if colunaPop in dadosSpotify:
    print(f"\n[ Estatísticas de {colunaPop} ]")
    resPop = stats.quartiles(colunaPop)
    print(f"Média: {stats.mean(colunaPop):.2f}")
    print(f"Mediana: {resPop['Q2']:.2f}")
    print(f"Quartis: Q1={resPop['Q1']:.2f} | Q3={resPop['Q3']:.2f}")
    

    print(f"\n[ Análise de Frequência: {colunaPop} ]")
    freqTotal = stats.absolute_frequency(colunaPop)
    print(f"Quantidade de músicas com popularidade 0 (Inativas): {freqTotal.get(0, 0)}")
    print(f"Quantidade de músicas com popularidade 50 (Média): {freqTotal.get(50, 0)}")
    print(f"Quantidade de músicas com popularidade 100 (Hits Máximos): {freqTotal.get(100, 0)}")
    print(f"Valor mais frequente (Moda): {stats.mode(colunaPop)}")

colunaDuracao = "track_duration_min"
if colunaDuracao in dadosSpotify:
    print(f"\n[ Estatísticas de {colunaDuracao} ]")
    resDur = stats.quartiles(colunaDuracao)
    print(f"Duração Média: {stats.mean(colunaDuracao):.2f} min")
    print(f"Duração Mediana: {resDur['Q2']:.2f} min")
    
    modaDuracao = stats.mode(colunaDuracao)
    print(f"Moda de Duração: {modaDuracao} min")




if "artist_popularity" in dadosSpotify and "track_popularity" in dadosSpotify:
    covariancia = stats.covariance("artist_popularity", "track_popularity")
    print(f"\nRelação Artista vs Música")
    print(f"Covariância: {covariancia:.2f}")