from ..services.openAi import OpenAIAgent

class OpenAiConfig:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "model": ("STRING", {"default":""}),
                "api_key": ("STRING", {"default": ""}),
                "api_type":  (["openai","caihulu","ollama"], {}),
                "api_base": ("STRING", {"default": ""}),
                "api_version": ("STRING", {"default": ""}),
                "api_proxy": ("STRING", {"default": ""}),
            }
        }
        return inputs
    RETURN_TYPES = ("Agent_OpenAi",)
    RETURN_NAMES = ("Agent_OpenAi",)
    FUNCTION = "execute"
    CATEGORY = "Agent"
    def execute(self, model, api_key, api_type, api_base,api_version,api_proxy):
        openai = OpenAIAgent(api_key, model, api_type, api_base,api_version,api_proxy)
        return ({"Agent_OpenAi": openai},)