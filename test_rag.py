from utils.rag import ask_question

""" question = "What is Docker?"

answer = ask_question(question)

print(answer) """

question = input("Ask a question: ")

response = ask_question(question)

print("\nAnswer:\n")
print(response["answer"])

print("\nSources:")

for source in response["sources"]:
    print(f"- {source}")