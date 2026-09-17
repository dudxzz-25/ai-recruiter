# AI Recruiter

Aplicação web de análise de compatibilidade entre currículo e vaga usando **NLP com TF-IDF + similaridade de cosseno**, extração de skills e histórico em SQL.

> O score é uma ferramenta demonstrativa de portfólio e não deve ser usado como decisão automatizada de contratação.

## Stack
Python, Flask, scikit-learn, SQLite, HTML, CSS e JavaScript.

## Execução
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app/app.py
```
Abra `http://127.0.0.1:5000`.

## Testes
```bash
python -m unittest discover -s tests -v
```
