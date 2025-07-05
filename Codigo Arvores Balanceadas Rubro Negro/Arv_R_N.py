class No:
    def __init__(self, dado, cor="vermelho", pai=None, esquerda=None, direita=None):
        self.dado = dado
        self.cor = cor  # "vermelho" ou "preto"
        self.pai = pai
        self.esquerda = esquerda
        self.direita = direita

class ArvoreRubroNegra:
    def __init__(self):
        self.NIL = No(dado=None, cor="preto")  # nó sentinela NIL
        self.raiz = self.NIL

    def inserir(self, chave):
        novo_no = No(dado=chave, cor="vermelho", esquerda=self.NIL, direita=self.NIL)
        pai = None
        atual = self.raiz

        while atual != self.NIL:
            pai = atual
            if novo_no.dado < atual.dado:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo_no.pai = pai

        if pai is None:
            self.raiz = novo_no
        elif novo_no.dado < pai.dado:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no

        self.corrigir_insercao(novo_no)

    def corrigir_insercao(self, k):
        while k.pai and k.pai.cor == "vermelho":
            if k.pai == k.pai.pai.esquerda: # Se o pai é filho esquerdo do avô
                u = k.pai.pai.direita  # u é o tio
                if u.cor == "vermelho":
                    # Caso 1: Tio é vermelho
                    # Recolorir pai, tio e avô. Move k para o avô.
                    k.pai.cor = "preto"
                    u.cor = "preto"
                    k.pai.pai.cor = "vermelho"
                    k = k.pai.pai
                else:
                    if k == k.pai.direita:
                        # Caso 2: Tio é preto e k é filho direito
                        # Rotação à esquerda no pai e k se move para o pai.
                        k = k.pai
                        self.rotacionar_esquerda(k)
                    # Caso 3: Tio é preto e k é filho esquerdo
                    # Recolorir pai e avô. Rotação à direita no avô.
                    k.pai.cor = "preto"
                    k.pai.pai.cor = "vermelho"
                    self.rotacionar_direita(k.pai.pai)
            else: # Se o pai é filho direito do avô (casos simétricos)
                u = k.pai.pai.esquerda  # u é o tio
                if u.cor == "vermelho":
                    # Caso 1 (simétrico): Tio é vermelho
                    k.pai.cor = "preto"
                    u.cor = "preto"
                    k.pai.pai.cor = "vermelho"
                    k = k.pai.pai
                else:
                    if k == k.pai.esquerda:
                        # Caso 2 (simétrico): Tio é preto e k é filho esquerdo
                        k = k.pai
                        self.rotacionar_direita(k)
                    # Caso 3 (simétrico): Tio é preto e k é filho direito
                    k.pai.cor = "preto"
                    k.pai.pai.cor = "vermelho"
                    self.rotacionar_esquerda(k.pai.pai)
        self.raiz.cor = "preto" # A raiz é sempre preta

    def rotacionar_esquerda(self, x):
        y = x.direita # y é o filho direito de x
        x.direita = y.esquerda # O filho esquerdo de y se torna o filho direito de x
        if y.esquerda != self.NIL:
            y.esquerda.pai = x # Atualiza o pai do filho esquerdo de y

        y.pai = x.pai # O pai de x se torna o pai de y
        if x.pai is None:
            self.raiz = y # Se x era a raiz, y se torna a nova raiz
        elif x == x.pai.esquerda:
            x.pai.esquerda = y # Se x era filho esquerdo, y se torna o novo filho esquerdo
        else:
            x.pai.direita = y # Se x era filho direito, y se torna o novo filho direito

        y.esquerda = x # x se torna o filho esquerdo de y
        x.pai = y # y se torna o pai de x

    def rotacionar_direita(self, x):
        y = x.esquerda # y é o filho esquerdo de x
        x.esquerda = y.direita # O filho direito de y se torna o filho esquerdo de x
        if y.direita != self.NIL:
            y.direita.pai = x # Atualiza o pai do filho direito de y

        y.pai = x.pai # O pai de x se torna o pai de y
        if x.pai is None:
            self.raiz = y # Se x era a raiz, y se torna a nova raiz
        elif x == x.pai.direita:
            x.pai.direita = y # Se x era filho direito, y se torna o novo filho direito
        else:
            x.pai.esquerda = y # Se x era filho esquerdo, y se torna o novo filho esquerdo

        y.direita = x # x se torna o filho direito de y
        x.pai = y # y se torna o pai de x

    def em_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no != self.NIL:
            self.em_ordem(no.esquerda)
            print(f"{no.dado} ({no.cor})", end=' ')
            self.em_ordem(no.direita)

# Exemplo de uso
# Exemplo de uso
if __name__ == "__main__":
    arvore = ArvoreRubroNegra()
    elementos = [20, 15, 25, 10, 5, 1, 30, 22]
    for e in elementos:
        arvore.inserir(e)

    print("Árvore rubro-negra (em ordem):")
    arvore.em_ordem()
    print()