import turtle
screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

import pandas
data = pandas.read_csv("50_states.csv")
score = 0
all_states = []
guessed_states = []
missing_states = []
for state in data['state'].values:
    all_states.append(state)

while score < 50:
    answer_state = screen.textinput(title=f'Guess the State {score}/50',  prompt="What's another states name").title()
    # print(answer_state)
    # print(data['state'])

    if answer_state == 'Exit':
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        study_data = pandas.DataFrame(missing_states)
        study_data.to_csv('states_to_learn.csv')
        break
    if answer_state in data['state'].values:
        score +=1
        guessed_states.append(answer_state)
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


# screen.exitonclick()