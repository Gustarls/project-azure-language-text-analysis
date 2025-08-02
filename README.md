# 💬 Azure Text Analysis – Análise de Texto com Azure AI

![badge-python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![badge-azure](https://img.shields.io/badge/Azure-Cognitive--Services-blue?logo=microsoft-azure)
![badge-status](https://img.shields.io/badge/Status-Concluído-success)

Este projeto demonstra como integrar o serviço **Azure AI Language** a uma aplicação em Python para analisar arquivos de texto contendo avaliações de hotéis. A solução utiliza o SDK oficial da Microsoft para:

- Detecção de idioma
- Análise de sentimento
- Extração de frases-chave
- Reconhecimento de entidades nomeadas
- Reconhecimento de entidades vinculadas à Wikipédia

---

## 📁 Estrutura do Projeto

```
project-azure-language-text-analysis/
├── reviews/                  # Textos para análise
├── imagens/                  # Capturas de tela e resultados
├── text-analysis.py          # Script principal
├── .env                      # Chaves e endpoints (não versionado)
├── .gitignore                # Itens ignorados pelo Git
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este documento
```

---

## 🚀 Tecnologias Utilizadas

- **Python 3.8+**
- **Azure AI Text Analytics SDK** (`azure-ai-textanalytics`)
- **python-dotenv** para gerenciamento de variáveis sensíveis

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/gustarls/project-azure-language-text-analysis.git
cd project-azure-language-text-analysis
```

### 2. Crie um ambiente virtual

```bash
python -m venv labenv
labenv\Scripts\activate       # Windows
# ou
source labenv/bin/activate   # Linux/macOS
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` com:

```env
AI_SERVICE_ENDPOINT=https://SEU_ENDPOINT.cognitiveservices.azure.com/
AI_SERVICE_KEY=SUA_CHAVE_AQUI
```

### 5. Execute o script

```bash
python text-analysis.py
```

---

## 🧠 Funcionalidades

O sistema percorre os arquivos `.txt` da pasta `reviews/` e realiza:

✅ Detecção de idioma  
✅ Classificação de sentimento (positivo, negativo, misto)  
✅ Extração de frases-chave  
✅ Reconhecimento de entidades nomeadas (pessoas, lugares, organizações)  
✅ Entidades vinculadas com URLs da Wikipédia

---

## 🖼️ Exemplos Visuais

### 📄 review2.txt – Sentimento **Negativo**

![review2](./imagens/review2_sentiment-negative.png)

### 🏨 review4.txt – Sentimento **Misto**

![review4a](./imagens/review4_sentiment-mixed-part1.png)
![review4b](./imagens/review4_sentiment-mixed-part2.png)

### 🇫🇷 review5.txt – Francês com Entidades Vinculadas

![review5](./imagens/review5_sentiment-positive-linked-entities.png)

---

## 🎬 Demonstração do Projeto

[![Clique para assistir no Google Drive](https://img.shields.io/badge/🎥%20Ver%20Demonstração%20no%20Google%20Drive-blue?style=for-the-badge)](https://drive.google.com/file/d/1yGrWhjYhcH1xfa_waQ3OdMzs7_eKwNxN/view?usp=sharing)

> 📌 Demonstração completa da execução, análise de sentimentos e entidades no Azure.

---

## 🧪 Testes

Adicione novos arquivos `.txt` na pasta `reviews/` e execute novamente o script para novos resultados.

---

## 📌 Observações

- Os arquivos devem estar em UTF-8.
- É necessário ter uma instância do **Azure AI Language** configurada e ativa.

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👨‍💻 Autor

**Gustavo Raphael de Lima Santos**  
📍 São José dos Campos – SP, Brasil  
🔗 [LinkedIn](https://www.linkedin.com/in/gustavo-r-l-santos-bb9295100/)
