import os
from dotenv import load_dotenv
from typing import TypedDict,Annotated, Optional, Literal
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    
)

model = ChatHuggingFace(llm=llm)

# ---------------------------------------------------------------------------------------
# Annotated is a type hint from the typing module in Python, 
# introduced in Python 3.9. It allows you to add arbitrary metadata to a type hint,
# while still maintaining the original type information.
# In other words, Annotated allows you to attach additional information to a type hint, 
# such as a description, a validation rule, or a transformation function, without changing the underlying type.

# General Syntax
# MyType = Annotated[OriginalType, Metadata]

# ---------------------------------------------------------------------------------------

# Literal is a type hint from the typing module in Python, 
# which allows you to specify a type that can only take on a specific set of literal values.
# In other words, Literal is used to define a type that is restricted to a specific set of values, 
# such as a set of strings, integers, or booleans.

# General Syntax
# MyType = Literal[Value1, Value2, ..., ValueN]

# ---------------------------------------------------------------------------------------
# Optional is a type hint from the typing module in Python, 
# which indicates that a variable or function parameter can be either a specific type or None.
# In other words, Optional is used to define a type that can take on either a specific value or no value at all (None).


class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    
structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nandavaram Mahesh
""")
print(response)
# {'name': 'Nandavaram Mahesh', 
# 'pros': ['Powerful Snapdragon 8 Gen 3 processor for fast performance in gaming, multitasking, and photo editing', 'Long-lasting 5000mAh battery with heavy use', '45W fast charging', 'S-Pen integration for note-taking and sketches', 'Stunning 200MP camera with excellent night mode', 'Effective zoom up to 100x for distant objects'], 
# 'sentiment': 'pos', 
# 'summary': "The Samsung Galaxy S24 Ultra is a high-performance flagship with an exceptional camera, long battery life, and useful S-Pen, though it's bulky, has software bloat, and carries a premium price tag."
# }
# print(response['name'])