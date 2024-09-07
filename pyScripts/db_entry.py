import mysql.connector

def get_translatelist(words):
    # Connect to the MariaDB database
    conn = mysql.connector.connect(
        host="localhost",
        user="username",
        password="assword",
        database="kr_vocab",
        collation='utf8mb4_unicode_ci'  # Use a supported collation
        
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor(dictionary=True)

    # Define the SQL query
    placeholders = ','.join(f"'{word}'" for word in words)
    sql_query = f"SELECT korean_word, translation FROM korean_words WHERE korean_word IN ({placeholders});"
    cursor.execute(sql_query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Create a dictionary with Korean words as keys and translations as values
    korean_dictionary = {}
    for row in rows:
        korean_word = row.pop('korean_word')  # Remove 'korean_word' from the dictionary and get its value
        korean_dictionary[korean_word] = row['translation']  # Use the Korean word as the key and assign the translation as the value

    return korean_dictionary


def get_nounlist(words):
    # Connect to the MariaDB database
    conn = mysql.connector.connect(
        host="localhost",
        user="username",
        password="assword",
        database="kr_vocab"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor(dictionary=True)

    quoted_words = ','.join(f"'{word}'" for word in words)
    sql_query = f"SELECT korean_word, is_noun, final_consonant FROM korean_words WHERE korean_word IN ({quoted_words});"

    cursor.execute(sql_query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return rows

