# 💸 Finance Tracker

A full-stack personal finance tracker built with:

- **React + TypeScript** for a responsive and modern frontend
- **Flask (Python)** backend for REST APIs and business logic

---

##  Features

-  Add/view spending categories and amounts
-  Responsive dashboard UI (React + Vite + Tailwind CSS)
-  Modular Flask backend with route separation and test cases
-  Unit tests for core backend features
---

## TODOES

- Switch to redis filesystem for prod
- Better UI/UX in general
- Integrate Plaid API for bank account
- Integrate Alpha Vantage for portfolio tracking

---
## Setup Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask --app run run
```
---
## Setup Frontend
```bash
cd frontend
npm install
npm run dev
```
---
## 📁 Project Structure
```bash
.
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── routes
│   ├── config.py
│   ├── run.py
│   └── tests
│       ├── test_auth.py
│       └── test_dashboard.py
├── frontend
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── public
│   │   └── vite.svg
│   ├── README.md
│   ├── src
│   │   ├── api.tsx
│   │   ├── App.css
│   │   ├── App.tsx
│   │   ├── assets
│   │   ├── components
│   │   ├── index.css
│   │   ├── main.tsx
│   │   ├── pages
│   │   └── vite-env.d.ts
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
└── project_tree.txt

```
