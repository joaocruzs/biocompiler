# BioCompiler

Projeto acadêmico de bioinformática desenvolvido para simular, de forma didática, etapas do fluxo de informação genética.

## Sobre o projeto

O BioCompiler simula etapas do processamento de informações genéticas utilizando programação.

O projeto está dividido em versões:

* **BioCompiler 1.0 — DNA Processor**
* **BioCompiler 2.0 — RNA Processor**

O BioCompiler 2.0 recebe um pré-mRNA e simula sua maturação até a formação do mRNA maduro.

## BioCompiler 1.0

O BioCompiler 1.0 trabalha com uma sequência de DNA e realiza:

* validação das bases A, T, C e G;
* identificação de START;
* identificação de STOP;
* detecção de frameshift;
* detecção de STOP prematuro;
* transcrição de DNA para pré-mRNA;
* geração de relatório.

## BioCompiler 2.0

O BioCompiler 2.0 recebe uma sequência de pré-mRNA e realiza:

1. validação das bases A, U, C e G;
2. identificação do sítio 5' `GU`;
3. identificação do branch point `A`;
4. identificação do sítio 3' `AG`;
5. validação do intron;
6. splicing;
7. adição do CAP 5' representado por `m7Gppp`;
8. adição de exatamente 100 adeninas na extremidade 3';
9. geração do mRNA maduro.

O BioCompiler 2.0 não realiza tradução para proteína.

## Tecnologias

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* Pytest

### Frontend

Planejado:

* React
* Vercel

### Deploy

* Backend: Railway
* Frontend: Vercel

## Estrutura

```text
biocompiler/
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── services/
│   │       ├── bio_compiler_1/
│   │       └── bio_compiler_2/
│   └── tests/
│
├── samples/
│   ├── biocompiler_1/
│   └── biocompiler_2/
│
├── .gitignore
└── README.md
```

## Executando localmente

Entre na pasta do backend:

```bash
cd backend
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
uvicorn app.main:app --reload
```

A documentação interativa estará disponível em:

```text
http://127.0.0.1:8000/docs
```

## Principais endpoints

### BioCompiler 1.0

```text
POST /analysis/sequence
POST /analysis/file
POST /analysis/file/report
```

### BioCompiler 2.0

```text
POST /rna/process
POST /rna/process/file
POST /rna/process/file/report
```

## Executando os testes

Na pasta `backend`:

```bash
pytest -v
```

Para executar somente os testes do BioCompiler 2.0:

```bash
pytest tests/bio_compiler_2/ -v
```

## Entrada

O BioCompiler 2.0 aceita arquivos `.txt` contendo uma sequência de pré-mRNA por linha.

Exemplo:

```text
AUGCCGUCCCCCCCCCCACCCCCCCCCAGGCCAU
```

Cada linha é processada independentemente.

## Resultado

Para uma sequência válida, o sistema gera um mRNA maduro contendo:

```text
m7Gppp
+
RNA após splicing
+
100 A
```

## Objetivo acadêmico

O projeto tem finalidade didática e busca representar conceitos de bioinformática e biologia molecular por meio de uma implementação computacional modular.

## Autoria

Universidade Federal do Piauí, Tópicos em Bioinformática.

Leticia Lopes e João Victor Cruz.

Projeto acadêmico — BioCompiler.
