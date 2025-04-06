import requests
import json

url = "https://best-ai-code-generator.toolzflow.app/api/chat/public"

def send_request(input, model="gpt-4o-turbo"):
    payload = {
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "code_response",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string"
                        }
                    },
                    "required": ["code"],
                    "additionalProperties": False
                }
            }
        },
        "chatSettings": {
            "model": f"{model}",
            "temperature": 0.3,
            "contextLength": 16385,
            "includeProfileContext": False,
            "includeWorkspaceInstructions": False,
            "embeddingsProvider": "openai"
        },
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in generating code snippets based on user input. Your task is to create clear and concise code."
            },
            {
                "role": "user",
                "content": f"{input}. Provide only the response without explanations."
            }
        ]
    }

    request_headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-length": "698",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://best-ai-code-generator.toolzflow.app",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://best-ai-code-generator.toolzflow.app/",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-fetch-storage-access": "active",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }
    response = requests.post(url, headers=request_headers, data=json.dumps(payload))
    
    return response.json()["code"]

# Available models: 
# GPT-4o-mini <- Basic 
# GPT-4o <- Forbidden on site but allowed in request, 
# GPT-4o-turbo <- Forbidden on site but allowed in request, 
if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    ai_response = send_request(user_input, model="GPT-4o") # Change model here
    print(ai_response)
