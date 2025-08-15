from typing import Any, Dict, List, Optional, Set, Tuple
from BFS import Node, Problem

class DLSResult:
    def __init__(self, solution: Optional[Node], cutoff: bool, expanded: int, generated: int):
        self.solution = solution
        self.cutoff = cutoff
        self.expanded = expanded
        self.generated = generated

def depth_limited_search(problem: Problem, limit: int) -> DLSResult:
    expanded = generated = 0
    visited_on_path: Set[Any] = set()

    def recursive_dls(node: Node, limit: int) -> DLSResult:
        nonlocal expanded, generated, visited_on_path
        expanded += 1
        if problem.goal_test(node.state):
            return DLSResult(node, False, expanded, generated)
        if limit == 0:
            return DLSResult(None, True, expanded, generated)

        cutoff_occurred = False
        visited_on_path.add(node.state)
        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            if child_state in visited_on_path:
                continue
            child = Node(child_state, node, action, node.depth + 1)
            generated += 1
            result = recursive_dls(child, limit - 1)
            if result.solution is not None:
                visited_on_path.discard(node.state)
                return result
            if result.cutoff:
                cutoff_occurred = True
        visited_on_path.discard(node.state)
        return DLSResult(None, cutoff_occurred, expanded, generated)

    root = Node(problem.initial)
    return recursive_dls(root, limit)

def iterative_deepening_search(problem: Problem, max_depth: int = 100) -> Tuple[Optional[Node], Dict[str, int]]:
    total_expanded = total_generated = 0
    for limit in range(max_depth + 1):
        res = depth_limited_search(problem, limit)
        total_expanded += res.expanded
        total_generated += res.generated
        if res.solution is not None:
            return res.solution, {"expanded": total_expanded, "generated": total_generated, "limit_found": limit}
        if not res.cutoff:
            return None, {"expanded": total_expanded, "generated": total_generated, "limit_found": limit}
    return None, {"expanded": total_expanded, "generated": total_generated, "limit_found": max_depth}
