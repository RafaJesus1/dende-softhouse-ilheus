class Statistics:
    """
    Uma classe para realizar cálculos estatísticos em um conjunto de dados.

    Atributos
    ----------
    dataset : dict[str, list]
        O conjunto de dados, estruturado como um dicionário onde as chaves
        são os nomes das colunas e os valores são listas com os dados.
    """
    def __init__(self, dataset):
        """
        Inicializa o objeto Statistics.

        Parâmetros
        ----------
        dataset : dict[str, list]
            O conjunto de dados, onde as chaves representam os nomes das
            colunas e os valores são as listas de dados correspondentes.
        """
        self.dataset = dataset

    def mean(self, column):
        """
        Calcula a média aritmética de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A média dos valores na coluna.
        """
        dados = self.dataset[column]
        QuantantidaDados = len(dados)
        Soma = sum(dados)

        Media = Soma/QuantantidaDados

        return Media
        pass

    def median(self, column):
        """
        Calcula a mediana de uma coluna.

        A mediana é o valor central de um conjunto de dados ordenado.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O valor da mediana da coluna.
        """
        mediana = 0
        if isinstance(column, str):
            dados = self.dataset[column]
        else:
            dados = column
        
        if type(dados[0]) == str:
             prioridade = {"baixa": 1, "media": 2, "alta": 3}
             dadosOrdenados = sorted(dados, key=prioridade.get)
             mediana = dadosOrdenados[len(dadosOrdenados)//2-1]
             return mediana

        else:
            dadosOrdenados = sorted(dados)
            if len(dadosOrdenados)%2 == 0:
             mediana = (dadosOrdenados[(len(dadosOrdenados)//2)-1]+ dadosOrdenados[(len(dadosOrdenados)//2)])/2
             return mediana 
            
            else:
             mediana = dadosOrdenados[len(dadosOrdenados)//2]
             return mediana

        pass

    def mode(self, column):
        """
        Encontra a moda (ou modas) de uma coluna.

        A moda é o valor que aparece com mais frequência no conjunto de dados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        list
            Uma lista contendo o(s) valor(es) da moda.
        """
        frequenciaAbsoluta = self.absolute_frequency(column)
        Moda = [max(frequenciaAbsoluta, key=frequenciaAbsoluta.get)]
        return Moda
         


    def variance(self, column):
        """
        Calcula a variância populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A variância dos valores na coluna.
        """
        dados = self.dataset[column]
        mediaDados = self.mean(column)
        variancia = 0
        somaQuadrados = 0

        for i in dados:
          somaQuadrados += (i - mediaDados) ** 2

        variancia = somaQuadrados/ len(dados)
        
        return variancia
        pass

    def stdev(self, column):
        """
        Calcula o desvio padrão populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O desvio padrão dos valores na coluna.
        """
        variancia = self.variance(column)
        desvioPadrao = variancia ** 0.5
        return desvioPadrao
        pass

    def covariance(self, column_a, column_b):
        """
        Calcula a covariância entre duas colunas.

        Parâmetros
        ----------
        column_a : str
            O nome da primeira coluna (X).
        column_b : str
            O nome da segunda coluna (Y).

        Retorno
        -------
        float
            O valor da covariância entre as duas colunas.
        """
        dadosA = self.dataset[column_a]
        dadosB = self.dataset[column_b]
        
        mediaA = self.mean(column_a)
        mediaB = self.mean(column_b)

        quantidadeDados = len(dadosA)
        somatoria = 0


        for valorA, valorB in zip(dadosA, dadosB):
            somatoria += (valorA - mediaA) * (valorB - mediaB) 
        

        covariancia = somatoria / quantidadeDados
        
        return covariancia
        pass

    def itemset(self, column):
        """
        Retorna o conjunto de itens únicos em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        set
            Um conjunto com os valores únicos da coluna.
        """
        dados = self.dataset[column]
        return set(dados)
        pass

    def absolute_frequency(self, column):
        """
        Calcula a frequência absoluta de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas contagens (frequência absoluta).
        """
        dados = self.dataset[column]
        frequenciaAbsoluta = {}
        for i in dados:
          if i not in frequenciaAbsoluta :
           frequenciaAbsoluta[i] = 0
          frequenciaAbsoluta[i] += 1

        return frequenciaAbsoluta 
        pass

    def relative_frequency(self, column):
        """
        Calcula a frequência relativa de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas proporções (frequência relativa).
        """
        frequenciaAbsoluta = self.absolute_frequency(column)
        frequenciaRelativa = {}
        frenqueciatotal = sum(frequenciaAbsoluta.values())

        for chave in frequenciaAbsoluta:
           porcentagem = frequenciaAbsoluta[chave]/frenqueciatotal
           frequenciaRelativa[chave] = porcentagem
        return frequenciaRelativa
        pass

    def cumulative_frequency(self, column, frequency_method='absolute'):
        """
        Calcula a frequência acumulada (absoluta ou relativa) de uma coluna.

        A frequência é calculada sobre os itens ordenados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        frequency_method : str, opcional
            O método a ser usado: 'absolute' para contagem acumulada ou
            'relative' para proporção acumulada (padrão é 'absolute').

        Retorno
        -------
        dict
            Um dicionário ordenado com os itens como chaves e suas
            frequências acumuladas como valores.
        """

        if frequency_method == 'absolute':
            frequenciaBase = self.absolute_frequency(column)
        else:
            frequenciaBase = self.relative_frequency(column)

        if column == "priority":
            dadosOrdenados = ["baixa", "media", "alta"]
        else:
            dadosOrdenados = sorted(frequenciaBase.keys())


        frequenciaAcumulada = {}
        somaAcumulada = 0
        
        for item in dadosOrdenados:
            if item in frequenciaBase:
                somaAcumulada += frequenciaBase[item]
                frequenciaAcumulada[item] = somaAcumulada
                
        return frequenciaAcumulada
        
        pass

    def conditional_probability(self, column, value1, value2):
        """
        Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2).

        Este método trata a coluna como uma sequência e calcula a probabilidade
        de encontrar `value1` imediatamente após `value2`.

        Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        value1 : any
            O valor do evento consequente (A).
        value2 : any
            O valor do evento condicionante (B).

        Retorno
        -------
        float
            A probabilidade condicional, um valor entre 0 e 1.
        """
        dados = self.dataset[column]
        contagemCondicionante = 0  
        contagemSequencia = 0     

   
        for i in range(len(dados) - 1):
            if dados[i] == value2:
                contagemCondicionante += 1
                if dados[i + 1] == value1:
                    contagemSequencia += 1

        if contagemCondicionante == 0:
            return 0
            
        return contagemSequencia / contagemCondicionante

        pass

    def quartiles(self, column):
        """
        Calcula os quartis (Q1, Q2 e Q3) de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário com os quartis Q1, Q2 (mediana) e Q3.
        """
        dados = self.dataset[column]
        Q2 = self.median(column)

        dados25perc = [i for i in dados if i <= Q2]
        dados75perc = [i for i in dados if i >= Q2]

        Q1 = self.median(dados25perc)
        Q3 = self.median(dados75perc)

        quartis = {"Q1": Q1, "Q2": Q2, "Q3": Q3}
        print(quartis)
        return quartis

        pass

    def histogram(self, column, bins):
        """
        Gera um histograma baseado em buckets (intervalos).

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        bins : int
            Número de buckets (intervalos).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os intervalos (tuplas)
            e os valores são as contagens.
        """
        dados = sorted(self.dataset[column])
        limiteMinimo = min(dados)
        limiteMaximo = max(dados)
        amplitudeTotal = limiteMaximo - limiteMinimo
        
        intervalo = amplitudeTotal / bins
        histograma = {}
        
        pontoAtual = limiteMinimo
        for i in range(bins):
            proximoPonto = pontoAtual + intervalo
            histograma[(pontoAtual, proximoPonto)] = 0
            pontoAtual = proximoPonto
        
        for valor in dados:
            for chave in histograma.keys():
                inicio, fim = chave
                if valor >= inicio and valor < fim:
                    histograma[chave] += 1
                    break
                elif valor == limiteMaximo and abs(valor - fim) < 1e-9: 
                    histograma[chave] += 1
                    break
    
        return histograma
        pass       
