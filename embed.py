import os
from openai import OpenAI
import pandas as pd
import tiktoken

# models
embedding_model = "text-embedding-3-small"
embedding_encoding = "cl100k_base"
max_tokens = 8000  # the maximum for text-embedding-3-small is 8191

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

input_datapath = "data/fine_food_reviews_1k.csv"
df = pd.read_csv(input_datapath, index_col=0)
df = df.dropna()

df["combined"] = (
    "Product Id: " + df["ProductId"].str.strip() \
    + "; User Id: " + df["UserId"].str.strip() \
    + "; Rating: " + df["Score"].apply(str) \
    + "; Summary: " + df["Summary"].str.strip() \
    + "; Content: " + df["Text"].str.strip()
)

encoding = tiktoken.get_encoding(embedding_encoding)
df["num_tokens"] = df["combined"].apply(lambda x: len(encoding.encode(x)))
df = df[df["num_tokens"] <= max_tokens]

def get_embedding(text, model):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

df["embedding"] = df.combined.apply(lambda x: get_embedding(x, model=embedding_model))
df.to_csv("data/fine_food_reviews_with_embeddings_1k.csv")