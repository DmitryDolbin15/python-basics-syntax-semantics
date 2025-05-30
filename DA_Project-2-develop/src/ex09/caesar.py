import sys

def caesar(mod,text,num):
    flag = 1
    if any(ord(char) > 127 for char in text):
        print("The script does not support your language yet.")
        flag = 0

    result = []
    if flag == 1:
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                if mod == 'encode':
                    result.append(chr((ord(char) - start + num) % 26 + start))
                elif mod == 'decode':
                    result.append(chr((ord(char) - start - num) % 26 + start))
            else:
                result.append(char)

        return ''.join(result)

if __name__ == "__main__":
    flag = 1
    if len(sys.argv) == 4:
        mod=sys.argv[1]
        text = sys.argv[2]
        try:
            num =int(sys.argv[3])
        except :
            print("Number must be an integer.")
            flag = 0

        if mod not in ['encode', 'decode'] and flag == 1:
            print("First argument must be 'encode' or 'decode'.")
            flag = 0

        if flag == 1:
            print(caesar(mod,text,num))

    else:
        print("Usage: python3 caesar.py <encode/decode> '<text>' <number>")
