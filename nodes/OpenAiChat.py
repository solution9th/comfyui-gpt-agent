from ..services.openAi import OpenAIAgent

class OpenAiChat:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "Agent_OpenAi": ("Agent_OpenAi", ),
                "Text": ("STRING", {"default": ""}),
            }
        }
        return inputs
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "execute"
    CATEGORY = "Agent"
    def execute(self, Agent_OpenAi,Text):
        agent_object = Agent_OpenAi['Agent_OpenAi']
        last_content = agent_object.chat(Text)
        return {"ui": {"text": [last_content,]},"result": (last_content,),}

