# Algoritmo A* Search - Análisis de Implementación

## 📋 Descripción

Este proyecto implementa el algoritmo **A* (A-star)** para encontrar la ruta óptima entre ciudades de Rumania. A* es un algoritmo de búsqueda de caminos que utilizando una función de evaluacion y heurística guía la exploración de manera eficiente.

## 🎯 Problema Resuelto

**Objetivo**: Encontrar la ruta más corta desde Arad hasta Bucharest en el mapa de Rumania.

### Características del Problema:
- **Estados**: 20 nodos conectados
- **Estado inicial**: Arad
- **Estado objetivo**: Bucharest  
- **Acciones**: Moverse entre nodos conectadas
- **Costos**: Distancias entre las ciudades (km)
- **Heurística clasica**: Distancia euclidiana (línea recta) hasta el destino

## 🔍 1. Análisis del Problema

El problema consiste en encontrar la ruta más corta entre dos ciudades rumanas (Arad → Bucharest) en un grafo ponderado con las caracteristicas previamente descritas

La complejidad es que existen múltiples rutas posibles con diferentes costos, y necesitamos encontrar la óptima sin explorar todo el espacio de búsqueda.

## ⚡ 2. Cómo aplicamos A*

El algoritmo A* utiliza la función de evaluación **f(n) = g(n) + h(n)** donde:

### Componentes Clave:
- g(n): Costo real acumulado desde Arad hasta el nodo actual
- h(n): Heurística (distancia hasta Bucharest)
- f(n): Estimación total del mejor camino que pasa por n

### Proceso de Ejecución:
1. **Inicialización**: Coloca Arad en la frontera con f(Arad) = 0 + 366 = 366
2. **Selección inteligente**: En cada iteración escoge el nodo con menor f(n)
3. **Expansión guiada**: Para cada ciudad que expande, calcula f(n) de sus vecinos
4. **Optimización continua**: Si encuentra un camino mejor a un estado ya visitado, lo actualiza

### Valores f(n) en la Ruta Óptima Encontrada:
```
Arad:           f(n) = 0 + 366 = 366
Sibiu:          f(n) = 140 + 253 = 393
Rimnicu Vilcea: f(n) = 220 + 193 = 413
Pitesti:        f(n) = 317 + 100 = 417
Bucharest:      f(n) = 418 + 0 = 418
```

## 🏆 3. ¿Por Qué la Ruta Encontrada es Óptima?

La ruta **Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest** (costo: 418 km) es óptima primero porque la heuristica clasica de distancia no sobreestima el costo real: 
- h(Arad) = 366 ≤ costo_real_óptimo = 418.
- Esto garantiza que A* encuentre la solución óptima.

Tambien, el algoritmo A* explora iteradamente el orden de costo estimado, crecientemente y si extistiera un camino mejor la heuristica habría guiado a el. (Propiedad de Optimalidad de A*)

## 📊 Resultados

### Ruta Óptima Encontrada:
```
Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest
```

### Detalles del Camino:
- Arad → Sibiu (costo: 140 km)
- Sibiu → Rimnicu Vilcea (costo: 80 km)
- Rimnicu Vilcea → Pitesti (costo: 97 km)
- Pitesti → Bucharest (costo: 101 km)

**VALORES DE f(n) = g(n) + h(n) EN EL CAMINO ÓPTIMO:**
- Arad: g(n)=0, h(n)=366, f(n)=366
- Sibiu: g(n)=140, h(n)=253, f(n)=393
- Rimnicu Vilcea: g(n)=220, h(n)=193, f(n)=413
- Pitesti: g(n)=317, h(n)=100, f(n)=417
- Bucharest: g(n)=418, h(n)=0, f(n)=418

**Costo Total**: 418 km

## 🔧 Implementación

### Estructura de Clases:
- **`Node`**: Representa un estado en el árbol de búsqueda
- **`Problem`**: Define el problema de búsqueda
- **`a_star_search()`**: Implementación del algoritmo A*

## 🎯 Conclusiones

✅ **A* encuentra la ruta óptima** gracias a su heurística admisible

✅ **La función f(n) = g(n) + h(n)** guía eficientemente la búsqueda

✅ **Distancia euclidiana como heuristica** nunca sobreestima el costo real

✅ **Eficiencia superior** comparado con búsqueda exhaustiva

La combinación de la heurística admisible (distancia euclidiana) con la estrategia de búsqueda de A* asegura encontrar el camino de menor costo sin necesidad de explorar exhaustivamente todo el grafo.