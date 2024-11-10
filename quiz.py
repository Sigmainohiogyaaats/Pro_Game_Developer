import pgzrun 

#define some constants 
TITLE = 'Quiz master' 
HEIGHT = 600
WIDTH = 500


# define variables 
marquee_box = Rect(10,10,480,80)  
question_box = Rect(10,100,410,80) 
timer_box = Rect(430,100,60,80) 
skip_box = Rect(430,200,60,200) 
answer_box1 = Rect(10,190,200,80) 
answer_box2 = Rect(10,280,200,80) 
answer_box3 = Rect(220,190,200,80) 
answer_box4 = Rect(220,280,200,80)   
marquee_message =  '' 
timer_message = '' 
skip_message = ''
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]   
questions = []
question_count = 0  
question_index = 0 
time_left = '' 
game_over = '' 
score = 0  
time_left = 10 
is_game_over = False 


def move_text(): 
    marquee_box.x += 2 
    if marquee_box.left > WIDTH: 
        marquee_box.right = 0  
def update(): 
    move_text()

def read_questions_file():  
    global question_count,questions
    q = open('questions.txt', 'r')
    for question in q:  
        questions.append(question) 
        question_count += 1  
    q.close() 

def read_next_question(): 
    global question_index 
    question_index += 1 
    return questions.pop(0).split(',')


def draw():  
    global marquee_message   
    screen.fill('grey') 
    screen.draw.filled_rect(marquee_box,'white') 
    screen.draw.filled_rect(question_box,'white') 
    screen.draw.filled_rect(timer_box,'white')
    screen.draw.filled_rect(skip_box,'white')   


    for i in answer_boxes: 
        screen.draw.filled_rect(i,'white')    
        global question
    marquee_message =  'Try and get ten out of ten'
    screen.draw.textbox(marquee_message , marquee_box ,color =  'black')  
    screen.draw.textbox(question[0],question_box , color = 'black')  
    index = 1
    for answer_box in answer_boxes:  
        screen.draw.textbox(question[index], answer_box,color = 'blue')
        index+=1

    global timer_message
    screen.draw.textbox(str(time_left) , timer_box, color = 'black') 

    global skip_message 
    skip_message = 'skip' 
    screen.draw.textbox(skip_message , skip_box, color = 'black')  

def game_over(): 
    global question, time_left, is_game_over 
    message = f'Game over! \n you got {score} questions correct !'  
    question = [message, '-','-','-','-',5] 
    time_left = 0 
    is_game_over = True

def update_time_left (): 
    global time_left 
    if time_left : 
        time_left -= 1 
    else:  
        game_over() 


def skip_question():  
    global question,time_left 
    if questions and not is_game_over: 
        question = read_next_question()  
        time_left = 10 
    else:
        game_over()

def on_mouse_down(pos): 
    if is_game_over : 
        return  

    if skip_box.collidepoint(pos) :
        skip_question()  

    index = 1 
    for box in answer_boxes: 
        if box.collidepoint(pos): 
            if index == int(question[5]): 
                correct_answer() 
            else: 
                game_over() 
        index = index +1 


def correct_answer(): 
    global questions, time_left, question,score
    score +=1
    if questions: 
        question = read_next_question() 
        time_left = 10 
    else: 
        game_over()    



read_questions_file()  
clock.schedule_interval(update_time_left, 1)
question = read_next_question()   
pgzrun.go() 