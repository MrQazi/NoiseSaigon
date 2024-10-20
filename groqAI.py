from groq import Groq 
from config import AI_KEY 
import json

def ParseWithAI(Query) :
    client = Groq(
        api_key=AI_KEY,
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{Query}",
            }
        ],
        model="llama3-70b-8192",
    )

    res = chat_completion.choices[0].message.content
    parts = res.split("```")
    return json.loads(parts[1])
    
