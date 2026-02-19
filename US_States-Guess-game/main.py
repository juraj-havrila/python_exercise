import turtle
import pandas
data=pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



guessed_states=[]
game_is_on = True
state_list = data["state"].to_list()


while len(guessed_states)<50:
    answer_state = (screen.textinput(title=f"Gues the State {len(guessed_states)}/50", prompt = "What's another state name?")).capitalize()
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

        my_writer = turtle.Turtle()
        my_writer.hideturtle()
        my_writer.penup()
        guessed_state = data[data.state == answer_state]
        my_writer.goto(guessed_state.x.item(), guessed_state.y.item())
        my_writer.write(answer_state, align="center", font=("Arial", 10, "bold"))

states_to_learn=[]
for state in state_list:
    if state not in guessed_states:
        states_to_learn.append(state)
states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv("states_to_learn.csv")

#Get coordinates of individual states
#def get_mouse_click_coor(x,y):
#    print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

#screen.exitonclick()