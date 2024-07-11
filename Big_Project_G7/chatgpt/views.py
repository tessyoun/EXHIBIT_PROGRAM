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
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from .models import ChatHistory, faq_aivle, faq_exhi
from .models import Booth_Info, Exhibition_info
from langchain.schema import Document
from langchain.memory import ConversationBufferMemory

from .function import *
import json

# Chroma 데이터베이스 초기화 >> FAQ DB 연결로 대체
# embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
# database = Chroma(persist_directory="./database", embedding_function=embeddings)

def index(request):
    return render(request, 'gpt/index.html')

#chatgpt 재시작: 아래 주석 두개 다 풀기, urls.py의 chat/링크 주석 풀기


# FAQ DB 연결
def getFAQdb():
    aivleQAdf=faq_aivle.objects.all() #에이블스쿨 FAQ
    exhiQAdf=faq_exhi.objects.all() #전시회장 FAQ
    boothINFO=Booth_Info.objects.all() # 부스 정보
    exhiINFO = Exhibition_info.objects.all() #전시 정보
    
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    database = Chroma(persist_directory="./database", embedding_function = embeddings )
    
    # 각 행의 데이터를 Document 객체로 변환 
    doc1 = [Document(page_content=QA.qalist)  for QA in aivleQAdf] # 에이블스쿨
    doc2 = [Document(page_content=QA.qalist)  for QA in exhiQAdf] # 전시장
    
    # 부스 정보 문서
    bdoc = [Document(page_content=f"""기업 "{booth.company_name}이"
            <에이블 {booth.exhibition_id}기 빅프로젝트 전시회>에 참여했으며,
            부스명은 "{booth.booth_name}"입니다.
            {booth.company_name} 기업의 부스 카테고리는 {booth.booth_category}에 해당하며,
            서비스를 제공하게 된 배경은 다음과 같습니다.
            {booth.background or ''}. 
            {booth.company_name}의 부스에 방문하면{booth.service or ''}의 기능을 체험할 수 있습니다.""") for booth in boothINFO]
    
    # 전시 정보
    edoc = [Document(page_content=f"""전시회 '{exhi.exhibition_name}'은 {exhi.start_date}부터 {exhi.end_date}까지
                     {chr(ord('A') + exhi.hall_id - 1)}홀에서 전시가 진행됩니다.""") for exhi in exhiINFO]
    
    # 데이터프레임에서 문서 추가
    docs=doc1+doc2+bdoc+edoc
    database.add_documents(docs)
    return database

database=getFAQdb()
print(database)




@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        query = data.get('question')
        # 대화 메모리 생성
        if 'chatlog' not in request.session:
            request.session['chatlog'] = []
            memory = ConversationBufferMemory(memory_key="chat_history", input_key="question", output_key="answer",
                                            return_messages=True)
            chatlog = []
        else:
            chatlog = request.session['chatlog']
            memory = memory_save(chatlog)
        
        # chatgpt API 및 lang chain을 사용을 위한 선언
        chat = ChatOpenAI(model="gpt-3.5-turbo")
        k = 10
        retriever = database.as_retriever(search_kwargs={"k": k})
        qa = ConversationalRetrievalChain.from_llm(llm=chat, retriever=retriever, memory=memory, return_source_documents=True, output_key="answer")

        # result = qa(query)
        result = qa({"question": query, "chat_history": chatlog})
        
        answer = result.get("answer", "Sorry, no answer was returned.")
        # 세션에 대화 로그 저장
        msg = {"question": query, "answer": answer}
        chatlog.append(msg)
        request.session['chatlog'] = chatlog
        
        # 질문, 응답 객체 생성
        ChatHistory.objects.create(question=query, answer=answer)
        
        # JSON 응답 반환
        return JsonResponse({'result': answer})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
