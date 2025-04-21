# FastAPI Backend

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx, os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GRANITE_API_KEY = os.getenv("GRANITE_API_KEY")
GRANITE_ENDPOINT = "https://bam-api.res.ibm.com/v1/generate"

class QueryInput(BaseModel):
    query: str

def retrieve_context(query: str) -> str:
    # Simulazione retrieval RAG (può essere rimpiazzata da vectordb)
    examples = {
        "data science": "Le competenze richieste includono Python, Pandas, Scikit-Learn, SQL, e visualizzazione con Plotly.",
        "machine learning": "Modelli supervisionati, regressione, classificazione, overfitting, cross-validation.",
    }
    for key in examples:
        if key in query.lower():
            return examples[key]
    return "Contesto non specifico. Rispondi comunque in modo utile."

@app.post("/ask")
async def ask(input: QueryInput):
    context = retrieve_context(input.query)
    prompt = f"""
Sei un assistente esperto in skill professionali. Usa il seguente contesto per rispondere alla domanda.

Contesto: {context}

Domanda: {input.query}
Risposta dettagliata:
""".strip()

    headers = {
        "Authorization": f"Bearer {GRANITE_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model_id": "granite-13b-chat",  # esempio IBM model
        "input": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7,
        },
    }

    async with httpx.AsyncClient(timeout=30) as client:
        res = await client.post(GRANITE_ENDPOINT, json=payload, headers=headers)

    if res.status_code != 200:
        raise HTTPException(status_code=res.status_code, detail=res.text)

    return {"answer": res.json().get("results", [{}])[0].get("generated_text", "").strip()}
