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
    global token
    if "program" in token:
        token = proxToken()
        if "Identificador" in token:
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
    global token
    if "real" in token:
        token = proxToken()
        return True
    elif "integer" in token:
        token = proxToken()
        return True
    else:
        print("erro: está faltando o token real ou integer na linha ", token[2])
        return False

def variaveis():
    global token
    if "Identificador" in token:
        token = proxToken()
        if mais_var():
            return True
        else:
            return False
    else:
        print(token)
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
    global token
    if "procedure" in token:
        token = proxToken()
        if "Identificador" in token:
            token = proxToken()
            if parametros():
                if corpo_p():
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
    global token
    if "(" in token:
        token = proxToken()
        if lista_par():
            if ")" in token:
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
    global tokens, saida, linha,i
    while i < len(tokens):
        if ( S() or programa() or corpo() or dc() or mais_dc() or dc_v or tipo_var() or variaveis() or mais_var() or dc_p() or parametros() or lista_par() or mais_par() or corpo_p() or dc_loc() or mais_dcloc() or lista_arg() or argumentos() or mais_ident() or pfalsa() or comandos() or mais_comandos() or comando() or restoIdent() or condicao() or relacao() or expressao() or op_un() or outros_termos() or op_ad() or termo() or mais_fatores() or op_mul() or fator()) != True:
            print("\nErro lexico !! na linha " + str(linha) + " no token " + str(pegartoken()) + "\n")
            return False
    print("\nParabéns programador, o seu código está sintaticamente correto!")


token = proxToken()

i = 0

sintatico()

#S()