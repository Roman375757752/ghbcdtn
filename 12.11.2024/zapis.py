def read_and_format_proxies(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            line = line.strip()
            if line:
                proxy_format = f'{{"http": "http://{line}", "https": "http://{line}"}},'
                file.write(proxy_format + '\n')

input_file = 'input.txt'  
output_file = 'output.txt'  


read_and_format_proxies(input_file, output_file)
