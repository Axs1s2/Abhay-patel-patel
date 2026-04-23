import mysql.connector

def manage_records():
    try:
        # 1. Database Connection (Details apni setup ke hisab se badlein)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="SchoolDB"
        )
        cursor = conn.cursor()

        # --- UPDATE OPERATION ---
        # Maan lijiye hum student ka naam change kar rahe hain jiski ID 101 hai
        update_query = "UPDATE students SET name = %s WHERE id = %s"
        new_values = ("Rahul Sharma", 101)
        
        cursor.execute(update_query, new_values)
        conn.commit()  # Change ko save karne ke liye commit zaroori hai
        print(f"{cursor.rowcount} record(s) updated successfully.")

        # --- DELETE OPERATION ---
        # Maan lijiye hum us student ko delete kar rahe hain jiski ID 105 hai
        delete_query = "DELETE FROM students WHERE id = %s"
        student_id = (105,)
        
        cursor.execute(delete_query, student_id)
        conn.commit()
        print(f"{cursor.rowcount} record(s) deleted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Connection close karna na bhoolein
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    manage_records()