# agent.py : un petit agent IA "assistant étudiant" construit avec smolagents
import os
import sys
from dotenv import load_dotenv
from smolagents import OpenAIModel, ToolCallingAgent, tool

load_dotenv()  # lit la clé API et le modèle dans le fichier .env

# 1. L'outil : une simple fonction Python que l'agent peut décider d'appeler
@tool
def lire_notes() -> str:
    """Lit le fichier notes-cours.txt et renvoie tout son contenu."""
    with open("notes-cours.txt", encoding="utf-8") as fichier:
        return fichier.read()

# 2. Le modèle (le "cerveau") : choisi dans le fichier .env, jamais de clé dans le code
model = OpenAIModel(
    model_id=os.getenv("MODEL_ID", "qwen/qwen3.8-27b"),
    api_base=os.getenv("API_BASE", "https://api.groq.com/openai/v1"),
    api_key=os.getenv("API_KEY"),
    flatten_messages_as_text=True,  # messages en texte simple, accepté par tous les fournisseurs
)

# 3. Les consignes + l'agent : la boucle "réfléchir, agir, observer" est gérée par smolagents
consignes = "Tu es Jang, un assistant qui aide des étudiants. Réponds en français, en t'appuyant sur les notes de cours."
agent = ToolCallingAgent(tools=[lire_notes], model=model, instructions=consignes, max_steps=5)

# 4. On lance l'agent avec la question passée en ligne de commande
print(agent.run(sys.argv[1]))
