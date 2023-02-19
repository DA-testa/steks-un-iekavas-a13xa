# python3
# Aleksandra Červinska, 12. grupa, 221RDB069
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    closing_brackets_stack = []
    wr = []
    for i, next in enumerate(text):
        if next in ")]}":
            if len(closing_brackets_stack) == 0:
                wr.append(i+1)
            else:
                top = closing_brackets_stack[-1]
                if not are_matching(top.char, next):
                    wr.append(i+1)
                    break
                else:
                    closing_brackets_stack.pop()
        elif next in "([{":
            closing_brackets_stack.append(Bracket(next, i+1))
    if len(closing_brackets_stack) > 0:
        for bracket in closing_brackets_stack:
            wr.append(bracket.position)
    if len(wr) == 0:
        return "Success"
    else:
        return wr[0]


def main():
    while True:
        text = input("Ievadiet 'F', lai palaistu testu vai 'I',  lai ievaditu tekstu: ")
        if text == "F":
            fails = input("Ievadiet faila nosaukumu (0-5): ")
            faila_nos = "test/" + fails
            with open(faila_nos, "r") as f:
                teksts = f.readline().strip()
            mismatch = find_mismatch(teksts)
            if mismatch == "Success":
                print("Success")
            else:
                print(mismatch)
            break
        elif text == "I":
            teksts = input("Ievadiet tekstu: ").strip()
            if len(teksts) == 0:
                continue
            elif len(teksts) >= 100000:
                print("Teksts ir " + str(len(teksts) - 100000) + " zimes par garu")
                continue
            mismatch = find_mismatch(teksts)
            if mismatch == "Success":
                print("Success")
            else:
                print(mismatch)
            break
        else:
            teksts = text.strip()
            if len(teksts) == 0:
                continue
            elif len(teksts) >= 100000:
                print("Teksts ir " + str(len(teksts) - 100000) + " zimes par garu")
                continue
            mismatch = find_mismatch(teksts)
            if mismatch == "Success":
                print("Success")
            else:
                print(mismatch)
            break


if __name__ == "__main__":
    main()
