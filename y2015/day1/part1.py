def main():
    with open("./input.txt", "r") as f:
        data = f.read()
    count = 0
    for item in data:
        if item == "(":
            count += 1
        else:
            count -= 1
    print(count)


if __name__ == "__main__":
    main()
