import os
from openai import OpenAI

# ✅ Create client with API key from environment
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_story(prompt: str) -> str:
    """
    Generate a story using OpenAI Chat API (modern client)
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Modern chat model
        messages=[
            {"role": "system", "content": "You are a creative story writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    
    story = response.choices[0].message.content.strip()
    return story

# ✅ Example usage
if __name__ == "__main__":
    user_prompt = input("Enter a story idea: ")
    story_output = generate_story(user_prompt)
    print("\nGenerated Story:\n")
    print(story_output)
