import os

def open_read_write_file(dir, new_file):
    folder_name_length = 1 + len(str(dir))
    file_list_temp = os.listdir(dir)
    file_list = []
    file_template = {}
    for file in file_list_temp:
        file_list.append(os.path.join(dir, file))
    for name in file_list:
        with open(name, 'r') as file:
            file_data = file.read() + '\n'
            counter = sum(1 for line in open(name))
            file_template.setdefault(name, [counter, file_data])
    sorted_file_template = dict(sorted(file_template.items(), key=lambda para: para[1]))
    with open(new_file, 'a') as new_file:
        for k, v in sorted_file_template.items():
            new_file.write(str(k)[folder_name_length:] + '\n')
            new_file.write(str(v[0])+'\n')
            new_file.write(str(v[1]))
    return new_file

open_read_write_file('files', 'fin.txt')