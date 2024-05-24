import sys

def countBytes(data):
    size=len(data.encode('utf-8'))
    return size

def countLines(data):
    lines=len(data.splitlines())
    return lines

def countWords(data):
    words=len(data.split())
    return words

def countChars(data):
    chars=len(data)
    return chars

if __name__ == '__main__':
    operation = None
    filename = None
    data = None

    if len(sys.argv) == 3:
        operation = sys.argv[1]
        filename = sys.argv[2]
    elif len(sys.argv) == 2:
        filename = sys.argv[1]

    if filename:
        with open(filename, "r") as f:
            data = f.read()
    else:
        data = sys.stdin.read()

    if operation == '-c':
        result = [countBytes(data)]
    elif operation == '-l':
        result = [countLines(data)]
    elif operation == '-w':
        result = [countWords(data)]
    elif operation == '-m':
        result = [countChars(data)]
    else:
        result = [countLines(data), countWords(data), countBytes(data)]

    if filename:
        result.append(filename)

    print(" ".join(map(str, result)))
