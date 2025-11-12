# function to perform various counting tasks.
def main():
    # 1) Count up from 0 to 50
    print("1) Count up from 0 to 50:")
    for i in range(0, 51):
        print(i)
    # 2) Count down from 50 to 0
    print("\n2) Count down from 50 to 0:")
    for i in range(50, -1, -1):
        print(i)
    # 3) Count up from 30 to 50
    print("\n3) Count up from 30 to 50:")
    for i in range(30, 51):
        print(i)
    # 4) Count down from 50 to 10
    print("\n4) Count down from 50 to 10:")
    for i in range(50, 9, -2):
        print(i)
    # 5) Count up from 100 to 200 
    print("\n5) Count up from 100 to 200:")
    for i in range(100, 201, 5):
        print(i)


if __name__ == "__main__":
    main()
