def main():
    with open("./input.txt", "r") as f:
        p = f.read()
    count = 0
    posn = 0
    for item in p:
        if item == "(":
            posn += 1
            count += 1
        elif item == ")":
            count -= 1
            posn += 1
            if count == -1:
                break

    print(posn)


main()
