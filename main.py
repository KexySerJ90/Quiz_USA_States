import turtle
import pandas
import subprocess

# Создаем экран и загружаем изображение штатов
screen = turtle.Screen()
screen.title('U.S.States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

# Загружаем данные о штатах из файла CSV
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

# Создаем пустой набор для хранения отгаданных штатов
score = set()

# Запускаем игру до тех пор, пока не будут отгаданы все 50 штатов или пользователь не введет 'Exit'
while len(score) < 50:
    # Получаем ответ пользователя и проверяем его на корректность
    answer_state = screen.textinput(title=f'Guess the State: {len(score)}/50',
                                    prompt="What's another state name? or write 'Exit'").title()
    if answer_state == 'Exit':
        # Если пользователь ввел 'Exit', сохраняем список незадействованных штатов в файл CSV и открываем его в приложении Numbers
        missing_state = [i for i in all_states if i not in score]
        df = pandas.DataFrame({'Missing state': missing_state})
        df.to_csv('missing_state.csv')
        subprocess.Popen(['open', '-a', 'Numbers.app', 'missing_state.csv'])
        break
    if answer_state in all_states:
        # Если пользователь ввел правильное название штата, добавляем его в набор отгаданных штатов и отмечаем его на карте
        score.add(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())