# task 1.1

name = input("Introduce yourself: ")

print(f"Hi, how are you {name}")

# task 1.2

mood = input("How are you feeling? ")

if mood == "Happy":
    print("Im happy that youre happy")
elif mood == "Sad":
    print("Let me give you a hug")
else:
    print("Im proud of you")
    
    
# task 1.3
name = input("Introduce yourself: ")

invalid = False

for char in name:
    if not char.isalpha():
        print("Invalid name")
        invalid = True
        break


if not invalid:
    
    print(f"Hi, how are you {name}")

# task 2.1 

def add(num1, num2):
    sum = 0
    sum = num1 + num2
    return sum

def minus(num1, num2):
    difference = 0
    difference = num1 - num2
    return  difference

def multi(num1, num2):
    product = 0
    product = num1 * num2
    return product

def divide(num1, num2):  #task 2.3
    quotient = 0
    if num2 == 0:
        quotient = "Error"
    elif num1 == 0:
        quotient = 0
    else:
        quotient = num1 / num2
    return quotient

# task 2.2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("What operator do you want to use: ")

# task 3.1

def cel_to_fah(celsius):
    # °F = (9/5 × °C) + 32.   
    fahrenheit = ((9 /5) * celsius) + 32
    return fahrenheit

# task 3.2

def fah_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    
    return celsius

# task 3.3
conversion = input("which conversion do you want c->f or f->c? ")

degree = int(input("Input the degree to convert: "))

if conversion == "c->f":
    print(cel_to_fah(degree))
elif conversion == "f->c":
    print(fah_to_cel(degree))
else:
    print("you entered the wrong conversion")
    
# task 4.1
def push_back(item, list):
    list.append(item)
    
# task 4.2
def remv(item, list):
    list.remove(item)
    
# task 4.3
def print_list(list):
    for item in list:
        print(list[item])
    
# task 5.1

def avg(list_grade):
    sum = 0
    
    for i in list_grade:
        sum += i
    
    avg = sum / list_grade.size()
    
    return avg

# task 5.2

def min_max(list_grade):
    min = min(list_grade)
    max = max(list_grade)
    
    return min, max

# task 5.3

def grade_catergorize(list_grade):
    letter_grade = []
    
    for grade in list_grade:
        if grade >= 90:
            letter_grade.append("A")
        elif grade >= 80:
            letter_grade.append("B")
        elif grade >= 70:
            letter_grade.append("C")
        elif grade >= 60:
            letter_grade.append("D")       
        else:
            letter_grade.append("F") 
            
    return letter_grade

# task 6.1

def add_task(task, time, schedule):
    
    for i in range(len(schedule)):
        if i == time:
            schedule.push_back(task)
            
            
# task 6.2
def remv_task(task, time, schedule):
    
    for i in range(len(schedule)):
        if schedule[i] == task:
            schedule.remove(task)
            
# task 6.3
def display(schedule):
    for i in range(len(schedule)):
        print(schedule[i])
        
        
# task 7.1

quiz = ["whats the sqr root of 4?", "H20 is water", "whats the opposite of up?"]
answers = [4, True, "down"]

# task 7.2
def quiz_user():
    num_right = 0
    for k in range(len(quiz)):
        print(quiz[k])
        user_answer = input("Answer: ")
        if user_answer == answers[k]:
            num_right += 1
    
    return num_right
                    

# task 7.3

score = quiz_user / quiz.size()

if score >= 66:
    print("good job")
else:
    print("better luck next time")
    
# task 8.1
def travel_time(dist, speed):
    
    time = dist/speed
    
    return time


# task 8.2
def stops(dist, speed):
    
    length = travel_time(100, 70)
    if length > 2:
        print("Stop at mile 50 after 2 hours, for the rest of the journey")
    elif length < 2:
        print("No stops")

# task 8.3
start = input("where is your starting point?")
destination = input("Where do you want to go?")
speed = input("What is your travel speed?")

# task 9.1

def add_book(list, title, author, genre):
        book = {"title": title, "author": author, "genre": genre}
        list.append(book)
        
# task 9.2

def search(list, key_find):
    for i in range(len(list)):
        book = list[i]
        for key in book:
            if key_find == book[key]:
                print(book)
                break
            
            
# task 9.3
def display(list):
    for i in range(len(list)):
        book = list[i]
        for key, value in book.items():    
            print(key, ": ", value)


# task 10.1

def log(activity, duration, fitness_dict):
    
    fitness_dict[activity] = duration
    
    return fitness_dict
    
# task 10.2

def calories_burned(activity, duration):
    
    cal_burn = 0
    if activity == "running":
        cal_burn = 20 * duration
    elif activity == "swimming":
        cal_burn = 50 * duration
    elif activity == "weight training":
        cal_burn = 40 * duration
    else: 
        cal_burn = 0
    
        
    return cal_burn

# task 10.3

def summary(fitness_dict, activity, duration):
    
    cal = calories_burned(activity, duration)
    
    for key, val in fitness_dict.items():
        print(key, ": ", val, " minutes")
    
    print("You burned ", cal, " total calories")
        