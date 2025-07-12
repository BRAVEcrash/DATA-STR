# Define the Morse code table
morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
}

# Reverse dictionary for decoding
reverse_morse_dict = {v: k for k, v in morse_code_dict.items()}


# Node for Morse code tree
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.dot = None
        self.dash = None


# Build Morse code decision tree
def make_morse_tree():
    root = TreeNode()
    for letter, code in morse_code_dict.items():
        current = root
        for symbol in code:
            if symbol == '.':
                if current.dot is None:
                    current.dot = TreeNode()
                current = current.dot
            elif symbol == '-':
                if current.dash is None:
                    current.dash = TreeNode()
                current = current.dash
        current.data = letter
    return root


# Encode a single character to Morse code
def encode(ch):
    ch = ch.upper()
    return morse_code_dict.get(ch, '')


# Decode Morse code using the tree
def decode(tree, code):
    current = tree
    for symbol in code:
        if symbol == '.':
            current = current.dot
        elif symbol == '-':
            current = current.dash
        if current is None:
            return '?'
    return current.data if current else '?'


# Main program
def main():
    morseCodeTree = make_morse_tree()
    str_input = input("입력 문장 : ").strip().upper()  # Korean: "Enter sentence"
    mlist = []

    for ch in str_input:
        code = encode(ch)
        mlist.append(code)

    print("Morse Code: ", mlist)

    print("Decoding :", end='')
    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end='')
    print()


if __name__ == "__main__":
    main()
