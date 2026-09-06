# GenPark AI Agent Skill - Backtracking Beam Search Explorer

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Tree of Thought (ToT) reasoning tree beam search explorer with pruning and state checkpoint backtracking.

```mermaid
flowchart TD
    A[Root State] --> B1[Branch 1] & B2[Branch 2] & B3[Branch 3]
    B1 & B2 & B3 --> C[Top-K Beam Pruner]
    C --> D1[Promising Node]
    C -. Pruned .-> D2[Dead End]
    D1 --> E[Deep Reasoning Exploration]
```

## Features
- **Top-K Beam Width**: Considers multiple parallel reasoning hypothesis trees.
- **Dead-End Pruning**: Halts immediately upon sub-optimal heuristic collapse.
- **Zero External Dependencies**: Standard library Python 3.9+.

## Quickstart
```python
from client import BeamSearchExplorerClient

explorer = BeamSearchExplorerClient(beam_width=3)
res = explorer.search(state, expand_fn, score_fn)
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
