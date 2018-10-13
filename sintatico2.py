# -*- coding: utf-8 -*-
''' Compiladores 2 - UFMT 2018.1
201411310004 - Lucas Afrânio Silva de Siqueira '''

from lexico2 import tokens

def proxToken():
    global tokens
    if tokens:
        prox = tokens.pop(0)
        return prox.split(' ')

def S():
    global token
    if token:
        programa()
    else:
        return False

def programa():
    global token
    if "program" in token:
        print('tudo ok programa')
        token = proxToken()
        if "Identificador" in token:
            print('tudo ok identificador do programa')
            token = proxToken()
            if corpo():
                if "." in token:
                    print('ok . \n \nParabéns programador, o seu código está sintaticamente correto!')
                    token = proxToken()
                    return True
                else:
                    print('erro: está faltando o token . na linha ', token[2])
                    return False
            else:
                print('erro ao ir no corpo')
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
            print('ok begin')
            token = proxToken()
            if comandos():
                if "end" in token:
                    print("deu certo no end")
                    token = proxToken()
                    return True
                else:
                    print("erro: está faltando o token end na linha ", token[2])
                    return False
            else:
                print("erro ao ir para comandos")
                return False
        else:
            print("erro: está faltando o token begin na linha ", token[2])
            return False
    else:
        print("erro ao ir para dc")
        return False

def dc():
    global token
    if dc_v():
        if mais_dc():
            print("ok no dc_v > mais_dc no dc")
            return True
        else:
            print("dando erro no mais_dc do dc_v")
            return False
    elif dc_p():
        print("ok no dc_p")
        return True
        if mais_dc():
            print("ok no mais_dc do dc_p")
            return True
    else:
        print("ok no dc_v vazio")
        return True

def mais_dc():
    global token
    if ";" in token:
        print("ok ;")
        token = proxToken()
        if dc():
            print("ok no dc do mais_dc")
            return True
        else:
            print("erro no dc do mais_dc")
            return False
    else:
        print("erro: está faltando o token ; na linha ", token[2])
        print("ok no mais_dc vazio")
        return True

def dc_v():
    global token
    if "var" in token:
        print("ok var")
        token = proxToken()
        if variaveis():
            if ":" in token:
                print("ok :")
                token = proxToken()
                if tipo_var():
                    print("ok no tipo_var")
                    return True
                else:
                    print("erro no tipo_var")
                    return False
            else:
                print("erro: está faltando o token : na linha ", token[2])
                return False
        else:
            print("erro ao voltar das variaveis")
            return False
    else:
        return False

def tipo_var():
    global token
    if "real" in token:
        print("achei real")
        token = proxToken()
        return True
    elif "integer" in token:
        print("achei inteiro")
        token = proxToken()
        return True
    else:
        print("não achei tipo_var")
        return False

def variaveis():
    global token
    if "Identificador" in token:
        print("ok identificador da variaveis")
        token = proxToken()
        if mais_var():
            print("ok no mais_var")
            return True
        else:
            print("erro no mais_var")
            return False
    else:
        print("erro: está faltando o token ident na linha ", token[2])
        return False

def mais_var():
    global token
    if "," in token:
        print("ok ,")
        token = proxToken()
        if variaveis():
            print("deu certo nas variaveis do mais_var")
            return True
        else:
            print("erro no variaveis do mais_var")
            return False
    else:
        print("ok no mais_var vazio")
        print("erro: está faltando o token , na linha ", token[2])
        return True

def dc_p():
    global token
    if "procedure" in token:
        print("ok procedure no dc_p")
        token = proxToken()
        if "Identificador" in token:
            print("ok identificador no dc_p")
            token = proxToken()
            if parametros():
                if corpo_p():
                    print("ok no corpo_p")
                    return True
                else:
                    print("erro no corpo_p do dc_p")
                    return False
            else:
                print("erro ao ir parametros")
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
        print("ok (")
        token = proxToken()
        if lista_par():
            if ")" in token:
                print("ok )")
                token = proxToken()
                return True
            else:
                print("erro: está faltando o token ) na linha ", token[2])
                return False
        else:
            print("erro no lista par")
            return False
    else:
        print("ok parametros vazio")
        print("erro: está faltando o token ( na linha ", token[2])
        return True

