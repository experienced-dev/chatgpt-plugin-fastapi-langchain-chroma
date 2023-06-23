from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
from langchain.vectorstores import Chroma

from langchain.embeddings import OpenAIEmbeddings

from chatgpt_plugin_fastapi_langchain_chroma.config import settings

embedding_function = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)

vectordb = Chroma(
    persist_directory=settings.persist_directory, embedding_function=embedding_function
)

quote = APIRouter(tags=["quote"])


class Quote(BaseModel):
    text: str = Field(
        description="The actual quote as a string. It can include any character.",
    )
    author: str = Field(
        description="The person or entity who originally spoke or wrote the quote.",
    )
    language: str = Field(
        description="The language the quote was written in.",
    )


@quote.get("/quote", response_model=Quote)
async def get_quote(
    q: str = Query(
        description="The search query to find quotes using similarity search.",
    ),
):
    docs = vectordb.similarity_search(q)
    doc = docs[0]
    return Quote(
        text=doc.page_content,
        author=doc.metadata["author"],
        language=doc.metadata["language"],
    )
