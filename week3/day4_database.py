import psycopg2
connection = psycopg2.connect("dbname=my_first_user")
cursor = connection.cursor()
name = input("What is the first name to search for?").lower()
password = input("Password?").lower()
cursor.execute("SELECT * FROM person_data WHERE first_name = %s and password = %s;",(name,password))
results = cursor.fetchall()
print(results)
print(results[0][3])




cursor.close()
connection.close()
