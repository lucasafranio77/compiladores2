# -*- coding: utf-8 -*-
''' Compiladores 2 - UFMT 2018.1
201411310004 - Lucas Afrânio Silva de Siqueira '''

from lexico3 import tokens

def proxToken():
    global tokens
    if tokens:
        prox = tokens.pop(0)
        return prox.split(' ')

def S():
    global token
    if token:
        if programa():
            return True
    else:
        return False

def programa():
    global token, cat
    if "program" in token:
        token = proxToken()
        cat = "nome_prog"
        if "Identificador" in token:
            insere_tabela(token,'')
            token = proxToken()
            if corpo():
                if "." in token:
                    token = proxToken()
                    return True
                else:
                    print('erro: está faltando o token . na linha ', token[2])
                    return False
            else:
                return False
        else:
            print("erro: está faltando o token ident na linha ", token[2])
            return False
    else:
        print("erro: está faltando o token program na linha ", token[2])
        return False

def corpo():
    global token
    if dc():
        if "begin" in token:
            token = proxToken()
            if comandos():
                if "end" in token:
                    token = proxToken()
                    return True
                else:
                    print("erro: está faltando o token end na linha ", token[2])
                    return False
            else:
                return False
        else:
            print("erro: está faltando o token begin na linha ", token[2])
            return False
    else:
        return False

def dc():
    global token
    if "var" in token:
        if dc_v():
            if mais_dc():
                return True
            else:
                return False
        else:
            return False
    elif 'procedure' in token:
        if dc_p() :
            if mais_dc():
                return True
        else:
            return True
    else:
        return False

def mais_dc():
    global token
    if ";" in token:
        token = proxToken()
        if dc():
            return True
        else:
            return False
    else:
        return True

def dc_v():
    global token, cat
    if "var" in token:
        cat = "var"
        token = proxToken()
        if variaveis():
            if ":" in token:
                token = proxToken()
                if tipo_var():
                    return True
                else:
                    return False
            else:   
                print("erro: está faltando o token : na linha ", token[2])
                return False
        else:
            return False
    else:
        print("erro: está faltando o token var na linha ", token)
        return False

def tipo_var():
    global token, var_aux, cat, param
    if "real" in token:
        insere_tabela(var_aux,tipo='real')
        var_aux = []
        token = proxToken()
        return True
    elif "integer" in token:
        insere_tabela(var_aux,tipo='integer')
        var_aux = []
        token = proxToken()
        return True
    else:
        print("erro: está faltando o token real ou integer na linha ", token[2])
        return False

def variaveis():
    global token, var_aux, sinal_comando
    if "Identificador" in token:
        if sinal_comando:
            busca_variaveis(token)
            token = proxToken()
        else:
            var_aux.append(token)
            token = proxToken()
        if mais_var():
            return True
        else:
            return False
    else:
        print("erro: está faltando o token ident na linha ", token[2])
        return False

def mais_var():
    global token
    if "," in token:
        token = proxToken()
        if variaveis():
            return True
        else:
            return False
    else:
        return True

def dc_p():
    global token, cat, proc
    if "procedure" in token:
        token = proxToken()
        proc = True
        cat = "proc"
        if "Identificador" in token:
            insere_tabela(token,'')
            token = proxToken()
            if parametros():
                if corpo_p():
                    proc = False
                    return True
                else:
                    return False
            else:
                return False
        else:
            print("erro no identificador do dc_p")
            print("erro: está faltando o token ident na linha ", token[2])
            return False
    else:
        print("erro procedure no dc_p")
        print("erro: está faltando o token procedure na linha ", token[2])
        return False

def parametros():
    global token, param, cat
    if "(" in token:
        cat = "param"
        token = proxToken()
        param = True
        if lista_par():
            if ")" in token:
                param = False
                token = proxToken()
                return True
            else:
                print("erro: está faltando o token ) na linha ", token[2])
                return False
        else:
            return False
    else:
        return True

