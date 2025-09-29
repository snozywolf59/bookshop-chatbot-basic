import mysql.connector

from rapidfuzz import process

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="bookshop"
)

cursor = db.cursor(dictionary=True)

# Cache để lưu books
_books_cache = None
_last_update = None

def get_all_books():
    global _books_cache
    
    if _books_cache is None:
        query = "SELECT * FROM Books;"
        cursor.execute(query)
        _books_cache = cursor.fetchall()
    return _books_cache

def find_books(keyword):
    books = get_all_books()
    print("all books:", books)
    if not keyword:
        return ValueError("Keyword không được để trống")
         
         
    best_match = process.extractOne(keyword.lower(), [book['title'] for book in books])
    
    if best_match and best_match[1] > 20: 
        matched_title = best_match[0]
        for book in books:
            if book['title'].lower() == matched_title.lower():
                return book
            
    return None
            

def refresh_cache():
    """Reset cache để lấy dữ liệu mới từ DB"""
    global _books_cache
    _books_cache = None