def lista_par():
    global token
    if variaveis():
        if ":" in token:
            print("ok :")
            token = proxToken()
            if tipo_var():
                if mais_par():
                    print("ok mais_par")
                    return True
                else:
                    print("erro no mais_par")
                    return False
            else:
                print("erro no tipo_var")
                return False
        else:
            print("erro: está faltando o token : na linha ", token[2])
            return False
    else:
        print("erro variaveis")
        return False

def mais_par():
    global token
    if ";" in token:
        print("ok ;")
        token = proxToken()
        if lista_par():
            print("ok lista_par no mais_par")
            return True
        else:
            print("erro lista_par no mais_par")
            return False
    else:
        print("ok mais_par vazio")
        print("erro: está faltando o token ; na linha ", token[2])
        return True

def corpo_p():
    global token
    if dc_loc():
        if "begin" in token:
            print("ok begin do corpo_p")
            token = proxToken()
            if comandos():
                if "end" in token:
                    print("ok end do corpo_p")
                    token = proxToken()
                    return True
                else:
                    print("erro end do corpo_p")
                    print("erro: está faltando o token end na linha ", token[2])
                    return False
            else:
                print("erro no comandos")
                return False
        else:
            print("erro begin do corpo_p")
            print("erro: está faltando o token begin na linha ", token[2])
            return False
    else:
        print("erro dc_loc no corpo_p")
        return False

def dc_loc():
    global tokens
    if dc_v():
        if mais_dcloc():
            print("ok mais_dcloc no dc_loc")
            return True
        else:
            print("erro mais_dcloc no dc_loc")
            return False
    else:
        print("ok dc_loc vazio")
        return True

def mais_dcloc():
    global token
    if ";" in token:
        print("ok ; no mais_dcloc")
        token = proxToken()
        if dc_loc():
            print("ok dc_loc no mais_dcloc")
            return True
        else:
            print("erro dc_loc no mais_dcloc")
    else:
        print("ok mais_dcloc vazio")
        print("erro: está faltando o token ; na linha ", token[2])
        return True

def lista_arg():
    global token
    if "(" in token:
        print("ok ( na lista_arg")
        token = proxToken()
        if argumentos():
            if ")" in token:
                print("ok ) na lista_arg")
                token = proxToken()
                return True
            else:
                print("erro ) na lista_arg")
                print("erro: está faltando o token ) na linha ", token[2])
                return False
        else:
            print('erro argumentos no lista_arg')
            return False
    else:
        print("ok lista_arg vazio")
        print("erro: está faltando o token ( na linha ", token[2])
        return True

def argumentos():
    global token
    if "Identificador" in token:
        print("ok identificador no argumentos")
        token = proxToken()
        if mais_ident():
            print("ok mais_ident no argumentos")
            return True
        else:
            print("erro mais_ident no argumentos")
            return False
    else:
        print("erro no identificador do argumentos")
        print("erro: está faltando o token ident na linha ", token[2])
        return False

def mais_ident():
    global token
    if ";" in token:
        print("ok ; no mais_ident")
        token = proxToken()
        if argumentos():
            print('ok argumento no mais_ident')
            return True
        else:
            print("erro argumentos no mais_ident")
            return False
    else:
        print("ok mais_ident vazio")
        print("erro: está faltando o token ; na linha ", token[2])
        return True

def pfalsa():
    global token
    if "else" in token:
        print("ok else no pfalsa")
        token = proxToken()
        if comandos():
            print("ok comandos no pfalsa")
            return True
        else:
            print("erro comandos no pfalsa")
            return False
    else:
        print("ok pfalsa vazio")
        print("erro: está faltando o token else na linha ", token[2])
        return True

