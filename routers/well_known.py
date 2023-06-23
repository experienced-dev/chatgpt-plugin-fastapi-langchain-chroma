import yaml
import json
from string import Template
from fastapi import APIRouter, Request, Response

from chatgpt_plugin_fastapi_langchain_chroma.config import settings

well_known = APIRouter(
    prefix="/.well-known",
    tags=["well-known"],
    include_in_schema=settings.include_well_known_in_schema,
)


def get_base_url(request: Request):
    host = request.headers.get("X-Forwarded-Host") or request.headers.get("Host")
    scheme = request.headers.get("X-Forwarded-Proto") or request.url.scheme
    return f"{scheme}://{host}"


def get_ai_plugin(base_url: str):
    tpl = {
        "schema_version": settings.schema_version,
        "name_for_model": settings.name_for_model,
        "name_for_human": settings.name_for_human,
        "description_for_model": settings.description_for_model,
        "description_for_human": settings.description_for_human,
        "auth": settings.auth,
        "api": settings.api,
        "logo_url": settings.logo_url,
        "contact_email": settings.contact_email,
        "legal_info_url": settings.legal_info_url,
    }
    return json.loads(Template(json.dumps(tpl)).substitute(base_url=base_url))


@well_known.get("/ai-plugin.json")
async def get_ai_plugin_json(request: Request):
    base_url = get_base_url(request)
    return get_ai_plugin(base_url)


@well_known.get("/openapi.yaml")
async def get_openapi_yaml(request: Request):
    openapi = request.app.openapi()
    base_url = get_base_url(request)
    openapi["servers"] = [{"url": base_url}]
    ai_plugin = get_ai_plugin(base_url)
    openapi["info"]["title"] = ai_plugin["name_for_human"]
    openapi["info"]["description"] = ai_plugin["description_for_human"]
    return Response(
        content=yaml.dump(openapi),
        media_type="text/vnd.yaml",
    )
