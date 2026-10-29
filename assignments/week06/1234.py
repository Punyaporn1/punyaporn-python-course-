@@ -30,7 +30,14 @@ def calculate_circle(radius):

def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    pass
    if premium == True:
        return f"{username} (age: {age}) - Premium User"
    else:
        return f"{username} (age: {age}) - Standard User"

print(create_user_profile("Frame", 40))
print(create_user_profile("OLE"))
print(create_user_profile("WIT", 23, True))

""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้: