"""
2º Projeto Fundamentos da Programação

Nome: Filippo da Costa Bortoli
Numero ist: ist1106103
Contacto: filippo.bortoli@tecnico.ulisboa.pt
Data: 10/11/2022
"""
def cria_gerador(b,s):
    """Função que recebe um inteiro correspondente ao numero de bits e outro 
    correspondete a seed e devolve um gerador, a funçao verifica a validade dos 
    argumentos de entrada

    Argumentos:
        b (int): inteiro correspondente ao numero de bits
        s (int): inteiro correspondete a seed

    Returns:
        gerador: um gerador é uma lista em que primeiro valor é o numero de
        bits e o segundo a seed
    """
    if type(b) != int or type(s) != int or s<=0 or b != 64 and b != 32:
        raise ValueError("cria_gerador: argumentos invalidos")
    if b==32 and s>=(2**32-1) or b==64 and s>=(2**64-1):
        raise ValueError("cria_gerador: argumentos invalidos")
    return list((b,s))

def cria_copia_gerador(g):
    """Cria uma copia do gerador de entrada

    Argumentos:
        g (gerador):  um gerador é uma lista em que primeiro valor é o numero de
        bits e o segundo a seed

    Returns:
       gerador:  copia do gerador de entrada
    """
    return g.copy()

def obtem_estado(g):
    """Obtem o estado do gerador de entrada sem o alterar

    Argumentos:
        g (gerador):  um gerador é uma lista em que primeiro valor é o numero de
        bits e o segundo a seed

    Returns:
        int: valor do estado do gerador
    """
    return g[1]

def define_estado(g,s):
    """Altera o estado do gerador para o valor de entrada s e devolve s

    Argumentos:
        g (gerador):  um gerador é uma lista em que primeiro valor é o numero de
        bits e o segundo a seed
        s (int): valor a atribuir ao estado do gerador

    Returns:
        int: novo valor do estado do gerador
    """
    g[1]=s
    return s

def atualiza_estado(g):
    """atualiza o estado do gerador utilizando o algoritmo xorshift

    Argumentos:
        g (gerador): um gerador é uma lista em que primeiro valor é o numero de
        bits e o segundo a seed

    Returns:
        int: novo estado do gerador 
    """
    s=obtem_estado(g)
    if g[0]==64:
        s ^= ( s << 13 ) & 0xFFFFFFFFFFFFFFFF
        s ^= ( s >> 7 ) & 0xFFFFFFFFFFFFFFFF
        s ^= ( s << 17 ) & 0xFFFFFFFFFFFFFFFF
    else:
        s ^= ( s << 13 ) & 0xFFFFFFFF
        s ^= ( s >> 17 ) & 0xFFFFFFFF
        s ^= ( s << 5 ) & 0xFFFFFFFF

    g[1]=s
    return s

def eh_gerador(g):
    """Verifica se argumento é um gerador e retorna True caso seja verdade, 
    retorna False caso contrario 

    Argumentos:
        g (universal): argumento que vai ser verificado

    Returns:
        bool: retorna True se argumento é do tipo gerador e False caso contrario 
    """
    if type(g) != list or len(g)!=2 or type(g[0]) != int or\
         type(obtem_estado(g)) != int or obtem_estado(g)<0:
        return False
    if g[0]==32 and obtem_estado(g)>=(2**32-1) or g[0]==64 and obtem_estado(g)\
        >=(2**64-1):
        return False
    return True

def geradores_iguais(g1,g2):
    """Verifica se dois geradores sao iguais

    Argumentos:
        g1 (gerador): gerador a verificar se é igual ao outro gerador nos 
        argumentos
        g2 (gerador): gerador a verificar se é igual ao outro gerador nos 
        argumentos

    Returns:
        bool: retorna True se os geradores forem iguais e False em caso 
        contrario, caso os argumentos nao sejam geradores a funçao tambem 
        retorna False
    """
    if eh_gerador(g1) and eh_gerador(g2) and g1[0]==g2[0] and\
         obtem_estado(g1)==obtem_estado(g2):
        return True
    return False

