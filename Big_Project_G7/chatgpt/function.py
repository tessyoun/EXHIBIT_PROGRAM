from langchain.memory import ConversationBufferMemory

def memory_save(message):
    memory = ConversationBufferMemory(memory_key='chat_history', input_key="question", output_key="answer", return_messages=True)
    for msg in message:
        memory.save_context({"question": msg['question']},
                        {"answer": msg['answer']})
    return memory