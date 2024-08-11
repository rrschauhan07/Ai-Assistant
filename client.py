# import os
# from openai import OpenAI


# # client = OpenAI()
# # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.getenv('OPENAIAPI_KEY'))

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named alex, skilled in general tasks like similar to assistants like Alexa and Gemini assistant."},
#     {"role": "user", "content": "What is coding"}
#   ]
# )

# print(completion.choices[0].message.content)