from utils.retrieve import collection

results = collection.get(
    limit=3,
    include=["documents", "metadatas"]
)

for i in range(len(results["ids"])):

    print("\n" + "=" * 50)

    print("ID:", results["ids"][i])

    print("Metadata:")
    print(results["metadatas"][i])

    print("\nDocument Preview:")
    print(results["documents"][i][:200])