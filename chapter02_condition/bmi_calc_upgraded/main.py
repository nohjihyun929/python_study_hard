print('''

d8888b. .88b  d88. d888888b       .o88b.  .d8b.  db       .o88b. db    db db       .d8b.  d888888b  .d88b.  d8888b.
88  `8D 88'YbdP`88   `88'        d8P  Y8 d8' `8b 88      d8P  Y8 88    88 88      d8' `8b `~~88~~' .8P  Y8. 88  `8D
88oooY' 88  88  88    88         8P      88ooo88 88      8P      88    88 88      88ooo88    88    88    88 88oobY'
88~~~b. 88  88  88    88         8b      88~~~88 88      8b      88    88 88      88~~~88    88    88    88 88`8b
88   8D 88  88  88   .88.        Y8b  d8 88   88 88booo. Y8b  d8 88b  d88 88booo. 88   88    88    `8b  d8' 88 `88.
Y8888P' YP  YP  YP Y888888P       `Y88P' YP   YP Y88888P  `Y88P' ~Y8888P' Y88888P YP   YP    YP     `Y88P'  88   YD
'''
)
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
height = float(input("당신의 키는 몇 cm입니까? >>> ")) /100 # 키 입력받고 바로 m로 변환
weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))
# print(f"당신의 bmi지수는 {int(weight/(height**2))}입니다.")
# print(f"당신의 bmi지수는 {round((weight/(height**2)),2)}입니다.")
bmi = round((weight/(height**2)),2)
'''
업그레이드 관련 지시 사항

1. chrome에서 사이트를 확인하신 후 bmi가 특정 구간일 때마다 
    당신의 bmi 지수는 xx.xx이고, 저체중/정상/과체중/비만입니다. 가 출력될 수 있도록
        

'''
# if bmi <25 :
#     if bmi <18.5:
#         print(f"당신의 bmi 지수는 {bmi}이고, 저체중입니다.")
#     elif bmi < 23 :
#         print(f"당신의 bmi 지수는 {bmi}이고, 정상입니다.")
#     else :
#         print(f"당신의 bmi 지수는 {bmi}이고, 과체중입니다.")
# else :
#     print(f"당신의 bmi 지수는 {bmi}이고, 비만입니다.")

#-------------------------
# if bmi < 18.5 :
#     print(f"당신의 bmi 지수는 {bmi}이고, 저체중입니다.")
# elif bmi < 23 :
#     print(f"당신의 bmi 지수는 {bmi}이고, 정상입니다.")
# elif bmi < 25 :
#     print(f"당신의 bmi 지수는 {bmi}이고, 과체중입니다.")
# else :
#     print(f"당신의 bmi 지수는 {bmi}이고, 비만입니다.")

#----------------------------