def lista_par():
    global token
    if variaveis():
        if ":" in token:
            token = proxToken()
            if tipo_var():
                if mais_par():
                    return True
                else:
                    return False
            else:
                return False
        else:
            print("erro: está faltando no lista_par o token : na linha ", token[2])
            return False
    else:
        return False

def mais_par():
    global token
    if ";" in token:
        token = proxToken()
        if lista_par():
            return True
        else:
            return False
    else:
        return True

def corpo_p():
    global token
    if dc_loc():
        if "begin" in token:
            token = proxToken()
            if comandos():
                if "end" in token:
                    token = proxToken()
                    return True
                else:
                    print("erro end do corpo_p")
                    print("erro: está faltando o token end na linha ", token[2])
                    return False
            else:
                return False
        else:
            print("erro begin do corpo_p")
            print("erro: está faltando o token begin na linha ", token[2])
            return False
    else:
        return False

def dc_loc():
    global tokens
    if "var" in token:
        if dc_v():
            if mais_dcloc():
                return True
            else:
                return False
        else:
            return False
    else:
        return True

def mais_dcloc():
    global token
    if ";" in token:
        token = proxToken()
        if dc_loc():
            return True
    else:
        return True

def lista_arg():
    global token, lista_tipos, nome_proc
    if "(" in token:
        token = proxToken()
        if argumentos():
            if ")" in token:
                # fazendo a checkagem dos tipos de parametros na chamada do procedimento - FEITO!
                if busca_parametros() == lista_tipos:
                    lista_tipos = []
                else:
                    print("erro: entrada de parametros está incorreta, conserte!")
                    lista_tipos = []
                    return False
                token = proxToken()
                return True
            else:
                print("erro ) na lista_arg")
                print("erro: está faltando o token ) na linha ", token[2])
                return False
        else:
            return False
    else:
        return True

def argumentos():
    global token , lista_tipos, proc, param, nome_proc
    if "Identificador" in token:
        lista_tipos.append(busca_arg(token))
        token = proxToken()
        if mais_ident():
            return True
        else:
            return False
    else:
        print("erro no identificador do argumentos")
        print("erro: está faltando o token ident na linha ", token[2])
        return False

def mais_ident():
    global token
    if ";" in token:
        token = proxToken()
        if argumentos():
            return True
        else:
            return False
    else:
        return True

def pfalsa():
    global token
    if "else" in token:
        token = proxToken()
        if comandos():
            return True
        else:
            return False
    else:
        return True

def comandos():
    global token
    if comando():
        if mais_comandos():
            return True
        else:
            return False
    else:
        return False

def mais_comandos():
    global token
    if ";" in token:
        token = proxToken()
        if comandos():
            return True
        else:
            return False
    else:
        return True

def comando():
    global token, nome_proc, sinal_comando
    if "read" in token:
        sinal_comando = True
        token = proxToken()
        if "(" in token:
            token = proxToken()
            if variaveis():
                sinal_comando = False
                if ")" in token:
                    token = proxToken()
                    return True
                else:
                    print("erro ) no comando")
                    print("erro: está faltando o token ) na linha ", token[2])
                    return False
            else:
                return False
        else:
            print("erro ( no comando")
            print("erro: está faltando o token ( na linha ", token[2])
            return False
    elif "write" in token:
        token = proxToken()
        if "(" in token:
            token = proxToken()
            if variaveis():
                if ")" in token:
                    token = proxToken()
                    return True
                else:
                    print("erro ) no comando")
                    print("erro: está faltando o token ) na linha ", token[2])
                    return False
            else:
                return False
        else:
            print("erro ( no comando")
            print("erro: está faltando o token ( na linha ", token[2])
            return False
    elif "while" in token:
        token = proxToken()
        if condicao():
            if "do" in token:
                token = proxToken()
                if comandos():
                    if "$" in token:
                        token = proxToken()
                        return True
                    else:
                        print("erro $ no comando")
                        print("erro: está faltando o token $ na linha ", token[2])
                        return True
                else:
                    return False
            else:
                print("erro - nao achei do na condicao")
                print("erro: está faltando o token do na linha ", token[2])
                return False
        else:
            return False
    elif "if" in token:
        token = proxToken()
        if condicao():
            if "then" in token:
                token = proxToken()
                if comandos():
                    if pfalsa():
                        if "$" in token:
                            token = proxToken()
                            return True
                        else:
                            print("erro $ then da condicao")
                            print("erro: está faltando o token $ na linha ", token[2])
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                print("erro then no comando")
                print("erro: está faltando o token then na linha ", token[2])
                return False
        else:
            return False
    elif "Identificador" in token:
        if busca_ident(token):
            nome_proc = token[0]
        token = proxToken()
        if restoIdent():
            return True
        else:
            return False
    else:
        print("erro no comando")
        print("erro: está faltando o token read ou write ou while ou if ou ident na linha ", token[2])
        return False

