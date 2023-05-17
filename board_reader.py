def import_boardsudoku(filename):
    file = open(filename,'r')
    content = file.read()
    file.close()
    return list(map(int, content.replace("\n", "").split(',')))

try:
    print(import_boardsudoku(input("Input filename: ")))
except:
    print("Can't find the board with that name.")