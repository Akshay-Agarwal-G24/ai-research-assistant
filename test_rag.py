from utils.rag import ask_question

""" question = "What is Docker?"

answer = ask_question(question)

print(answer) """

while True:

    question = input("Ask a question: ")

    if question.lower() == "exit":
        break

    response = ask_question(question)

    print("\nAnswer:\n")
    print(response["answer"])

    print("\nSources:")

    for source in response["sources"]:
        print(f"- {source}")