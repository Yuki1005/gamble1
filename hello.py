#少なくとも1回以上出るガチャ確立プログラム
percent = float(input("キャラクターの排出率を入力してください(％)\n")) / 100
print('{:%}'.format(percent))

print("ガチャを引く回数を入力してください(回)")
times = input()
print(times + "回")

print("少なくとも１回以上出る確率は....")
answer = 1 - ((1 - percent) **100)
print('{:%}'.format(answer))
