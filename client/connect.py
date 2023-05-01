import socket
import requests
from prettytable import PrettyTable

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

        # Define the Ensembl gene ID and genomic coordinates
        gene_id = 'ENSG00000134982'
        chromosome = '5'
        start = 112707498
        end = 112846239

        # Define the Ensembl REST API endpoint for retrieving exon information
        ensembl_endpoint = f'https://rest.ensembl.org/overlap/region/human/{chromosome}:{start}-{end}/?feature=exon;content-type=application/json;db_type=core;gene={gene_id}'

        # Send a GET request to the Ensembl REST API endpoint and retrieve the exon information in JSON format
        response = requests.get(ensembl_endpoint, headers={'Content-Type': 'application/json'})

        # Check that the response status code is 200 (OK)
        if response.status_code == 200:
            # Extract the exon information from the JSON response
            exons = []
            for exon in response.json():
                exon_start = exon['start']
                exon_end = exon['end']
                exons.append((exon_start, exon_end))

            # Put the exon information into the database
            print(f'Exon information for gene {gene_id}:')
            for i, exon in enumerate(exons):
                command = f'CREATE exon{i} {exons[i][0]},{exons[i][1]}'
                response = send_command(sock, command)
                #print(command)
            print("Create: ", response)
        else:
            # Handle errors
            print(f'Error: {response.status_code} - {response.reason}')

        # Read a record
        response = send_command(sock, 'READ exon93\n')
        print("Read: ", response)
        exon_table = PrettyTable()
        exon_table.field_names = ['Exon Number','Start','End']
        exon_table.add_row([93, response.split(' ')[1].split(',')[0], response.split(' ')[1].split(',')[1]])
        print(exon_table)

        # Close the connection
        send_command(sock, 'EXIT\n')

if __name__ == '__main__':
    main()