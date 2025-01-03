from .nodes.OpenAiConfig import OpenAiConfig
from .nodes.OpenAiChat import OpenAiChat


NODE_CLASS_MAPPINGS = {
    "OpenAiConfig":OpenAiConfig,
    "OpenAiChat":OpenAiChat,
}
NODE_DISPLAY_NAMES_MAPPINGS = {
    "OpenAiConfig":"OpenAiConfig",
    "OpenAiChat":"OpenAiChat",
}
WEB_DIRECTORY = "./js"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAMES_MAPPINGS','WEB_DIRECTORY']
