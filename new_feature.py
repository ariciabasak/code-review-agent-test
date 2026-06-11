
# New feature with intentional bugs
import os
import subprocess

API_KEY = "sk-hardcoded-api-key-123"  # Bug: hardcoded secret

def process_user_data(user_id):
    cmd = f"echo {user_id}"
    os.system(cmd)  # Bug: os.system with user input
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return query

def calculate(n):
    result = []
    for i in range(n):
        for j in range(n):
            for k in range(n):  # O(n^3) complexity
                result.append(i*j*k)
    return result

x = 10
y = 0
print(x / y)  # Bug: ZeroDivisionError
