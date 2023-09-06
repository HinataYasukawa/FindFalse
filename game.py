import tkinter as tk
import random
import pandas as pd

class NewGame:

    def __init__(self):
        #windowの設定
        self.base = tk.Tk()
        self.base.geometry('600x600')
        self.base.resizable(0,0)
        self.base.title('間違い探し')

        #windowの設定2
        self.mainframe = tk.Frame(
        self.base,
        relief='groove',
        borderwidth=5
        )
        self.mainframe.grid()

        #windowの設定2
        self.base.grid_columnconfigure(0, weight=1)
        self.base.grid_rowconfigure(0, weight=1)

        #漢字の設定
        self.labelk1 = ['True' + str(i) for i in range(1, 100)]
        self.k1 = pd.DataFrame(
            {
                "漢字" : ['田'] * 99,
                "正誤" : self.labelk1,
            }
        )
        self.kn = pd.DataFrame(
            {
                "漢字" : ['由'],
                "正誤" : ['False'],
            }
        )
        self.k1 = pd.concat([self.k1, self.kn], ignore_index=True)

    def main(self):
        self.makeBoard()

    def button_click(self, event):
        label = event.widget
        frame = label.master
        df_index = frame._df_index
        correctness = self.k1.at[df_index, '正誤']
        if correctness == 'False':
            print("正解です")
            self.remakeBoard()
        else:
            print("Oh, mistake!")

    
    def remakeBoard(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()
        self.makeBoard()

    def makeBoard(self):
        #buttonの設定
        for idx, row in self.k1.iterrows():
            x, y = divmod(idx, 10)
            self.button_frame = tk.Frame(self.mainframe, width=50, height=50, bd=3, relief='ridge', bg='LightGray')
            self.button_frame.grid(row=x, column=y)
            self.label = tk.Label(self.button_frame, text=row["漢字"], font=("Arial", 24))
            self.label.pack(pady=5)

            # indexの設定
            self.button_frame._df_index = idx
            self.label.bind("<1>", self.button_click)


        self.base.mainloop()

if __name__ == "__main__":
    game = NewGame()
    game.main()