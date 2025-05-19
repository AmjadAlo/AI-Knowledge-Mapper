import os
from graphviz import Digraph 
import re

# Ensure Graphviz system executable is accessible
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

def sanitize(text):
    clean = str(text).replace('"', "'").replace("\n", " ").strip()
    clean = re.sub(r"[<>\\]", "", clean)
    return clean[:120] + "..." if len(clean) > 120 else clean


###

def export_to_svg(graph_data, file_name="output_graph"):
    dot = Digraph(format="svg")

    # Consistent size and layout
    dot.attr(size="12,8", ratio="expand")
    dot.attr(bgcolor="white")
    dot.attr("graph", rankdir="TB", ranksep="1.2", nodesep="0.8")
    dot.attr("node",
             shape="box",
             style="filled,setlinewidth(2)",
             width="1.5",
             height="0.6",
             fontsize="16",
             fillcolor="#FFF8DC",
             fontname="Helvetica-Bold",
             color="#FFB300",
             fontcolor="#000000")
    dot.attr("edge", color="#999999", arrowsize="1.2", penwidth="1.5")

    seen_nodes = set()
    seen_edges = set()

    #  Detect real root node (first one in the node list)
    raw_nodes = graph_data.get("nodes", [])
    root_label = sanitize(raw_nodes[0]["name"]) if raw_nodes and isinstance(raw_nodes[0], dict) else ""

    # Add nodes
    for node in raw_nodes:
        name = sanitize(node["name"]) if isinstance(node, dict) else sanitize(node)

        #  Skip long duplicate or partial root variants
        if name != root_label and (name.startswith(root_label) or len(name) > 100):
            continue

        if name and name not in seen_nodes:
            dot.node(name)
            seen_nodes.add(name)

    # Add edges
    for edge in graph_data.get("edges", []):
        if isinstance(edge, dict):
            source = sanitize(edge.get("source", ""))
            target = sanitize(edge.get("target", ""))
        else:
            source, target = map(sanitize, edge)

        if source and target and (source, target) not in seen_edges:
            dot.edge(source, target)
            seen_edges.add((source, target))

    output_dir = "data/outputs"
    output_path = dot.render(filename=file_name, directory=output_dir, format="svg", cleanup=True)
    return output_path
