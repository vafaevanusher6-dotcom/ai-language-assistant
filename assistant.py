import random
from datetime import datetime

def run_bot():
    print("🤖 Welcome to AI Language Assistant v4!")

    name = input("Hi! What's your name? ")
    print(f"Nice to meet you, {name}! 😊")

    mood = input("How are you today? ")
    print("Thanks for sharing! 💬")

    start = input("Shall we start practicing? (yes / no): ").lower()
    if start != "yes":
        print("No problem! Come back anytime 👋")
        return

    language = input("Which language do you want to practice? (English / Korean): ").lower()

    print("\nChoose a topic:")
    print("1. Family")
    print("2. Hobbies")
    print("3. Work")
    print("4. Random topic")

    topic = input("Enter 1, 2, 3 or 4: ")

    questions = []

    english_topics = {
        "1": [
            "Can you tell me about your family?",
            "Who are you closest to in your family?",
            "Do you live with your family?"
        ],
        "2": [
            "What is your favorite hobby?",
            "How often do you do your hobby?",
            "Why do you like this hobby?"
        ],
        "3": [
            "What do you do for work or study?",
            "What do you like about your work or studies?",
            "What are your future career plans?"
        ]
    }

    korean_topics = {
        "1": [
            "가족에 대해 말해 주세요.",
            "가족 중에 누구와 가장 친해요?",
            "가족과 같이 살고 있어요?"
        ],
        "2": [
            "취미가 뭐예요?",
            "취미를 얼마나 자주 해요?",
            "왜 그 취미를 좋아해요?"
        ],
        "3": [
            "무슨 일을 하세요? 또는 무엇을 공부해요?",
            "일이나 공부에서 무엇이 좋아요?",
            "미래에 어떤 일을 하고 싶어요?"
        ]
    }

    if language == "english":
        topics = english_topics
    elif language == "korean":
        topics = korean_topics
    else:
        print("Sorry, this language is not supported yet.")
        return

    if topic == "4":
        topic = random.choice(list(topics.keys()))

    if topic not in topics:
        print("Invalid choice.")
        return

    try:
        num_questions = int(input("How many questions do you want? (1-3): "))
        num_questions = min(max(num_questions, 1), 3)
    except:
        num_questions = 2

    print("\n🎯 Let's start!\n")

    answers = []
    selected_questions = random.sample(topics[topic], num_questions)

    for q in selected_questions:
        print("Question:", q)
        ans = input("Your answer: ")
        answers.append(ans)

    score = random.randint(5, 7)

    print("\n📊 IELTS-style feedback:")
    print(f"Estimated speaking band: {score}.0")

    print("\n✅ Feedback:")
    if score <= 5:
        print("- Try to speak longer.")
        print("- Use simple but correct grammar.")
    elif score == 6:
        print("- Good job! Try to add more examples.")
        print("- Work on fluency.")
    else:
        print("- Very good! Try to use more complex sentences.")
        print("- Add opinions and reasons.")

    print("\n💡 Sample better answer:")
    print("I really enjoy my hobby because it helps me relax and improve myself. "
          "For example, I practice it several times a week and it gives me motivation.")

    save = input("\nDo you want to save your practice result? (yes / no): ").lower()
    if save == "yes":
        with open("practice_history.txt", "a", encoding="utf-8") as f:
            f.write(f"\n--- {datetime.now()} ---\n")
            f.write(f"Name: {name}\n")
            f.write(f"Language: {language}\n")
            for i, ans in enumerate(answers, 1):
                f.write(f"Answer {i}: {ans}\n")
            f.write(f"Score: {score}.0\n")
        print("📁 Your result was saved to practice_history.txt")

    print("\n🔥 Great job! You're improving every day.")
    print("Come back soon — I'll be waiting for you 🤝")


if __name__ == "__main__":
    run_bot()