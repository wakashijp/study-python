def word_quiz(word):  # word_quizジェネレータの定義
    hint_ = ""
    for letter in word:  # 引数で受け取った文字列から1文字ずつ取り出します
        hint_ += letter  # 先の取り出した文字に連結していく
        yield hint_  # ヒントを返す


# 出題する
ans = "Python"  # 正解
quiz = word_quiz(ans)  # ジェネレータを作る

while True:
    try:
        hint = next(quiz)  # ヒントを取り出す
        print(hint)
        ans_word = input("この単語は？： ")
        if ans.lower() == ans_word.lower():  # 大文字小文字を区別しないで比較
            point = len(ans) - len(hint)
            print(f"正解です！得点：{point}")
            break
        else:
            print("違います。")
    except StopIteration:
        print("終了です。得点：0")
        break
