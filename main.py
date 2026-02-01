from flask import Flask, jsonify, request

app = Flask(__name__)
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
    

app.run()