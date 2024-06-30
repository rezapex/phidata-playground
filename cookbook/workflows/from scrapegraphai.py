from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "model": "second-state/StarCoder2-15B-GGUF",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        "base_url": "http://192.168.4.55:1234/v1/chat/completions",  # set Ollama URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://192.168.4.55:1234",  # set Ollama URL
    },
    "verbose": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the projects with their descriptions",
    # also accepts a string with the already downloaded HTML code
    source="https://perinim.github.io/projects",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

