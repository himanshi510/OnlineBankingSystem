from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta, datetime
from random import randint
import mysql.connector

mydb=mysql.connector.connect(host="projectdb.coe4avf23rbf.ap-south-1.rds.amazonaws.com",user="bankdbgroup",passwd="bdbcse202", database="test1" )
mycursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = "bankDB"

# q=f"select * from customer  where c_id = 1050;"
# mycursor.execute(q)
# for i in mycursor:
#     for j in i:
#         print(j,end=" ")


@app.route("/", methods= ["POST", "GET"])
def home():
    if request.method == 'POST':
        session['usr'] = request.form
        print("session is of form ")
        print(session['usr'])
        
      
        if(request.form["Type"] == "Employee"):
            #print("Yessssssssssssssssssss")
            return redirect(url_for("Employee"))

        if(request.form["Type"] == "Customer"):
            return redirect(url_for("Customer"))

        if(request.form["Type"] == "Admin"):
            return redirect(url_for("Admin"))
    else:
        return render_template("home.html")


@app.route("/Employee")
def Employee():
    if 'usr' in session:
        return render_template("Employee.html",data=session['usr'])

@app.route("/Customer", methods= ["POST", "GET"])
def Customer():
    if 'usr' in session:
        print("not there yet.............")

        q=f"SELECT * FROM customer WHERE first_name= '{session['usr']['username']}';"
        mycursor.execute(q)
        customerDetails = mycursor.fetchall()

        customer_id = customerDetails[0][0]
        print("customer id is ")
        print(customer_id)
        

        q=f"select * from accounts where account_no = (select account_no from customer_account where c_id= '{customer_id }');;"
        mycursor.execute(q)
        myresult = mycursor.fetchall()


        print("myresult is of form ")
        print(myresult)
        return render_template("Customer.html",data=customerDetails)




@app.route("/Customer/Account")
def CustomerAccount():
    if 'usr' in session:
        q=f"SELECT * FROM customer WHERE first_name= '{session['usr']['username']}';"
        mycursor.execute(q)
        customerDetails = mycursor.fetchall()

        customer_id = customerDetails[0][0]
        print("customer id is ")
        print(customer_id)
        

        q=f"select * from accounts where account_no = (select account_no from customer_account where c_id= '{customer_id }');;"
        mycursor.execute(q)
        accountdetails = mycursor.fetchall()

        return render_template("CustomerAccount.html",data=accountdetails)


@app.route("/Customer/BankTransactions")
def BankTransactions():
    if 'usr' in session:
        q=f"SELECT * FROM customer WHERE first_name= '{session['usr']['username']}';"
        mycursor.execute(q)
        customerDetails = mycursor.fetchall()

        customer_id = customerDetails[0][0]
        
        

        q=f"select * from bank_transactions where sender = '{customer_id }' or receiver = '{customer_id }' ; "
        mycursor.execute(q)
        BankTransactionsdetails = mycursor.fetchall()
        print(BankTransactionsdetails)

        return render_template("BankTransactions.html",data=BankTransactionsdetails,len = len(BankTransactionsdetails))




if __name__ == "main":
    app.run(debug=True)


