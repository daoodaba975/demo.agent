# Ton premier agent IA, sans prise de tête

Supports du talk **« Ton premier agent IA, sans prise de tête »**, présenté au club AllTech de l'Université Amadou Makhtar Mbow (UAM), Dakar.

Ce dépôt contient la démo et les slides :

| Dossier | Contenu |
|---------|---------|
| [`demo/`](./demo) | **Jang**, un petit agent IA en Python ([smolagents](https://huggingface.co/docs/smolagents)) qui répond à tes questions à partir de tes notes de cours. Moins de 30 lignes de code. |
| [`slide/`](./slide) | Les slides de la présentation, faites avec [Slidev](https://sli.dev). |

*Jàng* veut dire « apprendre, étudier, lire » en wolof.

## Démarrage rapide

Tu veux juste tester l'agent ? Il te faut Python 3.10+ et une clé API Groq gratuite.

```bash
git clone https://github.com/daoodaba975/demo.agent.git
cd demo.agent/demo
```

Suis ensuite le guide pas à pas : **[demo/README.md](./demo/README.md)**. Il explique l'installation (Windows, macOS, Linux), la clé API, le code et des exercices pour aller plus loin.

## Voir les slides en local

```bash
cd slide
pnpm install
pnpm dev
```

## Pour aller plus loin

- Documentation smolagents : https://huggingface.co/docs/smolagents
- Cours gratuit sur les agents (Hugging Face) : https://huggingface.co/learn/agents-course
