# 국어, 수학, 영어, 도덕, 물리 5개 과목의 데이터를
# dic_sum 사전으로 생성하고, 전체 평균 점수를 구하시오.
# 점수는 직접 입력한다. (전체 점수 / 과목 개수)

# 내 답안
"""dic_sum = dict()
dic_sum["국어"] = 80
dic_sum["수학"] = 90
dic_sum["영어"] = 80
dic_sum["도덕"] = 100
dic_sum["물리"] = 100
print(dic_sum)

value_list = dic_sum.values()
summ = 0

for i in value_list:
    summ = summ + i
    
print("전체 평균 점수 : ", summ / 5)"""

# 답
dic_sum = {'국어': 95, '수학': 91, '영어': 89, '도덕': 83, '물리': 55}
average = sum(dic_sum.values()) / len(dic_sum)
print('사전 자료구조를 활용, 전체 평균 점수는 : ')
print(average)