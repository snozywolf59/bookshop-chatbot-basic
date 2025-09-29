# Bookshop Chatbot Basic

Một chatbot cơ bản cho cửa hàng sách — hỗ trợ người dùng tìm kiếm, đặt câu hỏi và tương tác đơn giản.

## 📦 Mô tả

Project gồm 2 phần chính:

- **Backend**: xử lý logic chatbot, API và dữ liệu sách.  
- **Frontend**: giao diện chat để người dùng tương tác.

Mục tiêu là xây dựng hệ thống đơn giản, dễ mở rộng với các tính năng nâng cao như NLP hoặc quản lý đơn hàng.

## 🧱 Cấu trúc thư mục
bookshop-chatbot-basic/
├── Backend/ # Mã nguồn server (FastAPI)
├── Frontend/ # Mã nguồn giao diện chat (Vue)
└── README.md

## Cài đặt & chạy

### Yêu cầu

- Python 3.x (nếu backend dùng Python)
- Ollama Gemma3:1b

### Backend

```bash
cd Backend
# Python
python3 -m venv venv
source venv/bin/activate   # hoặc venv\Scripts\activate trên Windows
pip install -r requirements.txt
python main.py

# hoặc NodeJS
npm install
npm start
```
## Cách hoạt động (Flow)

1. Người dùng nhập câu hỏi / yêu cầu từ giao diện frontend
2. Frontend gửi request đến backend (API)
3. Backend xử lý logic:
  - Intent classification
  - Slot filling
4. Trả về front-end các thông tin:
  - intent
  - thông tin yêu cầu liên quan (tên sách, tác giả,...)
  - metadata
