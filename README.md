# BioCompiler 🧬

Projeto de bioinformática desenvolvido para simular parte do fluxo da informação genética:

**DNA → pré-mRNA**

O sistema recebe sequências de DNA, realiza validações biológicas, identifica códons de início e término, detecta possíveis mutações e realiza a transcrição da sequência para pré-mRNA.

---

## Funcionalidades

O BioCompiler é capaz de:

* Validar sequências de DNA;
* Detectar bases inválidas;
* Identificar o códon START (`ATG`);
* Identificar códons STOP (`TAA`, `TAG`, `TGA`);
* Determinar o quadro de leitura em trincas;
* Detectar possíveis frameshifts;
* Detectar STOP prematuro (nonsense);
* Transcrever DNA para pré-mRNA;
* Processar múltiplas sequências através de arquivos `.txt`;
* Gerar relatórios consolidados;
* Disponibilizar uma API REST utilizando FastAPI.

---

## Casos analisados

| Caso            | Resultado                         |
| --------------- | --------------------------------- |
| Entrada correta | `CORRETO`                         |
| Base inválida   | `BUG - base inválida`             |
| START ausente   | `BUG - START ausente`             |
| STOP ausente    | `BUG - STOP ausente`              |
| Frameshift      | `BUG - frameshift`                |
| STOP prematuro  | `BUG - nonsense / STOP prematuro` |

---

## Regras biológicas utilizadas

### Bases válidas

As sequências de DNA devem conter apenas:

```text
A
T
C
G
```

---

### Códon START

O início da região codificante é identificado pelo códon:

```text
ATG
```

---

### Códons STOP

Os códons de término considerados são:

```text
TAA
TAG
TGA
```

A busca pelos códons STOP é realizada respeitando o quadro de leitura definido a partir do START.

---

## Fluxo de análise

```text
Sequência de DNA
        │
        ▼
Validação das bases
        │
        ▼
Identificação do START
        │
        ▼
Determinação do quadro de leitura
        │
        ▼
Verificação de Frameshift
        │
        ▼
Busca por STOP
        │
        ▼
Verificação de STOP prematuro
        │
        ▼
Classificação da sequência
        │
        ▼
Transcrição DNA → pré-mRNA
```

---

## Estrutura do projeto

```text
biocompiler/
│
├── backend/
│   │
│   ├── app/
│   │   ├── core/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── tests/
│   └── requirements.txt
│
├── samples/
│   └── sequences.txt
│
├── .gitignore
└── README.md
```

---

## Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* Pytest

---

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd biocompiler/backend
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Executando o projeto

Dentro da pasta `backend`:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

---

## Documentação da API

O FastAPI disponibiliza automaticamente uma interface Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Endpoints

### Health Check

```http
GET /health
```

Resposta:

```json
{
    "status": "healthy"
}
```

---

### Analisar sequência individual

```http
POST /analysis/sequence
```

Exemplo:

```json
{
    "sequence": "TGCATGCTCGAACGGTCACCAACGGGTTAG"
}
```

---

### Analisar arquivo

```http
POST /analysis/file
```

Recebe um arquivo `.txt` contendo uma sequência de DNA por linha.

Exemplo:

```text
ATGAAATAG
ATGCCCTAA
CATCAAAAGGCGGAAAAGGAGGGTTAG
```

---

### Gerar relatório

```http
POST /analysis/file/report
```

Recebe um arquivo `.txt` e retorna um relatório consolidado em formato `.txt`.

---

## Formato de entrada

O arquivo deve possuir uma sequência de DNA por linha:

```text
ATGAAATAG
ATGCCCTAA
ATGCXCGTAA
```

---

## Testes

Para executar os testes automatizados:

```bash
pytest
```

---

## Autor

Projeto desenvolvido como atividade acadêmica da disciplina de Bioinformática.
