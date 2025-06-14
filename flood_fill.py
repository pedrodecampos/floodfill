import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def flood_fill(matrix, start_x, start_y, target_color, replacement_color):
    """
    Implementa o algoritmo Flood Fill usando uma pilha.
    
    Args:
        matrix: Matriz numpy representando a imagem
        start_x: Coordenada x inicial
        start_y: Coordenada y inicial
        target_color: Cor que será substituída
        replacement_color: Nova cor
    
    Returns:
        Lista de frames para animação
    """
    if target_color == replacement_color:
        return [matrix.copy()]
    
    height, width = matrix.shape
    stack = [(start_x, start_y)]
    frames = [matrix.copy()]
    
    while stack:
        x, y = stack.pop()
        
        if (0 <= x < width and 0 <= y < height and 
            matrix[y, x] == target_color):
            
            matrix[y, x] = replacement_color
            frames.append(matrix.copy())
            
            # Adiciona os vizinhos à pilha
            stack.append((x + 1, y))  # direita
            stack.append((x - 1, y))  # esquerda
            stack.append((x, y + 1))  # baixo
            stack.append((x, y - 1))  # cima
    
    return frames

def create_animation(frames, title, output_file):
    """
    Cria uma animação dos frames do Flood Fill.
    
    Args:
        frames: Lista de frames (matrizes numpy)
        title: Título da animação
        output_file: Nome do arquivo de saída
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    def update(frame):
        ax.clear()
        im = ax.imshow(frame, cmap='viridis')
        ax.set_title(title)
        # Adiciona grade
        ax.grid(True, which='both', color='black', linewidth=0.5)
        # Adiciona números nos eixos
        ax.set_xticks(np.arange(-0.5, frame.shape[1], 1), minor=True)
        ax.set_yticks(np.arange(-0.5, frame.shape[0], 1), minor=True)
        return ax,
    
    anim = FuncAnimation(fig, update, frames=frames, 
                        interval=100, blit=True)
    anim.save(output_file, writer='pillow')
    plt.close()

def create_example_grids():
    """
    Cria diferentes exemplos de grids para demonstrar o Flood Fill.
    """
    examples = []
    
    # Exemplo 1: Grid pequeno com obstáculos simples
    grid1 = np.zeros((10, 10))
    grid1[2:8, 2:8] = 1  # Área navegável
    grid1[4:6, 4:6] = 0  # Obstáculo no centro
    examples.append(("grid1", grid1, 5, 5))
    
    # Exemplo 2: Grid médio com labirinto
    grid2 = np.zeros((15, 15))
    grid2[1:14, 1:14] = 1  # Área navegável
    # Cria um labirinto simples
    grid2[3:12, 3] = 0
    grid2[3:12, 11] = 0
    grid2[3, 3:12] = 0
    grid2[11, 3:12] = 0
    grid2[7, 3:11] = 0
    examples.append(("grid2", grid2, 7, 7))
    
    # Exemplo 3: Grid grande com padrão complexo
    grid3 = np.zeros((20, 20))
    grid3[1:19, 1:19] = 1  # Área navegável
    # Cria um padrão de obstáculos
    for i in range(2, 19, 4):
        grid3[i:i+2, 2:19] = 0
    examples.append(("grid3", grid3, 10, 10))
    
    return examples

def main():
    examples = create_example_grids()
    
    for name, grid, start_x, start_y in examples:
        # Define as cores
        target_color = 1
        replacement_color = 2
        
        # Executa o Flood Fill
        frames = flood_fill(grid.copy(), start_x, start_y, target_color, replacement_color)
        
        # Cria a animação
        create_animation(frames, f'Flood Fill - {name}', f'{name}_animation.gif')
        
        # Salva o grid inicial e final
        plt.figure(figsize=(8, 8))
        plt.imshow(grid, cmap='viridis')
        plt.title(f'Grid Inicial - {name}')
        plt.grid(True, which='both', color='black', linewidth=0.5)
        plt.savefig(f'{name}_initial.png')
        plt.close()
        
        plt.figure(figsize=(8, 8))
        plt.imshow(frames[-1], cmap='viridis')
        plt.title(f'Grid Final - {name}')
        plt.grid(True, which='both', color='black', linewidth=0.5)
        plt.savefig(f'{name}_final.png')
        plt.close()

if __name__ == "__main__":
    main() 