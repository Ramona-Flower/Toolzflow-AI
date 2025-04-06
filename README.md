# Toolzflow-AI in Python

This Python script is a client for interacting with the [ToolzFlow Best AI Code Generator](https://best-ai-code-generator.toolzflow.app/) API. It sends a prompt to the API and receives a code snippet as a JSON response.

## Features

- Sends a user prompt to a GPT-4o-based AI model.
- Supports different GPT-4o model variants (`gpt-4o`, `gpt-4o-turbo`, `gpt-4o-mini`).

## Requirements

- Python 3.7+
- `requests` library

Install dependencies with:

```bash
pip install requests
or
pip install -r requirements.txt
```
```bash
python script.py
```
## Example:
```bash
Enter your prompt: Create a Python function to sort a list of dictionaries by a key
```

The generated code will be printed to the console.

```python

ai_response = send_request("Create a Python script that fetches weather data", model="gpt-4o")
print(ai_response)

```
## Available Models
- `gpt-4o-mini` – Basic model
- `gpt-4o` – More powerful, not exposed in UI but works via API
- `gpt-4o-turbo` – Turbocharged variant of GPT-4o

Note: Even if gpt-4o or gpt-4o-turbo are not selectable on the website UI, you can still use them in the API request.

## License
This script is provided as-is under the Apache-2.0 license.
