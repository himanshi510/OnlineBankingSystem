import mysql.connector

def main():
	mydb = mysql.connector.connect(
		host="projectdb.coe4avf23rbf.ap-south-1.rds.amazonaws.com",
		user="bankdbgroup",
		password="bdbcse202",
		database="test3"
	)

	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM customer")
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)


if __name__ == "__main__":
	main()
