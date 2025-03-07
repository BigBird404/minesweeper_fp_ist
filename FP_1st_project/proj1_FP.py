"""
1º Projeto Fundamentos da Programação

Nome: Filippo da Costa Bortoli
Numero ist: ist1106103
Contacto: filippo.bortoli@tecnico.ulisboa.pt
Data: 27/10/2022
"""
#Exercicio num 1
#Exercicio num 1.2.1
def limpa_texto(t): 
    """Função que retira os caracteres brancos de uma cadeia de caracteres

    Argumentos:
        t (str): string com caracteres brancos 

    Returns:
        str: string limpa(os unicos caracteres brancos correspondem ao espaço
        entre as palavras)
    """
    t=" ".join(t.split())
    return t

#Exercicio num 1.2.2
def corta_texto(t,largura):
    """Funçao que devide uma cadeia de caracteres em duas, uma com todas as 
    palavras completas, incluindo os espaços, até a largura maxima(o comprimento
    desta primeira cadeia de caracteres pode ser menor que a largura definida) e
    outra com o resto das palavras, incluindo tambem nesta os espaços entre as 
    palavras.

    Argumentos:
        t (str): cadeia de caracteres limpa
        largura (int): comprimento maximo da cadeia de caracteres

    Returns:
        tuplo: o primeiro valor do tuplo é a cadeia de caracteres de entrada com
        um comprimento menor ou igual à largura, o segundo é o resto da cadeia 
        de caracteres de entrada
    """
    if largura >= len(t):
        c1=t
        c2=""  
    elif largura < len(t):
        palavras=t.split()
        i=0
        acm=-1
        while largura>=acm:     
            acm+=1                 
            acm=acm+len(palavras[i])                        
            i+=1

        #Juntar 'palavras' com os espaços entre elas
        #(i-1) porque i acumula 1 a mais no ciclo anterior
        c1=" ".join(palavras[:i-1])
        c2=" ".join(palavras[i-1:])
    return c1,c2

#Exercicio num 1.2.3
def insere_espacos(t,largura):
    """Funçao que insere espaços na cadeia de caracteres definida de modo a 
    que esta fique exatamente com o comprimento do argumento de entrada: largura
    (os espaços sao acrescentados da esquerda para a direita)

    Argumentos:
        t (str): cadeia de caracteres limpa
        largura (int): comprimento maximo da cadeia de caracteres

    Returns:
        str: cadeia de caracteres com comprimento do argumento largura
    """
    #cadeia de caracteres com que vamos trabalhar nesta funçao:
    c=corta_texto(t,largura)[0]  

    ct=""
    palavras=c.split() 
    lenC=0

    #medir comprimento das palavras 
    for i in palavras:
        lenC+=len(i)

    if len(palavras)==1:
        #encostar frase a esquerda e meter espaços no fim 
        ct='{:<{}}'.format(c,largura)
        return ct

    espacostot=largura-lenC
    espaços_por_palavra_1=espacostot/(len(palavras)-1)
    #parte a direita do 0 de 'espaços_por_palavra_1':
    espaços_por_palavra_2=espaços_por_palavra_1%1 

    #strings com espaços a inserir:
    espac1=""
    espac2=""

    icm=1
    while icm<=espaços_por_palavra_1:
        espac1=espac1+" "
        icm+=1

    icm=0
    while icm<espaços_por_palavra_2:
        espac2=espac2+" "
        icm+=1

    #Quantas vezes o programa deve inserir o 'espaços_por_palavra_2':
    vzs_esp_2=espacostot-((espaços_por_palavra_1-(espaços_por_palavra_2))*\
        (len(palavras)-1)) 

    #inserir espaços:
    icm=0
    for i in palavras:
        if i is not palavras[-1]:
            
            if vzs_esp_2<espaços_por_palavra_2:
                espac2=""
            ct=ct+'{}{}'.format(i,(espac1+espac2))
            vzs_esp_2-=1         
        else:
            ct=ct+'{:>{}}'.format(i,0) 
    return ct


