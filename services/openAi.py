from openai import OpenAI ,AzureOpenAI,DefaultHttpxClient
import httpx


class OpenAIAgent:
    def __init__(self, api_key="", model="gpt-3.5-turbo", api_type="", api_base=None,api_version="",api_proxy = ""):
        if api_type == "azure":
            self.client = AzureOpenAI(
                api_version=api_version,
                azure_endpoint=api_base,
            )
        else:
            if api_proxy != "":
                self.client = OpenAI(
                    api_key=api_key,
                    base_url=api_base, 
                    http_client=DefaultHttpxClient(
                        proxy=api_proxy,
                        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
                    )
                )
            else:
                self.client = OpenAI(
                    api_key=api_key,
                    base_url=api_base, 
                )
            
        self.type = api_type
        self.model = model
       

 

    def chat(self, user_message):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        return completion.choices[0].message.content
