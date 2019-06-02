'''
Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. 
Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
'''

import socket
import re
import sys

def main():
    (url, host) = get_url_with_host()
    socket_connection = open_http_connection(host)
    get_data_from_connection(socket_connection, url)
    return

def get_url_with_host():
    url = input('Enter URL: ')
    host_regex = r'^https?:\/\/([\w\d.]+)\/'
    host_names = re.findall(host_regex, url)
    return (url, host_names[0])

def open_http_connection(host):
    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Opening connection to:', host)
    
    try:
        socket_connection.connect((host, 80))
    except:
        print('Could not form connection, exiting.')
        sys.exit(2)

    print('Connection successful!')

    return socket_connection

def get_data_from_connection(socket_connection, url):
    cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n')
    print('Sending command:', cmd)
    cmd = cmd.encode()
    socket_connection.send(cmd)

    while True:
        data = socket_connection.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    socket_connection.close()
    return

if __name__ == "__main__":
    main()