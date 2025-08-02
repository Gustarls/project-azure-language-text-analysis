from dotenv import load_dotenv
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def main():
    try:
        # Carregar configurações do .env
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Criar cliente Azure
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

        # Caminho absoluto da pasta 'reviews'
        script_dir = os.path.dirname(os.path.abspath(__file__))
        reviews_folder = os.path.join(script_dir, 'reviews')

        # Feedback imediato no terminal
        print("\nIniciando análise de textos... Aguarde...\n", flush=True)
        
        # Analisar cada arquivo da pasta
        for file_name in os.listdir(reviews_folder):
            print(f'\n-------------\n{file_name}')
            with open(os.path.join(reviews_folder, file_name), encoding='utf8') as f:
                text = f.read()
            print(f'\n{text}')

            documents = [text]

            # Detectar idioma
            language = ai_client.detect_language(documents=documents)[0]
            print(f'\nLanguage: {language.primary_language.name}')

            # Análise de sentimento
            sentiment = ai_client.analyze_sentiment(documents=documents)[0]
            print(f'\nSentiment: {sentiment.sentiment}')

            # Extração de frases-chave
            key_phrases = ai_client.extract_key_phrases(documents=documents)[0].key_phrases
            if key_phrases:
                print('\nKey Phrases:')
                for phrase in key_phrases:
                    print(f'\t- {phrase}')

            # Reconhecimento de entidades
            entities = ai_client.recognize_entities(documents=documents)[0].entities
            if entities:
                print('\nEntities:')
                for entity in entities:
                    print(f'\t- {entity.text} ({entity.category})')

            # Entidades com links (ex: Wikipédia)
            linked_entities = ai_client.recognize_linked_entities(documents=documents)[0].entities
            if linked_entities:
                print('\nLinked Entities:')
                for linked_entity in linked_entities:
                    print(f'\t- {linked_entity.name}: {linked_entity.url}')

    except Exception as err:
        print(f"\n[ERROR] {err}")

if __name__ == "__main__":
    main()
