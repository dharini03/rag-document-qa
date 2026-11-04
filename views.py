
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from transformers import pipeline
from docx import Document
import fitz
import numpy as np

from .models import UploadedFile, TextChunk, Embedding
from .serializers import FileUploadSerializer
from .vector_store import VECTOR_DB


qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")


def extract_text(file_path):
    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        return "\n".join([page.get_text() for page in doc])
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""



def home_view(request):
    return render(request, "home.html")



def upload_view(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("pdf_file")
        if uploaded_file:
            file_instance = UploadedFile.objects.create(file=uploaded_file)
            text = extract_text(file_instance.file.path)

            if not text.strip():
                return render(request, "upload.html", {"message": "No text found in file."})

            chunks = [text[i:i + 500] for i in range(0, len(text), 500)]

            for idx, chunk in enumerate(chunks):
                chunk_obj = TextChunk.objects.create(file=file_instance, chunk_text=chunk, chunk_index=idx)
                embedding = VECTOR_DB.model.encode([chunk])[0]
                Embedding.objects.create(chunk=chunk_obj, vector=np.array(embedding, dtype=np.float32).tobytes())

            VECTOR_DB.add_texts(chunks)
            return render(request, "upload.html", {"message": "File uploaded and processed."})

    return render(request, "upload.html")



def chat_view(request):
    answer = None

    if request.method == "POST":
        question = request.POST.get("question", "")
        if question:
            top_chunks = VECTOR_DB.search(question, top_k=3)
            context = "\n".join(top_chunks)
            prompt = f"Answer the question based on the context.\n\nContext: {context}\nQuestion: {question}"
            try:
                outputs = qa_pipeline(prompt, max_new_tokens=100, do_sample=False)
                if outputs and isinstance(outputs[0], dict):
                    answer = outputs[0].get("generated_text", "").strip()
                else:
                    answer = "Model returned no output."
                if not answer:
                    answer = "Sorry, no answer could be generated."
            except Exception as e:
                answer = f"Error: {str(e)}"

    return render(request, "chat.html", {"answer": answer})
