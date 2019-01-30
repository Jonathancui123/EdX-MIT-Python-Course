func()
while True:
    try:
        x = int(input("GIve Number"))
        print(x/4)
        break
    except ValueError:
        print("Value error reached")
    except:
        print("Other error reached")