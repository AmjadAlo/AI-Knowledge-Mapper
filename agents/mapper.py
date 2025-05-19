import json
import re

def run_mapper(summary: str):
    nodes = set()
    edges = []

    for line in summary.splitlines():
        parts = [p.strip() for p in line.split("→")]
        for i in range(len(parts)):
            nodes.add(parts[i])
            if i > 0:
                edges.append((parts[i - 1], parts[i]))

    return {"nodes": list(nodes), "edges": edges}
