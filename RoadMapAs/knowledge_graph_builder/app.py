import streamlit as st
from workflows.langgraph_router import autonomous_pipeline
from utils.graphviz_exporter import export_to_svg
from utils.classification_helper import get_classification_options
from PIL import Image
import base64
import os

st.set_page_config(page_title="Knowledge Graph Builder", layout="wide")

# ==== Styling ====
st.markdown("""
    <style>
    .title {text-align: center; font-size: 36px; font-weight: bold; color: #4A90E2; margin-bottom: 20px;}
    .desc {text-align: center; font-size: 16px; color: #333; margin-bottom: 30px;}
    .footer {text-align: center; font-size: 13px; color: grey; margin-top: 40px;}
    </style>
""", unsafe_allow_html=True)

# ==== Header ====
st.markdown("""
    <div class='title'>🧠 Multi-Agent Knowledge Graph Builder</div>
    <div class='desc'>Get detailed, AI-generated mind maps and learning roadmaps instantly</div>
""", unsafe_allow_html=True)

# ==== Input ====
topic = st.text_input("🎯 Enter a question or topic (e.g., 'Roadmap for Machine Learning')")

if topic:
    if "classification_options" not in st.session_state:
        with st.spinner("🔍 Detecting classification strategies..."):
            st.session_state.classification_options = get_classification_options(topic)

    # Extract short labels only for dropdown
    labels = [item.split(":")[0] for item in st.session_state.classification_options]
    selected_label = st.selectbox("🗭 Choose a classification method:", labels)
    classification = next((full for full in st.session_state.classification_options if full.startswith(selected_label)), selected_label)

    # Only run after user confirms selection (not on first render)
    if "triggered" not in st.session_state:
        st.session_state.triggered = False

    if st.button("🚀 Generate Knowledge Map"):
        st.session_state.triggered = True

    # Run pipeline if triggered
    if st.session_state.get("triggered"):
        full_topic = f"{classification}"
        with st.spinner("🔧 Building the knowledge map..."):
            graph = autonomous_pipeline(full_topic)

        if isinstance(graph, dict) and "nodes" in graph and "edges" in graph:
            st.subheader("🔍 Roadmap Content Debug")
            st.write("🌩 Nodes:", len(graph["nodes"]))
            st.write("🔗 Edges:", len(graph["edges"]))
            if len(graph["nodes"]) == 0:
                st.warning("⚠️ No nodes generated. Check if the LLM returned a valid roadmap.")
        else:
            st.warning("⚠️ Invalid output structure from autonomous_pipeline.")
            st.code(graph, language="text")

        # Export to SVG
        svg_path = export_to_svg(graph)

        if os.path.exists(svg_path):
            st.success("✅ Graph generated successfully!")

            with open(svg_path, "r", encoding="utf-8") as f:
                svg_content = f.read()
                st.components.v1.html(svg_content, height=800, scrolling=True)

            # Optional: Download link
            with open(svg_path, "rb") as f:
                svg_data = f.read()
                b64 = base64.b64encode(svg_data).decode()
                href = f'<a href="data:image/svg+xml;base64,{b64}" download="{topic}.svg">📅 Download Graph</a>'
                st.markdown(href, unsafe_allow_html=True)
        else:
            st.error("❌ SVG file was not created. Check export_to_svg() logic.")
