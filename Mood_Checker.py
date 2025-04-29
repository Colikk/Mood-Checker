import time
import random

print("  __  __                 _    _____ _               _             ")
print(" |  \/  |               | |  / ____| |             | |            ")
print(" | \  / | ___   ___   __| | | |    | |__   ___  ___| | _____ _ __ ")
print(" | |\/| |/ _ \ / _ \ / _` | | |    | '_ \ / _ \/ __| |/ / _ \ '__|")
print(" | |  | | (_) | (_) | (_| | | |____| | | |  __/ (__|   <  __/ |   ")
print(" |_|  |_|\___/ \___/ \__,_|  \_____|_| |_|\___|\___|_|\_\___|_|   ")
time.sleep(1)

print("=============Options=============")
time.sleep(2)
print("1. Happy")
time.sleep(1)
print("2. Sad")
time.sleep(1)
print("3. Angry")
time.sleep(1)
print("4. Bad")
time.sleep(1)
print("5. Suprised")
time.sleep(1)
print("6. Disgusted")
time.sleep(1)
print("7. Fearful")

while True:
    mood = input("How are you feeling? ").strip()
    if mood in ["1", "2", "3", "4", "5", "6", "7"]:
        break
    else:
        print("❌ERROR: Please input a number 1-7")

if mood == "1":
    print("=============Happy=============")
    time.sleep(2)
    print("1. Playful")
    time.sleep(0.7)
    print("2. Content")
    time.sleep(0.7)
    print("3. Intrested")
    time.sleep(0.7)
    print("4. Proud")
    time.sleep(0.7)
    print("5. Accepted")
    time.sleep(0.7)
    print("6. Powerful")
    time.sleep(0.7)
    print("7. Peaceful")
    time.sleep(0.7)
    print("8. Trusting")
    time.sleep(0.7)
    print("9. Optimistic")

    while True:
        moodHappy = input("Which one best describes how you feel? ").strip()
        if moodHappy in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
           break
        else:
            print("❌ERROR: Please input a number 1-9")
    if moodHappy == "1":
        print("=============Playful=============")
        time.sleep(2)
        print("1. Aroused")
        time.sleep(0.7)
        print("2. Cheeky")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodPlayful = input("Which one best describes how you feel? ").strip()
            if moodPlayful in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")
        
        if moodPlayful == "1":
            mood = "Aroused"
            print("=============Message=============")
            print("When playful crosses the line into dangerous territory 😈... careful, you might start a fire.")

        if moodPlayful == "2":
            mood = "Cheeky"
            print("=============Message=============")
            print("Ohhh, feeling a little troublemaker energy today, huh? 😏 Try not to start too much chaos... or do.")

        if moodPlayful == "3":
            mood = "Playful"
            print("=============Message=============")
            print("Feeling playful? Todays the perfect day to cause just the right amount of chaos. 😎")

    elif moodHappy == "2":
        print("=============Content=============")
        time.sleep(2)
        print("1. Free")
        time.sleep(0.7)
        print("2. Joyful")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodContent = input("Which one best describes how you feel? ").strip()
            if moodContent in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodContent == "1":
            mood = "Free"
            print("=============Message=============")
            print("No chains, no limits. Just you, your dreams, and the whole damn sky. ☁️")

        if moodContent == "2":
            mood = "Joyful"
            print("=============Message=============")
            print("You're radiating joy like sunshine after a storm. 🌈 Keep shining.")

        if moodContent == "3":
            mood = "Content"
            print("=============Message=============")
            print("You're just... good. No rush, no worries, just vibes. 🛋️")

    elif moodHappy == "3":
        print("=============Interested=============")
        time.sleep(2)
        print("1. Curious")
        time.sleep(0.7)
        print("2. Inquisitive")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodInterested = input("Which one best describes how you feel? ").strip()
            if moodInterested in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodInterested == "1":
            mood = "Curious"
            print("=============Message=============")
            print("Curious minds always end up somewhere exciting... or chaotic. Either way, good luck. 🔥")

        if moodInterested == "2":
            mood = "Inquisitive"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: You've asked too many questions. Now you know *too much*. The FBI is on its way. 🚓👀")
            else:
                print("Asking questions most people dont even think about. Elite behavior. 🏆")

        if moodInterested == "3":
            mood = "Interested"
            print("=============Message=============")
            print("Somethings got your attention. Stay sharp — you might just find your next big thing. 🔎")

    elif moodHappy == "4":
        print("=============Proud=============")
        time.sleep(2)
        print("1. Successful")
        time.sleep(0.7)
        print("2. Confident")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodProud = input("Which one best describes how you feel? ").strip()
            if moodProud in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodProud == "1":
            mood = "Successful"
            print("=============Message=============")
            print("This is just the beginning. You're built for bigger wins. 🎯")

        if moodProud == "2":
            mood = "Confident"
            print("=============Message=============")
            print("Confidence: when you know you're the right person for the job because you made yourself that way. 👑")

        if moodProud == "3":
            mood = "Proud"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: You're so proud right now the Statue of Liberty just filed a copyright claim on your vibe. 🗽🔥")
            else:
                print("You've earned this moment. Stand tall — you're living proof that hard work pays off. 🏆")

    elif moodHappy == "5":
        print("=============Accepted=============")
        time.sleep(2)
        print("1. Respected")
        time.sleep(0.7)
        print("2. Valued")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodAccepted = input("Which one best describes how you feel? ").strip()
            if moodAccepted in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodAccepted == "1":
            mood = "Respected"
            print("=============Message=============")
            print("People see you. People listen. That's real respect. 🗣️✨")

        if moodAccepted == "2":
            mood = "Valued"
            print("=============Message=============")
            print("Your voice, your time, your presence — it all matters. Big time. 🕰️")

        if moodAccepted == "3":
            mood = "Accepted"
            print("=============Message=============")
            print("No need to force anything. You fit exactly where you're supposed to. 🧩")

    elif moodHappy == "6":
        print("=============Powerful=============")
        time.sleep(2)
        print("1. Courageous")
        time.sleep(0.7)
        print("2. Creative")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodPowerful = input("Which one best describes how you feel? ").strip()
            if moodPowerful in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodPowerful == "1":
            mood = "Courageous"
            print("=============Message=============")
            print("Courage isn't the absence of fear — it's doing it anyway. And you're doing it. 🎯")

        if moodPowerful == "2":
            mood = "Creative"
            print("=============Message=============")
            print("Every idea you breathe into life changes the world just a little. Keep going. 🛠️")

        if moodPowerful == "3":
            mood = "Powerful"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: You just hit a new power level. Warning: nearby small objects may now orbit you. 🪐💥")
            else:
                print("You're not just surviving — you're commanding your own story. 📖👑")

    elif moodHappy == "7":
        print("=============Peaceful=============")
        time.sleep(2)
        print("1. Loving")
        time.sleep(0.7)
        print("2. Thankful")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodPeaceful = input("Which one best describes how you feel? ").strip()
            if moodPeaceful in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodPeaceful == "1":
            mood = "Loving"
            print("=============Message=============")
            print("You're leading with love today. That's rare. And powerful. ✨")

        if moodPeaceful == "2":
            mood = "Thankful"
            print("=============Message=============")
            print("Gratitude turns what you have into enough — and more. 🛖➡️🏰")

        if moodPeaceful == "3":
            mood = "Peaceful"
            print("=============Message=============")
            print("You're floating above the noise. Keep that peace protected at all costs. 🛡️🕊️")

    elif moodHappy == "8":
        print("=============Trusting=============")
        time.sleep(2)
        print("1. Sensitive")
        time.sleep(0.7)
        print("2. Intimate")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodTrusting = input("Which one best describes how you feel? ").strip()
            if moodTrusting in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodTrusting == "1":
            mood = "Sensitive"
            print("=============Message=============")
            print("Being sensitive means you experience the world more richly. Never apologize for that. 🎨")

        if moodTrusting == "2":
            mood = "Intimate"
            print("=============Message=============")
            print("Opening up is scary — but you're doing it anyway. That's real strength. 🔥")

        if moodTrusting == "3":
            mood = "Trusting"
            print("=============Message=============")
            print("You're trusting. That means hope is alive and kicking in you. 🌱")

    elif moodHappy == "9":
        print("=============Optimistic=============")
        time.sleep(2)
        print("1. Hopeful")
        time.sleep(0.7)
        print("2. Inspired")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodOptimistic = input("Which one best describes how you feel? ").strip()
            if moodOptimistic in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodOptimistic == "1":
            mood = "Hopeful"
            print("=============Message=============")
            print("Hope isn't naïve — it's powerful. You're holding the line for better days. 🛡️🌈")

        if moodOptimistic == "2":
            mood = "Inspired"
            print("=============Message=============")
            print("Inspired people don't just see the world — they remake it. You're on the right path. 🔥")

        if moodOptimistic == "3":
            mood = "Optimistic"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Your optimism is so strong NASA just detected it from space. 🌎🛰️")
            else:
                print("Your optimism is contagious. Don't be surprised if you start a chain reaction. 🌟")

