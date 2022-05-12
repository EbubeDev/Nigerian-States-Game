import turtle
import pandas

screen = turtle.Screen()
screen.title("Nigeria States Game")
screen.setup(width=900, height=750)
image = "map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("36_states.csv")
list_of_states = data.states.to_list()

guessed_states = []

while len(guessed_states) < 37:
    guess = screen.textinput(title=f"{len(guessed_states)}/37 correct guesses",
                             prompt="Make another guess").title()

    if guess == "End":
        missed_states = []
        for state in list_of_states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if guess in list_of_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.states == guess]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(guess)
        t.penup()


# def get_mouse(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse)
#
# turtle.mainloop()






