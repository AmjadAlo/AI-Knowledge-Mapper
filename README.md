# 🧠 Knowledge Graph Builder

An AI-powered app that turns any topic into a **structured concept map** using GPT-4 and LangGraph agents. It suggests classification strategies and lets you generate clear, organized roadmaps with one click.

---

## 🚀 Features

- 📚 Dynamic classification detection using GPT-4
- 🌐 Multi-agent pipeline: Research → Synthesis → Mapping
- 🧭 Interactive concept map with one root node
- 📈 Clean SVG visualization with download support
- ⚙️ Built with **LangGraph**, **Streamlit**, **Graphviz**, and **OpenAI APIs**

---

## 🗂️ Project Structure

```
roadMap/
├── app.py                 # Main Streamlit interface
├── .env                   # API keys
├── requirements.txt       # Dependencies
│
├── agents/                # AI agents (researcher, synthesizer, mapper)
├── data/                  # Output SVG graphs
├── tools/                 # Web data tools (Wikipedia, SerpAPI)
├── utils/                 # Utilities (export, classification helper)
├── workflows/             # LangGraph orchestration
```

---

## 📦 Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set API keys**
   Create a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_key
   SERPAPI_API_KEY=your_serpapi_key
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 💡 Example Topics

- Roadmap for Machine Learning
- Roadmap for Human Anatomy
- Roadmap for Vitamins

Each classification generates a focused map based on your selection (e.g., by paradigm, function, tools, symptoms...).

---

## 🧠 Powered By

- [LangGraph](https://www.langgraph.dev/)
- [OpenAI GPT-4](https://openai.com/)
- [Streamlit](https://streamlit.io/)
- [Graphviz](https://graphviz.org/)
- [SerpAPI](https://serpapi.com/)
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)

---

## 📥 Output

SVG graphs are saved automatically to the `data/outputs/` folder and are downloadable via the interface.

---

> Built for structured learning, curriculum design, and idea exploration.