elif mood == "2":
    print("=============Sad=============")
    time.sleep(2)
    print("1. Lonely")
    time.sleep(0.7)
    print("2. Vulnerable")
    time.sleep(0.7)
    print("3. Despair")
    time.sleep(0.7)
    print("4. Guilty")
    time.sleep(0.7)
    print("5. Depressed")
    time.sleep(0.7)
    print("6. Hurt")

    while True:
        moodSad = input("Which one best describes how you feel? ").strip()
        if moodSad in ["1", "2", "3", "4", "5", "6"]:
           break
        else:
            print("❌ERROR: Please input a number 1-6")

    if moodSad == "1":
        print("=============Lonely=============")
        time.sleep(2)
        print("1. Isolated")
        time.sleep(0.7)
        print("2. Abandoned")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodLonely = input("Which one best describes how you feel? ").strip()
            if moodLonely in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodLonely == "1":
            mood = "Isolated"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Sometimes isolation isn't punishment — it's preparation. You're building strength nobody can see yet. 🏔️")
            else:
                print("You're in your own space right now — and even if it hurts, you're growing. 🌱")

        if moodLonely == "2":
            mood = "Abandoned"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: The ones who abandoned you never defined you. Your worth has always been yours alone. 🕯️")
            else:
                print("Being left behind doesn't define you. What you build next does. 🏗️")

        if moodLonely == "3":
            mood = "Lonely"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Even when you feel invisible, the universe still sees you. You're not lost — just finding a new path. 🌌")
            else:
                print("Lonely moments hurt, but they also teach you how strong you really are. 🛡️")

    elif moodSad == "2":
        print("=============Vulnerable=============")
        time.sleep(2)
        print("1. Victimized")
        time.sleep(0.7)
        print("2. Fragile")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodVulnerable = input("Which one best describes how you feel? ").strip()
            if moodVulnerable in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodVulnerable == "1":
            mood = "Victimized"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: They hurt you thinking you would stay broken. Your existence is already your revenge. 🌹")
            else:
                print("Vulnerability isn't weakness. It's honesty with no armor on. 🖤")

        if moodVulnerable == "2":
            mood = "Fragile"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Fragility is not failure. Even the strongest materials crack before they reshape into something new. 🔥")
            else:
                print("Feeling fragile doesn't mean you'll shatter. It means you need care — and you deserve it. 🌸")

        if moodVulnerable == "3":
            mood = "Vulnerable"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: True strength isn't hiding your wounds — it's surviving with them. You're stronger than you know. 🖤")
            else:
                print("Vulnerability isn't weakness. It's honesty with no armor on. 🖤")

    elif moodSad == "3":
        print("=============Despair=============")
        time.sleep(2)
        print("1. Grief")
        time.sleep(0.7)
        print("2. Powerless")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodDespair = input("Which one best describes how you feel? ").strip()
            if moodDespair in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodDespair == "1":
            mood = "Grief"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Grief doesn't erase love — it proves it existed. Your heart is still alive. 🕊️")
            else:
                print("You're carrying something heavy — and you're doing it with more strength than you realize. 🛡️")

        if moodDespair == "2":
            mood = "Powerless"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Power isn't always force. Sometimes it's the quiet decision to not give up today. 🖤")
            else:
                print("Powerlessness isn't permanent. Even broken wings heal over time. 🕊️")

        if moodDespair == "3":
            mood = "Despair"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Even when everything feels lost, the smallest spark of you still burns. That's enough to rebuild. 🔥")
            else:
                print("It's okay to admit when it feels like the light is gone. Just don't forget — darkness doesn't last forever. 🌑")

    elif moodSad == "4":
        print("=============Guilty=============")
        time.sleep(2)
        print("1. Ashamed")
        time.sleep(0.7)
        print("2. Remorseful")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodGuilty = input("Which one best describes how you feel? ").strip()
            if moodGuilty in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodGuilty == "1":
            mood = "Ashamed"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Shame whispers lies about who you are. The truth? You're still worthy, still growing. 🌱")
            else:
                print("You're not defined by your worst moments. You're the full story — not a single page. 📖")

        if moodGuilty == "2":
            mood = "Remorseful"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Remorse hurts because you have a heart. Don't let pain make you forget your humanity. 🤍")
            else:
                print("You can't undo the past. But you can rewrite the future with what you know now. ✍️")

        if moodGuilty == "3":
            mood = "Guilty"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Guilt is a heavy thing, but it means your conscience is alive. That spark can still light the way. 🕯️")
            else:
                print("Guilt means you care about doing right. It's not the enemy — it's the signal. 🛑")

    elif moodSad == "5":
        print("=============Depressed=============")
        time.sleep(2)
        print("1. Empty")
        time.sleep(0.7)
        print("2. Inferior")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodDepressed = input("Which one best describes how you feel? ").strip()
            if moodDepressed in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodDepressed == "1":
            mood = "Empty"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Feeling empty means you've survived every battle so far. You're not broken — you're rebuilding. 🛠️")
            else:
                print("Feeling empty doesn't mean there's nothing inside you — it means you've been carrying too much for too long. 🛑")

        if moodDepressed == "2":
            mood = "Inferior"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: The ones who seem bigger aren't better — they're just different. Your path is your own. 🛤️")
            else:
                print("Inferiority feelings don't define your reality. Your existence alone already proves you're enough. 🌟")

        if moodDepressed == "3":
            mood = "Depressed"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Depression doesn't erase your worth. Even in the dark, you're still made of stars. 🌌")
            else:
                print("You're still breathing, still fighting, even when it feels pointless. That's strength most people never see. 🥊")

    elif moodSad == "6":
        print("=============Hurt=============")
        time.sleep(2)
        print("1. Embarrassed")
        time.sleep(0.7)
        print("2. Disappointed")
        time.sleep(0.7)
        print("3. N/A")
        
        while True:
            moodHurt = input("Which one best describes how you feel? ").strip()
            if moodHurt in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodHurt == "1":
            mood = "Embarrassed"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Embarrassment fades, but the courage to show up leaves a permanent mark. 💬")
            else:
                print("Embarrassment fades faster than it feels. What matters is you showed up. 👣")

        if moodHurt == "2":
            mood = "Disappointed"
            print("=============Message=============")
            if random.randint(1, 20) == 1:
                print("🔒 SECRET UNLOCKED: Disappointment stings, but it never means you dreamed too big. Dream bigger. 🚀")
            else:
                print("Being disappointed means you had standards. That's not a flaw. 🎯")

        if moodHurt == "3":
            mood = "Hurt"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Hurt is the price of living with your heart open. It means you're still in the fight. 🖤")
            else:
                print("Hurt is the proof that you opened yourself up to something real. Healing will come. 🌱")

