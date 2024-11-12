def format_and_save_proxies(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            line = line.strip()
            if line:
                proxy_format = f'{{"http": "http://{line}", "https": "http://{line}"}},'
                file.write(proxy_format + '\n')

def main():
    socks4_file = 'socks4.txt'
    socks5_file = 'socks5.txt'

    output_socks4_file = 'output_socks4.txt'
    output_socks5_file = 'output_socks5.txt'

    format_and_save_proxies(socks4_file, output_socks4_file)

    format_and_save_proxies(socks5_file, output_socks5_file)

if __name__ == '__main__':
    main()
