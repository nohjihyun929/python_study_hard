'''
bmi_calc를 만들기 위한 사전 준비
'''
# age = input("당신의 나이는 몇 살입니까? >>>")
# print(type(age))
# print(f"당신은 내년에 {age+1}살이 됩니다.")
'''
input() 함수의 결과값은 언제나 str입니다. -> 즉, 수학 연산을 하기 위해서는 별도의 과정이 필요합니다.

이때 필요한 함수가 '형변환 함수'입니다. (Conversion)
'''

# age1 = input("당신의 나이는 몇 살입니까? >>> ")
# print(type(age1)) #결과값 : str
# age1_int = int(age1) #str인 age1을 int로 자료형을 변환시켜서 age1_int라는 새로운 변수에 대입
# print(type(age1_int))
# print(f"당신은 내년에 {age1_int+1}살이 됩니다.") #여기서는 오류 발생 x
'''
자주 쓰이는 형변환 함수
1. int() -> str 또는 float를 int로 변경 
2. float() -> str 또는 int를 float으로 변경
3. round() -> 반올림 해주는 함수
'''
# temp = int(3.8)
# print(temp) #결과값 3 : 소수의 경우 버림을 한다
# temp2 = float(4)
# print(temp2) #결과값 4.0
#
# temp3 = round(3.8)
# print(temp3)
#
# temp4 = round(5.3491285, 2) #괄호 첫번째 수를 소수점 둘째자리까지 표기
# print(temp4)

'''
BMI 계산기를 작성합니다.

1. 키(cm)를 입력 받아(input()를 쓰라는 의미) 변수 height에 저장합니다.
height = input("당신의 키는 몇 cm입니까? >>> ")
2. 몸무게(kg)를 입력 받아 변수 weight에 저장합니다.

3. 몸무게/ (키(m)의 제곱)을 계산하면 bmi 지수가 나옵니다.
4. bmi 지수를 int로 출력하세요. -> int() 함수 사용하라는 의미
5. bmi 지수를 소수점 셋째자리에서 반올림하여 둘째자리까지 출력하세요. -> round() 함수 사용

실행 예

로고 출력하세요(구글에서 text to ascii art 검색하면 나옵니다.)
당신의 키는 몇 cm입니까? >>>
당신의 몸무게는 몇 kg입니까? >>>
당신의 bmi 지수는 23입니다.
당신의 bmi 지수는 23.xx입니다. 
'''
# print('''
#
# d8888b. .88b  d88. d888888b       .o88b.  .d8b.  db       .o88b. db    db db       .d8b.  d888888b  .d88b.  d8888b.
# 88  `8D 88'YbdP`88   `88'        d8P  Y8 d8' `8b 88      d8P  Y8 88    88 88      d8' `8b `~~88~~' .8P  Y8. 88  `8D
# 88oooY' 88  88  88    88         8P      88ooo88 88      8P      88    88 88      88ooo88    88    88    88 88oobY'
# 88~~~b. 88  88  88    88         8b      88~~~88 88      8b      88    88 88      88~~~88    88    88    88 88`8b
# 88   8D 88  88  88   .88.        Y8b  d8 88   88 88booo. Y8b  d8 88b  d88 88booo. 88   88    88    `8b  d8' 88 `88.
# Y8888P' YP  YP  YP Y888888P       `Y88P' YP   YP Y88888P  `Y88P' ~Y8888P' Y88888P YP   YP    YP     `Y88P'  88   YD
# '''
# )
# height = input("당신의 키는 몇 cm입니까? >>> ")
# weight = input("당신의 몸무게는 몇 kg입니까? >>> ")
# height = float(height)
# height_m= height/100
# weight = float(weight)
# bmi = weight/height_m**2
# bmi_round = round(bmi,2)
# bmi_int = int(bmi)
# print(f"당신의 bmi 지수는 {bmi_int}입니다.")
# print(f"당신의 bmi 지수는 {bmi_round}입니다.")

#-----------------------------------------------
#예시 답안
# height = float(input("당신의 키는 몇 cm입니까? >>> ")) /100 # 키 입력받고 바로 m로 변환
# weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))
# print(f"당신의 bmi지수는 {int(weight/(height**2))}입니다.")
# print(f"당신의 bmi지수는 {round((weight/(height**2)),2)}입니다.")