#Exercicio num 1.2.4
def justifica_texto(t,largura):                                        
    """Funçao que justifica cadeia de caracteres com comprimento de cada linha
    definido como 'largura' nos argumentos de entrada. A ultima linha do texto
    justificado estará encostada a esquerda, com espaços a perfazer o
    comprimento a direita.
    A funçao verifica ainda a validade dos argumentos de entrada e gera um 
    'ValueError' caso os argumentos sejam invalidos

    Argumentos:
        t (str): cadeia de caracteres
        largura (int): comprimento maximo da cadeia de caracteres
        
    Returns:
        tuplo: cada elemento do tuplo corresponde a uma linha do texto
        justificado
    """
    if type(t) != str or type(largura)!= int or t == "" or largura<=0:
        raise ValueError("justifica_texto: argumentos invalidos")

    max=0
    for i in t.split():
        if len(i)>max:
            max=len(i)
    
    if max>largura:
        raise ValueError("justifica_texto: argumentos invalidos")    

    cadeia_Nfinal=[]
    cadeia_final=()
    output_corta_texto=list(corta_texto(t,largura+1))
    
    #Justificamos todas as linhas usando as funçõs corta_texto e insere_espacos,
    #em seguida formatamos a ultima linha para que os espaços estejam a direita
    #da cadeia de caracteres
    while output_corta_texto[0] != "":
        
        cadeia_Nfinal=cadeia_Nfinal+\
            [insere_espacos(output_corta_texto[0],largura),]  
        output_corta_texto[0]=output_corta_texto[1]
        output_corta_texto=list(corta_texto(output_corta_texto[0],largura))

    cadeia_Nfinal[-1]='{:<{}}'.format(limpa_texto(cadeia_Nfinal[-1]),largura)
    cadeia_final=tuple(cadeia_Nfinal)

    return cadeia_final


#-------------------------------------------------------------------------------
#Exercicio num 3

#exercicio num 3.2.1
def produto_interno(t1,t2):
    """
    Calcula o produto interno entre os dois vetores de entrada

    Argumentos:
        t1 (tuple): tuplo, com valores inteiros ou reais, correspondente a um
        vetor
        t2 (tuple): tuplo, com valores inteiros ou reais, correspondente a um
        vetor

    Returns:
        float: valor do produto interno entre os 2 vetores de entrada
    """
    res=0
    index=-1
    for i in t1:
        index+=1
        res+=i*t2[index]

    return float(res)

#exercicio num 3.2.2
def verifica_convergencia(A1,c1,x,p):
    """
    Verifica se o valor absoluto do erro é inferior a precisão e retorna True
    caso isto se verifique

    Argumentos:
        A1 (tuple): tuplo de tuplos em que cada tuplo corresponde a uma linha da
        matriz, o tuplo de tuplos corresponde a matriz
        c1 (tuple): vetor das constantes da matriz
        x (tuple): solução atual
        p (float): precisão

    Returns:
        boolean: se é convergente retorna True caso contrario retorna False
    """
    acm=0
    for i in A1:
        if abs(produto_interno(i,x)-c1[acm])>p:
            return False
        acm+=1

    return True

#exercicio num 3.2.3
def retira_zeros_diagonal(A1,c1):
    """Retiras os zeros da diagonal da matriz A, trocando a ordem das linhas

    Argumentos:
        A1 (tuplo): tuplo de tuplos em que cada tuplo corresponde a uma linha da
        matriz, o tuplo de tuplos corresponde a matriz
        c1 (tuplo): vetor das constantes da matriz

    Returns:
        tuplo: tuplo de 2 tuplos em que o primeiro tuplo corresponde a matriz
        com as linhas já trocadas e o segundo tuplo corresponde ao vetor das 
        constantes com os valores trocados pela mesma ordem da matriz

    """
    
    A1lst=list(A1)
    c1lst=list(c1)
    d=-1
    
    #linczd-->linha com zero na diagonal
    #lszd-->linha sem zero na diagonal
    #d-->diagonal
    for linczd in A1lst:
        troca = False
        d+=1
        if linczd[d] == 0:
            for lszd in A1lst:
                if troca == False:
                    if lszd[d] != 0 and linczd[A1lst.index(lszd)] != 0:
                        index_linha_s_0=A1lst.index(lszd)
                        #trocar a ordem das linhas e dos valores do vetor 
                        # constante:
                        A1lst[A1lst.index(linczd)],A1lst[index_linha_s_0]= \
                            A1lst[index_linha_s_0],A1lst[A1lst.index(linczd)]
                        c1lst[A1lst.index(linczd)],c1lst[A1lst.index(lszd)]= \
                            c1lst[A1lst.index(lszd)],c1lst[A1lst.index(linczd)]
                        troca=True                 
            
    c1=tuple(c1lst)
    A1=tuple(A1lst)

    return A1,c1

