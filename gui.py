from tkinter import *
from test2 import mendel 

root = Tk()
root.title("Mendel's experiment")

myLabel = Label(root, text="")

options = {
        "Yellow Round": ['Y', 'R'],
        "Yellow Wrinkled": ['Y', 'r'],
        "Green Round": ["y", "R"],
        "Green Wrinkled": ["y", "r"]
    }


p1_g1_clicked = StringVar()
p1_g1_clicked.set( "Select the 1st parent's 1st genotype" )
p1_g1_drop = OptionMenu( root , p1_g1_clicked , *list(options.keys()))
p1_g1_drop.pack()

p1_g2_clicked = StringVar()
p1_g2_clicked.set( "Select the 1st parent's 2nd genotype")
p1_g2_drop = OptionMenu( root , p1_g2_clicked , *list(options.keys()))
p1_g2_drop.pack()

p2_g1_clicked = StringVar()
p2_g1_clicked.set( "Select the 2nd parent's 1st gentoype" )
p2_g1_drop = OptionMenu( root , p2_g1_clicked ,  *list(options.keys()))
p2_g1_drop.pack()

p2_g2_clicked = StringVar()
p2_g2_clicked.set( "Select the 2nd parent's 2nd genotype" )
p2_g2_drop = OptionMenu( root , p2_g2_clicked , *list(options.keys()))
p2_g2_drop.pack()

def display_result():
    selected = [
            p1_g1_clicked.get(),
            p1_g2_clicked.get(),
            p2_g1_clicked.get(),
            p2_g2_clicked.get(),
    ]

    
    not_selected = False
    for element in selected:
        if element[0] == 'S':
            not_selected = True
            break

    if not_selected:
        result = "Please Select an option for each dropdown menu above."
    else:
        parent1 = [ options[selected[0]], options[selected[1]] ]
        parent2 = [ options[selected[2]], options[selected[3]] ] 

        result = mendel(parent1, parent2)
        result = f"Yellow Rounded Percentage: {result[0]}, Yellow Wrinkled Percentage: {result[1]}, Green rounded Percentage: {result[2]} , Green Wrinkled Percentage: {result[3]}"

    result_label =  Label(root, text=result)
    result_label.pack()

input_button = Button(root, text="Perform Mendel's calculations", command=display_result)


myLabel.pack()
input_button.pack()

root.mainloop()