# 사전의 데이터를 정렬/역정렬 하는 코드를 작성하시오.
# 또는 집합은 순서가 없다. Sorted 함수를 활용한다.
# 키는 a, b, c, d, e 까지 값은 정수를 사용한다. (정의)


dic_sum = {'국어': 95, '수학': 91, '영어': 89, '도덕': 83, '물리': 55}
print(sorted(dic_sum)) # 정렬
print(sorted(dic_sum, reverse = True)) # 역정렬