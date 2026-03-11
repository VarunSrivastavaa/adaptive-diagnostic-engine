from openai import OpenAI

client = OpenAI()

def generate_plan(topics):

    prompt = f"""
    Create a 3 step GRE study plan for weak topics: {topics}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content