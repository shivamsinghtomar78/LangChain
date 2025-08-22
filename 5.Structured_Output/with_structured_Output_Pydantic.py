from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, TypedDict, Annotated, Literal, List
from pydantic import BaseModel, EmailStr, Field
 

load_dotenv()

model= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2
)

#schema 
class Review(BaseModel):  
    key_themes: List[str] = Field(description="write down all the Key themes or topics discussed in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="Return sentiment of the review ,either negative or positive or neutral")
    pros: Optional[List[str]] = Field(description="write down all the pros of the product")
    cons: Optional[List[str]] = Field(description="write down all the cons of the product")
    name: Optional[str] = Field(description="Name of the person who wrote the review")
    
    
structured_model=model.with_structured_output(Review) 
result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Shivam Singh
""")
print(result)
if result is not None:
    print(result.key_themes)
    print(result.name)
else:
    print("Result is None - structured output failed")