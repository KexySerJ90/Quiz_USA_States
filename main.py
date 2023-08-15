import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S.States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

# Pop up a dialog window for input of a string.Arguments: title is the title of the dialog window, prompt is a text mostly describing what information to input.

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
score = set()
while len(score) < 50:
    answer_state = screen.textinput(title=f'Guess the State: {len(score)}/50',
                                    prompt="What's another state name? or write 'Exit'").title()
    if answer_state == 'Exit':
        missing_state = [i for i in all_states if i not in score]
        df=pandas.DataFrame({'Missing state': missing_state})
        df.to_csv('missing_state.csv')
        break
    if answer_state in all_states:
        score.add(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())
