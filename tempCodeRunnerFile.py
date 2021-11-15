name_string = input("내기를 할 친구들의 이름을 적습니다. 콤마(,)로 분리해서 적으세요\n")
names = name_string.split(",")

name = random.choice(names)
print("오늘의 점심은 %s님이 쏩니다." % name)