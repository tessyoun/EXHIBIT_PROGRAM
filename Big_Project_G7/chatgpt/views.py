# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from langchain.chat_models import ChatOpenAI
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
# from langchain.chains import RetrievalQA
# from .models import ChatHistory

# import json

# # Chroma 데이터베이스 초기화
# embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
# database = Chroma(persist_directory="./database", embedding_function=embeddings)

# def index(request):
#     return render(request, 'gpt/index.html')

# @csrf_exempt
# def chat(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         query = data.get('question')

#         # chatgpt API 및 lang chain을 사용을 위한 선언
#         chat = ChatOpenAI(model="gpt-3.5-turbo")
#         k = 3
#         retriever = database.as_retriever(search_kwargs={"k": k})
#         qa = RetrievalQA.from_llm(llm=chat, retriever=retriever, return_source_documents=True)

#         result = qa(query)
#         # 질문, 응답 객체 생성
#         ChatHistory.objects.create(question=query, answer=result["answer"])
#         # JSON 응답 반환
#         return JsonResponse({'result': result['result']})

#     return JsonResponse({'error': 'Invalid request method'}, status=400)


from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from .models import ChatHistory

import json

# Chroma 데이터베이스 초기화
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
database = Chroma(persist_directory="./database", embedding_function=embeddings)

def index(request):
    return render(request, 'gpt/index.html')

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        query = data.get('question')

        # chatgpt API 및 lang chain을 사용을 위한 선언
        chat = ChatOpenAI(model="gpt-3.5-turbo")
        k = 3
        retriever = database.as_retriever(search_kwargs={"k": k})
        qa = RetrievalQA.from_llm(llm=chat, retriever=retriever, return_source_documents=True)

        result = qa(query)
        
        # result에 "result" 대신 "answer" 키 사용
        answer = result.get("result", "Sorry, no answer was returned.")
        
        # 질문, 응답 객체 생성
        ChatHistory.objects.create(question=query, answer=answer)
        
        # JSON 응답 반환
        return JsonResponse({'result': answer})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

