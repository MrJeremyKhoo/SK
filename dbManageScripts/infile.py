import mysql.connector
import csv

def insert_data_from_csv(csv_file):
    # Connect to the MariaDB database
    conn = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="kr_vocab"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor(dictionary=True)

    # Define the SQL query with IGNORE to skip duplicate entries based on primary key or unique key
    query = """
    INSERT IGNORE INTO korean_words (id, korean_word, translation, final_consonant, is_adjetive, is_verb, is_noun, is_preposition)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Read data from CSV file
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            cursor.execute(query, row)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    # CSV file path
    csv_file = 'out.csv'

    # Call the function to insert data from CSV
    insert_data_from_csv(csv_file)