def restoIdent():
    global token
    if ":=" in token:
        token = proxToken()
        if expressao():
            return True
        else:
            return False
    elif lista_arg():
        return True
    else:
        print("erro no restoIdent")
        print("erro: está faltando o token := na linha ", token[2])
        return False

def condicao():
    if expressao():
        if relacao():
            if expressao():
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def relacao():
    global token
    if "=" in token:
        token = proxToken()
        return True
    elif "<>" in token:
        token = proxToken()
        return True
    elif ">=" in token:
        token = proxToken()
        return True
    elif "<=" in token:
        token = proxToken()
        return True
    elif ">" in token:
        token = proxToken()
        return True
    elif "<" in token:
        token = proxToken()
        return True
    else:
        print("erro no op_un")
        print("erro: está faltando o token = ou <> ou >= ou <= ou < ou > na linha ", token[2])
        return False

def expressao():
    global token
    if termo():
        if outros_termos():
            return True
        else:
            return False
    else:
        return False

def op_un():
    global token
    if "+" in token:
        token = proxToken()
        return True
    elif "-" in token:
        token = proxToken()
        return True
    else:
        return True

def outros_termos():
    global token
    if "+" in token or "-" in token:
        if op_ad():
            if termo():
                if outros_termos():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return True

def op_ad():
    global token
    if "+" in token:
        token = proxToken()
        return True
    elif "-" in token:
        token = proxToken()
        return True
    else:
        print("erro no op_ad")
        print("erro: está faltando o token + ou - na linha ", token[2])
        return False

def termo():
    global token
    if op_un():
        if fator():
            if mais_fatores():
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def mais_fatores():
    global token
    if "*" in token or "/" in token:
        if op_mul():
            if fator():
                if mais_fatores():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return True

def op_mul():
    global token
    if "*" in token:
        token = proxToken()
        return True
    elif "/" in token:
        token = proxToken()
        return True
    else:
        print("erro no op_mul")
        print("erro: está faltando o token * ou / na linha ", token[2])
        return False

def fator():
    global token, cat
    if "Identificador" in token:
        token = proxToken()
        return True
    elif "NumeroInteiro" in token:
        cat = "-"
        insere_tabela(token,'integer')
        token = proxToken()
        return True
    elif "NumeroReal" in token:
        cat = "-"
        insere_tabela(token,'real')
        token = proxToken()
        return True
    elif "(" in token:
        token = proxToken()
        if expressao():
            if ")" in token:
                token = proxToken()
                return True
            else:
                print("erro ) no fator")
                print("erro: está faltando o token ) na linha ", token[2])
                return False
        else:
            return False
    else:
        print("erro fator")
        print("erro: está faltando o token ( ou ident ou numero_int ou numero_real na linha ", token[2])
        return False

