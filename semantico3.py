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
            return True
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
    global token
    if "var" in token:
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
    if param:
        cat = "param"
    else:
        cat = "var"
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
    global token, var_aux
    if "Identificador" in token:
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
        print("parametros:",token)
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
    global token
    if "(" in token:
        token = proxToken()
        if argumentos():
            if ")" in token:
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
    global token
    if "Identificador" in token:
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
    global token
    if "read" in token:
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
        #print("retornando vazio nos outros_termos")
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
        #print("retornando vazio nos mais_fatores")
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
    global token
    if "Identificador" in token:
        token = proxToken()
        return True
    elif "NumeroInteiro" in token:
        token = proxToken()
        return True
    elif "NumeroReal" in token:
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

def sintatico():
    global tokens, i
    while i < len(tokens):
        if ( S() or programa() or corpo() or dc() or mais_dc() or dc_v or tipo_var() or variaveis() or mais_var() or dc_p() or parametros() or lista_par() or mais_par() or corpo_p() or dc_loc() or mais_dcloc() or lista_arg() or argumentos() or mais_ident() or pfalsa() or comandos() or mais_comandos() or comando() or restoIdent() or condicao() or relacao() or expressao() or op_un() or outros_termos() or op_ad() or termo() or mais_fatores() or op_mul() or fator()) != True:
            print("\nErro sintatico !! na linha " + str(token[2]) + " no token " + str(token[0]) + "\n")
            return False
    print("Parabéns programador, o seu código está sintaticamente correto!\n")


# A tabela de simbolos
# [cadeia, token, categoria, tipo, valor, linha, escopo]

# caso seja cat="param", insere os parametros e variaveis no ultimo proc


# TODO: ver melhor essa busca aqui
def busca_tabela(lex):
    global tabela_simbolos, proc
    if proc:
        lex2 = lex
        lex2[2] = 'parametro'
        if param:
            if lex in tabela_simbolos:
                return True
            else:
                return False
        else:
            if lex in tabela_simbolos:
                return True
            elif lex2 in tabela_simbolos:
                return True
            else:
                return False
    else:
        for lista in tabela_simbolos:
            if lex in lista:
                print("mostrando lex na busca: ", lex)
                return True
            else:
                return False

def insere_tabela(lex,tipo):
    global tabela_simbolos,cat,var_aux
    print("proc: ", proc, "param: ", param, "token: ", lex, " cat: ", cat)
    if cat == "nome_prog":
        tabela_simbolos.append([lex[0],lex[1], cat, '-', '-', lex[2],"global"])
    # este caso é só para os parametros
    elif param:
        for lex in var_aux:
            if not busca_tabela([lex,cat,tipo]):
                tabela_simbolos.append([lex[0],lex[1], cat, tipo, '-', lex[2],"local"])
                print("to salvando param local")
            else:
                print("Erro: variavel já foi declarada")
                return  False
    # este caso é só para variaveis locais
    elif proc and param == False and cat == "var":
        for lex in var_aux:
            if not busca_tabela([lex,cat,tipo]):
                tabela_simbolos.append([lex[0],lex[1], cat, '-', '-', lex[2],"local"])
                print("to salvando variavel local da procedure")
            else:
                print("Erro: variavel já foi declarada")
                return  False
    # este caso é só para a procedure
    elif proc and param == False:
        if not busca_tabela([lex,cat,tipo]):
            # FIXME: atualizar categoria para PROC, está VAR
            tabela_simbolos.append([lex[0],lex[1], cat, '-', '-', lex[2],"global"])
            print("to salvando proc")
        else:
            print("Erro: variavel já foi declarada")
            return  False
    else:
        for lex in var_aux:
            if not busca_tabela([lex[0],lex[1],cat,tipo,lex[2]]):
                tabela_simbolos.append([lex[0],lex[1], cat, tipo, '-', lex[2],"global"])
                print("to salvando global")
            else:
                print("Erro: variavel já foi declarada")
                return  False
    print('\n------- Tabela de Simbolos ------- \n [cadeia, token, categoria, tipo, valor, linha, escopo]\n\n', tabela_simbolos,'\n')



token = proxToken()
i = 0
tabela_simbolos = []

cat = ''
param = False
proc = False
var_aux = []


sintatico()
