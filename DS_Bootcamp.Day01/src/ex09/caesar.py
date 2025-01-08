import sys


def caeser(mod: str, words: str, count: int):
    result = []
    for letter in words:
        if '\u0400' <= letter <= '\u04FF':
            print(ord(letter))
            raise ValueError("Cyrillic symbol is not supported")
        if letter.isalpha():
            if letter.islower():
                start = ord('a')
            elif letter.isupper():
                start = ord('A')
            shift = count if mod == 'encode' else -count
            new_letter = chr((ord(letter) - start + shift) % 26 + start)
            result.append(new_letter)
        else:
            result.append(letter)

    print("".join(result))


if __name__ == "__main__":
    try:
        if len(sys.argv) == 4:
            mode, string, step = sys.argv[1], sys.argv[2], sys.argv[3]
            if mode not in ["decode", "encode"]:
                raise ValueError("Use: mode (decode|encode)")
            if not step.isdigit():
                raise ValueError(f'{step} is not digit')

            caeser(mode, string, int(step))
        else:
            print(f"Use: {sys.argv[0]} <decode|encode> <string> <shift>")
    except ValueError as e:
        print(f"Error: {e}")
