import mysql.connector

def retrieve_data():
    try:
        # 1. Database Connection
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="SchoolDB"
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            
            # 2. SELECT query execute karein
            query = "SELECT * FROM students"
            cursor.execute(query)
            
            # 3. Saara data fetch karein
            records = cursor.fetchall()
            
            print(f"Total number of rows in table: {cursor.rowcount}")
            print("\n--- Student Records ---")
            
            # Header display karein
            print(f"{'ID':<10} {'Name':<20} {'Marks':<10}")
            print("-" * 40)
            
            # 4. Loop chala kar data display karein
            for row in records:
                # Maan lijiye table mein 3 columns hain: id, name, marks
                print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # 5. Connection band karein
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("\nMySQL connection closed.")

if __name__ == "__main__":
    retrieve_data()