def comandos():
    global token
    if comando():
        if mais_comandos():
            print("ok mais_comandos no comandos")
            return True
        else:
            print("erro mais_comandos no comando")
            return False
    else:
        print("erro no comandos")
        return False

# TODO: Add "erro: faltando token esperado" nos terminais da gramática

def mais_comandos():
    global token
    if ";" in token:
        print("ok ; no mais_comandos")
        token = proxToken()
        if comandos():
            print("ok comandos no mais_comandos")
            return True
        else:
            print("erro no comandos no mais_comandos")
            return False
    else:
        print("ok mais_comandos vazio")
        print("erro: está faltando o token ; na linha ",token[2])
        return True

# TODO: quando não achar o $, tem que parar o código

def comando():
    global token
    if "read" in token:
        print("ok read no comando")
        token = proxToken()
        if "(" in token:
            print("ok ( no comando")
            token = proxToken()
            if variaveis():
                if ")" in token:
                    print("ok ) no comando")
                    token = proxToken()
                    return True
                else:
                    print("erro ) no comando")
                    print("erro: está faltando o token ) na linha ", token[2])
                    return False
            else:
                print("erro variaveis no comando")
                return False
        else:
            print("erro ( no comando")
            print("erro: está faltando o token ( na linha ", token[2])
            return False
    elif "write" in token:
        print("ok write no comando")
        token = proxToken()
        if "(" in token:
            print("ok ( no comando")
            token = proxToken()
            if variaveis():
                if ")" in token:
                    print("ok ) no comando")
                    token = proxToken()
                    return True
                else:
                    print("erro ) no comando")
                    print("erro: está faltando o token ) na linha ", token[2])
                    return False
            else:
                print("erro variaveis no comando")
                return False
        else:
            print("erro ( no comando")
            print("erro: está faltando o token ( na linha ", token[2])
            return False
    elif "while" in token:
        print("ok while no comando")
        token = proxToken()
        if condicao():
            if "do" in token:
                print("ok DO no comando")
                token = proxToken()
                if comandos():
                    if "$" in token:
                        print("ok $ no comando")
                        token = proxToken()
                        return True
                    else:
                        print("erro $ no comando")
                        print("erro: está faltando o token $ na linha ", token[2])
                        return True
                else:
                    print("erro while > do no comando")
                    return False
            else:
                print("erro - nao achei do na condicao")
                print("erro: está faltando o token do na linha ", token[2])
                return False
        else:
            print("erro na condicao do while")
            return False
    elif "if" in token:
        print("ok IF no comando")
        token = proxToken()
        if condicao():
            if "then" in token:
                print("ok then no comando")
                token = proxToken()
                if comandos():
                    if pfalsa():
                        if "$" in token:
                            print("ok $ no then do condicao")
                            token = proxToken()
                            return True
                        else:
                            print("erro $ then da condicao")
                            print("erro: está faltando o token $ na linha ", token[2])
                            return False
                    else:
                        print("erro pfalsa > then da condicao")
                        return False
                else:
                    print("erro comandos > then da condicao")
                    return False
            else:
                print("erro then no comando")
                print("erro: está faltando o token then na linha ", token[2])
                return False
        else:
            print("erro na condicao > if no comando")
            return False
    elif "Identificador" in token:
        print("ok identificador no comando")
        token = proxToken()
        if restoIdent():
            print("ok restoIdent no comando")
            return True
        else:
            print("erro restoIdent no comando")
            return False
    else:
        print("erro no comando")
        print("erro: está faltando o token ident na linha ", token[2])
        return False

def restoIdent():
    global token
    if ":=" in token:
        print("ok restoIdent")
        token = proxToken()
        if expressao():
            print("ok expressao no restoIdent")
            return True
        else:
            print("erro expressao no restoIdent")
            return False
    elif lista_arg():
        print("ok lista_arg")
        return True
    else:
        print("erro no restoIdent")
        print("erro: está faltando o token := na linha ", token[2])
        return False

