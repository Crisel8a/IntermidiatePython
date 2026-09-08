sample_articles = [
    {
        "title": "python logra nuevo exito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnologia",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "finance"},
        "description": "Analisis completo",
        "category": "Economia",
    },
    {
        "title": "Nueva tecnologia",
        "source": {"name": "TechNews"},
        "description": "Innovacion",
        "category": "Tecnologia",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "politica actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "politica",
    },
    {
        "title": "ciencia avanzada",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_sources_traditional(articles):
    """Extraer las fuentes sin repetir elementos"""
    sources = set()
    for article in articles:
        sources.add(article["source"]["name"])
    return sources


def extract_sources(articles):
    """Extraer las fuentes sin repetir elementos"""
    return {article["source"]["name"] for article in articles}


print(extract_sources_traditional(sample_articles))
print(extract_sources(sample_articles))
print(type(extract_sources_traditional(sample_articles)))
print(type(extract_sources(sample_articles)))
