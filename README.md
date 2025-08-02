# Azure Text Analysis - Análise de Texto com Azure AI

Este projeto demonstra como usar o serviço **Azure AI Language** para analisar arquivos de texto contendo avaliações de hotéis. A aplicação realiza detecção de idioma, análise de sentimento, extração de frases-chave, reconhecimento de entidades e entidades vinculadas utilizando o SDK oficial da Azure em Python.

## 📂 Estrutura do Projeto

```
azure-language-text-analysis/
├── reviews/                # Pasta contendo arquivos .txt com avaliações
├── text-analysis.py        # Script principal para análise de texto
├── .env                    # Variáveis de ambiente com endpoint e chave da Azure
├── .gitignore              # Arquivos e pastas ignorados pelo Git
├── requirements.txt        # Bibliotecas necessárias
└── README.md               # Este arquivo
```

## 🚀 Tecnologias Utilizadas

- Python 3.8+
- Azure AI Text Analytics SDK (`azure-ai-textanalytics`)
- Dotenv para gerenciamento de variáveis de ambiente

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/azure-language-text-analysis.git
cd azure-language-text-analysis
```

### 2. Crie o ambiente virtual

```bash
python -m venv labenv
source labenv/Scripts/activate  # Windows
# ou
source labenv/bin/activate      # Linux/macOS
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure suas variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
AI_SERVICE_ENDPOINT=https://SEU_ENDPOINT.cognitiveservices.azure.com/
AI_SERVICE_KEY=SUA_CHAVE_AQUI
```

Substitua pelos dados da sua instância do Azure Language Service.

### 5. Execute o script

```bash
python text-analysis.py
```

## 📈 Funcionalidades

Para cada arquivo `.txt` dentro da pasta `reviews/`, o script:

- Detecta o **idioma** do texto
- Realiza a **análise de sentimento**
- Extrai as **frases-chave**
- Reconhece **entidades nomeadas** (pessoas, locais, organizações)
- Reconhece **entidades vinculadas** (com links da Wikipédia)

### Exemplo de Saída

```text
-------------
review1.txt

Good Hotel and staff
...

Language: English

Sentiment: positive

Key Phrases:
    - good service
    - Westminster Abbey
    ...

Entities:
    - Hotel (Location)
    - Westminster Abbey (Location)
    ...

Linked Entities:
    - Westminster Abbey: https://en.wikipedia.org/wiki/Westminster_Abbey
```

### 🎬 Demonstração do Projeto

[![Clique para assistir no Google Drive](https://img.shields.io/badge/🎥%20Ver%20Demonstração%20no%20Google%20Drive-blue?style=for-the-badge)](https://drive.google.com/file/d/1yGrWhjYhcH1xfa_waQ3OdMzs7_eKwNxN/view?usp=sharing)

> 📌 Este vídeo mostra a execução completa da aplicação e os resultados de análise de sentimentos, entidades, idioma e frases-chave diretamente do Azure.

## 📌 Notas

- Os arquivos de texto devem estar codificados em UTF-8.
- É necessário possuir uma conta na Azure com o serviço de **Language Resource** criado e configurado.

## 🧪 Testes

Você pode incluir mais arquivos `.txt` na pasta `reviews/` para testar com outros textos.

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
