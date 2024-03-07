from .llama2_chat import BedrockMetaLLama2ChatAdapter
from ..registry import registry


class BedrockMistralAdapter(BedrockMetaLLama2ChatAdapter): ...


# Register the adapter
registry.register(
    r"^bedrock.mistral.mi.*",
    BedrockMistralAdapter,
)
