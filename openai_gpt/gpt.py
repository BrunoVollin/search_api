import openai
import matplotlib.pyplot as plt
import io
import os
import base64
import json 

class Bot:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate(self, question: str, document_data: str):
        prompt = f"{question} {document_data}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI q/a assistant. You will receive a question and then data extracted from a document. Based on the data, you will formulate the best answer. Answer in the same language as the question. . Just give the answer, no need to say based on the data "},
                {"role": "user", "content": prompt},
            ]
        )
        content = response['choices'][0]['message']['content']
        return content
    
    def generate_chart(self, question: str, document_data: str):
        answer = self.generate(question, document_data)

        x = [1, 2, 3, 4, 5]
        y = [10, 20, 25, 30, 35]

        plt.plot(x, y)
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.title('Exemplo de Gráfico')

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)


        chart_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        
        response = {
            "answer" : answer,
            "chart_base64": chart_base64
        }

        return response
