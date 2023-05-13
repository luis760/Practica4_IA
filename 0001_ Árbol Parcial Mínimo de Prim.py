# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:26:35 2023

@author: 52331
"""


# Definir la función para encontrar el Árbol Parcial Mínimo de Prim
def prim(graph, start):
    # Inicializar el conjunto de vértices visitados y por visitar
    visited = set()
    unvisited = set(graph.keys())
    unvisited.remove(start)
    
    # Inicializar el árbol parcial mínimo y la cola de bordes
    mst = {}
    edges = []
    
    # Empezar desde el vértice inicial
    current = start
    
    while unvisited:
        # Añadir el vértice actual al conjunto de visitados
        visited.add(current)
        
        # Añadir todos los bordes del vértice actual a la cola de bordes
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                edges.append((current, neighbor, weight))
        
        # Escoger el borde de menor peso que conecte un vértice visitado con uno no visitado
        edge = min(edges, key=lambda x: x[2])
        edges.remove(edge)
        mst[(edge[0], edge[1])] = edge[2]
        
        # Mover al vértice no visitado conectado por el borde seleccionado
        current = edge[1]
        unvisited.remove(current)
        
    return mst
# Definir el grafo de ejemplo
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'B': 4, 'D': 2},
    'D': {'A': 3, 'B': 1, 'C': 2}
}

# Encontrar el Árbol Parcial Mínimo desde el vértice 'A'
mst = prim(graph, 'A')

# Imprimir el resultado
print(mst)
    