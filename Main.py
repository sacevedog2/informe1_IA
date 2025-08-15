import time
import tracemalloc
import pandas as pd
from BFS import Problem, bfs
from IDS import iterative_deepening_search

Graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "H", "I"],
    "F": ["C", "J"],
    "G": ["D"],
    "H": ["E"],
    "I": ["E", "J"],
    "J": ["F", "I"],
}

def run_with_metrics(algorithm_name: str, func, *args, **kwargs):
    tracemalloc.start()
    t0 = time.perf_counter()
    solution, stats = func(*args, **kwargs)
    t1 = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    path = solution.path() if solution else None
    return {
        "algorithm": algorithm_name,
        "path": " - ".join(path) if path else None,
        "stops (nodes)": len(path) if path else None,
        "edges traversed": (len(path) - 1) if path else None,
        "expanded nodes": stats.get("expanded"),
        "generated nodes": stats.get("generated"),
        "found at depth": stats.get("limit_found") if "limit_found" in stats else (len(path)-1 if path else None),
        "time_ms": round((t1 - t0) * 1000, 3),
        "peak_kb": round(peak / 1024, 2),
    }

if __name__ == "__main__":
    problem = Problem("A", "J", Graph)

    bfs_metrics = run_with_metrics("BFS", bfs, problem)
    ids_metrics = run_with_metrics("IDS", iterative_deepening_search, problem, 100)

    df = pd.DataFrame([bfs_metrics, ids_metrics])
    print("\n=== Comparación BFS vs IDS ===")
    print(df.to_string(index=False))
