# -*- coding: utf-8 -*-
''' Compiladores 2 - UFMT 2018.1
201411310004 - Lucas Afrânio Silva de Siqueira '''

def pegartoken():
    global entrada,i
    if i < len(entrada):
        return entrada[i]
    else:
        return False

def tira_espaco():
    global i, linha
    if (pegartoken() == " " or pegartoken() == "\t"):
        i += 1
        return True
    elif (pegartoken() == "\n"):
        i += 1
        linha += 1
        return True
    else:
        return False

# comentario { .... }
def comentario1():
    global i
    if pegartoken() == '{':
        i += 1
        while pegartoken() != '}':
            i += 1
        i += 1
        return True
    else:
        return False

# comentario /* ...... */
def comentario2():
    global i, tokens
    if pegartoken() == '/':
        i += 1
        if pegartoken() == '*':
            i += 1
            while pegartoken() != "*":
                i += 1
            final_comentario2()
        else:
            tokens.append("/ SimbolosSimples " + str(linha) + ' \n')
            return True
    else:
        return False

def final_comentario2():
    global i
    if pegartoken() == '*':
        i += 1
        if pegartoken() == '/':
            i += 1
            return True
        else:
            while pegartoken() != "*":
                i += 1
            final_comentario2()


def ident_num():
    global entrada, i, linha, tokens
    palavra = ""
    aux = str(pegartoken())
    if aux.isalpha():
        palavra = palavra + aux
        i += 1
        aux = str(pegartoken())
        while aux.isalnum():
            palavra = palavra + aux
            i += 1
            aux = str(pegartoken())
        if palavra in p_reservada:
            tokens.append(palavra + " PalavraReservada " + str(linha) + " \n")
            return True
        else:
            tokens.append(palavra + " Identificador " + str(linha) + " \n")
            return True
    elif aux.isdigit():
        palavra = palavra + aux
        i += 1
        aux = str(pegartoken())
        while aux.isdigit():
            palavra = palavra + aux
            i += 1
            aux = str(pegartoken())
        if pegartoken() == '.':
            palavra = palavra + str(pegartoken())
            i += 1
            aux = str(pegartoken())
            if aux.isdigit():
                palavra = palavra + str(pegartoken())
                i += 1
                aux = str(pegartoken())
                while aux.isdigit():
                    palavra = palavra + str(pegartoken())
                    i += 1
                    aux = str(pegartoken())
                tokens.append(palavra + " NumeroReal " + str(linha) + " \n")
                return True
            else:
                return False
        else:
            tokens.append(palavra + " NumeroInteiro " + str(linha)  + " \n")
            return True
    else:
        return False

def simbolos():
    global i, tokens, simbolos_simples, simbolos_duplos
    buff = ""
    if pegartoken() in simbolos_simples:
        aux = str(pegartoken())
        i += 1
        buff = aux + str(pegartoken())
        if str(pegartoken()) in simbolos_simples and buff in simbolos_duplos:
            tokens.append(buff + " SimbolosDuplos " + str(linha) + ' \n')
            i += 1
            return True
        else:
            tokens.append(aux + " SimbolosSimples " + str(linha) + ' \n')
            return True
    else:
        return False

def lexico():
    global tokens, saida, linha
    while i < len(entrada):
        if ( comentario1() or comentario2() or tira_espaco() or ident_num() or simbolos() ) != True:
            print("\nErro lexico !! na linha " + str(linha) + " no token " + str(pegartoken()) + "\n")
            return False
    print("\nParabéns programador, o seu código está lexicamente correto! \n")
    
    saida.writelines(tokens)

arquivo=open("./Entrada/entrada_certa.txt", "r")
entrada=arquivo.read()

saida=open("tokens.txt", "w")

p_reservada=['procedure', '$', 'program', 'if', 'then', 'while','do', 'write', 'read', 'else', 'begin', 'end', 'var']
simbolos_simples=['(', ')', '*', '+', '-', '=','>', '<', '$', ';', ':', ',', '.']
simbolos_duplos=[':=','<>','<=','>=']
i = 0
linha = 1
tokens=[]

lexico()

saida.close()
