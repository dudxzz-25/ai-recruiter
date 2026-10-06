# AI Recruiter

[![CI](https://github.com/dudxzz-25/ai-recruiter/actions/workflows/ci.yml/badge.svg)](https://github.com/dudxzz-25/ai-recruiter/actions/workflows/ci.yml)

Aplicação web de análise de compatibilidade entre currículo e vaga usando **NLP com TF-IDF, similaridade de cosseno e extração de competências**.

> **Uso responsável:** o score é demonstrativo e não deve ser utilizado como decisão automatizada de contratação.

## 🎯 Objetivo

Transformar currículo e descrição de vaga em uma análise simples e explicável, mostrando:

- score geral de aderência;
- similaridade textual;
- compatibilidade de skills;
- competências encontradas em comum;
- competências presentes na vaga e ausentes no currículo.

## 🛠️ Stack

**Python · Flask · scikit-learn · SQLite · pypdf · HTML · CSS · JavaScript**

## ⚙️ Como funciona

```text
Currículo + Vaga
      ↓
Normalização do texto
      ↓
TF-IDF + similaridade de cosseno
      ↓
Extração de skills
      ↓
Score combinado + matched/missing skills
      ↓
Interface web + histórico em SQLite
```

O score combina **similaridade textual (55%)** e **aderência de competências (45%)**. Currículos podem ser inseridos como texto ou enviados em PDF.

## 📂 Estrutura

```text
ai-recruiter/
├── app/
│   ├── app.py
│   ├── scoring.py
│   ├── static/
│   └── templates/
├── data/
│   ├── sample_job.txt
│   └── sample_resume.txt
├── tests/
│   └── test_scoring.py
├── requirements.txt
└── README.md
```

## ▶️ Como executar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app/app.py
```

Abra:

```text
http://127.0.0.1:5000
```

### Testes

```bash
python -m unittest discover -s tests -v
```

## 🧠 O que este projeto demonstra

- processamento e normalização de texto;
- vetorização com TF-IDF;
- similaridade de cosseno;
- extração baseada em vocabulário de competências;
- desenvolvimento web com Flask;
- leitura de PDF;
- persistência de resultados em SQLite;
- preocupação com explicabilidade e uso responsável.

## ⚠️ Limitações

O modelo não entende contexto semântico profundo, senioridade, qualidade da experiência ou equivalências entre todas as competências. O resultado deve ser interpretado apenas como apoio exploratório.

---

Desenvolvido por **Eduardo de Toledo Dias**.

[Portfólio](https://dudxzz-25.github.io/portfolio-web/) · [GitHub](https://github.com/dudxzz-25) · [LinkedIn](https://www.linkedin.com/in/eduardo-de-toledo-dias-880b9834b/)