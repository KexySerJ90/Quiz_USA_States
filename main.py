import turtle
import pandas

screen=turtle.Screen()
screen.title('U.S.States Game')
image='blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

#Pop up a dialog window for input of a string.Arguments: title is the title of the dialog window, prompt is a text mostly describing what information to input.
answer_state=screen.textinput(title='Guess the State', prompt="What's another state name?")
data=pandas.read_csv('50_states.csv')
all_states=data.state.to_list()
score=0
if answer_state.lower() in all_states or answer_state in all_states :
        score+=1
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x,state_data.y)
        t.write(state_data.state)