elif mood == "3":
    print("=============Angry=============")
    time.sleep(2)
    print("1. Let down")
    time.sleep(0.7)
    print("2. Humiliated")
    time.sleep(0.7)
    print("3. Bitter")
    time.sleep(0.7)
    print("4. Mad")
    time.sleep(0.7)
    print("5. Aggressive")
    time.sleep(0.7)
    print("6. Frustrated")
    time.sleep(0.7)
    print("7. Distant")
    time.sleep(0.7)
    print("8. Critical")

    while True:
        moodAngry = input("Which one best describes how you feel? ").strip()
        if moodAngry in ["1", "2", "3", "4", "5", "6", "7", "8"]:
           break
        else:
            print("❌ERROR: Please input a number 1-8")

    if moodAngry == "1":
        print("=============Let down=============")
        time.sleep(2)
        print("1. Betrayed")
        time.sleep(0.7)
        print("2. Resentful")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodLetdown = input("Which one best describes how you feel? ").strip()
            if moodLetdown in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodLetdown == "1":
            mood = "Betrayed"
            print("=============Message=============")
            print("The betrayal wasn't your fault. Their loyalty broke, not your worth. 🔥")

        if moodLetdown == "2":
            mood = "Resentful"
            print("=============Message=============")
            print("Holding on too long burns you more than them. Heal for yourself, not for them. 🔥")

        if moodLetdown == "3":
            mood = "Let down"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Being let down doesn't diminish your worth. It proves your loyalty runs deeper than most can handle. 🛡️")
            else:
                print("You expected more because you deserved more. Don't lower your standards. 🔥")

    elif moodAngry == "2":
        print("=============Humiliated=============")
        time.sleep(2)
        print("1. Disrespected")
        time.sleep(0.7)
        print("2. Ridiculed")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodHumiliated = input("Which one best describes how you feel? ").strip()
            if moodHumiliated in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodHumiliated == "1":
            mood = "Disrepected"
            print("=============Message=============")
            print("Respect isn't a gift — it's a reflection. Their disrespect says nothing about your worth. 🖤")

        if moodHumiliated == "2":
            mood = "Ridiculed"
            print("=============Message=============")
            print("They laugh because they're uncomfortable with your light. Don't dim it. 🌟")

        if moodHumiliated == "3":
            mood = "Humiliated"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: They tried to humiliate you. Instead, they revealed your resilience. Keep standing. 🛡️")
            else:
                print("Humiliation stings because your dignity matters. Don't let temporary shame erase permanent worth. 🛡️")

    elif moodAngry == "3":
        print("=============Bitter=============")
        time.sleep(2)
        print("1. Indignant")
        time.sleep(0.7)
        print("2. Violated")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodBitter = input("Which one best describes how you feel? ").strip()
            if moodBitter in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodBitter == "1":
            mood = "Indignant"
            print("=============Message=============")
            print("Indignation is righteous anger — it means your soul recognizes injustice. ⚡")

        if moodBitter == "2":
            mood = "Violated"
            print("=============Message=============")
            print("What happened wasn't okay. Your reaction is proof that your self-respect is alive. 🖤")

        if moodBitter == "3":
            mood = "Bitter"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Bitterness is unhealed hurt — but underneath, your heart still hopes for better. That hope is power. 🖤")
            else:
                print("You're allowed to be bitter about what hurt you. You're just not meant to stay there forever. 🌱")

    elif moodAngry == "4":
        print("=============Mad=============")
        time.sleep(2)
        print("1. Furious")
        time.sleep(0.7)
        print("2. Jealous")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodMad = input("Which one best describes how you feel? ").strip()
            if moodMad in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodMad == "1":
            mood = "Furious"
            print("=============Message=============")
            print("Fury is fire. It can burn everything down — or forge something unbreakable. 🔥⚒️")

        if moodMad == "2":
            mood = "Jealous"
            print("=============Message=============")
            print("When you feel jealousy, it's a sign you're hungry for something real. Use it to build, not destroy. 🛠️")

        if moodMad == "3":
            mood = "Mad"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Your anger is real — but your power is what you do with it next. Build, don't burn. 🛡️")
            else:
                print("Being mad doesn't make you wrong — it means your boundaries are waking up. 🛡️")

    elif moodAngry == "5":
        print("=============Aggressive=============")
        time.sleep(2)
        print("1. Provoked")
        time.sleep(0.7)
        print("2. Hostile")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodAggressive = input("Which one best describes how you feel? ").strip()
            if moodAggressive in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodAggressive == "1":
            mood = "Provoked"
            print("=============Message=============")
            print("You didn't wake up mad — someone pushed you there. Recognize that. 🎯")

        if moodAggressive == "2":
            mood = "Hostile"
            print("=============Message=============")
            print("Hostility is a shield. Underneath it, there's usually hurt. 🛡️")

        if moodAggressive == "3":
            mood = "Aggressive"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Aggression is raw fire. Forge it — don't fear it. You can shape anything with enough heat. 🔥⚒️")
            else:
                print("Aggression is energy. Control it, and you can move mountains. 🏔️")

    elif moodAngry == "6":
        print("=============Frustrated=============")
        time.sleep(2)
        print("1. Infuriated")
        time.sleep(0.7)
        print("2. Annoyed")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodFrustrated = input("Which one best describes how you feel? ").strip()
            if moodFrustrated in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodFrustrated == "1":
            mood = "Infuriated"
            print("=============Message=============")
            print("Anger at its peak shows where your real values are. That's powerful information. 🧠")

        if moodFrustrated == "2":
            mood = "Annoyed"
            print("=============Message=============")
            print("Annoyance is the mind's way of saying 'this isn't worth my energy.' Listen to it. 🎧")

        if moodFrustrated == "3":
            mood = "Frustrated"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Frustration is the pressure before the floodgate breaks. You're closer than you think. 🛠️⚡")
            else:
                print("Frustration isn't failure — it's friction before the breakthrough. 🛠️")

    elif moodAngry == "7":
        print("=============Distant=============")
        time.sleep(2)
        print("1. Withdrawn")
        time.sleep(0.7)
        print("2. Numb")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodDistant = input("Which one best describes how you feel? ").strip()
            if moodDistant in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodDistant == "1":
            mood = "Withdrawn"
            print("=============Message=============")
            print("When you withdraw, you're protecting the parts of you that still need healing. 🛡️")

        if moodDistant == "2":
            mood = "Numb"
            print("=============Message=============")
            print("Numbness fades eventually. You're still alive underneath it all. ❤️‍🩹")

        if moodDistant == "3":
            mood = "Distant"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Distance doesn't make you lost. It's part of how you find your way back stronger. 🌌")
            else:
                print("Pulling away isn't quitting. It's protecting peace when you're overstretched. 🛡️")

    elif moodAngry == "8":
        print("=============Critical=============")
        time.sleep(2)
        print("1. Skeptical")
        time.sleep(0.7)
        print("2. Dismissive")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodCritical = input("Which one best describes how you feel? ").strip()
            if moodCritical in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodCritical == "1":
            mood = "Skeptical"
            print("=============Message=============")
            print("Trust takes time to rebuild — and it should. Skepticism keeps your heart safe while it heals. 🛡️")

        if moodCritical == "2":
            mood = "Dismissive"
            print("=============Message=============")
            print("Dismissiveness can be armor — just don't let it become a wall that keeps the good out too. 🧱")

        if moodCritical == "3":
            mood = "Critical"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Critical minds shape sharper futures. Doubt isn't weakness — it's awareness. 🧠")
            else:
                print("You're not wrong for seeing flaws — just remember, building is harder than tearing down. 🏗️")
        
