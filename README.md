# Jang : ton assistant de révision

*Jàng* veut dire « apprendre, étudier, lire » en wolof.

Jang est un petit **agent IA** qui répond à tes questions à partir de tes notes de cours (`notes-cours.txt`).
Il est construit avec [smolagents](https://huggingface.co/docs/smolagents) (Hugging Face), en moins de 30 lignes de Python.

Projet de démo du talk **« Ton premier agent IA, sans prise de tête »**, présenté au club AllTech de l'UAM.

```text
> python agent.py "Quelle est la différence entre une pile et une file ?"

Calling tool: 'lire_notes'
...
Une pile suit le principe LIFO (dernier entré, premier sorti), une file le principe FIFO (premier entré, premier sorti).
```

## C'est quoi un agent ?

Un chatbot répond avec ce qu'il sait déjà. Un agent peut **agir** : il décide lui-même d'utiliser des outils.

Un agent, c'est :

| Pièce | Rôle | Dans Jang |
|-------|------|-----------|
| **Un modèle** | Le cerveau, qui réfléchit | Un LLM gratuit chez Groq |
| **Des outils** | Les mains, qui agissent | La fonction `lire_notes` |
| **Des consignes** | Son rôle | « Tu es Jang, un assistant qui aide des étudiants... » |
| **Une boucle** | Réfléchir, agir, observer, recommencer | Gérée par smolagents (`agent.run`) |

Quand tu poses une question, Jang :

1. **réfléchit** : « Pour répondre, j'ai besoin des notes de cours » ;
2. **agit** : il appelle l'outil `lire_notes` ;
3. **observe** : il lit le contenu du fichier ;
4. **répond** à partir de ce qu'il a lu.

## Prérequis

- **Python 3.10 ou plus récent**. Pour vérifier : `py --version` sous Windows, `python3 --version` sous macOS ou Linux.
  Pour l'installer : https://www.python.org/downloads/ (sous Windows, coche **« Add python.exe to PATH »**).
- **Git** : https://git-scm.com/downloads
- **Une clé API gratuite Groq**, sans carte bancaire (voir l'étape 3).

## Installation pas à pas

### 1. Récupérer le projet

```bash
git clone https://github.com/daoodaba975/demo.agent.git
cd demo.agent
```

Tu peux aussi faire **Code** puis **Download ZIP** sur GitHub, dézipper le dossier et l'ouvrir dans un terminal.

### 2. Créer l'environnement virtuel et installer les dépendances

**Windows (PowerShell)**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si PowerShell bloque `Activate.ps1` avec le message « l'exécution de scripts est désactivée », lance cette commande puis réessaie :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Une fois le venv activé, `(.venv)` apparaît au début de la ligne du terminal.
Pense à le réactiver chaque fois que tu ouvres un nouveau terminal.

### 3. Obtenir une clé API Groq (gratuit)

1. Crée un compte sur https://console.groq.com
2. Va dans **API Keys**, puis clique sur **Create API Key**.
3. Copie la clé. Elle commence par `gsk_`.

### 4. Créer le fichier `.env`

Le fichier `.env` contient ta clé. Il n'est **jamais** dans le code ni sur GitHub (il est listé dans `.gitignore`).

**Windows**

```powershell
Copy-Item .env.example .env
notepad .env
```

**macOS / Linux**

```bash
cp .env.example .env
nano .env
```

Remplace `gsk_ta_cle_ici` par ta vraie clé, puis enregistre. Le fichier doit ressembler à ceci :

```env
API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
MODEL_ID=qwen/qwen3.8-27b
API_BASE=https://api.groq.com/openai/v1
```

### 5. Lancer Jang

Toujours depuis le dossier `demo.agent`, venv activé :

```bash
python agent.py "Quelle est la différence entre une pile et une file ?"
```

N'oublie pas les **guillemets** autour de la question.

Autres questions à essayer :

```bash
python agent.py "Combien d'adresses utilisables dans un réseau /24 ?"
python agent.py "Quelles sont mes notes en bases de données ?"
python agent.py "Qui es-tu ?"
```

Dans le terminal, les cadres `Calling tool: 'lire_notes'` montrent l'agent en train d'utiliser son outil.

## Comprendre le code

Ouvre `agent.py`. Il tient en quatre blocs :

1. **L'outil** : `lire_notes` est une fonction Python normale. Le décorateur `@tool` la transforme en outil.
   Sa docstring (le texte entre `"""`) explique au modèle à quoi sert l'outil : c'est grâce à elle qu'il sait quand l'utiliser.
2. **Le modèle** : `OpenAIModel` se connecte à n'importe quel fournisseur compatible OpenAI.
   Le nom du modèle, l'adresse et la clé viennent du fichier `.env`.
3. **Les consignes et l'agent** : `ToolCallingAgent` réunit le modèle, les outils et les consignes.
   `max_steps=5` limite le nombre de tours de boucle, pour éviter qu'il tourne sans fin.
4. **Le lancement** : `agent.run(...)` démarre la boucle avec ta question (`sys.argv[1]`, le texte passé après `agent.py`).

## À toi de jouer : exercices

1. **Change les notes.** Remplace le contenu de `notes-cours.txt` par tes propres cours, puis pose-lui des questions.
2. **Change sa personnalité.** Modifie les consignes, par exemple : « Réponds toujours avec un exemple concret ».
3. **Ajoute un 2e outil `calculer_moyenne`.** Il prend une liste de notes et renvoie la moyenne.
   Puis demande : `"Quelle est ma moyenne en algorithmique ?"`.
   - Indice : l'outil a besoin d'un type (`notes: list[float]`) et d'une docstring avec une section `Args:`.
   - Corrigé : `solution/agent.py`. Lance-le depuis le dossier `demo.agent` :

     ```bash
     python solution/agent.py "Quelle est ma moyenne générale ?"
     ```

4. **Va plus loin.** Imagine un outil qui écrit dans un fichier, qui cherche dans plusieurs fichiers de cours, ou qui génère un quiz.

Astuce : tu peux demander à un agent de code (OpenCode, Claude Code...) de t'aider. Donne-lui un prompt clair, puis **relis et teste** ce qu'il produit.

## Changer de modèle

Le modèle par défaut, `qwen/qwen3.8-27b` chez Groq, appelle ses outils de façon fiable.
Évite `openai/gpt-oss-120b` avec cet agent : il échoue souvent avec `Error code: 400 - Tool choice is required`.
La liste des modèles Groq change souvent ; vérifie-la sur https://console.groq.com/docs/models.

**Alternative : Google Gemini** (offre gratuite, clé sur https://aistudio.google.com/apikey).
Dans `.env`, commente les lignes Groq et décommente les lignes Gemini. Vérifie le nom exact du modèle dans AI Studio.

N'importe quel fournisseur **compatible OpenAI** fonctionne : il suffit de changer les 3 lignes du `.env`.

L'offre gratuite a des limites (requêtes par minute et par jour), mais elles suffisent largement pour apprendre.

## Problèmes fréquents

| Message | Solution |
|---------|----------|
| `Missing credentials. Please pass an api_key...` | Pas de fichier `.env`, ou ligne `API_KEY=` vide. |
| `Error code: 401 - Invalid API Key` | Clé mal copiée dans `.env` (espace en trop, guillemets...). |
| `Error code: 429` | Limite gratuite atteinte : attends une minute. |
| `Error code: 404 - The model ... does not exist` | Modèle retiré par Groq : choisis-en un autre sur https://console.groq.com/docs/models et change `MODEL_ID`. |
| `Error code: 400 - Tool choice is required` | Le modèle gère mal les outils : reviens à `qwen/qwen3.8-27b`. |
| `IndexError: list index out of range` | Tu as oublié la question entre guillemets après `agent.py`. |
| `FileNotFoundError: notes-cours.txt` | Lance la commande depuis le dossier `demo.agent`. |
| `ModuleNotFoundError: No module named 'smolagents'` | Le venv n'est pas activé, ou `pip install -r requirements.txt` n'a pas été lancé. |
| `python` ouvre le Microsoft Store (Windows) | Le venv n'est pas activé : `.\.venv\Scripts\Activate.ps1` |

## Contenu du dépôt

| Fichier | Rôle |
|---------|------|
| `agent.py` | L'agent de base, avec un seul outil `lire_notes`. |
| `notes-cours.txt` | Des notes de cours d'exemple (algorithmique, bases de données, réseaux) et des notes de contrôle. |
| `solution/agent.py` | Le corrigé de l'exercice 3, avec un 2e outil `calculer_moyenne`. |
| `requirements.txt` | Les dépendances Python, avec leurs versions. |
| `.env.example` | Le modèle du fichier `.env`, à copier. |

## Pour aller plus loin

- Documentation smolagents : https://huggingface.co/docs/smolagents
- Cours gratuit sur les agents (Hugging Face) : https://huggingface.co/learn/agents-course

---

Fait par [Daouda BA](https://github.com/daoodaba975) · [Galsen DEV](https://galsen.dev)
