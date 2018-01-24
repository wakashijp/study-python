def route(start, end, *args):  # startとendは必須です
    # 引数からルートのリストを作る
    route_list = [start]  # スタート地点
    route_list += list(args)  # 経由地点
    route_list += [end]  # ゴール地点
    # リストの要素を→で連結した文字列にする
    route_str = "→".join(route_list)
    print(route_str)


# route()を試す
start_point = "東京"
end_point = "宮崎"
route(start_point, end_point, "神戸", "長崎", "熊本")