'''def sintatico():
    global tokens, i
    while i < len(tokens):
        if ( S() or programa() or corpo() or dc() or mais_dc() or dc_v or tipo_var() or variaveis() or mais_var() or dc_p() or parametros() or lista_par() or mais_par() or corpo_p() or dc_loc() or mais_dcloc() or lista_arg() or argumentos() or mais_ident() or pfalsa() or comandos() or mais_comandos() or comando() or restoIdent() or condicao() or relacao() or expressao() or op_un() or outros_termos() or op_ad() or termo() or mais_fatores() or op_mul() or fator()) != True:
            print("\nErro sintatico !! na linha " + str(token[2]) + " no token " + str(token[0]) + "\n")
            return False
    print("Parabéns programador, o seu código está sintaticamente correto!\n")'''



'''def busca_tabela(lex):
    global tabela_simbolos, proc, param, cat
    #print("printando o lex que to recebendo: ", lex)
    if proc and param == False:
        for lista in tabela_simbolos:
            if lex[0] == lista[0] and lex[1] == lista[1] and lex[2] == lista[2]:
                print('ta comparando proc na busca')
                return True
    else:
        for lista in tabela_simbolos:
            if lex[0] == lista[0] and lex[1] == lista[1] and lex[2] == lista[2] and lex[3] == lista[3] and lex[4] == lista[5]:
                print('ta comparando na busca')
                return True'''

'''def busca_fator(lex):
    global tabela_simbolos, proc
    print("printando o lex que to recebendo busca_fator: ", lex)
    for lista in tabela_simbolos:
        if lex[0] == lista[0]:
            tipo = lista[5]
        if lista[2] == "proc":
            for item in lista[5]:
                print(tipo)
                print(item)
                print(item[5])
                if tipo == item[5] and item[2] == "param":
                    print("o tipo deste parametro é igual")
                    return True
                else:
                    print("o tipo deste parametro não é compativel")'''

'''def search (lista, valor):
    return [(lista.index(x), x.index(valor)) for x in lista if valor in x]
'''

# busca para o semantico

def busca_arg(lex):
    global tabela_simbolos, nome_proc, arg
    for lista in tabela_simbolos:
        if lex[0] in lista and lista[2] == "var":
            return lista[5]
        '''elif nome_proc == lista[0] and lista[2] == "proc":
            pos = tabela_simbolos.index(lista)
            for item in lista[pos]:
                if lex[0] == item[0]:
                    print ("o tipo é esse aqui: ", item[5])
                    return item[5]'''
            
def busca_ident(lex):
    global tabela_simbolos, nome_proc
    for lista in tabela_simbolos:
        if lex[0] == lista[0] and lista[2] == "proc":
            return True

def busca_parametros():
    global tabela_simbolos, nome_proc
    lista_parametros = []
    for lista in tabela_simbolos:
        if nome_proc == lista[0] and lista[2] == "proc":
            pos = tabela_simbolos.index(lista)
            for item in lista[pos]:
                if item[2] == 'param':
                    lista_parametros.append(item[5])
            return lista_parametros

def busca_variaveis(lex):
    global tabela_simbolos, proc
    print("busca_variaveis: ",lex)
    if proc:
        for lista in tabela_simbolos:
            if lista[2] == "proc":
                pos = tabela_simbolos.index(lista)
                for item in lista[pos]:
                    if item[0] == lista[0] and item[2] == "var":
                        print("encontrada essa variavel no escopo local")

        
'''        for lista in tabela_simbolos[len(tabela_simbolos) - 1][5]:
            if lex[0] == lista[0] and lista[2] == "var":
                print("encontrada essa variavel no escopo local")
                return True'''


# A tabela de simbolos
# [cadeia, token, categoria, valor, linha, tipo]

# busca e inserção da tabela de simbolos

def busca_escopo(lex):
    global tabela_simbolos
    print("to recebendo o lex na busca_escopo: ", lex)
    for lista in tabela_simbolos[len(tabela_simbolos) - 1][5]:
        if lex[0] == lista[0]:
            print("tem parametro igual no proc")
            print(lex)
            return True

