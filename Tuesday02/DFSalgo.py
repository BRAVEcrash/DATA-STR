from Tuesday02.ArrayStack import ArrayStack
map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]
SIZE = 6
def isValidPos(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    return False

def DES():
    print("DES: ")
    S = ArrayStack()
    S.push((1, 0 ))

    while not S.isEmpty():
        pos = S.pop()
        [r, c]= pos
        print(pos, end= '->')

        if(map[r][c] == 'x'):
            return True
        else:
            map[r][c] = '.'
            if isValidPos(r - 1, c - 1): S.push((r - 1, c))
            if isValidPos(r + 1, c): S.push((r + 1, c))
            if isValidPos(r, c - 1): S.push((r, c - 1))
            if isValidPos(r, c + 1): S.push((r, c + 1))
        print(S.array[S.top::-1])
    return False

if __name__ == "__main__":
    result = DES()

    if result: print(result)