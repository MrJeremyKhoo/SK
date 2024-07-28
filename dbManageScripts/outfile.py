import mysql.connector

def main():
    # Connect to the MariaDB database
    conn = mysql.connector.connect(
        host="localhost",
        user="username",
        password="assword",
        database="kr_vocab"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor(dictionary=True)
    # Define the SQL query
    query = """
    SELECT * INTO OUTFILE '/home/jeremy/out.csv'
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    FROM korean_words;
    """

    try:
        # Execute the SQL query
        cursor.execute(query)
        print("Data exported successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
