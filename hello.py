#少なくとも指定のキャラクターが1回以上出るガチャ確立プログラム
print("キャラクターの排出率を入力してください(％)")
percent = float(input("キャラクターの排出率を入力してください(％)\n")) / 100
print('{:%}'.format(percent))

print("ガチャを引く回数を入力してください(回)")
times = input()
print(times + "回")

print("少なくとも１回以上出る確率は....")
answer = 1 - ((1 - percent) ** float(times))
print('{:%}'.format(answer))