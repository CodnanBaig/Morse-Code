morse = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

def continue_code():
    write_more = True
    while write_more:
        ask = input("Want to write more? Y/N:\n").lower()
        if ask == "y":
            text_to_morse()
        else:
            print("−··· −·−− · = BYE")
            write_more = False



def text_to_morse():
    text = input("Type in your message:\n").lower()
    code = []
    for letter in text:
        code.append(morse[letter])
        output = " ".join(code)
    print(output)

text_to_morse()
continue_code()