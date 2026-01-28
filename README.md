# 📊 Aplicação Streamlit

Este projeto utiliza **Streamlit** para visualização e teste de componentes.

> ⚠️ **Importante:** Todos os comandos abaixo devem ser executados **a partir da raiz do projeto**. Não é necessário (nem desejado) mudar de diretório.

---

## ✅ Pré-requisitos

* Python 3.10+
* Ambiente virtual configurado (opcional, mas recomendado)
* Dependências instaladas:

```bash
pip install -r requirements.txt
```

---

## 🧪 Executar arquivo de testes de componentes

O arquivo de testes de componentes está localizado **na raiz do projeto** e se chama `testing.py`.

Para executá-lo, utilize:

```bash
streamlit run testing.py
```

Esse comando inicia o Streamlit usando diretamente o arquivo de testes.

---

## 🚀 Executar a aplicação principal

A aplicação principal está localizada dentro da pasta `Streamlit`, no arquivo `Home.py`.

Para iniciar a aplicação, execute **a partir da raiz do projeto**:

```bash
streamlit run Streamlit/Home.py
```

---

## 📁 Estrutura relevante do projeto

```text
./
├── testing.py
├── Streamlit/
│   └── Home.py
├── requirements.txt
└── README.md
```

---

## 📝 Observações

* O Streamlit sempre pode ser executado apontando diretamente para o arquivo desejado, sem necessidade de `cd`.
* Caso utilize ambiente virtual, lembre-se de ativá-lo antes de rodar os comandos.

---

Qualquer dúvida ou problema na execução, verifique se o Streamlit está corretamente instalado e se os caminhos dos arquivos permanecem os mesmos.