#exercicio num 3.2.4
def eh_diagonal_dominante(A1):
    """
    Verifica se diagonal é dominante, isto é, se valor absoluto do valor da 
    diagonal é superior a soma dos outros valores dessa mesma linha

    Argumentos:
        A1 (tuplo): tuplo de tuplos em que cada tuplo corresponde a uma linha da
        matriz, o tuplo de tuplos corresponde a matriz

    Returns:
        boolean: Retorna True se diagonal é dominante e False caso contrario
    """
    diagonal=0
    soma_s_diagonal=0
    
    #soma todos os valores de uma linha e subtrai o valor que se encontra na
    #diagonal
    for linha in A1:   
        for valor in linha:
            soma_s_diagonal+=abs(valor)
        
        soma_s_diagonal-=abs(linha[diagonal])

        if abs(linha[diagonal])<soma_s_diagonal: 
            return False
        diagonal+=1
        soma_s_diagonal=0

    return True

#exercicio num 3.2.5
def resolve_sistema(A1,c1,p):
    """Esta funçao resolve o sistema de equações em que cada equação corresponde 
    a uma linha da matriz atraves do metodo de jacobi. A função verifica ainda a 
    validade dos argumentos de entrada
    
    Argumentos:
        A1 (tuple): tuplo de tuplos em que cada tuplo corresponde a uma linha da
        matriz, o tuplo de tuplos corresponde a matriz
        c1 (tuple): vetor das constantes da matriz
        p (float): precisão

    Returns:
        tuple: Retorna um tuplo em que que os valores correspondem a soluçao do
        sistema de equações
    """

    if type(A1) != tuple or type(c1) != tuple or type(p) != float or p<=0\
        or len(A1) != len(c1):
        raise ValueError("resolve_sistema: argumentos invalidos") 
    
    for i in A1:
        if type(i) != tuple or len(A1) != len(i):
            raise ValueError("resolve_sistema: argumentos invalidos")

        for j in i:
            if type(j) != int and type(j) != float:
                raise ValueError("resolve_sistema: argumentos invalidos")

    for i in c1: 

        if type(i) != int and type(i) != float:
            raise ValueError("resolve_sistema: argumentos invalidos")

    nova_sol=[]
    rzd=retira_zeros_diagonal(A1,c1)
    A1=rzd[0]
    c1=rzd[1]                   

    if eh_diagonal_dominante(A1) is False:
        raise ValueError("resolve_sistema: matriz nao diagonal dominante")

    #Iniciar todos os valores da soluçao a 0
    for linha in A1:
        nova_sol.append(0)

    #Aplicar a formula do metodo de jacobi e a cada iteraçao alterar a solução
    #atual
    while verifica_convergencia(A1,c1,nova_sol,p) is False:
        velha_sol=nova_sol.copy()
        for linha in A1:
            i=A1.index(linha)
            nova_sol[i]=nova_sol[i]+(c1[i]-produto_interno(linha,velha_sol))\
                /linha[i]

    nova_sol=tuple(nova_sol)     

    return nova_sol

#-------------------------------------------------------------------------------
#Exercicio num 2

#exercicio num 2.2.1
def calcula_quocientes(dict_in,n_dept):
    """Funçao que para cada partido calcula o quociente entre o numero de votos
    e os numeros naturais até ao numero de deputados(n_dept)

    Argumentos:
        dict_in (dict): dicionario com o nome dos partidos e o numero dos seus 
        votos
        n_dept (int): numero de deputados
    Returns:
        dict: Retorna um dicionario em que a cada partido(chave do dicionario)
        corresponde uma lista com os valores dos quocientes
    """
    dict_out={}

    for i in dict_in:
        acm=1
        while acm <= n_dept:
            if i not in dict_out:
                dict_out[i]=[dict_in[i]/acm]
            else:   
                dict_out[i].append(dict_in[i]/acm)
            acm+=1

    return  dict_out

