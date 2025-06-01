import random

def guess_the_number():
    print("🌟 歡迎來到終極密碼：Python 初學者特別版 🌟")
    print("我已經偷偷選了一個 1 到 100 的整數，你猜猜是什麼？")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("請輸入你的猜測（1-100）："))
        except ValueError:
            print("拜託輸入整數好嗎😐")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("不要亂輸入範圍外的數字啦🥲")
        elif guess < number:
            print("太小了，再試一次 👇")
        elif guess > number:
            print("太大了，再試一次 👆")
        else:
            print(f"🎉 恭喜你猜對了！答案就是 {number}，你總共猜了 {attempts} 次。")
            break

if __name__ == "__main__":
    guess_the_number()
