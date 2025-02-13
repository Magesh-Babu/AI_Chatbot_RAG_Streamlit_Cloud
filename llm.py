import os
from llama_index.llms.azure_inference import AzureAICompletionsModel

AZURE_META_API = os.getenv("AZURE_META_API")
AZURE_META_ENDPOINT = os.getenv("AZURE_META_ENDPOINT")

def initialize_llm():
    """Initialize and return the Azure AI completions model."""
    return AzureAICompletionsModel(
        endpoint = AZURE_META_ENDPOINT,
        credential = AZURE_META_API
    )

