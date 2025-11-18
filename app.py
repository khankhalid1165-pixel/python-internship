from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {
    1: {"id": 1, "name": "John Doe", "email": "john@example.com"},
    2: {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
}

# Counter for generating new user IDs
next_id = 3

# Helper function to find user by ID
def find_user(user_id):
    return users.get(user_id)

# Routes

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to User Management API",
        "endpoints": {
            "GET /users": "Get all users",
            "GET /users/<id>": "Get user by ID",
            "POST /users": "Create new user",
            "PUT /users/<id>": "Update user by ID",
            "DELETE /users/<id>": "Delete user by ID"
        }
    })

# GET all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify({
        "users": list(users.values()),
        "total": len(users)
    })

# GET user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    if user:
        return jsonify({"user": user})
    else:
        return jsonify({"error": "User not found"}), 404

# POST - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    
    # Check if request contains JSON data
    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # Validate required fields
    if 'name' not in request.json or 'email' not in request.json:
        return jsonify({"error": "Name and email are required"}), 400
    
    # Create new user
    new_user = {
        "id": next_id,
        "name": request.json['name'],
        "email": request.json['email']
    }
    
    # Add optional fields if provided
    if 'age' in request.json:
        new_user['age'] = request.json['age']
    
    users[next_id] = new_user
    next_id += 1
    
    return jsonify({
        "message": "User created successfully",
        "user": new_user
    }), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # Update user fields
    if 'name' in request.json:
        user['name'] = request.json['name']
    if 'email' in request.json:
        user['email'] = request.json['email']
    if 'age' in request.json:
        user['age'] = request.json['age']
    
    return jsonify({
        "message": "User updated successfully",
        "user": user
    })

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    
    return jsonify({
        "message": "User deleted successfully",
        "deleted_user": user
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)