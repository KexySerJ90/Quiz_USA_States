import turtle

screen=turtle.Screen()
screen.title('U.S.States Game')
image='blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

#Pop up a dialog window for input of a string.Arguments: title is the title of the dialog window, prompt is a text mostly describing what information to input.
answer_state=screen.textinput(title='Guess the State', prompt="What's another state name?")
print(answer_state)