import random
import time

class Homeless:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 1
        self.money = 30
        self.happy = 10
        self.isAlive = True
        self.slept_today = False  # Now toggles True/False
        self.time_of_day = 0
        self.slept = 0
        self.days = 0
        self.new_days = 0
        self.has_job = False
        self.days_since_work = 0
        self.days_until_reapply = 0
        self.worked_today = False

    def info(self):
        print(f"Name = {self.name} | Age = {self.age} | Health = {self.health} | Money = {self.money} | Happy = {self.happy} | Slept_today = {self.slept_today} | Time_of_day = {self.time_of_day} | Alive = {self.isAlive} | Days = {self.days} | Job = {'Yes' if self.has_job else 'No'}")

    def checkAlive(self):
        if self.happy <= 0 or self.money <= 0:
            self.isAlive = False
        if self.new_days == 12 and self.slept == 0:
            print("You haven't slept in 12 days... your body gave out.")
            self.isAlive = False
        if self.money >= 10000:
            print("You bought a car for going places and to live in... you have beaten the game!")
            self.isAlive = False

    def sleep(self, hours):
        if hours >= 15:
            print("ТА КУДИ ТАК БАГАТО СПАТИ?? А НУ ВСТАВАЙ!!")
        elif self.slept_today:
            print("Ти сьогодні спав! давай щось інше роби уже")
        else:
            self.happy += hours * 2
            self.slept = 1
            self.new_days = 0
            print(f"Він поспав.. він і так спить весь день тому він отримує {hours * 2} очки радості")
            self.slept_today = True  # Set to True after sleeping

        self.checkAlive()

    def update_day(self):
        self.time_of_day += 1
        if self.time_of_day == 3:
            self.new_days += 1
            self.days += 1
            self.time_of_day = 0
            self.slept_today = False  # Reset slept_today to False at the start of a new day

            if self.days % 365 == 0:
                self.age += 1

            if self.has_job:
                self.days_since_work += 1
                if self.days_since_work == 3:
                    print("You got kicked out of your job for not showing up for 3 days.")
                    self.has_job = False
                    self.days_until_reapply = 7

            if self.days_until_reapply > 0:
                self.days_until_reapply -= 1

            self.worked_today = False

    def go_do(self, hours):
        self.update_day()
        if self.money >= 50:
            self.money -= hours * 10
            self.happy += hours * 20
            print("You.. did something")
        else:
            print("Чим він буде цікавим заніматися без грошей?")
            self.happy -= 1

        self.checkAlive()

    def rob_a_bank(self):
        self.update_day()
        rng = random.randint(1, 2)
        self.happy += 70
        self.money += 400
        print("You robbed a bank.. you didn't have a gun but a banana worked.. you only robbed the cashiers")

        if rng == 1:
            print("You got caught by the cops and... yeah robbing a bank is basically a life sentence. (They took your money btw)")
            self.happy = 0
            self.money -= 400
            self.checkAlive()
        elif rng == 2:
            print("You got $400 out of those cashiers... I don't know how you did it, but you did.")

    def apply_for_a_job(self):
        self.update_day()
        if self.days_until_reapply > 0:
            print(f"You can't apply for a job for another {self.days_until_reapply} days.")
            return

        chance = random.randint(1, 20)
        if chance == 1:
            self.happy += 100
            self.has_job = True
            self.days_since_work = 0
            print("WOAH! you found a job. CONGRATS (there's another thing to worry about now lol)")
        else:
            self.happy -= 10
            print("You couldn't find a job and feel even sadder.")

    def go_to_work(self):
        if not self.has_job:
            print("You don't have a job to go to.")
            return

        if self.worked_today:
            print("You have already worked today.")
            return

        if self.time_of_day + 2 > 3:
            print("There's not enough time left in the day to go to work.")
            return

        self.money += 50
        self.days_since_work = 0
        self.time_of_day += 2
        self.worked_today = True
        print("You went to work and earned $50.")


Homeless = Homeless("poor guy")
print("Welcome to my game!")
while Homeless.isAlive:
    action = input("Type a command (go do, sleep, rob a bank(50% chance), apply for a job, go to work): ").lower()

    if action == "go do":
        hours = int(input("Скільки годин він буде робити щось? "))
        Homeless.go_do(hours)

    elif action == "sleep":
        hours = int(input("Скільки годин він буде спати? "))
        Homeless.sleep(hours)

    elif action == "rob a bank":
        Homeless.rob_a_bank()

    elif action == "apply for a job":
        Homeless.apply_for_a_job()

    elif action == "go to work":
        Homeless.go_to_work()

    Homeless.info()
    print("")
    print("Цікавий факт: три дії рахуются як день, що дозволяє тобі спати знову.")
    print("")

print(f"Sorry, but {Homeless.name} has passed away... Final stats:")
print("")
print("")
Homeless.info()
print("")
print("")
print("this will close in 60 seconds.. bye.")
print("")
print("")
time.sleep(60)
exit(1)
