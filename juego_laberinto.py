import networkx as nx
import random
import py5
import time

# Configuración inicial
n = 5  # Tamaño del laberinto
jugador_pos = (0, 0)  # Posición inicial del jugador
laberinto = None
inicio = (0, 0)
salida = (n - 1, n - 1)
tiempo_inicio = time.time()
tiempo_limite = 30  # Tiempo límite de 30 segundos

# Función para generar un laberinto aleatorio (grafo)
def generar_laberinto(n):
    G = nx.grid_2d_graph(n, n)
    edges = list(G.edges())
    random.shuffle(edges)
    maze = nx.Graph()
    maze.add_edges_from(edges[:n * n - 1])
    return maze

def setup():
    global laberinto
    py5.size(400, 400)
    py5.background(255)
    py5.stroke(0)
    laberinto = generar_laberinto(n)

def draw():
    global jugador_pos
    py5.background(255)
    dibujar_laberinto(laberinto)
    dibujar_jugador(jugador_pos)
    
    tiempo_actual = time.time()
    if tiempo_actual - tiempo_inicio > tiempo_limite:
        mostrar_solucion()  # Mostrar solución si se vence el tiempo

def dibujar_laberinto(grafo):
    for (nodo1, nodo2) in grafo.edges():
        x1, y1 = nodo1
        x2, y2 = nodo2
        py5.line(x1 * 80 + 40, y1 * 80 + 40, x2 * 80 + 40, y2 * 80 + 40)

def dibujar_jugador(pos):
    x, y = pos
    py5.fill(0, 0, 255)
    py5.ellipse(x * 80 + 40, y * 80 + 40, 20, 20)

def mostrar_solucion():
    py5.stroke(255, 0, 0)
    camino = nx.shortest_path(laberinto, source=inicio, target=salida, method='bfs')
    for i in range(len(camino) - 1):
        x1, y1 = camino[i]
        x2, y2 = camino[i + 1]
        py5.line(x1 * 80 + 40, y1 * 80 + 40, x2 * 80 + 40, y2 * 80 + 40)

def key_pressed():
    global jugador_pos
    x, y = jugador_pos
    if py5.key == py5.CODED:
        if py5.key_code == py5.UP and (x, y - 1) in laberinto.neighbors((x, y)):
            jugador_pos = (x, y - 1)
        elif py5.key_code == py5.DOWN and (x, y + 1) in laberinto.neighbors((x, y)):
            jugador_pos = (x, y + 1)
        elif py5.key_code == py5.LEFT and (x - 1, y) in laberinto.neighbors((x, y)):
            jugador_pos = (x - 1, y)
        elif py5.key_code == py5.RIGHT and (x + 1, y) in laberinto.neighbors((x, y)):
            jugador_pos = (x + 1, y)

py5.run_sketch()
