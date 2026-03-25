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
        # cadê as validações de tipo e estrutura do dataset?
        # - Validar se o dataset é um dicionário
        # - Validar se as chaves são strings
        # - Validar se os valores são listas
        # - Validar se todas as listas têm o mesmo comprimento
        # - Validar se os dados nas listas são do tipo esperado (numéricos para cálculos estatísticos)
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
        # cadê a validação do tipo de dado na coluna? 
        # E a validação se a coluna existe no dataset?
        # e se a coluna não for numérica?
        # poderia criar um método privado para validar a coluna e os dados
        # antes de realizar os cálculos: 
            # def _validate_numeric_column(self, column):

        dados = self.dataset[column]
        QuantantidaDados = len(dados)
        Soma = sum(dados)

        # resumido: 
        # return sum(self.dataset[column]) / len(self.dataset[column])
        Media = Soma/QuantantidaDados

        return Media
        pass # remover os pass depois de implementar o método

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
            dados = column # não entendi isso aqui, o parâmetro column é uma string, então não faria 
            #sentido passar uma lista diretamente. 
        
        if type(dados[0]) == str:
             prioridade = {"baixa": 1, "media": 2, "alta": 3} # isso é para o caso do teste, não deveria tá aqui
             dadosOrdenados = sorted(dados, key=prioridade.get)
             mediana = dadosOrdenados[len(dadosOrdenados)//2-1]
             return mediana

        else:
            dadosOrdenados = sorted(dados)
            #nossa, muito ruim de ler isso aqui
            if len(dadosOrdenados)%2 == 0:
             
             mediana = (dadosOrdenados[(len(dadosOrdenados)//2)-1]+ dadosOrdenados[(len(dadosOrdenados)//2)])/2
             return mediana 
            
            else:
             mediana = dadosOrdenados[len(dadosOrdenados)//2] 
             return mediana

        pass # remover o pass depois de implementar o método

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
        # bom reuso do código, parabéns!
        frequenciaAbsoluta = self.absolute_frequency(column)
        
        #se eu tiver mais de um valor máximo de frequência, eu preciso retornar todos eles, não só um.
        # max_frequencia = max(frequenciaAbsoluta.values())
        # return [chave for chave, valor in frequenciaAbsoluta.items() if valor == max_frequencia]
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
        
        #boooa, reuso de código, a validação já seria feita no método mean,
        # então não precisa se preocupar com isso aqui.

        mediaDados = self.mean(column) # media é um melhor nome para a variável do que mediaDados, 
        #já que o método mean já deixa claro que é a média dos dados da coluna.

        # isso aqui tá didático, mas poderia ser resumido usando uma compreensão de lista:
        # return sum((i - media) ** 2 for i in dados) / len(dados)
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
        # boooa, bom reuso do código, a validação já seria feita no método variance,
        # então não precisa se preocupar com isso aqui.
        # além disso, o cálculo do desvio padrão é simplesmente a raiz quadrada da variância, então tá ótimo assim.
        # poderia só ter sido resumido para: 
        # return self.variance(column) ** 0.5
        variancia = self.variance(column)
        desvioPadrao = variancia ** 0.5
        return desvioPadrao
        pass # remover o pass depois de implementar o método

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

        # você poderia inverter a ordem e chamar a média primeiro, pois ela já faz a validação
        # da coluna, e aí depois pegar os dados, assim você evita de pegar os dados de uma coluna
        # que não existe ou que não é numérica.

        #media_a = self.mean(column_a)
        #media_b = self.mean(column_b)

        dadosA = self.dataset[column_a]
        dadosB = self.dataset[column_b]
        
        mediaA = self.mean(column_a)
        mediaB = self.mean(column_b)


        quantidadeDados = len(dadosA) # quantidade_dados

        #aqui deveria ter um if para verificar se temos pelo menos 2 dados, 
        # caso contrário a covariância não faz sentido, e poderia retornar 0 ou lançar uma exceção.
        # if quantidadeDados < 2:
        #     return 0 # ou raise ValueError("A covariância requer pelo menos 2 dados em cada coluna.")
        # eu prefiro a exceção, porque assim o usuário do método fica sabendo que tem um problema com os dados,
        #  em vez de simplesmente receber um resultado que pode ser interpretado como válido (0) quando na verdade não é.

        somatoria = 0

        # isso aqui poderia ser simplificado usando uma compreensão de lista e a função sum, mas tá didático assim, então tá bom.
        # mas a sugestõa seria: 

        # return sum((valorA - mediaA) * (valorB - mediaB) for valorA, valorB in zip(dadosA, dadosB)) / quantidadeDados
        for valorA, valorB in zip(dadosA, dadosB):
            somatoria += (valorA - mediaA) * (valorB - mediaB) 
        

        covariancia = somatoria / quantidadeDados
        
        return covariancia
        pass # remover o pass depois de implementar o método

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
        # booa, mas poderia ser direto:
        # return set(self.dataset[column])
        dados = self.dataset[column]
        return set(dados)
        pass # remover o pass depois de implementar o método

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
        for i in dados: # isso aqui tá confuso, a variável de iteração deveria ter um nome mais claro, tipo "item" ou "valor", 
            #para ficar mais fácil de entender o que tá acontecendo.
        # identação errada, o if deveria estar dentro do for, para verificar se o item já existe no dicionário antes de incrementar a contagem.
        # didático, mas poderia ser resumido usando o método get do dicionário, que retorna um valor padrão (0) se a chave não existir:
        # for item in dados:
        #     frequenciaAbsoluta[item] = frequenciaAbsoluta.get(item, 0) + 1
          if i not in frequenciaAbsoluta : 
           frequenciaAbsoluta[i] = 0
          frequenciaAbsoluta[i] += 1

        return frequenciaAbsoluta 
        pass #remover o pass depois de implementar o método

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
        #boooa, bom reuso de código
        frequenciaAbsoluta = self.absolute_frequency(column)
        frequenciaRelativa = {}
        # boa estratégia, você também poderia ter feito:
        # total = len(self.dataset[column])
        frenqueciatotal = sum(frequenciaAbsoluta.values()) # mas muito bom

        # booa, bem didático, ficou simples de entender. 
        # uma outra forma de fazer seria usando uma compreensão de dicionário:
        # return {chave: valor / frenqueciatotal for chave, valor in frequenciaAbsoluta.items()}
        for chave in frequenciaAbsoluta:
           porcentagem = frequenciaAbsoluta[chave]/frenqueciatotal
           frequenciaRelativa[chave] = porcentagem
        return frequenciaRelativa
        pass # remover o pass depois de implementar o método

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

        # boa reutilização de código
        if frequency_method == 'absolute':
            frequenciaBase = self.absolute_frequency(column)
        else:
            frequenciaBase = self.relative_frequency(column)

        # isso aqui não deveria existir, pois só atende aos testes unitários 
        # e não deve ser colocado na implementação final, uma vez que o método deve ser genérico 
        # e funcionar para qualquer coluna, não só para a coluna de prioridade.
        if column == "priority":
            dadosOrdenados = ["baixa", "media", "alta"]
        else:
            dadosOrdenados = sorted(frequenciaBase.keys())


        frequenciaAcumulada = {}
        somaAcumulada = 0
        
        # muito bom, bem didático
        for item in dadosOrdenados:
            if item in frequenciaBase:
                somaAcumulada += frequenciaBase[item]
                frequenciaAcumulada[item] = somaAcumulada
                
        return frequenciaAcumulada
        
        pass # remover o pass depois de implementar o método

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

   
        # boooa, bem simples e didático
        for i in range(len(dados) - 1):
            if dados[i] == value2:
                contagemCondicionante += 1
                if dados[i + 1] == value1:
                    contagemSequencia += 1

        # booa, verificação bem feita e poderia ser resumido assim: 
        # return contagemSequencia / contagemCondicionante if contagemCondicionante > 0 else 0
        if contagemCondicionante == 0:
            return 0
            
        return contagemSequencia / contagemCondicionante

        pass # remover o pass depois de implementar o método

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

        dados25perc = [i for i in dados if i <= Q2] # pode acabar acontecendo que o valor esteja uma posição deslocado
        # da posição real do quartil
        dados75perc = [i for i in dados if i >= Q2]

        # aaaaa agora eu entendi a adaptação qu vocês fizeram na função median
        # mas tem um problema, esse não era o comportamento esperado. 
        # o ideal mesmo era que vocês tivessem criado uma função auxiliar def _median 
        Q1 = self.median(dados25perc)
        Q3 = self.median(dados75perc)

        quartis = {"Q1": Q1, "Q2": Q2, "Q3": Q3}
        print(quartis)
        return quartis

        pass # remover o pass depois de implementar o método

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

        # vocês deveriam ter validado o bins antes: 
        # if bins < 0: 
            #raise ValueError("Valor do bins deve ser positivo")

        dados = sorted(self.dataset[column])
        limiteMinimo = min(dados)
        limiteMaximo = max(dados)

        amplitudeTotal = limiteMaximo - limiteMinimo #boa, a amplitude é a base para definir o tamanho do intervalo
        
        intervalo = amplitudeTotal / bins #show de bola, temos a largura do intervalo
        histograma = {}
        
        # interessante a construção dos intervalos
        pontoAtual = limiteMinimo
        for i in range(bins):
            proximoPonto = pontoAtual + intervalo
            histograma[(pontoAtual, proximoPonto)] = 0
            pontoAtual = proximoPonto
        
        for valor in dados:
            for chave in histograma.keys():
                inicio, fim = chave
                if valor >= inicio and valor < fim: #poderia ser feito assim: if valor <= inicio < fim : 
                    histograma[chave] += 1
                    break
                elif valor == limiteMaximo and abs(valor - fim) < 1e-9: # essa parte final é mais complicado mesmo
                    histograma[chave] += 1
                    break
    
        return histograma
        pass # remover o pass depois de implementar o método   
