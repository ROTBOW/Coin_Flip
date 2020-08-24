### flips numbers of coins as asked then returns the amount of each. ###
import random
import tkinter as tk

# main function
def flip():
    amounts =[]
    try:
        count = int(input_num.get()) - 1
    except Exception as exp:
        def kill_window():
            error_window.destroy()
        print(exp)
        error_window = tk.Tk(); error_window.title('Error')
        l1 = tk.Label(master = error_window, text = 'Sorry, only numbers please!'); l1.pack()
        b1 = tk.Button(master = error_window, text = 'okay', command = kill_window); b1.pack()
        error_window.mainloop
        return

    while count >= 0:
        coin = round(random.uniform(1, 2), 0)
        if coin == 1:
            amounts.append('heads')
        else:
            amounts.append('tails')
        count = count - 1
    count_heads = amounts.count('heads')
    count_tails = amounts.count('tails')
    num_view.config(text = (f' Heads: {count_heads} ----- Tails: {count_tails} '))

# kills the gui
def destroy():
    window.destroy()

# GUI
window = tk.Tk(); window.title('Coin Flip')

main_frame = tk.Frame(master = window,
                      ); main_frame.pack()

label1 = tk.Label(master = main_frame,
                  text = 'Coin Flip',
                  width = 25,
                  height = 2,
                  relief = tk.GROOVE,
                  borderwidth = 3,
                  ); label1.grid(row = 0, column = 0, pady = 1)

num_view = tk.Label(master = main_frame,
                    text = ' Heads: 0 ----- Tails: 0 ',
                    relief = tk.GROOVE,
                    borderwidth = 3,
                    width = 25,
                    ); num_view.grid(row = 1, column = 0, pady = 1)

low_frame = tk.Frame(master = window,
                     ); low_frame.pack(side = 'bottom')

quit = tk.Button(master = low_frame,
                 text = 'quit',
                 command = destroy,
                 relief = tk.GROOVE,
                 borderwidth = 3,
                 width = 10,
                 ); quit.grid(row = 0, column = 0, rowspan = 2, sticky = 'WENS')

input_num = tk.Entry(master = low_frame,
                     width = 13,
                     relief = tk.SOLID,
                     borderwidth = 1,
                     ); input_num.grid(row = 0, column = 1)

start = tk.Button(master = low_frame,
                  text = 'Flip!',
                  command = flip,
                  ); start.grid(row = 1, column = 1, sticky = 'WE')



window.mainloop()