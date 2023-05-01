import socket
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
        
        my_table = PrettyTable()
        my_table.field_names = ['seqname','source','feature','start','end','score','strand','frame','hid','hstart','hend','genscan','gene_id','transcript_id','exon_id','gene_type','variation_name','probe_name']
        my_table.add_row([5,'Ensembl','similarity',112707718,112707882,298,'+','.','B7Z2B6.1',1,55,'','','','','','',''])
        print(my_table)

        # Close the connection
        send_command(sock, 'EXIT\n')

if __name__ == '__main__':
    main()