#exercicio num 2.2.2
def atribui_mandatos(dict_in,n_dept):
    """Esta funçao percorre o dicionario obtido atraves do calculo dos
    quocientes criando uma lista com os nomes dos partidos que conseguiram os
    mandatos segundo o metodos de Hondt. Os mandatos sao atribuidos ao quociente
    mais elevado, caso o quociente seja igual entre dois partidos o mandato é
    atribuido ao que tiver menos votos.  Esta lista está ordenada por ordem 
    decrescente de quociente calculado pelo metodo de Hondt

    Argumentos:
        dict_in (dict): dicionario com o nome dos partidos e o numero dos seus 
        votos
        n_dept (int): numero de deputados

    Returns:
        list : lista ordenada por ordem decrescente de quociente calculado pelo 
        metodo de Hondt
    """
     
    lst_quocientes=calcula_quocientes(dict_in,n_dept)
    lst_mandatos=[]

    #Dentro do proximo ciclo while o primeiro if atribui o mandato ao partido
    #com o quociente mais elevado, caso o quociente seja igual para dois
    #partidos o mandato é atribuido ao partido com menos votos
    while len(lst_mandatos) != n_dept:
        max=0
        for partido in lst_quocientes:         
            for quociente in lst_quocientes[partido]:
                if max<quociente:
                    max=quociente
                    mandato=partido

                if max==quociente:
                    if dict_in[partido] < dict_in[mandato]:
                        max=quociente
                        mandato=partido

        lst_mandatos+=[mandato,]
        lst_quocientes[mandato].remove(max)
        max=0

    return lst_mandatos

#exercicio num 2.2.3
def obtem_partidos(info):
    """Esta funçao percorre o dicionario de entrada e devolve uma lista com os 
    nomes dos partidos que participam nas eleições ordenados por ordem 
    alfabetica

    Argumentos:
        info (dict):  dicionario com a informação sobre as eleições num 
        territorio com varios circulos eleitorais

    Returns:
        list:  retorna uma lista com os nomes dos partidos que participam nas 
        eleições ordenados por ordem alfabetica
    """
    lst_partidos=[]
    for i in info:
        for j in info[i]['votos']:
            if j not in lst_partidos:
                lst_partidos.append(j)
            
    lst_partidos.sort()

    return lst_partidos

#exercicio num 2.2.4
def obtem_resultado_eleicoes(info):                                        
    """Esta funçao recebe um dicionario com as informações sobre as eleições num 
    teritorio com varios circulos eleitorais e devolve uma lista de tuplos com 
    informaçoes sobre o resultado de cada partido que participou nas eleiçoes, 
    esta lista está ordenada por ordem decrescente de numero de deputados e em 
    caso de empate por numero de votos total. A função verifica a validade dos 
    argumentos de entrada

    Argumentos:
        info (dict): dicionario com a informação sobre as eleições num 
        territorio com varios circulos eleitorais

    Returns:
        list: retorna uma lista de tuplos de comprimento 3 em que o primeiro 
        valor é o nome do partido, o segundo o numero de mandatos total e em
        terceiro o numero total de votos, esta lista está ordenada por ordem 
        decrescente de numero de deputados e em casa de empate por numero de 
        votos total.
    """

    if type(info) != dict or len(info) < 1:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')

    for i in info:
        it=info[i]
        nomes_info=[]

        if type(it) != dict or type(i) != str:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')

        for j in it:
            nomes_info.append(j)

        if 'deputados' not in nomes_info or 'votos' not in nomes_info:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
 
        if  type(it['deputados']) != int or type(it['votos']) != dict or \
            len(it['votos']) < 1 or it['deputados'] < 1:
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        for j in it['votos']:
            if type(j) != str or type(it['votos'][j]) != int or\
                it['votos'][j]<1:
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            
    lst_final=[]
    #cria dicionarios com as mesmas chaves da lista obtida em obtem_partidos,
    #com valor 0 
    dict_num_mandatos=dict.fromkeys(obtem_partidos(info),0)
    dict_num_votos=dict.fromkeys(obtem_partidos(info),0)

    #percorre dicionarios e para cada partido calcula numero de deputados total
    #e numero de votos total
    for i in info:
        for partidos in info[i]['votos']:
            dict_num_votos[partidos]+=info[i]['votos'][partidos]

        for j in atribui_mandatos(info[i]['votos'],info[i]['deputados']):
            dict_num_mandatos[j]+=1
            
    for i in dict_num_mandatos:
        tuple_final=(i,dict_num_mandatos[i],dict_num_votos[i])
        lst_final+=[tuple_final,]
    
    #Ordena a lista de forma decrescente por numeros de deputados e em caso de 
    #empate por numero de votos 
    #x[1] é o numero de deputados e x[2] é o numero de votos
    lst_final.sort(key=lambda x: (x[1],x[2]), reverse=True)

    return lst_final





