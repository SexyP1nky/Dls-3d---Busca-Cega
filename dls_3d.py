class DLS3D:
    def __init__(self, inicio, objetivo, limite_espacial):
        self.inicio = inicio
        self.objetivo = objetivo
        self.limite_espacial = limite_espacial
        self.visitados = set()
        self.passos = []
        self.nos_expandidos = 0
        
    def movimentos_possiveis(self, posicao):
        x, y, z = posicao
        movimentos = [
            (x+1, y, z),  
            (x-1, y, z),  
            (x, y+1, z),  
            (x, y-1, z),  
            (x, y, z+1),  
            (x, y, z-1),  
        ]
        
        # Filtra movimentos válidos
        validos = []
        for mov in movimentos:
            if all(0 <= coord <= self.limite_espacial for coord in mov):
                validos.append(mov)
        
        return validos
    
    def dls_recursivo(self, posicao_atual, profundidade, limite, caminho):
        """
        Busca em profundidade limitada recursiva
        """
        # Imprime o estado atual
        print(f"\n{'  ' * profundidade}┌─ Profundidade {profundidade}: Explorando posição {posicao_atual}")
        self.nos_expandidos += 1
        
        # se chegou ao objetivo
        if posicao_atual == self.objetivo:
            print(f"{'  ' * profundidade}└─  Encontrado")
            return caminho + [posicao_atual]
        
        # se atingiu o limite de profundidade
        if profundidade >= limite:
            print(f"{'  ' * profundidade}└─  Limite de profundidade atingido")
            return None
        
        # Marca como visitado neste caminho
        self.visitados.add(posicao_atual)
        
        # movimentos possíveis
        movimentos = self.movimentos_possiveis(posicao_atual)
        print(f"{'  ' * profundidade}  Movimentos possíveis: {movimentos}")
        
        for i, proximo in enumerate(movimentos):
            if proximo not in self.visitados:
                print(f"{'  ' * profundidade}  -> Tentando movimento {i+1}/{len(movimentos)}: {proximo}")
                
                resultado = self.dls_recursivo(proximo, profundidade + 1, limite, caminho + [posicao_atual])
                
                if resultado is not None:
                    return resultado
            else:
                print(f"{'  ' * profundidade} Posição {proximo} já visitada, ignorando")
        
        # Remove da lista de visitados (backtracking)
        self.visitados.remove(posicao_atual)
        print(f"{'  ' * profundidade}└─ ⤴ Backtracking de {posicao_atual}")
        
        return None
    
    def buscar(self, limite_profundidade):
        """Executa a busca DLS"""
        print("ALGORITMO DLS  TRIDIMENSIONAL")
        print(f"\nPosição Inicial: {self.inicio}")
        print(f"Objetivo: {self.objetivo}")
        print(f"Espaço: (0,0,0) até ({self.limite_espacial},{self.limite_espacial},{self.limite_espacial})")
        print(f"Limite de Profundidade: {limite_profundidade}")
        print(" iniciando busca...")
        
        
        self.visitados.clear()
        self.nos_expandidos = 0
        
        resultado = self.dls_recursivo(self.inicio, 0, limite_profundidade, [])
        
        print("Resultado  da Busca")
                
        if resultado:
            print(f"\nObjetivo encontrado")
            print(f"\nEstatísticas:")
            print(f"   -Nós expandidos: {self.nos_expandidos}")
            print(f"   -Profundidade da solução: {len(resultado) - 1}")
            print(f"   -Comprimento do caminho: {len(resultado)} posições")
            
            print(f"\nCaminho encontrado:")
            for i, pos in enumerate(resultado):
                if i == 0:
                    print(f"   {i}. {pos} (início) ")
                elif i == len(resultado) - 1:
                    print(f"   {i}. {pos} (objetivo) ")
                else:
                    print(f"   {i}. {pos}")
            
            return resultado
        else:
            print(f"\n Falha. Objetivo não encontrado dentro do limite de profundidade.")
            print(f"\nEstatísticas:")
            print(f"   Nós expandidos: {self.nos_expandidos}")
            return None


def main():
    # Configuração
    inicio = (0, 0, 0)
    objetivo = (1, 2, 1)
    limite_espacial = 3
    limite_profundidade = 10
    
    
    dls = DLS3D(inicio, objetivo, limite_espacial)
    caminho = dls.buscar(limite_profundidade)
    


if __name__ == "__main__":
    main()