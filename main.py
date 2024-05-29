import tkinter
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
Timer = None


def time_reset():
    window.after_cancel(Timer)
    canvas.itemconfig(timer, text=f'00:00')
    time_label.config(text='')
    new_label.config(text='Timer')
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        new_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        new_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        new_label.config(text='Work', fg=GREEN)


def count_down(count):
    global Timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # this is what we call dynamic typing
    # if count_sec==0:
    #     count_sec='00'
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        Timer = canvas.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_Session = math.floor(reps / 2)
        for i in range(work_Session):
            mark += '✓'
            time_label.config(text=mark)


window = tkinter.Tk()
window.title('🍅🍅Pomodoro🍅🍅')
# window.minsize(width=200,height=200)
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tkinter.Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(102, 110, image=tomato_image)
timer = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='White')
canvas.grid(column=1, row=1)

new_label = tkinter.Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)

new_label.grid(column=1, row=0)
button = tkinter.Button(text='Start', font=(FONT_NAME, 20), highlightthickness=0, command=start_timer)
button.grid(column=0, row=2)
button.config(padx=5, pady=5)
second_button = tkinter.Button(text='Reset', font=(FONT_NAME, 20), highlightthickness=0, command=time_reset)
second_button.config(padx=5, pady=5)
second_button.grid(column=2, row=2)

time_label = tkinter.Label(font=(FONT_NAME, 15, 'bold'), fg=GREEN, bg=YELLOW)
time_label.grid(column=1, row=3)

window.mainloop()
