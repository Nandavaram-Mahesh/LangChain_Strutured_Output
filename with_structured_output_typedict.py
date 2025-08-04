import os
from dotenv import load_dotenv
from typing import TypedDict
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    
)

model = ChatHuggingFace(llm=llm)


class Review(TypedDict):
    summary: str
    sentiment: str
    
structured_model = model.with_structured_output(Review)

response = structured_model.invoke("The movie was great , I loved it")
print(response)