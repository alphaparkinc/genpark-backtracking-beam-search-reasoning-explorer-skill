"""
Demonstration of genpark-backtracking-beam-search-reasoning-explorer-skill
"""

from client import BeamSearchExplorerClient

def main():
    explorer = BeamSearchExplorerClient(beam_width=2, max_depth=3)

    # Simulated math exploration graph
    def expand(state: int):
        if state >= 20:
            return []
        return [
            {"action": "add_3", "next_state": state + 3},
            {"action": "mult_2", "next_state": state * 2}
        ]

    def score(state: int):
        # Target: get as close to 17 without exceeding
        if state > 17:
            return 0.0
        return float(state) / 17.0

    result = explorer.search(root_state=1, expand_fn=expand, score_fn=score)
    print("=== BEAM SEARCH REASONING RESULT ===")
    print("Optimal Action Path:", result["optimal_path"])
    print("Terminal State Value:", result["terminal_state"])
    print("Normalized Score:", result["score"])

if __name__ == "__main__":
    main()
