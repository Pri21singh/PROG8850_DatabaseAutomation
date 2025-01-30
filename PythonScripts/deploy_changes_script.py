import pymysql

# Database connection details
db_host = "localhost"
db_user = "root"
db_password = "Software@2025" #we can set the connection details in .env file as well
db_name = "my_database"

# Connect to the MySQL database
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = connection.cursor()

# SQL statement to add a new table
sql_query = """
CREATE TABLE IF NOT EXISTS Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Execute the SQL statement
try:
    cursor.execute(sql_query)
    connection.commit()
    print("Table 'Students' created successfully!")
except Exception as e:
    print(f"Error deploying changes: {e}")
finally:
    cursor.close()
    connection.close()