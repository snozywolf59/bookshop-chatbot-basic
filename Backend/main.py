from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json


from utils import ask_chatbot, clean_response, handle_intent


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI 🚀"}

@app.get("/chat")
def chat(user_input: str):    
    try:
        result = clean_response(ask_chatbot("gemma3:1b", user_input))
        if not result:
            return {"err": "Không nhận được phản hồi từ chatbot"}
            
        try:
            result = json.loads(result)
        except json.JSONDecodeError as je:
            print(f"Invalid JSON response: {result}")
            return {"err": "Phản hồi không hợp lệ từ chatbot"}
            
        return handle_intent(result)
    except Exception as e:
        print(f"Error: {e}; {e.__traceback__.tb_lineno}")
        return {"err": "Lỗi khi xử lý yêu cầu"}


