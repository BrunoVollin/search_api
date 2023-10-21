import openai

class Bot:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate(self, question: str, document_data: str):
        prompt = f"{question} {document_data}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI q/a assistant. You will receive a question and then data extracted from a document. Based on the data, you will formulate the best answer. Answer in the same language as the question. . Just give the answer, no need to say based on the data. ANALYSE IF THE DATA MATCHES THE QUESTION. Answer ONLY if it matches. If the data is nonsense or doesnt answer the question. YOU WILL ONLY SAY THE WORD: FALSO, SO IN THATR CASE ONLY GIVE FALSO AS THE ANSWER "},
                {"role": "user", "content": prompt},
            ]
        )
        content = response['choices'][0]['message']['content']
        return content
