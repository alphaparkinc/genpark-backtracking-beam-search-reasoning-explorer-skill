"""
Backtracking Beam Search Reasoning Tree Explorer.
Zero external dependencies, standard library only.
"""

from typing import Dict, List, Any, Optional, Callable

class BeamSearchExplorerClient:
    """
    Explores reasoning branches using beam search with dead-end backtracking:
    - Maintains top-K candidate paths per exploration step
    - Prunes unpromising dead-ends
    - Restores previous state checkpoints when a branch collapses
    """

    def __init__(self, beam_width: int = 3, max_depth: int = 4):
        self.beam_width = beam_width
        self.max_depth = max_depth

    def search(self, root_state: Any, expand_fn: Callable[[Any], List[Dict[str, Any]]], score_fn: Callable[[Any], float]) -> Dict[str, Any]:
        """
        Executes beam search:
        expand_fn(state) -> List of {"action": str, "next_state": Any}
        score_fn(state) -> float
        """
        # A beam candidate: {"path": [actions], "state": state, "score": float}
        beam = [{"path": [], "state": root_state, "score": score_fn(root_state)}]

        best_terminal = beam[0]

        for depth in range(self.max_depth):
            all_candidates = []

            for candidate in beam:
                expansions = expand_fn(candidate["state"])
                if not expansions:
                    # Dead end or terminal
                    if candidate["score"] > best_terminal["score"]:
                        best_terminal = candidate
                    continue

                for exp in expansions:
                    new_state = exp["next_state"]
                    new_path = candidate["path"] + [exp["action"]]
                    s = score_fn(new_state)
                    new_cand = {"path": new_path, "state": new_state, "score": s}
                    all_candidates.append(new_cand)
                    if s > best_terminal["score"]:
                        best_terminal = new_cand

            if not all_candidates:
                break

            # Retain top-K
            all_candidates.sort(key=lambda c: c["score"], reverse=True)
            beam = all_candidates[:self.beam_width]

        return {
            "optimal_path": best_terminal["path"],
            "terminal_state": best_terminal["state"],
            "score": round(best_terminal["score"], 3),
            "depth_reached": len(best_terminal["path"])
        }