def condicao():
    global token
    exp1 = token
    if expressao():
        if relacao():
            exp2 = token
            if expressao():
                print("ok expressao na condicao")
                return True
            else:
                print("erro expressao na condicao")
                return False
        else:
            print("erro no op_un na condicao")
            return False
    else:
        print("erro na expressao na condicao")
        return False

def relacao():
    global token
    if "=" in token:
        print("encontrei = no op_un")
        token = proxToken()
        return True
    elif "<>" in token:
        print("encontrei <> no op_un")
        token = proxToken()
        return True
    elif ">=" in token:
        print("encontrei >= no op_un")
        token = proxToken()
        return True
    elif "<=" in token:
        print("encontrei <= no op_un")
        token = proxToken()
        return True
    elif ">" in token:
        print("encontrei > no op_un")
        token = proxToken()
        return True
    elif "<" in token:
        print("encontrei < no op_un")
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
            print("ok outros_termos na expressao")
            return True
        else:
            print("erro outros_termos na expressao")
            return False
    else:
        print("erro termo na expressao")
        return False

def op_un():
    global token
    if "+" in token:
        print("encontrei + no op_un")
        token = proxToken()
        return True
    elif "-" in token:
        print("encontrei - no op_un")
        token = proxToken()
        return True
    else:
        print("ok na op_un vazio")
        print("erro: está faltando o token + ou - na linha ", token[2])
        return True

def outros_termos():
    global token
    if op_ad():
        if termo():
            if outros_termos():
                print("ok outros_termos")
                return True
            else:
                print("erro outros_termos")
                return False
        else:
            print("erro termo no outros_termos")
            return False
    else:
        print("ok outros_termos vazio")
        return True

def op_ad():
    global token
    if "+" in token:
        print("encontrei + no op_ad")
        token = proxToken()
        return True
    elif "-" in token:
        print("encontrei - no op_ad")
        token = proxToken()
        return True
    else:
        print("erro no op_ad")
        print("erro: está faltando o token + ou -  na linha ", token[2])
        return False

def termo():
    global token
    if op_un():
        if fator():
            if mais_fatores():
                print("ok mais_fatores no termo")
                return True
            else:
                print("erro mais_fatores no termo")
                return False
        else:
            print("erro fator no termo")
            return False
    else:
        print("erro op_un no termo")
        return False

def mais_fatores():
    global token
    if op_mul():
        print("cheguei no op_mul dos mais_fatores")
        if fator():
            if mais_fatores():
                print("ok mais_fatores no mais_fatores")
                return True
            else:
                print("erro mais_fatores no mais_fatores")
                return False
        else:
            print("erro fator no mais_fatores")
            return False
    else:
        print("ok mais_fatores vazio")
        return True

def op_mul():
    global token
    if "*" in token:
        print("encontrei * no op_mul")
        token = proxToken()
        return True
    elif "/" in token:
        print("encontrei / no op_mul")
        token = proxToken()
        return True
    else:
        print("erro no op_mul")
        print("erro: está faltando o token * ou / na linha ", token[2])
        return False

def fator():
    global token
    if "Identificador" in token:
        print("ok identificador no fator")
        token = proxToken()
        return True
    elif "NumeroInteiro" in token:
        print("ok numero inteiro no fator")
        token = proxToken()
        return True
    elif "NumeroReal" in token:
        print("ok numero real no fator")
        token = proxToken()
        return True
    elif "(" in token:
        print("ok ( no fator")
        token = proxToken()
        if expressao():
            if ")" in token:
                print("ok ) no fator")
                token = proxToken()
                return True
            else:
                print("erro ) no fator")
                print("erro: está faltando o token ) na linha ", token[2])
                return False
        else:
            print("erro expressao no fator")
            return False
    else:
        print("erro fator")
        print("erro: está faltando o token ( ou ident ou numero_int ou numero_real na linha ", token[2])
        return False

token = proxToken()
S()

'''
if S():
    print('O codigo está sintaticamente correto! \n Parabéns brow, programador dos bons ehin')
else:
    print('Não foi dessa vez, programador! \n Ta dando erro, vá corrigir programador')
'''