def gerador_para_str(g):
    """Transforma o gerador numa cadeia de caracteres 

    Arguemntos:
        g (gerador): gerador a transformar 

    Returns:
        str: Cadeia de caracteres correspondente ao gerador
    """
    return ('xorshift' + str(g[0]) + '(s=' + str(obtem_estado(g)) + ')')

def mod(s,n):
    """Funçao que calcula o resto da divisao inteira entre os argumentos de
    entrada

    Argumentos:
        s (int): divisor
        n (int): dividendo
    Returns:
       int: resto da divisao inteira entre os argumentos de entrada
    """
    return s%n

def gera_numero_aleatorio(g,n):
    """Funçao que atualiza o estado do gerador de entrada e gera um numero 
    aleatorio no intervalo de 1 a n

    Argumentos:
        g (gerador): gerador cujo estado vai ser atualizado
        n (int): valor maximo para o numero aleatorio

    Returns:
        int: devolve um numero aleatorio no intervalo de 1 a n
    """
    atualiza_estado(g)
    return 1+mod(obtem_estado(g),n)
    

def gera_carater_aleatorio(g,c):
    """Funçao que atualiza o estado do gerador de entrada e gera um caracter 
    aleatorio no intervalo de 'A' ao caracter maiusculo de entrada

    Argumentos:
        g (gerador): gerador cujo estado vai ser atualizado
        c (str): Caracter maximo para o caracter aleatorio

    Returns:
        str: caracter aleatorio entre 'A' e o caracter maiusculo de entrada
    """
    atualiza_estado(g)
    az='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in az:
        if i==c:
            index=az.index(c)+1
            return az[mod(obtem_estado(g),index)]

#-------------------------------------------------------------------------------
def cria_coordenada(col,l):
    """Cria uma coordenada com os argumentos de entrada, a funçao verifica a 
    validade dos arguemntos de entrada

    Argumentos:
        col (str): letra que representa a coluna
        l (int): valor que representa a linha

    Returns:
        coordenada: uma coordenada é um tuplo em que o primeiro valor representa
        a coluna e o segundo a linha
    """

    if type(col) != str or len(col) != 1 or col not in\
         'ABCDEFGHIJKLMNOPQRSTUVXWXYZ' or type(l) != int or l<=0 or l>=100:
         raise ValueError('cria_coordenada: argumentos invalidos')
    return col,l


def obtem_coluna(c):
    """devolve a coluna da coordenada de entrada

    Argumentos:
        c (coordenada): uma coordenada é um tuplo em que o primeiro valor 
        representa a coluna e o segundo a linha

    Returns:
        str: coluna da coordenada de entrada
    """
    return c[0]

def obtem_linha(c):
    """devolve a linha da coordenada de entrada

    Argumentos:
        c (coordenada): uma coordenada é um tuplo em que o primeiro valor 
        representa a coluna e o segundo a linha

    Returns:
        str: linha da coordenada de entrada
    """
    return c[1]

def eh_coordenada(c):
    """verifica se argumento de entrada é uma coordenada

    Argumentos:
        c (universal): argumento que vamos verificar se é uma coordenada

    Returns:
        bool: retorna True caso o argumento de entrada seja uma coordenada e
    False caso contrario
    """
    if type(c) != tuple or len(c) != 2 or len(obtem_coluna(c)) != 1 or\
        obtem_coluna(c) not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return False
    return True

def coordenadas_iguais(c1,c2):
    """Verifica se as duas coordenadas de entrada sao iguais

    Arguemntos:
        c1 (coordenada): coordenada que vamos verificar se é igual a outra 
        coordenada argumento
        c2 (coordenada): coordenada que vamos verificar se é igual a outra 
        coordenada argumento

    Returns:
        bool: retorna True caso sejam iguais e False caso contrario
    """
    if obtem_coluna(c1) != obtem_coluna(c2) or obtem_linha(c1) != \
        obtem_linha(c2):
        return False
    return True

