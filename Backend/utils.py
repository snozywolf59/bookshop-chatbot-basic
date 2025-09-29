from db import find_books

def prepare_prompt(user_input):
    prompt = f"""
    Bạn là chatbot cho hiệu sách. 
    Nhiệm vụ:
    1. Xác định intent của người dùng. Intent chỉ được chọn trong: ["mua_sach", "hoi_thong_tin", "spam"].
    2. Trích xuất các slot nếu có: 
       - name (tên sách)
       - quantity (số lượng)
       - price (giá)
       - author (tác giả)
    3. Nếu không có thông tin cho slot thì để giá trị null.
    4. Trả về **chỉ duy nhất JSON** với 2 field: 
       - "intent": string
       - "slots": object

    Ví dụ:
    Input: "Mình muốn mua 2 cuốn Đắc Nhân Tâm"
    Output:
    {{
        "intent": "mua_sach",
        "slots": {{
            "name": "Đắc Nhân Tâm",
            "quantity": 2,
            "price": null,
            "author": "null"
        }}
    }}
    
    Input: "mua 2 cuốn Đắc Nhân Tâm"
    Output:
    {{
        "intent": "mua_sach",
        "slots": {{
            "name": "Đắc Nhân Tâm",
            "quantity": 2,
            "price": null,
            "author": "null"
        }}
    }}
    
    Input: "Mình muốn mua 2 cuốn Đắc Nhân Tâm của Dale Carnegie"
    Output:
    {{
        "intent": "mua_sach",
        "slots": {{
            "name": "Đắc Nhân Tâm",
            "quantity": 2,
            "price": null,
            "author": "Dale Carnegie"
        }}
    }}
    
    Input: "Đắc Nhân Tâm"
    Output:
    {{
        "intent": "hoi_thong_tin",
        "slots": {{
            "name": "Đắc Nhân Tâm",
            "author": "null"
        }}
    }}
    
    Input: "Đắc Nhân Tâm của Dale Carnegie"
    Output:
    {{
        "intent": "hoi_thong_tin",
        "slots": {{
            "name": "Đắc Nhân Tâm",
            "author": "Dale Carnegie"
        }}
    }}

    Câu hỏi: {user_input}
    """
    return prompt


def ask_chatbot(model, user_input):
    import ollama

    prompt = prepare_prompt(user_input)

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

def clean_response(response):
    response = response.replace('```json', '').replace('```', '').strip()
    return response


def handle_intent(result):
    intent = result.get("intent")
    slots = result.get("slots", {})
    
    title = slots.get("name")
    book = find_books(title)
    
    author = book.get("author", "Chưa xác định")
    price = book.get("price", "Chưa xác định")

    if intent == "mua_sach":
        quantity = slots.get("quantity", 1)
        
        stock = book.get("stock", 0)
        if stock < quantity:
            return {
                "intent": intent,
                "message": f"Xin lỗi, hiện chỉ còn {stock} cuốn '{title}' trong kho."
            }
            
       
        
        message = f"Bạn muốn đặt mua {quantity} cuốn '{title}'"
        if author != "null":
            message += f" của {author}"
        if price != "null":
            message += f" với giá {price}"
        message += "?"
        
        return {
            "intent": intent,
            "message": message,
            "meta" : {
                "title": title,
                "quantity": quantity,
                "author": author if book else "null",
                "price": price if book else "null"
            }
        }
    
    elif intent == "hoi_thong_tin":
        author = book.get("author", "Chưa xác định") if book else "Chưa xác định"
        stock = book.get("stock", 0)
        message = f"Thông tin về sách '{title}'"
        if author != "null":
            message += f" của {author}"
        message += f", còn {stock} cuốn trong kho." if book else " không tìm thấy trong kho."
        
        return {
            "intent": intent,
            "message": message,
            "meta": {
                "author": author if book else "null",
                "stock": stock if book else 0,
                "title": title,
                "price": price
            }
        }
    
    else:
        return {
            "intent": "spam",
            "message": "Xin lỗi, tôi không hiểu yêu cầu của bạn."
        }