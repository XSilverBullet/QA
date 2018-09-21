
def loadFile(filename):
    content = None
    try:
        f = open(filename, encoding="utf-8")
        content = f.readlines()

    finally:
        f.close()
    return content

print(loadFile("data/knowledge.txt"))
