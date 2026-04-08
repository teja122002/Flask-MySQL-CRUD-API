from flask import Flask,request,jsonify
import mysql.connector
app=Flask(__name__)
def get_db():
    conn=mysql.connector.connect(
        host="localhost",
        user='root',
        password='root123',
        database="testdb"
    )
    return conn
#create table
def create_table():
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(50),
                   age INT
                    )""")
    conn.commit()
    cursor.close()
    conn.close()
#create post
@app.route('/users',methods=['POST'])
def create_users():
    data=request.get_json()
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO users (name,age) values(%s,%s)",
                   (data['name'],data['age']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"Message": "User has added"}),201
@app.route('/users',methods=['GET'])
def get_users():
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("SELECT *FROM users ")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    users=[{"id":r[0] ,"name":r[1],"age":r[2]} for r in rows]
    return jsonify(users),200
@app.route('/users/<int:id>',methods=['GET'])
def get_user(id):
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("select *from users WHERE ID=%s",(id,))
    row=cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return jsonify({"id":row[0],"name":row[1],"age":row[2]}),200
    return jsonify({"Message":"User has not found"}),404
@app.route('/users/<int:id>',methods=['PUT'])
def update_users(id):
    data=request.get_json()
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("UPDATE users SET name=%s ,age=%s WHERE id=%s",
                   (data['name'],data['age'],id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message":"Users has updated"})
@app.route('/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"Message":"User deleted"}),200
if __name__=="__main__":
    create_table()
    app.run(debug=True)

