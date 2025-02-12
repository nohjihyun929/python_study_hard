# hangman_arts / hangman_word_list를 전부 import 해온 상태의
# play_hangman2() 함수를 정의한 다음
# main.py 파일에서

def play_hangman2() :
    from hangman_arts import stages,logo
    import random
    from hangman_word_list import word_list
    end_of_game = False

    lives = 6
    chosen_word = random.choice(word_list)
    print(f"테스트 코드 : {chosen_word}")
    display = []

    for letter in chosen_word:
        display.append("_")

    print(logo)

    while not end_of_game:

        guess = input("알파벳 입력하세요 >>> ").lower()

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

        if guess not in chosen_word:
            lives -= 1

            print(f"당신의 기회는 {lives}번 남았습니다.")

            if lives == 0:
                print("모든 기회를 잃었습니다.")
                end_of_game = True
                print(f"정답은 {chosen_word}입니다.")

        if "_" not in display:
            print("정답입니다:)")
            end_of_game = True
            break

        # print(display)
        # todo - 3 : display list의 모든 요소를 결합하여 문자열로 변환하세요.
        print(" ".join(display))
        print(stages[lives])



'''