elif mood == "4":
    print("=============Bad=============")
    time.sleep(2)
    print("1. Bored")
    time.sleep(0.7)
    print("2. Busy")
    time.sleep(0.7)
    print("3. Stressed")
    time.sleep(0.7)
    print("4. Tired")

    while True:
        moodBad = input("Which one best describes how you feel? ").strip()
        if moodBad in ["1", "2", "3", "4"]:
           break
        else:
            print("❌ERROR: Please input a number 1-4")

    if moodBad == "1":
        print("=============Bored=============")
        time.sleep(2)
        print("1. Indifferent")
        time.sleep(0.7)
        print("2. Apathetic")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodBored = input("Which one best describes how you feel? ").strip()
            if moodBored in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodBored == "1":
            mood = "Indifferent"
            print("=============Message=============")
            print("Feeling indifferent doesn't mean you don't care — it means you're tired of pretending. 🎭")

        if moodBored == "2":
            mood = "Apathetic"
            print("=============Message=============")
            print("Apathy is exhaustion, not emptiness. Your spark is still there. 🕯️")

        if moodBored == "3":
            mood = "Bored"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Boredom is the whisper of unrealized potential. You're closer to something new than you think. 🚀")
            else:
                print("Bored minds are restless minds. Restlessness builds dreamers. 🚀")

    elif moodBad == "2":
        print("=============Busy=============")
        time.sleep(2)
        print("1. Pressured")
        time.sleep(0.7)
        print("2. Rushed")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodBusy = input("Which one best describes how you feel? ").strip()
            if moodBusy in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodBusy == "1":
            mood = "Pressured"
            print("=============Message=============")
            print("The weight you're carrying proves how much you're capable of — but strength doesn't mean carrying it all alone. 🧱")

        if moodBusy == "2":
            mood = "Rushed"
            print("=============Message=============")
            print("Rushing steals peace faster than anything else. Breathe — the moment is still yours. 🕰️")

        if moodBusy == "3":
            mood = "Busy"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Busyness is noise. Stillness is strength. Don't lose your direction. 🧭")
            else:
                print("Busy is a season, not a lifestyle. Don't lose yourself in it. 🛤️")

    elif moodBad == "3":
        print("=============Stressed=============")
        time.sleep(2)
        print("1. Overwhelmed")
        time.sleep(0.7)
        print("2. Out of control")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodStressed = input("Which one best describes how you feel? ").strip()
            if moodStressed in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodStressed == "1":
            mood = "Overwhelmed"
            print("=============Message=============")
            print("You don't have to fix it all today. Tiny wins are still wins. 🎯")

        if moodStressed == "2":
            mood = "Out of control"
            print("=============Message=============")
            print("Feeling out of control doesn't mean you're doomed. Regaining ground starts with one choice. 🛡️")

        if moodStressed == "3":
            mood = "Stressed"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Stress tests your limits. Peace rebuilds them. Take your power back one breath at a time. 🌬️🛡️")
            else:
                print("You're not weak because you're stressed — you're human because you feel it. 🛡️")

    elif moodBad == "4":
        print("=============Tired=============")
        time.sleep(2)
        print("1. Sleepy")
        time.sleep(0.7)
        print("2. Unfocused")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodTired = input("Which one best describes how you feel? ").strip()
            if moodTired in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodTired == "1":
            mood = "Sleepy"
            print("=============Message=============")
            print("Sleepiness isn't the enemy. Exhaustion is. Refuel before you crash. 🔋")

        if moodTired == "2":
            mood = "Unfocused"
            print("=============Message=============")
            print("You're not failing because you're unfocused. You're tired because you've been giving your all. 🛡️")

        if moodTired == "3":
            mood = "Tired"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Tired doesn't mean defeated. It means you're ready to rise again — after you rest. 🛏️⚡")
            else:
                print("Rest isn't earned — it's necessary. Even machines need downtime. 🔋")

