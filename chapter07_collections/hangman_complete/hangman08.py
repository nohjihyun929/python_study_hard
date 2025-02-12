def play_hangman() :
    import random

    logo = '''
     _                                         
    | |                                        
    | |__  _____ ____   ____ ____  _____ ____  
    |  _ \(____ |  _ \ / _  |    \(____ |  _ \ 
    | | | / ___ | | | ( (_| | | | / ___ | | | |
    |_| |_\_____|_| |_|\___ |_|_|_\_____|_| |_|
                      (_____|                  
    '''

    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
    ]
    end_of_game = False
    #todo - 1 : 남은 목숨 수를 추적하기 위한 'lives'라는 변수를 선언하고, 6으로 초기화하세요.
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
            # else:
            #     lives -= 1
            #     print(f"당신의 기회는 {lives}번 남았습니다.")
            #     if lives == 0:
            #         print("모든 기회를 잃었습니다.")
            #         break
            #         end_of_game = True
            # 라고 작성하시면 안됩니다. -> 알파벳을 하나 입력할 때마다 모든 단어에서 알파벳이 맞는지
            # 확인하는 조건문이 실행되기 때문
            # -> 즉, 반복문 내부에 조건문이 있기 때문에 guess를 한 번만 입력 하고도
            # lives가 여러분 -= 1이 이루어집니다.

        # 이상을 이유로 for 반복문 바깥에서(즉 들여쓰기 적용 x) guess가 chosen_word에 속하지
        # 않는지를 확인하는 조건문을 작성해야 함.
        # todo - 2 : 추측한 알파벳이 chosen_word에 없으면 lives를 1 감소시키세요.
        #  lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.
        if guess not in chosen_word:
            lives -= 1

            print(f"당신의 기회는 {lives}번 남았습니다.")

            if lives == 0:
                print("모든 기회를 잃었습니다.")
                end_of_game = True
                print(f"정답은 {chosen_word}입니다.")
        # todo - 4 : 사용자가 모든 문자를 맞췄는지 확인하세요 -> 정답을 맞췄다면 "정답입니다!!:)"를 출력하세요
        if "_" not in display:
            print("정답입니다:)")
            end_of_game = True
            break


        # print(display)
        # todo - 3 : display list의 모든 요소를 결합하여 문자열로 변환하세요.
        print(" ".join(display))
        print(stages[lives])

    #여기까지 작성했을 때 비어있는 점
    # 1. 로고
    # 2. word_list가 부족하다
    # 3. 혹시 테스트 해보고 유지 보수 및 리팩토링 지점이 있는지 확인할 필요가 있음. -> 함수화


play_hangman()