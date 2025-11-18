import requests
import json

BASE_URL = "http://localhost:5000"

def test_api():
    print("Testing User Management API\n")
    
    try:
        # Test 1: Get all users
        print("1. GET All Users:")
        response = requests.get(f"{BASE_URL}/users")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
        # Test 2: Get specific user
        print("2. GET User by ID (1):")
        response = requests.get(f"{BASE_URL}/users/1")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
        # Test 3: Create new user
        print("3. POST Create New User:")
        new_user = {
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "age": 25
        }
        response = requests.post(f"{BASE_URL}/users", json=new_user)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
        # Test 4: Update user
        print("4. PUT Update User:")
        updated_data = {
            "name": "John Updated",
            "email": "john.updated@example.com"
        }
        response = requests.put(f"{BASE_URL}/users/1", json=updated_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
        # Test 5: Get all users after changes
        print("5. GET All Users After Changes:")
        response = requests.get(f"{BASE_URL}/users")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
        # Test 6: Delete user
        print("6. DELETE User:")
        response = requests.delete(f"{BASE_URL}/users/2")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
        # Test 7: Get non-existent user
        print("7. GET Non-existent User:")
        response = requests.get(f"{BASE_URL}/users/999")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to the server. Make sure Flask app is running.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()