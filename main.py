import turtle
screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

import pandas
data = pandas.read_csv("50_states.csv")
score = 0
while score < 50:
    answer_state = screen.textinput(title=f'Guess the State {score}/50',  prompt="What's another states name")
    # print(answer_state)
    # print(data['state'])
    if answer_state in data['state'].values:
        score +=1
        selected_state = data[data.state == answer_state]
        print(selected_state)
        x_cor = int(selected_state.x)
        y_cor = int(selected_state.y)
        name = str(selected_state.state)
        text = turtle.Turtle()
        text.hideturtle()

        text.penup()
        text.goto(x_cor, y_cor)
        text.write(answer_state, align='right')


screen.exitonclick()