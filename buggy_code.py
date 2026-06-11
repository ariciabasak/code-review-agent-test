
import os
import subprocess
import hashlib

# Bug 1: SQL Injection vulnerability
def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query

# Bug 2: Hardcoded password
SECRET_KEY  = "password123"
DB_PASSWORD = "admin123"

# Bug 3: Shell injection
def run_command(user_input):
    result = subprocess.run(user_input, shell=True)  # dangerous!
    return result

# Bug 4: Weak hashing
def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()  # MD5 is insecure

# Bug 5: Unused imports + bad style
import sys
import json

# Bug 6: Overly complex function (high cyclomatic complexity)
def complex_logic(a, b, c, d, e):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        return a + b + c + d + e
                    else:
                        return a + b + c + d
                else:
                    if e > 0:
                        return a + b + c + e
                    else:
                        return a + b + c
            else:
                return a + b
        else:
            return a
    else:
        return 0

# Bug 7: Path traversal vulnerability
def read_file(filename):
    with open("/var/data/" + filename, "r") as f:  # path traversal risk
        return f.read()

# Bug 8: No error handling
def divide(a, b):
    return a / b  # ZeroDivisionError possible

# Bug 9: Mutable default argument
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# Bug 10: assert in production code
def validate_age(age):
    assert age > 0, "Age must be positive"
    return age
