from flask import Flask, jsonify, request
import random

app = Flask(__name__)
gifts = [
    {
        "name": "Teddy Bear",
        "price": 29.99,
        "ULRImage":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_KfcishZysQ2FS-ryOUqW7BJomtsbw_jhcQ&s"
    },
    {
        "name": "Lego Set",
        "price": 59.99,
        "ULRImage":"https://www.lego.com/cdn/cs/set/assets/blt52d7fce5233e7f7f/76300_Prod_en-gb.png?fit=crop&quality=80&width=400&height=400&dpr=1"
    }
]
taikhoan = []

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello, World!"})

@app.route('/register', methods=['POST'])
def register():
    user_name = request.json.get('username')
    password = request.json.get('password')

    
    # Thêm username và password vào mảng tài khoản
    if user_name and password:
        taikhoan.append({
            'username': user_name,
            'password': password,
            'spins': 1
        })
        return jsonify({
            "message": "User registered successfully!",
            "accounts": taikhoan
        })
    else:
        return jsonify({"message": "Username and password are required!"}), 400
@app.route('/login', methods=['POST'])
def login():
    user_name = request.json.get('username')
    password = request.json.get('password')

    for account in taikhoan:
        if account['username'] == user_name and account['password'] == password:
            return jsonify({
                "message": "Login successful!",
                "account": account
            })
    return jsonify({"message": "Invalid username or password!"}), 401

@app.route('/random-gifts', methods=['GET'])
def random_gifts():
    random_gift = random.choices(gifts, weights=[gift["price"] for gift in gifts])
    return jsonify(random_gift)
@app.route('/add-gift/<gift_name>,<gift_price>,<gift_image>', methods=['POST'])
def add_gift(gift_name, gift_price, gift_image):
    if(not gift_name or not gift_price or not gift_image):
        return jsonify({"error": "All fields (name, price, image URL) are required."}), 400
    new_gift = {
        "name": gift_name,
        "price": float(gift_price),
        "ULRImage": gift_image
    }
    gifts.append(new_gift)
    return jsonify({"message": f"Gift '{gift_name}' added successfully!"})
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/gifts/<int:gift_id>', methods=['PUT'])
def update_gift(gift_id):
    data = request.get_json()

    name = data.get('name')
    url_image = data.get('ULRImage')
    price = data.get('price')

    return jsonify({
        "message": "Gift updated successfully",
        "gift_id": gift_id,
        "data": data
    }), 200


app.run()