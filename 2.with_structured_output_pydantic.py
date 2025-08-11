import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict,Annotated, Optional, Literal
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Warning --- Opensource Models doesn't support structured output with pydantic , but premium models like OpenAi , Anthropic etc does 
# So if you are using premium models then this code works , but if you are using opensource models then this code doesn't work and needs modification

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    
)

model = ChatHuggingFace(llm=llm)

# Field
# ---------------------------------------------------------------------------------------------------
# In Pydantic, Field is a special type that allows you to add additional information to a model's field, 
# such as a description, a default value, or validation rules.

# When you use Field to define a field in a Pydantic model, 
# you can pass additional arguments to customize the field's behavior. Here are some common uses of Field:

# Description: Add a human-readable description to the field.
# Default value: Set a default value for the field if no value is provided.
# Validation: Add validation rules to the field, such as minimum or maximum length, or a regular expression pattern.
# Alias: Define an alias for the field, which can be used to access the field by a different name.

# Field(...)
# ---------------------------------------------------------------------------------------------------
# In Pydantic, the ... in the Field definition is called an "ellipsis" or " ellipsis literal". 
# It's a special value that indicates that the field is required.
# When you use ... as the default value for a field, Pydantic will raise a ValidationError if the field is not provided when creating an instance of the model.
# In other words, ... is a shorthand way to indicate that the field is required and must be provided.

# class User(BaseModel):
#     name: str = Field(...)  # name is required
#     email: str = Field("example@example.com")  # email has a default value

# In this example, the name field is required and must be provided when creating a User instance. 
# If you try to create a User instance without providing a name, Pydantic will raise a ValidationError.
# On the other hand, the email field has a default value, so it's not required to be provided when creating a User instance.
# Using ... instead of None or another default value makes it clear that the field is required and helps Pydantic to enforce this constraint.
# ---------------------------------------------------------------------------------------------------

# schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)