elif mood == "5":
    print("=============Surprised=============")
    time.sleep(2)
    print("1. Startled")
    time.sleep(0.7)
    print("2. Confused")
    time.sleep(0.7)
    print("3. Amazed")
    time.sleep(0.7)
    print("4. Excited")

    while True:
        moodSurprised = input("Which one best describes how you feel? ").strip()
        if moodSurprised in ["1", "2", "3", "4"]:
           break
        else:
            print("❌ERROR: Please input a number 1-4")

    if moodSurprised == "1":
        print("=============Startled=============")
        time.sleep(2)
        print("1. Shocked")
        time.sleep(0.7)
        print("2. Dismayed")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodStartled = input("Which one best describes how you feel? ").strip()
            if moodStartled in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodStartled == "1":
            mood = "Shocked"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Shock is loud, but your spirit is louder. You're built for storms. 🌩️🛡️")
            else:
                print("Even in shock, your mind is working — protecting you, preparing you. 🧠")

        if moodStartled == "2":
            mood = "Dismayed"
            print("=============Message=============")
            print("Dismay tries to freeze you. Compassion — especially for yourself — melts it. 🧡")

        if moodStartled == "3":
            mood = "Startled"
            print("=============Message=============")
            print("Startled is the body's fast-forward button. Ride the energy, don't fight it. 🌪️")

    elif moodSurprised == "2":
        print("=============Confused=============")
        time.sleep(2)
        print("1. Disillusioned")
        time.sleep(0.7)
        print("2. Perplexed")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodConfused = input("Which one best describes how you feel? ").strip()
            if moodConfused in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodConfused == "1":
            mood = "Disillusioned"
            print("=============Message=============")
            print("Being disillusioned hurts — but it means you're waking up to truth. 👁️🛡️")

        if moodConfused == "2":
            mood = "Perplexed"
            print("=============Message=============")
            print("Being perplexed means you're asking better questions than the world has answers for. 🧠")

        if moodConfused == "3":
            mood = "Confused"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Confusion is the birthplace of real understanding. Keep asking questions. 🧠🔎")
            else:
                print("You're not lost — you're just on the edge of new territory. 🚀")

    elif moodSurprised == "3":
        print("=============Amazed=============")
        time.sleep(2)
        print("1. Astonished")
        time.sleep(0.7)
        print("2. Awe")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodAmazed = input("Which one best describes how you feel? ").strip()
            if moodAmazed in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodAmazed == "1":
            mood = "Astonished"
            print("=============Message=============")
            print("You’re living a story that you didn't see coming — and that's part of the magic. 📖")

        if moodAmazed == "2":
            mood = "Awe"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Awe isn't weakness — it's the oldest kind of power. You're touching something eternal. 🌌🛡️")
            else:
                print("Awe humbles the mind and lifts the soul. Let it fill you. 🌟")

        if moodAmazed == "3":
            mood = "Amazed"
            print("=============Message=============")
            print("Amazement is a reminder that not everything can be planned — some things are meant to surprise you. 🎁")

    elif moodSurprised == "4":
        print("=============Excited=============")
        time.sleep(2)
        print("1. Eager")
        time.sleep(0.7)
        print("2. Energetic")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodExcited = input("Which one best describes how you feel? ").strip()
            if moodExcited in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodExcited == "1":
            mood = "Eager"
            print("=============Message=============")
            print("Eagerness is pure momentum. Aim it where your heart truly wants to go. 🎯")

        if moodExcited == "2":
            mood = "Energetic"
            print("=============Message=============")
            print("You’re moving faster because your spirit's catching up to your dreams. 🌟")

        if moodExcited == "3":
            mood = "Excited"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Excitement is sacred fuel. Aim it, focus it, unleash it. 🚀🛡️")
            else:
                print("Feeling excited means something good is within reach. Keep moving toward it. 🚀")