def coordenada_para_str(c):
    """Transforma a coordenada de entrada numa cadeia de caracteres

    Argumentos:
        c (coordenada): coordenada que iremos transformar

    Returns:
        str: cadeia de caracteres em que o primeiro representa a coluna e os
        dois seguintes a linha
    """
    return str(obtem_coluna(c))+'{:0>2d}'.format(obtem_linha(c))

def str_para_coordenada(cc):
    """Transforma a cadeia de caracteres de entrada numa coordenada

    Arguemntos:
        cc (str): cadeia de caracteres a ser transformada em coordenada

    Returns:
        coordenada: coordenada obtida atraves da cadeia de caracteres de entrada
    """
    if len(cc) !=3 or cc[1] not in '1234567890' or cc[2] not in '1234567890' \
        or cc[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return 'a'
    col=cc[0]
    linha=int(cc[1:])
    return cria_coordenada(col,linha)

def obtem_coordenadas_vizinhas(c):
    """funçao que retorna as coordenadas vizinhas, pertemcentes ao campo, à 
    coordenada de entrada 

    Argumentos:
        c (coordenada): vamos obter as coordenadas vizinhas à coordenada de 
        entrada

    Returns:
        tuple: tuplo com as coordenadas vizinhas à coordenada C, começando pela 
        coordenada acima-esquerda e continuando no sentido horário
    """
    codigo_col=ord(obtem_coluna(c))
    lstres=[]
    linha=obtem_linha(c)
    r1=()
    r2=()
    r3=()
    r4=()
    r5=()
    r6=()
    r7=()
    r8=()
    
    #a funçao nao cria coordenadas fora do limite maximo de qualquer campo
    if obtem_coluna(c) != 'Z':
        if linha != 1:
            r3=cria_coordenada(chr(codigo_col+1),linha-1)
        r4=cria_coordenada(chr(codigo_col+1),linha)
        if linha != 99:
            r5=cria_coordenada(chr(codigo_col+1),linha+1)  
    if obtem_coluna(c)!='A':
        if linha != 99:
            r7=cria_coordenada(chr(codigo_col-1),linha+1)   
        r8=cria_coordenada(chr(codigo_col-1),linha)
        if linha != 1:
            r1=cria_coordenada(chr(codigo_col-1),linha-1)
    if linha != 1:
        r2=cria_coordenada(obtem_coluna(c),linha-1)
    if linha != 99:
        r6=cria_coordenada(obtem_coluna(c),linha+1)

    lstres+=r1,r2,r3,r4,r5,r6,r7,r8
    index=0

    #remove da lista as coordenadas que nao foram criadas
    while index != len(lstres):
        if lstres[index]==():
            del lstres[index]
        else:
            index+=1

    return tuple(lstres)

def obtem_coordenada_aleatoria(c,g):
    """cria uma coordenada aleatoria, c é uma coordenada que define a maior 
    coluna e linhas possiveis

    Argumentos:
        c (coordenada): define a maior coluna e linhas possiveis
        g (gerador): necessario para gerar a coluna e a linha da coordenada
        aleatoria

    Returns:
        coordenada: coordenada aleatoria
    """

    return cria_coordenada(gera_carater_aleatorio(g,obtem_coluna(c)),\
        gera_numero_aleatorio(g,obtem_linha(c)))

#-------------------------------------------------------------------------------

def cria_parcela():
    """funçao que cria uma parcela

    Returns:
        parcela: uma parcela é uma lista em que o primeiro valor coresponde ao
        estado da parcela(tapada, limpa ou marcada) e o segundo valor coresponde 
        a ter ou nao uma mina escondida
    """
    #0 corresponde a nao ter mina e 1 a ter mina
    return ['tapadas',0]

def cria_copia_parcela(p):
    """cria copia da parcela de entrada

    Argumentos:
        p (parcela): parcela por copiar

    Returns:
        parcela: copia da parcela de entrada
    """
    return p.copy()

def limpa_parcela(p):
    """funçao que limpa a parcela de entrada

    Argumentos:
        p (parcela): parcela por limpar

    Returns:
        parcela_: parcela limpa
    """
    p[0]='limpas'
    return p

def marca_parcela(p):
    """funçao que marca a parcela de entrada

    Argumentos:
        p (parcela): parcela por marcar

    Returns:
        parcela: parcela marcada
    """
    p[0]='marcadas'
    return p

def desmarca_parcela(p):
    """funçao que desmarca a parcela de entrada

    Argumentos:
        p (parcela): parcela por desmarcar

    Returns:
        parcela: parcela tapada
    """
    p[0]='tapadas'
    return p

def esconde_mina(p):
    """funçao que esconde uma mina na parcela de entrada

    Argumentos:
        p (parcela): parcela em que vamos esconder uma mina

    Returns:
        parcela: _parcela minada
    """
    p[1]=1
    return p

def eh_parcela(p):
    """funçao que verifica se o argumento de entrada é uma parcela

    Argumentos:
        p (universal): argumento por verificar se é uma parcela

    Returns:
        bool: retorna True caso o argumento de entrada seja uma percela e False
         caso contrario
    """
    if type(p) != list or len(p) != 2 or type(p[0]) != str or p[1] not in (0,1):
        return False
    return True

def eh_parcela_tapada(p):
    """funçao que verifica se a parcela de entrada é uma parcela tapada

    Argumentos:
        p (parcela): parcela por verificar se é tapada

    Returns:
        bool: retorna True caso seja uma parcela tapada e False caso contrario
    """
    if p[0] != 'tapadas':
        return False
    return True

def eh_parcela_marcada(p):
    """funçao que verifica se a parcela de entrada é uma parcela marcada

    Argumentos:
        p (parcela): parcela por verificar se é marcada
    Returns:
        bool: retorna True caso seja uma parcela marcada e False caso contrario
    """
    if p[0] != 'marcadas':
        return False
    return True

def eh_parcela_limpa(p):
    """funçao que verifica se a parcela de entrada é uma parcela limpa

    Argumentos:
        p (parcela): parcela por verificar se é limpa

    Returns:
        bool: retorna True caso seja uma parcela limpa e False caso contrario
    """
    if p[0] != 'limpas':
        return False
    return True

def eh_parcela_minada(p):
    """funçao que verifica se a parcela de entrada é uma parcela minada
    Argumentos:
        p (parcela): parcela por verificar se é minada

    Returns:
        bool: retorna True caso seja uma parcela minada e False caso contrario
    """
    if p[1] != 1:
        return False
    return True

def parcelas_iguais(p1,p2):
    """funçao que verifica se as parcela de entrada sao iguais

    Argumentos:
        p1 (parcela): parcela por verificar se é igual a outra parcela de
        entrada
        p2 (parcela): parcela por verificar se é igual a outra parcela de
        entrada

    Returns:
        bool: retorna True caso as duas parcelas sejam iguais e False caso 
        contrario
    """
    if not eh_parcela(p1) or not eh_parcela(p2) or p1[0] != p2[0] or p1[1] !=\
         p2[1]:
        return False
    return True

def parcela_para_str(p):
    """funçao que transforma a parcela de entrada numa string

    Argumentos:
        p (parcela): parcela a tranformar em string

    Returns:
        str: retorna um simbolo para cada tipo de parcela
        'x'-minada \\ '?'-limpa \\ '#'-tapada \\ '@'-marcada
    """
    #x-minada \\ ?-limpa \\ #-tapada \\ @-marcada
    if eh_parcela_limpa(p):
        if eh_parcela_minada(p):
            return 'X'
        return '?'
    elif eh_parcela_tapada(p):
        return '#'
    elif eh_parcela_marcada(p):
        return '@'

def alterna_bandeira(p):
    """funçao que marca uma parcela se esta estiver desmarcada e desmarca a 
    parcela se esta estiver marcada

    Argumentos:
        p (parcela): parcela por marcar ou desmarcar

    Returns:
        bool: retorna True caso a parcela tenho sido marcada ou desmarcada e 
        False em caso contrario
    """
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    return False

#-------------------------------------------------------------------------------

def cria_campo(c,l):
    """funçao que cria um campo sendo os argumento de entrada c e l o limite 
    para a coluna e para a linha respetivamente, a funçao verifica a validade 
    dos argumentos de entrada

    Argumentos:
        c (str): valor maximo para a coluna
        l (int): valor maximo para a linha

    Returns:
        campo: um campo é um dicionario em que as chaves correspondem as
        coordenadas do campo e os valores as parcelas correspondente a essas
        coordenadas
    """
    if type(c) != str or len(c) != 1 or c not in\
         'ABCDEFGHIJKLMNOPQRSTUVXWXYZ' or type(l) != int or l<=0 or l>=100:
         raise ValueError('cria_campo: argumentos invalidos')
    m={}
    #lnl-->linha não limite
    lnl=1
    #ocnl-->ordem coluna não limite
    ocnl=ord('A')
    while lnl <= l and ocnl <= ord(c):
        m[cria_coordenada(chr(ocnl),lnl)]=cria_parcela()  
        if lnl==l:
            ocnl+=1
            lnl=0    
        lnl+=1
    return m

def cria_copia_campo(m):
    """funçao que cria copia do campo de entrada

    Args:
        m (campo): campo por copiar

    Returns:
        campo: copia do campo de entrada
    """
    m2={}
    for chave in m:
        m2[chave]=m[chave]
    return m2

def obtem_ultima_coluna(m):
    """funçao que devolve a ultima coluna do campo de entrada

    Argumentos:
        m (campo): campo do qual queremos saber a ultima coluna

    Returns:
        str: retorna a ultima coluna do campo de entrada
    """
    return max(m.keys())[0]

def obtem_ultima_linha(m):
    """funçao que devolve a ultima linha do campo de entrada

    Argumentos:
        m (campo): campo do qual queremos saber a ultima linha

    Returns:
        int: retorna a ultima linha do campo de entrada
    """
    return max(m.keys())[1]

def obtem_parcela(m,c):
    """funçao que retorna a parcela correspondente à coordenada de entrada no 
    campo de entrada

    Argumentos:
        m (campo): campo no qual esta a coordenada da qual queremos obter a 
        parcela
        c (coordenada): coordenada da qual queremos obter a parcela
         correspondente

    Returns:
        parcela: parcela correspondente à coordenada de entrada no campo de 
        entrada
    """
    return m[c]

def obtem_coordenadas(m,s):
    """funçao que retorna todas as coordenadas do tipo de entrada s no campo de
    entrada m

    Argumentos:
        m (campo): campo do qual queremos obter as coordenadas do tipo s
        s (str): tipo do qual queremos todas as coordenadas no campo m

    Returns:
       tuple: retorna um tuplo com todas as coordenadas do tipo s ordenadas em 
       ordem ascendente de esquerda para a direita e de cima a baixo
    """
    res=[]
    for item in list(m.items()):
        if item[1][0]==s:
            res+=[item[0],]
        elif s=='minadas' and item[1][1]==1:
            res+=[item[0],]

    #ordena a lista segundo a linha e depois segundo a coluna
    res.sort(key=lambda x: (x[1],x[0]), reverse=False)

    return tuple(res)

def obtem_numero_minas_vizinhas(m,c):
    """funçao que devolve o numero de minas vizinhas da coordenada de entrada no
    campo de entrada

    Argumentos:
        m (campo): campo no qual esta a coordenada da qual queremos saber o 
        numero de minas vizinhas
        c (coordenada): coordenada da qual queremos saber o numero de minas 
        vizinhas

    Returns:
        int: numero de minas vizinhas à coordenada de entrada no campo de 
        entrada
    """
    res=0
    for coordenada in obtem_coordenadas_vizinhas(c):
        if eh_coordenada_do_campo(m,coordenada):
            if eh_parcela_minada(obtem_parcela(m,coordenada)):
                res+=1
    return res

def eh_campo(m):
    """funçao que verifica se o argumento de entrada é um campo

    Argumentos:
        m (universal): argumento que vamos verifcar se é um campo

    Returns:
        bool: retorna True caso o argumento de entrada seja um campo e False
        caso contrario
    """
    if type(m) != dict or m=={}:
        return False
    for item in list(m.items()):
        if type(item[0]) != tuple or type(item[1]) != list:
            return False
    return True

def eh_coordenada_do_campo(m,c):
    """funçao que verifica se a coordenada de entrada é uma coordenada do campo 
    de entrada

    Argumentos:
        m (campo): campo do qual queremos saber se c é uma coordenada
        c (coordenada): coordenada que queremos saber se pertence ao campo m

    Returns:
        bool: retorna True caso a coordenada pertença ao campo m e False caso 
        contrario
    """
    if obtem_coluna(c)>obtem_ultima_coluna(m) or obtem_linha(c)>\
        obtem_ultima_linha(m):
        return False
    return True

def campos_iguais(m1,m2):
    """Funçao que verifica se os dois campos de entrada sao iguais

    Argumentos:
        m1 (campo): campo que vamos verificar se é igual ao outro campo de 
        entrada
        m2 (_type_): campo que vamos verificar se é igual ao outro campo de 
        entrada

    Returns:
        bool: retorna True se os dois campos de entrada sao iguais e False caso
        contrario
    """
    if m1.items() == m2.items():
        return True
    return False

def campo_para_str(m):
    """funçao que transforma o campo de entrada numa cadeia de caracteres

    Argumentos:
        m (campo): campo que queremos transformar numa cadeia de caracteres

    Returns:
        str: retorna a cadeia de caracteres equivalente ao campo
    """
    az='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    colunas=az[:az.index(obtem_ultima_coluna(m))+1]
    separador='+'+'-'*len(colunas)+'+'
    new_line='\n'
    linhas=''
    #latual-->linha atual
    latual=1
    ocol_atual=ord('A')

    while latual <= obtem_ultima_linha(m):
        colunas2=az[:az.index(obtem_ultima_coluna(m))+1]
        ocol_atual=ord('A')
        #formatar linhas para ter sempre 2 caracteres
        linhas+='{:0>2}'.format(str(latual))+'|'
        while ocol_atual <= ord(obtem_ultima_coluna(m)):
            if parcela_para_str(obtem_parcela(m,(colunas2[0],latual)))=='?':
                if obtem_numero_minas_vizinhas(m,(colunas2[0],latual))!=0:
                    linhas+=str(obtem_numero_minas_vizinhas\
                        (m,(colunas2[0],latual)))
                else:
                    linhas+=' '
            else:
                linhas+=parcela_para_str(obtem_parcela(m,(colunas2[0],latual)))
            colunas2=colunas2[1:]
            ocol_atual+=1
        linhas+='|'+new_line
        latual+=1
        
    return '   '+colunas+new_line+'  '+separador+new_line+linhas+'  '+separador


def coloca_minas(m,c,g,n):
    """funçao que coloca  n minas no campo de entrada m em coordenadas
     aleatorias excepto na coordenada de entrada c

    Argumentos:
        m (campo): campo no qual vao ser colocadas as minas
        c (coordenada): coordenada na qual nao deve ser colocada nenhuma mina
        g (gerador): necessaorio para obter as coordenadas aleatorias
        n (int): numero de minas

    Returns:
        campo: campo com as n minas colocadas em coordenadas aleatorias
    """
    lst_c_minadas=[]

    #se numero de minas igual ao numero de coordenadas do campo-1(porque a
    # primeira coordenada nunca pode ter mina) entao as minas sao colocadas em 
    #todas as coordenadas sem necessidade de calcular coordenadas aleatorias
    if n==(obtem_ultima_linha(m)*(ord(obtem_ultima_coluna(m))-ord('A')+1))-1:
        lst_c_minadas=obtem_coordenadas(m,'tapadas')
        for cord in lst_c_minadas:
            if not coordenadas_iguais(c,cord):
                esconde_mina(obtem_parcela(m,cord))
    
    while len(obtem_coordenadas(m,'minadas')) < n:
        c_alt= obtem_coordenada_aleatoria(cria_coordenada\
            (obtem_ultima_coluna(m),obtem_ultima_linha(m)),g)
        if not coordenadas_iguais(c_alt,c) and c_alt not in lst_c_minadas:
            if c_alt not in obtem_coordenadas_vizinhas(c):
                lst_c_minadas+=[c_alt,]
                esconde_mina(obtem_parcela(m,c_alt))
    return m

def limpa_campo(m,c):
    """funçao que limpa o campo m a partir da coordenada c até encontrar 
    coordenadas com minas vizinhas

    Argumentos:
        m (campo): campo que vamos limpar
        c (coordenada): coordenada a partir da qual vamos limpar o campo

    Returns:
        campo: campo que foi limpo a partir da coordenada c até encontrar 
    coordenadas com minas vizinhas
    """
    lst_c=[c,]
    index=-1
    lst_complete=False
    if eh_parcela_minada(obtem_parcela(m,c)):
        lst_complete=True
        lst_c=[]
    
    #mete numa lista todas as coordenadas que devem ser limpas
    while lst_complete==False:
        for cord in obtem_coordenadas_vizinhas(c):
            if eh_coordenada_do_campo(m,cord) and\
                 obtem_numero_minas_vizinhas(m,cord)==0 and cord not in lst_c\
                     and not eh_parcela_marcada(obtem_parcela(m,cord)) and\
                         eh_parcela_tapada(obtem_parcela(m,cord)) and not\
                             eh_parcela_minada(obtem_parcela(m,cord)):
                lst_c+=[cord,]
        
        if not coordenadas_iguais(c,lst_c[-1]):
            index+=1
        
        if not coordenadas_iguais(c,lst_c[-1]) or\
             coordenadas_iguais(lst_c[0],lst_c[-1]):
            lst_complete=False
        else:
            lst_complete=True
        
        if obtem_numero_minas_vizinhas(m,lst_c[index])!=0 and not\
             eh_parcela_tapada(obtem_parcela(m,lst_c[index])) or len(lst_c)==1:
            break
        else:
            c=lst_c[index+1]

    #limpa as coordenadas da lista e as suas vizinhas que ainda nao foram limpas       
    for cord in lst_c:
        limpa_parcela(obtem_parcela(m,cord))
        for cord2 in obtem_coordenadas_vizinhas(cord):
            if eh_coordenada_do_campo(m,cord2) and\
                 obtem_numero_minas_vizinhas(m,cord2)!=0 and\
                     eh_parcela_tapada(obtem_parcela(m,cord2)) and not\
                         eh_parcela_minada(obtem_parcela(m,cord2)) :
                limpa_parcela(obtem_parcela(m,cord2))
    return m

#-------------------------------------------------------------------------------

def jogo_ganho(m):
    """funçao que retorna True se o jogo estiver ganho e False em caso contrario
    para isso verifica se o numero de coordenadas do campo é igual ao numero de
    coordenadas limpas mais o numero de coordenadas minadas

    Argumentos:
        m (campo): campo no qual vamos verificar se o jogo foi ganho

    Returns:
        bool: retorna True caso o jogo esteja ganho e False caso ainda nao 
        esteja ganho
    """
    #n_c_m-->numero de coordenadas do campo
    n_c_m=obtem_ultima_linha(m)*(ord(obtem_ultima_coluna(m))-ord('A')+1)

    if n_c_m==(len(obtem_coordenadas(m,'limpas'))+\
        len(obtem_coordenadas(m,'minadas'))):
        return True
    return False

def fcord(m):
    """funçao para receber a coordenada com a qual se vai trabalhar, a funçao 
    so aceita a coordenada quando esta for valida

    Argumentos:
        m (campo): campo no qual se esta a trabalhar, serve para verificar se 
        a coordenada inserida é uma coordenada deste campo

    Returns:
        coordenada: coordenada com a qual se vai trabalhar
    """
    cord=()
    while not eh_coordenada(cord) : 
        cord=str_para_coordenada(input('Escolha uma coordenada:'))
    while not eh_coordenada_do_campo(m,cord) or\
         eh_parcela_limpa(obtem_parcela(m,cord)) :
        cord=str_para_coordenada(input('Escolha uma coordenada:'))
    return cord

def turno_jogador(m):
    """funçao que permite ao jogador escolher uma açao e uma coordenada e em 
    seguida modifica destrutivamente o campo segundo as escolhas do jogador

    Argumentos:
        m (campo): campo no qual se esta a trabalhar

    Returns:
        bool: retorna True caso se tenha limpo uma parcela sem mina ou se tenha
        marcado uma parcela sem mina e False caso se tenha limpo uma parcela com
        mina
    """
    acao=''
    while acao != 'L' and acao != 'M':
        acao=input('Escolha uma ação, [L]impar ou [M]arcar:')
    cord=()
    cord=fcord(m) 

    if acao=='M':
        
        if eh_parcela_marcada(obtem_parcela(m,cord)):
            desmarca_parcela(obtem_parcela(m,cord))
        else:
            if eh_parcela_tapada(obtem_parcela(m,cord)):
                marca_parcela(obtem_parcela(m,cord))
                if not eh_parcela_minada(obtem_parcela(m,cord)):
                    return True
                
    elif acao=='L':
        if obtem_numero_minas_vizinhas(m,cord) != 0:

            limpa_parcela(obtem_parcela(m,cord))
        else:
            limpa_parcela(obtem_parcela(m,cord))
            limpa_campo(m,cord)

        if eh_parcela_minada(obtem_parcela(m,cord)):
            return False
        else:
            return True

def minas(c,l,n,d,s):
    """Funçao principal que permite jogar ao jogo minas, a funçao valida os 
    argumentos de entrada

    Argumentos:
        c (str): coluna maxima do campo
        l (int): linha maxima do campo
        n (int): numero de minas com que se pretende jogar
        d (int): dimensão do gerador
        s (int): estado inicial do gerador

    Returns:
        bool: retorna True caso se tenha ganho o jogo e False caso contrario
    """
    if type(c) != str or len(c) != 1 or c not in 'ABCDEFGHIJKLMNOPQRSTUVXWXYZ'\
        or type(l) != int or l<0 or l>=100 or type(n) != int or l<0 or l>=100\
            or type(d) != int or type(s) != int or s<0 or n >= \
                ((ord(c)-ord('A')+1)*l) or n<=0:
            raise ValueError('minas: argumentos invalidos')
    if type(d) != int or type(s) != int or s<=0 or d != 64 and d != 32:
        raise ValueError('minas: argumentos invalidos')
    if d==32 and s>=(2**32-1) or d==64 and s>=(2**64-1):
        raise ValueError('minas: argumentos invalidos')
      
    m=cria_campo(c,l)
    g=cria_gerador(d,s)

    if g[0]==32 and obtem_estado(g)>=(2**32-1) or g[0]==64 and obtem_estado(g)\
        >=(2**64-1) or len(m)==4:
         raise ValueError('minas: argumentos invalidos')

    def printTurno(m,n):
        """funçao que imprime numero de bandeiras e o campo de minas

        Argumentos:
            m (campo): campo no qual estamos a trabalhar
            n (int): numero de bandeiras utilizadas
        """
        print('   '+'[Bandeiras '+str(len(obtem_coordenadas(m,'marcadas')))+'/'\
            +str(n)+']')
        print(campo_para_str(m))

    printTurno(m,n)
    
    cord=()
    cord=fcord(m)

    coloca_minas(m,cord,g,n)
    limpa_parcela(obtem_parcela(m,cord))
    limpa_campo(m,cord)
    
    while not jogo_ganho(m):
        printTurno(m,n)
        t=turno_jogador(m)
        if t==False:
            printTurno(m,n)
            print('BOOOOOOOM!!!')
            return False

    printTurno(m,n)
    print('VITORIA!!!')
    return True