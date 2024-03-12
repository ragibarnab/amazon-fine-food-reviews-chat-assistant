import chromadb
import pandas as pd

chroma_client = chromadb.PersistentClient("data/chroma")

try:
    chroma_client.delete_collection("fine_food_reviews_1k")
except ValueError:
    pass

collection = chroma_client.create_collection(name="fine_food_reviews_1k", metadata={"hnsw:space": "cosine"})

input_datapath = "data/fine_food_reviews_with_embeddings_1k.csv"
df = pd.read_csv(input_datapath, index_col=0)

# parse embeddings
embeddings = df["embedding"].tolist()
to_float = lambda embedding_str : [float(i) for i in embedding_str[1:-1].split(", ")]
embeddings = list(map(to_float, embeddings))

# parse metadata
product_ids = df["ProductId"].tolist()
user_ids = df["UserId"].tolist()
metadata = [{"UserId": user_id, "ProductId": product_id} for user_id, product_id in zip(user_ids, product_ids)]

ids = list(map(str, range(len(embeddings))))
documents = df["combined"].tolist()

collection.add(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadata)

