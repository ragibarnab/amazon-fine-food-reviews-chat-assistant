import chromadb
from openai import OpenAI
import os
import tiktoken

try:
    chroma_client = chromadb.PersistentClient("data/chroma")
    collection = chroma_client.get_collection(name="fine_food_reviews_1k")
except ValueError:
    print("No collection to retrieve from!")
    exit()

# models
embedding_model = "text-embedding-3-small"
embedding_encoding = "cl100k_base"
gpt_model = "gpt-3.5-turbo"
token_budget = 4096 - 500

openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

print("(Optional) Enter product id: ")
product_id = input().strip()
print("(Optional) Enter user id: ")
user_id = input().strip()
print("Enter your prompt:")
query_text = input().strip()

metafields = {}
if product_id:  metafields["ProductId"] = product_id
if user_id: metafields["UserId"] = user_id

query_embedding = openai_client.embeddings.create(input = [query_text], model=embedding_model).data[0].embedding
results = collection.query(query_embeddings=[query_embedding], where=metafields if metafields else None)
reviews = collection.get(ids=results["ids"][0], include=["documents"])["documents"]

def num_tokens(text, model):
    """Return the number of tokens in a string."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

introduction = "Use the following retrieved reviews from the dataset to answer the subsequent prompt."
prompt = f"\n\nPrompt: {query_text}"

message = introduction
for i, review in enumerate(reviews):
    next_review = f'\n\nReview #{i+1}:\n"""\n{review}\n"""'
    if (num_tokens(message + next_review + prompt, model=gpt_model) > token_budget):
        break
    else:
        message += next_review
message += prompt

messages = [
    {"role": "system", "content": "You answer questions about the Amazon Fine Food Reviews dataset, which consists of reviews of fine foods from Amazon."},
    {"role": "user", "content": message},
]

response = openai_client.chat.completions.create(
    model=gpt_model,
    messages=messages,
    temperature=0
)
print("\nMessage sent to assistant:\n# # # # # # # # # #\n")
print(message)
print("\n# # # # # # # # # #\n")
response_message = response.choices[0].message.content
print(f"Assistant response ({gpt_model}): \n{response_message}")
