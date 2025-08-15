from collections import deque
from typing import Any, Dict, List, Optional, Tuple, Set
from dataclasses import dataclass

@dataclass
class Node:
    state: Any
    parent: Optional["Node"] = None
    action: Optional[Any] = None
    depth: int = 0

    def path(self) -> List[Any]:
        n, p = self, []
        while n:
            p.append(n.state)
            n = n.parent
        return list(reversed(p))

class Problem:
    def __init__(self, initial: Any, goal: Any, graph: Dict[Any, List[Any]]):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, state: Any) -> List[Any]:
        return self.graph.get(state, [])

    def result(self, state: Any, action: Any) -> Any:
        return action

    def goal_test(self, state: Any) -> bool:
        return state == self.goal

def bfs(problem: Problem) -> Tuple[Optional[Node], Dict[str, int]]:
    frontier = deque([Node(problem.initial)])
    explored: Set[Any] = set()
    in_frontier: Set[Any] = {problem.initial}
    expanded = generated = 0

    while frontier:
        node = frontier.popleft()
        in_frontier.discard(node.state)
        expanded += 1
        if problem.goal_test(node.state):
            return node, {"expanded": expanded, "generated": generated}

        explored.add(node.state)
        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            if child_state not in explored and child_state not in in_frontier:
                child = Node(child_state, node, action, node.depth + 1)
                frontier.append(child)
                in_frontier.add(child_state)
                generated += 1

    return None, {"expanded": expanded, "generated": generated}