elif mood == "6":
    print("=============Disgusted=============")
    time.sleep(2)
    print("1. Disapproving")
    time.sleep(0.7)
    print("2. Disappointed")
    time.sleep(0.7)
    print("3. Awful")
    time.sleep(0.7)
    print("4. Repelled")

    while True:
        moodDisgusted = input("Which one best describes how you feel? ").strip()
        if moodDisgusted in ["1", "2", "3", "4"]:
           break
        else:
            print("❌ERROR: Please input a number 1-4")

    if moodDisgusted == "1":
        print("=============Disapproving=============")
        time.sleep(2)
        print("1. Judgmental")
        time.sleep(0.7)
        print("2. Embarrassed")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodDisapproving = input("Which one best describes how you feel? ").strip()
            if moodDisapproving in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodDisapproving == "1":
            mood = "Judgmental"
            print("=============Message=============")
            print("Judgment often protects the heart from what once hurt it. Be gentle with yourself. 🕯️")

        if moodDisapproving == "2":
            mood = "Embarrassed"
            print("=============Message=============")
            print("Embarrassment humbles you — but it doesn't define you. 🌱")

        if moodDisapproving == "3":
            mood = "Disapproving"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Disapproval without cruelty is strength. You're guarding what matters. 🛡️")
            else:
                print("Standing firm in disapproval isn't cold — it's clarity. 🛤️")

    elif moodDisgusted == "2":
        print("=============Disappointed=============")
        time.sleep(2)
        print("1. Appalled")
        time.sleep(0.7)
        print("2. Revolted")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodDisappointed = input("Which one best describes how you feel? ").strip()
            if moodDisappointed in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodDisappointed == "1":
            mood = "Appalled"
            print("=============Message=============")
            print("You're reacting because your spirit refuses to accept less. Honor that. 🧠")

        if moodDisappointed == "2":
            mood = "Revolted"
            print("=============Message=============")
            print("Being revolted shows you still have a powerful sense of right and wrong. ⚖️")

        if moodDisappointed == "3":
            mood = "Disappointed"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Disappointment means you believed. That belief can still build something stronger. 🛡️🌱")
            else:
                print("Being disappointed doesn't make you naive. It means you cared enough to expect better. 🛡️")

    elif moodDisgusted == "3":
        print("=============Awful=============")
        time.sleep(2)
        print("1. Nauseated")
        time.sleep(0.7)
        print("2. Detestable")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodAwful = input("Which one best describes how you feel? ").strip()
            if moodAwful in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodAwful == "1":
            mood = "Nauseated"
            print("=============Message=============")
            print("Nausea is your body's raw truth detector. Something isn't sitting right — and that matters. 🧠")

        if moodAwful == "2":
            mood = "Detestable"
            print("=============Message=============")
            print("Not everything deserves your forgiveness or acceptance. Protect your standards. 🎯")

        if moodAwful == "3":
            mood = "Awful"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Awful moments pass. What stays is the strength you gain surviving them. 🛡️🌱")
            else:
                print("Awfulness feels endless when you're inside it. It never is. 🌅")

    elif moodDisgusted == "4":
        print("=============Repelled=============")
        time.sleep(2)
        print("1. Horrified")
        time.sleep(0.7)
        print("2. Hesitant")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodRepelled = input("Which one best describes how you feel? ").strip()
            if moodRepelled in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodRepelled == "1":
            mood = "Horrified"
            print("=============Message=============")
            print("Horrified today, wiser tomorrow. You're growing even when it hurts. 🌱")

        if moodRepelled == "2":
            mood = "Hesitant"
            print("=============Message=============")
            print("Hesitation doesn't mean you're wrong — it means you're thinking. That's wisdom. 🧠")

        if moodRepelled == "3":
            mood = "Repelled"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Instincts aren't obstacles — they're ancient armor. Trust the signal when you feel repelled. 🛡️⚡")
            else:
                print("Feeling repelled isn't weakness — it's instinct protecting you from harm. 🛡️")

