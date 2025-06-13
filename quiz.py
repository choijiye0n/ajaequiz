import random

questions = [
    {"q": "자동차가 웃으면?", "a": "카카오"},
    {"q": "물고기가 싫어하는 컴퓨터는?", "a": "아쿠아"},
    {"q": "고양이가 컴퓨터를 하면?", "a": "캣북"},
    {"q": "소가 노래를 부르면?", "a": "음메"},
    {"q": "이불을 깨물면?", "a": "이불킥"}
]

def quiz_game():
    print("아재개그 퀴즈 게임을 시작합니다!")
    print("틀리면 게임이 종료됩니다. 잘 맞혀보세요!\n")
    score = 0
    asked = []

    while True:
        # 안 나온 문제만 선택
        remaining = [q for q in questions if q not in asked]
        if not remaining:
            print("모든 문제를 맞혔습니다! 축하합니다!")
            break

        q = random.choice(remaining)
        asked.append(q)

        print(f"문제: {q['q']}")
        answer = input("정답은? ").strip()

        if answer == q["a"]:
            score += 1
            print(f"정답입니다! 현재 점수: {score}\n")
        else:
            print(f"틀렸습니다! 정답은 '{q['a']}'였어요.")
            print(f"최종 점수: {score}점")
            break

if __name__ == "__main__":
    quiz_game()
