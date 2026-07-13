import sqlite3

def save_message(session_id, role, message):
    connection = sqlite3.connect('db/memory.db')
    cursor = connection.cursor()
    
    cursor.execute("""
        INSERT INTO conversation_memory (session_id, role, message) 
        VALUES (?, ?, ?)
    """, (session_id, role, message))
    
    connection.commit()
    connection.close()