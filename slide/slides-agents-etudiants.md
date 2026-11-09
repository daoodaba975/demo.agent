---
theme: default
title: "Ton premier agent IA, sans prise de tête"
info: |
  AllTech UAM, Club Informatique, Université Amadou Makhtar Mbow
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: fade
mdc: true
fonts:
  sans: "Inter"
  mono: "Fira Code"
---

<style>
:root {
  --slidev-theme-primary: #281168;
}

.accent  { color: #281168; }
.accent2 { color: #4B2AC7; }
.accent3 { color: #6D28D9; }
.muted   { color: #555555; }

.card {
  background: #ffffff;
  border: 1px solid rgba(40,17,104,0.2);
  border-radius: 12px;
  padding: 1.1rem 1.3rem;
  color: #1f1f1f;
}

.card-light {
  background: #f5f3ff;
  border: 1px solid rgba(40,17,104,0.15);
  border-radius: 12px;
  padding: 1.1rem 1.3rem;
  color: #1f1f1f;
}

.tool-card {
  background: #ffffff;
  border: 1px solid rgba(40,17,104,0.2);
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
  color: #1f1f1f;
}

.step-num {
  background: #281168;
  color: #fff;
  font-weight: 800;
  border-radius: 6px;
  width: 2rem;
  height: 2rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-right: 0.6rem;
  flex-shrink: 0;
}

.cmd {
  background: #281168;
  color: #fff;
  font-family: "Fira Code", monospace;
  font-size: 0.75rem;
  border-radius: 6px;
  padding: 0.4rem 0.7rem;
}

.big-quote {
  font-size: 1.3rem;
  font-style: italic;
  color: #1f1f1f;
  line-height: 1.6;
}
</style>

---
layout: cover
background: "#281168"
---

<div class="h-full flex flex-col justify-center pl-2">
  <div class="text-xs tracking-widest mb-6" style="color:rgba(255,255,255,0.6)">ALLTECH UAM · CLUB INFORMATIQUE · 2026</div>

  <h1 class="text-5xl font-black leading-tight mb-5" style="color:#fff">
    Ton premier<br>
    <span style="color:#C4B5FD">agent IA</span>,<br>
    sans prise de tête
  </h1>

  <p class="text-xl italic mb-8" style="color:rgba(255,255,255,0.7)">
    Les compétences à maîtriser à l'ère de l'IA
  </p>

  <div class="text-sm" style="color:rgba(255,255,255,0.5)">
    Daouda BA · Fondateur & Lead Galsen DEV
  </div>
</div>

---
layout: default
background: "#ededed"
---

# <span class="accent">Au programme</span>

<div class="grid grid-cols-1 gap-3 mt-6">
  <div class="card flex items-center justify-between">
    <div class="flex items-center gap-3">
      <span class="step-num">1</span>
      <span class="font-semibold">Comprendre ce qu'est un agent IA</span>
    </div>
    <span class="accent text-sm">12 min</span>
  </div>
  <div class="card flex items-center justify-between">
    <div class="flex items-center gap-3">
      <span class="step-num">2</span>
      <span class="font-semibold">Concevoir l'architecture de son agent</span>
    </div>
    <span class="accent text-sm">6 min</span>
  </div>
  <div class="card flex items-center justify-between">
    <div class="flex items-center gap-3">
      <span class="step-num">3</span>
      <span class="font-semibold">Choisir ses outils et son framework open source</span>
    </div>
    <span class="accent text-sm">5 min</span>
  </div>
  <div class="card flex items-center justify-between">
    <div class="flex items-center gap-3">
      <span class="step-num">4</span>
      <span class="font-semibold">Démo live : on construit un agent</span>
    </div>
    <span class="accent text-sm">20 min</span>
  </div>
  <div class="card flex items-center justify-between">
    <div class="flex items-center gap-3">
      <span class="step-num">5</span>
      <span class="font-semibold">Les compétences à garder</span>
    </div>
    <span class="accent text-sm">5 min</span>
  </div>
  <div class="card flex items-center justify-between">
    <div class="flex items-center gap-3">
      <span class="step-num">6</span>
      <span class="font-semibold">Questions et échanges</span>
    </div>
    <span class="accent text-sm">12 min</span>
  </div>
</div>

---
layout: default
background: "#ededed"
---

# <span class="accent">Une question pour commencer</span>

<div class="mt-6 card-light py-8 text-center">
  <p class="big-quote mb-0">
    "Qui utilise déjà ChatGPT ou une autre IA<br>
    pour ses TD ou ses projets ?"
  </p>
</div>

<div class="mt-6 text-center">
  <span class="text-lg font-bold">Aujourd'hui, on passe au niveau suivant : <span class="accent">une IA qui agit, pas seulement qui répond.</span></span>
</div>

---
layout: default
background: "#ededed"
---

# Chatbot ou <span class="accent">agent</span> ?

<div class="grid grid-cols-2 gap-5 mt-6">
  <div class="card">
    <div class="font-bold mb-4 text-lg" style="color:#555">Chatbot</div>
    <ul class="space-y-3 text-sm">
      <li>Tu poses une question</li>
      <li>Il répond avec du texte</li>
      <li>C'est toi qui copies le code et le testes</li>
      <li>Il ne voit pas ton projet</li>
    </ul>
  </div>
  <div class="card" style="border-color:rgba(40,17,104,0.5)">
    <div class="font-bold accent mb-4 text-lg">Agent IA</div>
    <ul class="space-y-3 text-sm">
      <li>Tu donnes un objectif</li>
      <li>Il fait un plan</li>
      <li>Il utilise des outils : fichiers, commandes, recherche</li>
      <li><strong class="accent">Il vérifie et corrige tout seul</strong></li>
    </ul>
  </div>
</div>

---
layout: default
background: "#ededed"
---

# L'agent, c'est comme un <span class="accent">stagiaire</span>

<div class="card-light mt-4 mb-5 text-center py-3">
  <span class="text-sm">Tu lui donnes une mission. Il travaille. Tu valides.</span>
</div>

<div class="grid grid-cols-5 gap-3 mt-2">
  <div class="tool-card">
    <div class="step-num mx-auto mb-2" style="margin-right:auto">1</div>
    <div class="font-bold accent text-sm mb-1">Lire</div>
    <div class="text-xs muted">Il comprend la demande et le contexte</div>
  </div>
  <div class="tool-card">
    <div class="step-num mx-auto mb-2" style="margin-right:auto">2</div>
    <div class="font-bold accent text-sm mb-1">Planifier</div>
    <div class="text-xs muted">Il décide des étapes</div>
  </div>
  <div class="tool-card">
    <div class="step-num mx-auto mb-2" style="margin-right:auto">3</div>
    <div class="font-bold accent text-sm mb-1">Agir</div>
    <div class="text-xs muted">Il appelle ses outils</div>
  </div>
  <div class="tool-card">
    <div class="step-num mx-auto mb-2" style="margin-right:auto">4</div>
    <div class="font-bold accent text-sm mb-1">Vérifier</div>
    <div class="text-xs muted">Il lit les résultats et les erreurs</div>
  </div>
  <div class="tool-card">
    <div class="step-num mx-auto mb-2" style="margin-right:auto">5</div>
    <div class="font-bold accent text-sm mb-1">Corriger</div>
    <div class="text-xs muted">Il recommence jusqu'à réussir</div>
  </div>
</div>

<div class="mt-6 text-center text-sm">
  Cette boucle s'appelle la <strong class="accent">boucle agentique</strong>. Toi, tu restes le responsable du projet.
</div>

---
layout: default
background: "#ededed"
---

# L'architecture d'un <span class="accent">agent</span>

<div class="grid grid-cols-4 gap-4 mt-6">
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#281168">Modèle</div>
    <div class="text-xs muted mb-2">Le cerveau</div>
    <div class="text-xs">Un LLM qui comprend la demande et décide quoi faire.</div>
  </div>
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#4B2AC7">Outils</div>
    <div class="text-xs muted mb-2">Les mains</div>
    <div class="text-xs">Lire un fichier, lancer une commande, chercher sur le web, appeler une API.</div>
  </div>
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#6D28D9">Mémoire</div>
    <div class="text-xs muted mb-2">Le contexte</div>
    <div class="text-xs">Ce qu'il a déjà fait, tes consignes et les fichiers du projet.</div>
  </div>
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#281168">Boucle</div>
    <div class="text-xs muted mb-2">Le pilote</div>
    <div class="text-xs">Le code qui répète : réfléchir, agir, observer, jusqu'à la fin.</div>
  </div>
</div>

<div class="card-light mt-6 text-center py-3">
  <span class="text-sm">Un agent, c'est <strong class="accent">un modèle + des outils + de la mémoire + une boucle</strong>. Pas de magie.</span>
</div>

---
layout: default
background: "#ededed"
---

# Choisir son <span class="accent">framework</span> open source

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#281168">smolagents</div>
    <div class="text-xs mb-2 accent2 font-semibold">Le plus simple pour débuter</div>
    <div class="text-xs muted">Hugging Face. Quelques lignes de Python pour un premier agent avec outils.</div>
  </div>
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#4B2AC7">CrewAI</div>
    <div class="text-xs mb-2 accent2 font-semibold">Équipes d'agents</div>
    <div class="text-xs muted">Tu définis des rôles (chercheur, rédacteur) qui collaborent.</div>
  </div>
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#6D28D9">LangGraph</div>
    <div class="text-xs mb-2 accent2 font-semibold">Contrôle fin</div>
    <div class="text-xs muted">Pour modéliser des workflows complexes. Plus avancé.</div>
  </div>
</div>

<div class="card mt-5 py-3">
  <div class="text-sm font-semibold mb-2 accent">Comment choisir ?</div>
  <ul class="text-sm space-y-1">
    <li>Débutant : le plus simple, le plus de documentation</li>
    <li>Communauté active et licence open source</li>
    <li>Compatible avec plusieurs modèles, pas d'enfermement chez un seul fournisseur</li>
  </ul>
</div>

---
layout: default
background: "#ededed"
---

# Nos outils pour la démo

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="tool-card" style="border-color:rgba(40,17,104,0.6); border-width:2px">
    <div class="font-bold text-lg mb-1" style="color:#281168">OpenCode</div>
    <div class="text-xs mb-3 accent2 font-semibold">Notre outil principal</div>
    <div class="text-xs mb-3 muted">Open source, dans le terminal. Fonctionne avec plusieurs modèles, dont des options gratuites.</div>
    <div class="cmd">npm i -g opencode-ai</div>
  </div>
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#4B2AC7">Claude Code</div>
    <div class="text-xs mb-3 muted">Agent d'Anthropic, très fort sur les projets de plusieurs fichiers. Abonnement requis.</div>
    <div class="cmd">npm i -g @anthropic-ai/claude-code</div>
  </div>
  <div class="tool-card">
    <div class="font-bold text-lg mb-1" style="color:#6D28D9">Codex</div>
    <div class="text-xs mb-3 muted">Agent d'OpenAI, utilisable dans le terminal. Même principe, autre modèle.</div>
    <div class="cmd">npm i -g @openai/codex</div>
  </div>
</div>

<div class="card mt-5 text-center py-3">
  <span class="text-sm">Ces outils sont eux-mêmes des agents. <strong class="accent">Aujourd'hui, on les utilise pour en construire un.</strong></span>
</div>

---
layout: default
background: "#ededed"
---

# <span class="accent">Démo live</span>

<div class="card-light text-center py-4 mt-4 mb-5">
  <p class="text-lg font-bold mb-1">Objectif : un petit agent assistant étudiant</p>
  <p class="text-sm muted">Un dossier vide, un README, OpenCode.</p>
</div>

<div class="grid grid-cols-1 gap-3">
  <div class="card flex items-start gap-3">
    <span class="step-num">01</span>
    <div>
      <div class="font-bold accent">On décrit l'agent dans le README</div>
      <div class="text-sm mt-1 muted">Sa mission, ses outils, le framework choisi.</div>
    </div>
  </div>
  <div class="card flex items-start gap-3">
    <span class="step-num">02</span>
    <div>
      <div class="font-bold accent">OpenCode construit l'agent</div>
      <div class="text-sm mt-1 muted">Il planifie, crée les fichiers, installe les dépendances et lance l'agent.</div>
    </div>
  </div>
  <div class="card flex items-start gap-3">
    <span class="step-num">03</span>
    <div>
      <div class="font-bold accent">On casse quelque chose volontairement</div>
      <div class="text-sm mt-1 muted">L'agent lit l'erreur et la corrige : la boucle en action.</div>
    </div>
  </div>
  <div class="card flex items-start gap-3">
    <span class="step-num">04</span>
    <div>
      <div class="font-bold accent">On teste notre agent</div>
      <div class="text-sm mt-1 muted">On lui pose une vraie question et on regarde quels outils il utilise.</div>
    </div>
  </div>
</div>

---
layout: default
background: "#ededed"
---

# Le <span class="accent">prompt</span> fait la différence

<div class="grid grid-cols-2 gap-5 mt-6">
  <div class="card" style="border-color:rgba(220,38,38,0.3)">
    <div class="font-bold mb-3" style="color:#DC2626">Prompt flou</div>
    <div class="cmd" style="background:#f3f3f3;color:#1f1f1f">Fais-moi un agent</div>
    <div class="text-xs mt-3 muted">Résultat générique, souvent à refaire.</div>
  </div>
  <div class="card" style="border-color:rgba(40,17,104,0.5)">
    <div class="font-bold accent mb-3">Prompt clair</div>
    <div class="cmd" style="background:#f5f3ff;color:#1f1f1f">Crée un agent Python avec smolagents qui répond aux questions sur mes notes de cours. Outils : lire un fichier texte et faire un calcul.</div>
    <div class="text-xs mt-3 muted">Objectif, framework, outils : l'agent sait quoi faire.</div>
  </div>
</div>

---
layout: default
background: "#ededed"
---

# Les compétences à <span class="accent">garder</span>

<div class="grid grid-cols-2 gap-4 mt-5">
  <div class="card flex items-start gap-3">
    <span class="step-num">1</span>
    <div>
      <div class="font-bold accent">Comprendre le problème</div>
      <div class="text-sm mt-1 muted">Bien formuler ce que tu veux avant de demander.</div>
    </div>
  </div>
  <div class="card flex items-start gap-3">
    <span class="step-num">2</span>
    <div>
      <div class="font-bold accent">Lire et relire le code</div>
      <div class="text-sm mt-1 muted">Ne valide jamais ce que tu ne comprends pas.</div>
    </div>
  </div>
  <div class="card flex items-start gap-3">
    <span class="step-num">3</span>
    <div>
      <div class="font-bold accent">Tester et déboguer</div>
      <div class="text-sm mt-1 muted">L'agent se trompe aussi. C'est toi qui vérifies.</div>
    </div>
  </div>
  <div class="card flex items-start gap-3">
    <span class="step-num">4</span>
    <div>
      <div class="font-bold accent">Les bases solides</div>
      <div class="text-sm mt-1 muted">Algorithmique, HTTP, bases de données. Les outils changent, les bases restent.</div>
    </div>
  </div>
</div>

<div class="card-light mt-5 text-center py-3">
  <span class="text-sm font-semibold">L'agent est un accélérateur, pas un remplaçant de ton apprentissage.</span>
</div>

---
layout: default
background: "#ededed"
---

# Par où <span class="accent">commencer</span> cette semaine ?

<div class="grid grid-cols-1 gap-4 mt-6">
  <div class="card" style="border-color:rgba(40,17,104,0.5)">
    <div class="flex items-center gap-3 mb-2">
      <span class="step-num">1</span>
      <span class="font-bold">Installe OpenCode</span>
    </div>
    <div class="ml-11"><span class="cmd">npm install -g opencode-ai</span></div>
  </div>
  <div class="card" style="border-color:rgba(40,17,104,0.5)">
    <div class="flex items-center gap-3 mb-2">
      <span class="step-num">2</span>
      <span class="font-bold">Choisis un petit agent utile pour toi</span>
    </div>
    <div class="text-sm ml-11 muted">Un assistant pour tes notes de cours, un résumeur de PDF, un aide-mémoire de commandes. Écris un README clair.</div>
  </div>
  <div class="card" style="border-color:rgba(40,17,104,0.5)">
    <div class="flex items-center gap-3 mb-2">
      <span class="step-num">3</span>
      <span class="font-bold">Construis, observe, corrige</span>
    </div>
    <div class="text-sm ml-11 muted">Lis ce que fait l'agent, pose des questions, corrige quand il se trompe.</div>
  </div>
</div>

---
layout: cover
background: "#281168"
---

<div class="h-full flex flex-col justify-center">
  <h1 class="text-6xl font-black mb-6" style="color:#fff">
    Questions et<br><span style="color:#C4B5FD">échanges</span>
  </h1>
  <p class="text-lg italic mb-10" style="color:rgba(255,255,255,0.7)">
    Quel agent voudrais-tu construire en premier ?
  </p>
  <div class="text-sm" style="color:rgba(255,255,255,0.5)">
    Galsen DEV · galsen.dev
  </div>
</div>
