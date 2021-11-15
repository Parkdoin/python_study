# # 랜덤모듈 불러오기
# import random
# import myModule as my

# x = random.randint(0, 1) # 0, 1 중에서 랜덤으로 숫자를 뽑는다.
# # 동전을 던졌을때 랜덤으로 앞 뒷면이 나오도록 코드 작성
# if x == 1:
#     print("앞면")
# else:
#     print("뒷면")
    
# # 내가 만든 마이모듈의 변수 pi를 불러옴
# print(my.pi)

# # 예제 1
# import random
# name_string = input("내기를 할 친구들의 이름을 적습니다. 콤마(,)로 분리해서 적으세요\n")
# names = name_string.split(",")

# #n = random.choice(names)
# n = random.randint(0, len(names))
# print(f"오늘의 점심은 {names[n]}님이 쏩니다.")

# # 예제 2
# import random

# 바위 = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# 보 = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# 가위 = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [가위,바위,보]

# user_choice = int(input("가위는 0 바위는 1 보는 2 를 적어 주세요.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("컴퓨터 선택:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("잘못된 번호를 선택했어요 0 , 1, 2 중 선택하세요") 
# elif user_choice == 0 and computer_choice == 2:
#   print("이겼습니다!")
# elif  user_choice == 2 and computer_choice == 0:
#   print("졌습니다.")
# elif computer_choice > user_choice:
#   print("졌습니다.")
# elif user_choice > computer_choice:
#   print("이겼습니다!")
# elif computer_choice == user_choice:
#   print("비겼습니다.")


# # 예제 3
# import random

# heights = input("학생의 키를 입력하세요.\n").split()
# print(heights)

# for n in range(0, len(heights)):
#     heights[n] = int(heights[n])
# print(heights)

# total_height = 0
# for h in heights:
#     total_height += h
# print(f'전체 키의 합 = {total_height}')
# print(f'학생의 숫자는 {len(heights)}')
# print(f'평균 키는 {total_height/len(heights)}')


# 예제 4
import random

student_scores = input("학생의 점수를 입력하세요.\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
lowest_score = 1000
for n in student_scores:
    if n > highest_score:
        highest_score = n
    if n < lowest_score:
        lowest_score = n

print(f'가장 높은 점수는 : {highest_score}')
print(f'가장 낮은 점수는 : {lowest_score}')