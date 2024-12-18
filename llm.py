from llama_index.llms.azure_inference import AzureAICompletionsModel

def initialize_llm():
    """Initialize and return the Azure AI completions model."""
    return AzureAICompletionsModel(
        endpoint = "https://Meta-Llama-3-8B-Instruct-ulxuk.swedencentral.models.ai.azure.com",
        credential = " "
    )
