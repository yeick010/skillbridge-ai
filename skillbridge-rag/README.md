# SkillBridge AI – RAG Template

Questo notebook è un proof-of-concept per SkillBridge AI. Usa RAG (Retrieval-Augmented Generation) con Granite AI via Replicate per suggerire skill professionali e rispondere a domande personalizzate a partire da una knowledge base interna.


# 🌉 SkillBridge AI – Predictive Skills RAG System

SkillBridge AI is an AI-powered platform that uses Retrieval-Augmented Generation (RAG) to predict, explain, and recommend emerging professional skills across rapidly evolving industries such as applied AI, insurance, fintech, and more.

🔍 **Objective**  
Support economic growth and decent work (UN SDG 8) by helping workers, students, and organizations close the gap between current and future-needed skills.

---

## 🧠 Tech Stack

- **IBM Granite** via [Replicate](https://replicate.com/ibm)
- **LangChain** (retrieval, chains, prompt management)
- **FAISS** for vector store and semantic search
- **HuggingFace Embeddings** integrated with LangChain
- (Coming soon) **FastAPI** for API exposure
- (Coming soon) **React** for interactive UI

---

## 🚀 How it works

1. 📚 A knowledge base stores textual skills or is extended via CSV uploads
2. 🔗 Skills are embedded into vector representations using IBM Granite
3. 🔍 Users ask questions about current or future career skills
4. 🤖 The system answers using a Granite LLM that generates personalized, context-aware responses

---

## 🧪 Example usage

```python
query = "What skills should I develop to specialize in AI for the insurance industry?"
result = rag_chain({"query": query})
print(result["result"])
```

---

## 📦 Planned Integrations

- [ ] FastAPI-based endpoint for frontend/backend communication
- [ ] React UI for interactive skill queries and suggestions
- [ ] CSV upload for custom knowledge base
- [ ] Performance metrics and explainability module

---

## 🤝 Built for:
**IBM Lean AI Solutions Hackathon 2025**  
Participating in Call for Code for Goal 8 – Decent Work & Economic Growth.

---

## 🧑‍💻 Author

**Yeison Riascos Sanchez**  
With support from AI Specialist Agents and strategic orchestration by ChatGPT.

---

## 📄 License
MIT – Open Source, reusable and adaptable for educational and social impact use cases.
