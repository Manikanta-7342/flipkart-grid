from langchain.tools import BaseTool
import io,requests
from PIL import Image
from scrapper.link_getter import provideLinks


class ImageGeneratorTool(BaseTool):
    name = "Image genrator"
    description = "It will return a generated image by considering latest trends."

    def query(self,payload):
        API_URL = "https://api-inference.huggingface.co/models/MohamedRashad/diffusion_fashion"
        response = requests.post(API_URL, json=payload)
        return response.content
    def _run(self,user_question ):
        image_bytes = self.query({
            "inputs": user_question,  # Replace with your fashion-related text input
        })

        # Open and display the generated image
        generated_image = Image.open(io.BytesIO(image_bytes))

        return generated_image

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")


class WebSrappingTool(BaseTool):
    name = "Web Scrapper"
    description = "Use this tool when user asks to provide trendy images. " \
                  "It will return path to a list of all image urls, names and their reviews. Each element in the list should be given to llm " \
                  "and llm gets trained by embedings."

    def _run(self):
        provideLinks()
        return "scrapper/data"

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")