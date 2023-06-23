from pydantic import BaseSettings


class Settings(BaseSettings):
    schema_version: str = "v1"
    name_for_model: str = "quote"
    name_for_human: str = "Quote"
    description_for_model: str = "This plugin provides quotes to enrich your text. It can be used whenever a user requests a quote."
    description_for_human: str = "Simply request a quote whenever you need one."
    auth: dict[str, str] = {"type": "none"}
    api: dict[str, str] = {
        "type": "openapi",
        "is_user_authenticated": "false",
        "url": "$base_url/.well-known/openapi.yaml",
    }
    logo_url: str = "$base_url/logo.png"
    contact_email: str = "contact@localhost"
    legal_info_url: str = "$base_url"

    allow_origins: list[str] = ["http://localhost:8000", "https://chat.openai.com"]
    openai_api_key: str | None = None
    persist_directory: str = "data"
    include_well_known_in_schema: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
