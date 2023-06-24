# chatgpt-plugin-fastapi-langchain-chroma

An Example Plugin for ChatGPT, Utilizing FastAPI, LangChain and Chroma

[Blog Post](https://blog.experienced.dev/chatgpt-plugin-fastapi-langchain-chroma/?utm_source=github&utm_medium=repo&utm_content=010)

[Video Version](https://youtu.be/2TIj1Ger_qE)

## Install the dependencies
```bash
pip install -r requirements.txt
```

## Create .env file
```bash
python -c "import shutil; shutil.copy('.env.example', '.env')"
```
## Set OPENAI_API_KEY in `.env`

## Create embeddings for the data and persist Chroma
```bash
python persist_chroma.py
```
## Start
```bash
uvicorn main:app --log-level debug --reload
```
