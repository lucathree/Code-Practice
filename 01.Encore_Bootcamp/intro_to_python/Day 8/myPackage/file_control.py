def file_read(path):
    f = open(path, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    return s


def file_write(path, content):
    f = open(path, 'a', encoding='utf-8')
    f.write(content)
    f.close()
