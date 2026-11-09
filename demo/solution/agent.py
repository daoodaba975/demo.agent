# agent.py (solution) : l'assistant étudiant avec un 2e outil, calculer_moyenne
import os
import sys
from dotenv import load_dotenv
from smolagents import OpenAIModel, ToolCallingAgent, tool

load_dotenv()  # lit la clé API et le modèle dans le fichier .env

# 1. Outil 1 : lire les notes de cours
@tool
def lire_notes() -> str:
    """Lit le fichier notes-cours.txt et renvoie tout son contenu."""
    with open("notes-cours.txt", encoding="utf-8") as fichier:
        return fichier.read()

# 1 bis. Outil 2 : calculer une moyenne
@tool
def calculer_moyenne(notes: list[float]) -> float:
    """Calcule la moyenne d'une liste de notes sur 20.

    Args:
        notes: La liste des notes, par exemple [12, 14, 10].
    """
    return round(sum(notes) / len(notes), 2)

# 2. Le modèle (le "cerveau") : choisi dans le fichier .env, jamais de clé dans le code
model = OpenAIModel(
    model_id=os.getenv("MODEL_ID", "qwen/qwen3.8-27b"),
    api_base=os.getenv("API_BASE", "https://api.groq.com/openai/v1"),
    api_key=os.getenv("API_KEY"),
    flatten_messages_as_text=True,  # messages en texte simple, accepté par tous les fournisseurs
)

# 3. Les consignes + l'agent
consignes = (
    "Tu es Jang, un assistant qui aide des étudiants. Réponds en français, en t'appuyant sur les notes de cours. "
    "Pour toute moyenne, utilise l'outil calculer_moyenne."
)
agent = ToolCallingAgent(tools=[lire_notes, calculer_moyenne], model=model, instructions=consignes, max_steps=6)

# 4. On lance l'agent avec la question passée en ligne de commande
print(agent.run(sys.argv[1]))