def busca_global(lex):
    global tabela_simbolos
    for lista in tabela_simbolos:
        if lex[0] == lista[0] and lex[1] == lista[1] and lex[2] == lista[2] and lex[3] == lista[5]:
            print('ta comparando na busca')
            return True

def insere_tabela(lex,tipo):
    global tabela_simbolos,cat,var_aux, proc, param
    print("proc: ", proc, "param: ", param, "token: ", lex, " cat: ", cat)
    # este é o caso que salva o nome do programa
    if cat == "nome_prog":
        tabela_simbolos.append([lex[0],lex[1], cat, '-', lex[2] ,""])
    # este é o caso que salva os numeros
    elif cat == "-":
        if proc:
            if lex[1] == "NumeroInteiro":
                tabela_simbolos[len(tabela_simbolos)-1][5].append([lex[0],"num", cat, int(lex[0]), lex[2], tipo])
                print("to salvando num inteiro local")
            elif lex[1] == "NumeroReal":
                tabela_simbolos[len(tabela_simbolos)-1][5].append([lex[0],"num", cat, float(lex[0]), lex[2], tipo])
                print("to salvando num real local")
            else:
                print("erro na hora de salvar os numeros no escopo local")
                return False
        else:
            if lex[1] == "NumeroInteiro":
                tabela_simbolos.append([lex[0],"num", cat, int(lex[0]), lex[2], tipo])
                print("to salvando num inteiro global")
            elif lex[1] == "NumeroReal":
                tabela_simbolos.append([lex[0],"num", cat, float(lex[0]), lex[2], tipo])
                print("to salvando num real global")
            else:
                print("erro na hora de salvar os numeros no escopo global")
                return False
    # este caso é só para os parametros
    elif param:
        for lex in var_aux:
            if not busca_escopo([lex[0],lex[1],cat,tipo,lex[2]]): # busca escopo
                tabela_simbolos[len(tabela_simbolos)-1][5].append([lex[0],lex[1], cat, '-', lex[2], tipo])
                print("to salvando param local")
            else:
                print("Erro: essa variavel já foi declarada => ", lex[0], " , na linha: ", lex[2])
                return  False
    # este caso é só para variaveis locais
    elif proc and param == False and cat == "var": #busco local e depois busco global
        for lex in var_aux:
            if not busca_escopo([lex[0],lex[1],cat,tipo,lex[2]]):
                tabela_simbolos[len(tabela_simbolos)-1][5].append([lex[0],lex[1], cat, '-', lex[2], tipo])
                print("to salvando variavel local da procedure")
            else:
                print("Erro: essa variavel já foi declarada => ", lex[0], " , na linha: ", lex[2])
                return  False
    # este caso é só para a procedure
    elif proc and param == False:
        if not busca_global([lex[0],lex[1],cat,tipo,lex[2]]): #busca global
            tabela_simbolos.append([lex[0],lex[1], cat, '-', lex[2], []])
            print("to salvando proc")
        else:
            print("Erro: essa variavel já foi declarada => ", lex[0], " , na linha: ", lex[2])
            return  False
    else:
        for lex in var_aux:
            if not busca_global([lex[0],lex[1],cat,tipo,lex[2]]): # busca global
                tabela_simbolos.append([lex[0],lex[1], cat, '-', lex[2], tipo])
                print("to salvando global")
            else:
                print("Erro: essa variavel já foi declarada => ", lex[0], " , na linha: ", lex[2])
                return  False
    print('\n------- Tabela de Simbolos ------- \n # [cadeia, token, categoria, valor, linha, tipo]\n\n', tabela_simbolos,'\n')


token = proxToken()
i = 0
tabela_simbolos = []
cat = ''
param = False
proc = False
var_aux = []

lista_tipos = []
nome_proc = ""

sinal_comando = False

#sintatico()
S()