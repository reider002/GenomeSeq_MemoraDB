import socket

def send_command(sock, command):
    sock.sendall(command.encode('utf-8'))
    response = sock.recv(1024).decode('utf-8')
    return response.strip()

def main():
    server_address = '127.0.0.1'
    port = 5000

    # Connect to the MemoraDB server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_address, port))

        # Create a record
        response = send_command(sock, 'CREATE key1 value1\n')
        print("Create: ", response)

        # Read a record
        response = send_command(sock, 'READ key1\n')
        print("Read: ", response)

        # Update a record
        response = send_command(sock, 'UPDATE key1 new_value1\n')
        print("Update: ", response)

        # Read the updated record
        response = send_command(sock, 'READ key1\n')
        print("Read: ", response)

        # Delete a record
        response = send_command(sock, 'DELETE key1\n')
        print("Delete: ", response)

        # Try to read the deleted record
        response = send_command(sock, 'READ key1\n')
        print("Read: ", response)

        # Close the connection
        send_command(sock, 'EXIT\n')

if __name__ == '__main__':
    main()