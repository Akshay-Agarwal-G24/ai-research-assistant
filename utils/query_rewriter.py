from utils.llm import ask_llm

def rewrite_question(history, question):
    history_str = ''

    for hist in history:
        if hist["role"] == 'user':
            history_str += f'User: {hist["content"]}\n'
        else:
            history_str += f'Assistant: {hist["content"]}\n'

    prompt = f"""
You are a query rewriting assistant.

Your task is to rewrite follow-up questions into standalone questions.

Use the conversation history to resolve references such as:
- it
- this
- that
- they
- them

Rules:
1. Return ONLY the rewritten question.
2. Do not explain your reasoning.
3. Do not answer the question.
4. If the question is already standalone, return it unchanged.

Examples:

History:
User: What is MCP?

Question:
Why is it useful?

Output:
Why is Model Context Protocol useful?

History:
User: What is Docker?

Question:
What are its advantages?

Output:
What are Docker's advantages?


Conversation History:
{history_str}

Question:
{question}
"""
    try:
        rewritten_question = ask_llm(prompt)
    except Exception:
        return {
        "success": False,
        "question": None
    }    

    rewritten_question_success = True

    if not rewritten_question or not rewritten_question.strip():
        rewritten_question_success = False
        rewritten_question = None

    return {
        "success": rewritten_question_success,
        "question": rewritten_question
    }

