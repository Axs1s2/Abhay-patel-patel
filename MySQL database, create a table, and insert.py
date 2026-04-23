import mysql.connector

def setup_database():
    try:
        # 1. Database Connection 
        # (Yahan 'host', 'user', aur 'password' apne MySQL setup ke hisab se badlein)
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )
        
        cursor = db_connection.cursor()

        # 2. Database banana (agar pehle se nahi hai)
        cursor.execute("CREATE DATABASE IF NOT EXISTS SchoolDB")
        cursor.execute("USE SchoolDB")
        print("Database 'SchoolDB' ready.")

        # 3. Table banana
        # Hum 'students' naam ki table bana rahe hain jisme ID, Name, aur Marks hain
        table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(100),
            marks INT
        )
        """
        cursor.execute(table_query)
        print("Table 'students' created successfully.")

        # 4. Records Insert karna
        insert_query = "INSERT INTO students (id, name, marks) VALUES (%s, %s, %s)"
        
        # Multiple records ki list
        student_data = [
            (101, 'Rahul', 85),
            (102, 'Sneha', 92),
            (103, 'Amit', 78),
            (104, 'Priya', 88)
        ]

        # executemany() ka use karke ek saath saara data insert karein
        cursor.executemany(insert_query, student_data)
        
        # 5. Changes ko Commit (Save) karein
        db_connection.commit()
        print(f"{cursor.rowcount} records inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Connection band karna
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    setup_database()