from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import chromadb
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from groq import Groq
from hispter_chatbot_project.settings import GROQ_API_KEY

# Path to the folder where ChromaDB is stored
persist_directory = "chromadb"
# Load the ChromaDB instance
db= Chroma(persist_directory="chromadb\\", embedding_function=HuggingFaceEmbeddings())

# retriever
retriever = db.as_retriever()
# client groq
client = Groq(
    api_key= GROQ_API_KEY
)

def grok_api_call(user_question):
    
    try:

        query_results = retriever.invoke(user_question)
        
        retrieved_docs= [str(doc) for doc in query_results]

        # Prepare the messages
        messages = [
            {
                "role": "system",
                "content": f"""You are a helpful assistant designed to respond to users' questions in a conversational tone. 
                Your task is to provide precise, step-by-step instructions and relevant information based on the user's query, 
                ensuring your answers are practical and easy to understand. Do not mention any limitations or lack of information in your response. 
                If additional context is necessary, assume a user-friendly and supportive tone while maintaining clarity."""
            },
            {
                "role": "assistant",
                "content": f"Here are the documents for context:\n\n" + "\n\n".join(retrieved_docs)
            },
            {
                "role": "user",
                "content": user_question
            }
        ]

        # Create chat completion
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",
        )

        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return str(e)

# API View to handle chatbot interactions
class ChatbotView(APIView):

    def post(self, request):
        user_question = request.data.get("question")

        if not user_question:
            return Response(
                {"error": "Question is required.", "status": False, "status_code": status.HTTP_400_BAD_REQUEST},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # chatbot response
        bot_response = self.generate_bot_response(user_question)
      

        #  Return the response
        return Response(
            {"message": "Chat processed successfully.", "data": bot_response, "status": True, "status_code": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )
    
    # chat response function
    def generate_bot_response(self, question):

        chat_result= grok_api_call(question)

        return chat_result