elif mood == "7":
    print("=============Fearful=============")
    time.sleep(2)
    print("1. Scared")
    time.sleep(0.7)
    print("2. Anxious")
    time.sleep(0.7)
    print("3. Insecure")
    time.sleep(0.7)
    print("4. Weak")
    time.sleep(0.7)
    print("5. Rejected")
    time.sleep(0.7)
    print("6. Threatened")

    while True:
        moodFearful = input("Which one best describes how you feel? ").strip()
        if moodFearful in ["1", "2", "3", "4", "5", "6"]:
           break
        else:
            print("❌ERROR: Please input a number 1-6")

    if moodFearful == "1":
        print("=============Scared=============")
        time.sleep(2)
        print("1. Helpless")
        time.sleep(0.7)
        print("2. Frightened")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodScared = input("Which one best describes how you feel? ").strip()
            if moodScared in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodScared == "1":
            mood = "Helpless"
            print("=============Message=============")
            print("Feeling helpless doesn't mean you are helpless. Even a breath is an act of power. 🌬️")

        if moodScared == "2":
            mood = "Frighened"
            print("=============Message=============")
            print("Fright tells you danger is near. Wisdom is knowing not all fear needs to be obeyed. 🧠")

        if moodScared == "3":
            mood = "Scared"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Fear only visits when you're close to leveling up. Keep walking. 🛡️🚶‍♂️")
            else:
                print("Fear shows up when you're close to something important. You're braver than you feel right now. 🛡️")

    elif moodFearful == "2":
        print("=============Anxious=============")
        time.sleep(2)
        print("1. Overwhelmed")
        time.sleep(0.7)
        print("2. Worried")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodAnxious = input("Which one best describes how you feel? ").strip()
            if moodAnxious in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodAnxious == "1":
            mood = "Overwhelmed"
            print("=============Message=============")
            print("You don't have to do it all right now. One breath. One step. That's enough. 🌱")

        if moodAnxious == "2":
            mood = "Worried"
            print("=============Message=============")
            print("Most of what we worry about never happens. Don't borrow trouble from tomorrow. 🌅")

        if moodAnxious == "3":
            mood = "Anxious"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Anxiety doesn't control you. You're the storm's center — not its prisoner. 🌪️🛡️")
            else:
                print("Anxiety lies — it makes small problems feel massive. Breathe and take back your power. 🌬️")

    elif moodFearful == "3":
        print("=============Insecure=============")
        time.sleep(2)
        print("1. Inadequate")
        time.sleep(0.7)
        print("2. Inferior")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodInsecure = input("Which one best describes how you feel? ").strip()
            if moodInsecure in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodInsecure == "1":
            mood = "Inadequate"
            print("=============Message=============")
            print("Not measuring up today doesn't erase your worth. You're a whole story, not a single scene. 📖")

        if moodInsecure == "2":
            mood = "Inferior"
            print("=============Message=============")
            print("Comparison steals peace. You're running your own race. 🏃‍♂️")

        if moodInsecure == "3":
            mood = "Insecure"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Insecurity speaks in fear. Your spirit speaks louder — when you listen. 🛡️")
            else:
                print("Insecurity thrives in silence. Remind yourself of every mountain you've already climbed. 🏔️")

    elif moodFearful == "4":
        print("=============Weak=============")
        time.sleep(2)
        print("1. Worthless")
        time.sleep(0.7)
        print("2. Insignificant")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodWeak = input("Which one best describes how you feel? ").strip()
            if moodWeak in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodWeak == "1":
            mood = "Worthless"
            print("=============Message=============")
            print("No mistake, no failure, no low moment can erase your existence's worth. 🌟")

        if moodWeak == "2":
            mood = "Insignificant"
            print("=============Message=============")
            print("Insignificance is the enemy's lie. Your story matters — even if no one reads it yet. 📖")

        if moodWeak == "3":
            mood = "Weak"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Weakness isn't defeat. It's the seed of the next version of you. 🌱🛡️")
            else:
                print("Weakness isn't failure — it's the body and mind asking for rest, not surrender. 🛏️")

    elif moodFearful == "5":
        print("=============Rejected=============")
        time.sleep(2)
        print("1. Excluded")
        time.sleep(0.7)
        print("2. Persecuted")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodRejected = input("Which one best describes how you feel? ").strip()
            if moodRejected in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodRejected == "1":
            mood = "Excluded"
            print("=============Message=============")
            print("You weren't kicked out — you outgrew the space they could offer. 📈")

        if moodRejected == "2":
            mood = "Persecuted"
            print("=============Message=============")
            print("You were never meant to fit into small spaces. They feared what they couldn't control. 🔥")

        if moodRejected == "3":
            mood = "Rejected"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Rejection isn't the end. It's proof you were never meant to fit in cages. 🕊️")
            else:
                print("You're not for everyone — and you're not supposed to be. 🌟")


    elif moodFearful == "6":
        print("=============Threatened=============")
        time.sleep(2)
        print("1. Nervous")
        time.sleep(0.7)
        print("2. Exposed")
        time.sleep(0.7)
        print("3. N/A")

        while True:
            moodThreatened = input("Which one best describes how you feel? ").strip()
            if moodThreatened in ["1", "2", "3"]:
                break
            else:
                print("❌ERROR: Please input a number 1-3")

        if moodThreatened == "1":
            mood = "Nervous"
            print("=============Message=============")
            print("Feeling nervous isn't a stop sign. It's just a sign you're stepping out of the old limits. 🚶‍♂️")

        if moodThreatened == "2":
            mood = "Exposed"
            print("=============Message=============")
            print("Being exposed hurts, but it also lets the right people find the real you. 🕯️")

        if moodThreatened == "3":
            mood = "Threatened"
            print("=============Message=============")
            if random.randint(1, 20) == 1:  # 1 in 20 chance
                print("🔒 SECRET UNLOCKED: Feeling threatened is instinct — but rising anyway is power. 🛡️⚡")
            else:
                print("Threat is fear trying to protect you. Strength is deciding how you respond. ⚔️")

import os
from datetime import datetime

log_file = os.path.join("mood_log.txt")

print("=============Log=============")
time.sleep(1)
while True:
    log_mood = input("Would you like to talk about why you feel this way? (yes/no) ").strip().lower()
    if log_mood in ["yes", "no"]:
        break
    else:
        time.sleep(0.5)
        print("❌ERROR: Please put 'yes' or 'no'")

if log_mood == "yes":
    details = input("Type anything you'd like to say: ")

    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"{timestamp} | Mood: {mood} | Reason: {details}\n")
    
    print("📒 Your thoughts were saved.")

elif log_mood == "no":
    print("No worries, moving on! 💖")

    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"{timestamp} | Mood: {mood} | Reason: Not Given\n")
