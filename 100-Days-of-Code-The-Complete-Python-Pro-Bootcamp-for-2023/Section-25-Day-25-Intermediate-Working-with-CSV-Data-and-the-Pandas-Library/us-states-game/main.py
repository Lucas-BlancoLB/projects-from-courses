import turtle
import pandas as pd

states_guessed = 0
game_is_on = True
def x_y_coordinates(x, y):
    #print x, y coordinates from the mouse position click
    print(x,y)


def ask_for_user_input(num_st_guessed):
        answer = screen.textinput(title=f"Guessed {num_st_guessed}/50", prompt=f"").title()
        if answer in data_sates:
            mark_states_guessed(answer)
            return True, answer
        elif answer.lower() == "off":
            return "off", None

def mark_states_guessed(ans_state):
    #check the answer in the df for it row
    instance = data[data["state"] == ans_state].values.tolist()[0] # values takes array data | tolist() convert to list
    x, y = instance[1], instance[2]

    write_text.setpos(x, y)
    write_text.write(f"{ans_state}")
    # print(instance)
# create screen object
screen = turtle.Screen()
write_text = turtle.Turtle()

# set turtle object
write_text.hideturtle()
write_text.penup()
# Set up the window
screen.setup(width= 725, height= 490)
screen.title("Guess The States: US")
screen.bgpic("blank_states_img.gif")
screen.bgcolor("black")

#listen for mouse click coordinates x_y_coordinates()
screen.listen()
screen.onscreenclick(x_y_coordinates)

# reads csv file create a pd data table and use its values
data_file = pd.read_csv("50_states.csv")
data = pd.DataFrame(data_file)
data_sates, data_sates_list =  data.state.values, data.state.values.tolist()


#ask for user input from a popup
while game_is_on:
    if states_guessed != 50:
        var, state_guessed = ask_for_user_input(states_guessed)
        if state_guessed is not None:
            data_sates_list.remove(state_guessed)

        elif var == "off":
            game_is_on = False

        elif var:
            states_guessed += 1
    else:
        game_is_on = False

to_learn_table = pd.DataFrame(data_sates_list, columns=["To Learn"])
to_learn_table.to_csv("states_to_learn.csv")

turtle.mainloop()
