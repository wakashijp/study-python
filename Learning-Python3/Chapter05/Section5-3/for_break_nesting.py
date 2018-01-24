for i in range(4):
    for j in range(4):
        if i < j:  # iよりjが大きくなったらブレイク
            print("." * j)
            break  # ブレイクする
        print(f"i={i}, j={j}")
