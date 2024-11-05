import sqlite3
conn=sqlite3.connect('choco.db')
cursor=conn.cursor()
cursor.execute("CREATE TABLE chocolate(id INTEGER PRIMARY KEY, name TEXT, type TYPE, ingredients_present TEXT, price INTEGER, season TEXT)")
cursor.execute("INSERT INTO chocolate VALUES (1,'Dark Delight','Dark','Cocoa beans,sugar,cocoa butter',250,'All Year')")
cursor.execute("INSERT INTO chocolate VALUES (2,'Mint Chocolate Chip','Milk','Cocoa beans,sugar,cocoa butter,mint extracts',150,'Winter')")
cursor.execute("INSERT INTO chocolate VALUES (3,'Couverture Chocolate','Milk','Cocoa beans,sugar,cocoa butter',450,'Summer')")
cursor.execute("INSERT INTO chocolate VALUES (4,'Truffles','Dark','Cocoa beans,sugar,chocolate ganache,nuts',350,'All Year')")
cursor.execute("INSERT INTO chocolate VALUES (5,'Pistachio bars','Dark','Cocoa beans,sugar,cocoa butter,pistachio,caramel',550,'Autumn')")
cursor.execute("INSERT INTO chocolate VALUES (6,'Pumpkin Spice Latte','Dark','Cocoa beans,sugar,cocoa butter,milk powder,chocolate chips',240,'Winter')")
conn.commit()
rows=cursor.execute("SELECT id,name,type,ingredients_present,price,season from chocolate").fetchall()
print(rows)
cursor.execute("CREATE TABLE ingredient(id INTEGER PRIMARY KEY,name TEXT,quantity INTEGER,reorderlevel INTEGER)")
cursor.execute("INSERT INTO ingredient VALUES (1,'cocoa beans',1000,200)")
cursor.execute("INSERT INTO ingredient VALUES (2,'sugar',500,100)")
cursor.execute("INSERT INTO ingredient VALUES (3,'milk powdre',300,50)")
cursor.execute("INSERT INTO ingredient VALUES (4,'cocoa butter',250,50)")
cursor.execute("INSERT INTO ingredient VALUES (5,'mint extract',50,10)")
cursor.execute("INSERT INTO ingredient VALUES (6,'chocolate chips',200,40)")
conn.commit()
cursor.execute("CREATE TABLE CC(id INTEGER PRIMARY KEY, cust_name TEXT, ratings INTEGER, feedback TEXT, allergy TEXT)")
cursor.execute("INSERT INTO CC VALUES (11,'John Doe','Love the Dark flavour',NULL,5)")
cursor.execute("INSERT INTO CC VALUES (12,'Jane Smith','Love for Milk chocolate','Allergic to nuts',4)")
cursor.execute("INSERT INTO CC VALUES (13,'Milke Jackson','Can you add more fruity flavour','None',3)")
cursor.execute("INSERT INTO CC VALUES (14,'Kim Kardash','Add some unique flavours','Allergic to peanuts',4)")
cursor.execute("INSERT INTO CC VALUES (15,'Skippe','Love thw Whitess!',NULL,4)")
cursor.execute("INSERT INTO CC VALUES (16,'Manchestre','Love the nutfull fills','Allergic to gluten',5)")
rows1=cursor.execute("SELECT id,name,quantity,reorderlevel from ingredient").fetchall()
print(rows1)
rows=cursor.execute("SELECT name,type from chocolate WHERE season='All Year'").fetchall()
print(rows)



pip install Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Untitled.html')

if __name__ == '__main__':
    app.run(debug=True)
