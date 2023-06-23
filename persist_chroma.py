import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from chatgpt_plugin_fastapi_langchain_chroma.config import settings

df = pd.read_csv("data.csv")
loader = DataFrameLoader(df, page_content_column="quote")
documents = loader.load()

embedding = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)

vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    persist_directory=settings.persist_directory,
)
vectordb.persist()
