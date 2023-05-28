from knapsack_solve import Solution
from decimal import Decimal
import tkinter as tk

float = Decimal

class CustomInput:
    """ Qulay input """
    def __init__(self,window: tk.Tk, width: int, height: int, position_x: int, position_y: int, *args, **kwargs):
        self.input = tk.Entry(window, *args, **kwargs)
        self.input.place(height=height, width=width, x=position_x, y=position_y)
    
    def get_text(self) -> str:
        return self.input.get()
    
    def set_text(self, text: str) -> None:
        self.input.delete(0, tk.END)
        self.input.insert(0, text)
    
    def change_place(self, x: int, y: int) -> None:
        self.input.place(x=x,y=y)
    
    def delete(self) -> None:
        self.input.destroy()


class CustomButton:
    """ Qulay button """
    def __init__(self, window: tk.Tk, text: str, width: int, height: int, position_x: int, position_y: int, *args, **kwargs) -> None:
        self.button = tk.Button(window, text=text, *args, **kwargs)
        self.button.place(height=height, width=width, x=position_x, y=position_y)

    def change_text(self, arg: str):
        self.button.config(text=str(arg))
        



class KnapsackProblemGUI:
    """ Knapsack muammosini yechishda GUI oynasi.\n 
    Oynani ishga tushurish uchun run() metodi ishlatilsin
    """
    def __init__(self, window_name: str, default_item_name: str, 
            profit_name: str, weight_name: str, solve_text: str = "Hisoblash",
            error_window_title: str = "Dastur xatosi"        
        ) -> None:
        self.solution_class = Solution
        self.window_name: str = window_name
        self.default_item_name: str = default_item_name
        self.profit_name: str = profit_name
        self.weight_name: str = weight_name
        self.solve_text = solve_text
        self.error_window_title = error_window_title

        self.n = 4

    def run(self) -> None:
        """ GUIni ishga tushirish funksiyasi """
        self.window = tk.Tk()
        self.window.title(self.window_name)
        self.window.geometry("560x260+100+100")

        self.profit_input_list: list[CustomInput] = []
        self.weight_input_list: list[CustomInput] = []
        self.name_input_list: list[CustomInput] = []

        # Buttonlarni chizish
        self.draw_buttons()

        # Inputlarni chizish
        self.draw_inputs()

        self.window.mainloop()
    
    def draw_buttons(self) -> None:
        self.button_n_plus = CustomButton(window=self.window, text='+', width=40, height=30, position_x=10, position_y=10, font=('Arial 15'), fg='blue', command=self.button_plus)
        self.button_n_minus = CustomButton(window=self.window, text='-', width=40, height=30, position_x=110, position_y=10, font=('Arial 15'), fg='red', command=self.button_minus)
        self.button_n_draw = CustomButton(window=self.window, text=str(self.n), width=60,  height=30, position_x=50, position_y=10, fg='black', font=('Arial 13'), state=tk.DISABLED)

        CustomButton(window=self.window, width=140, height=30, position_x=40, position_y=60, text=self.default_item_name, font=('Arial 10'), state=tk.DISABLED, borderwidth=1, relief="ridge")
        CustomButton(window=self.window, width=140, height=30, position_x=200, position_y=60, text=self.profit_name, font=('Arial 10'), state=tk.DISABLED, borderwidth=1, relief="ridge")
        CustomButton(window=self.window, width=140, height=30, position_x=340, position_y=60, text=self.weight_name, font=('Arial 10'), state=tk.DISABLED, borderwidth=1, relief="ridge")

        self.solve_button = CustomButton(window=self.window, text=self.solve_text, width=150, height=30, position_x=350, position_y=10, font=('Arial 11'), command=self.calculation)

    def draw_inputs(self) -> None:
        for i in range(self.n):
            inp = CustomInput(
                window=self.window, width=140,
                height=30, position_x=40,
                position_y=100 + i*30,
                font=('Arial 10')
            )
            inp.set_text(f'{self.default_item_name} - {i+1}')
            self.name_input_list.append(inp)
        
        for i in range(self.n):
            self.profit_input_list.append(
                CustomInput(
                    window=self.window, width=140,
                    height=30, position_x=200,
                    position_y=100 + i*30,
                    font=('Arial 10')
                )
            )
        
        for i in range(self.n):
            self.weight_input_list.append(
                CustomInput(
                    window=self.window, width=140,
                    height=30, position_x=340,
                    position_y=100 + i*30,
                    font=('Arial 10')
                )
            )
        
        self.w_input = CustomInput(window=self.window, width=100, height=30, position_x=200, position_y=10, font=('Arial 12'))

    def button_minus(self) -> None:
        """ minus buttoni funksiyasi """
        if self.n <= 1:
            return
        self.n -= 1
        self.button_n_draw.change_text(arg=self.n)

        self.name_input_list[self.n].delete()
        self.profit_input_list[self.n].delete()
        self.weight_input_list[self.n].delete()
        del self.name_input_list[self.n]
        del self.profit_input_list[self.n]
        del self.weight_input_list[self.n]

        if self.window.winfo_height() > 180:
            self.window.geometry(f'{self.window.winfo_width()}x{self.window.winfo_height() - 30}')

    def button_plus(self) -> None:
        """ plus buttoni funksiyasi """
        self.n += 1
        self.button_n_draw.change_text(arg=self.n)
        
        inp = CustomInput(window=self.window, width=140,height=30, position_x=40,position_y=70 + self.n*30,font=('Arial 10'))
        inp.set_text(f'{self.default_item_name} - {self.n}')
        self.name_input_list.append(inp)
        self.profit_input_list.append(CustomInput(window=self.window, width=140,height=30, position_x=200,position_y=70 + self.n*30,font=('Arial 10')))
        self.weight_input_list.append(CustomInput(window=self.window, width=140,height=30, position_x=340,position_y=70 + self.n*30,font=('Arial 10')))
        self.window.geometry(f'{self.window.winfo_width()}x{self.window.winfo_height() + 30}')

    def calculation(self) -> Solution:
        """ Hisoblash tugmasi funksiyasi """
        profit_list: list[float] = []
        weight_list: list[int] = []
        W: int = int()
        
        # Vazn qiymatini olish
        try:
            W = int(self.w_input.get_text())
        except Exception as e:
            if self.w_input.get_text() == "":
                return self.error_view("Iltimos imkoniyatlar qanchaligini kiriting !")
            else:
                return self.error_view("Imkoniyatlar qiymatini kiritishda xatolik sodir bo'ldi !")
        
        # Profitlarni olish 
        for i in range(self.n):
            text = self.profit_input_list[i].get_text()
            try:
                profit_list.append(float(text))
            except:
                return self.error_view(f"{i + 1} - {self.profit_name.lower()}da xatolik mavjud !")
        
        # weightlarni olish
        for i in range(self.n):
            text = self.weight_input_list[i].get_text()
            try:
                weight_list.append(int(text))
            except:
                return self.error_view(f"{i+1} - {self.weight_name}da xatolik mavjud !")
        
        solve = self.solution_class(profit=profit_list, weigth=weight_list, W=W)
        self.solve_view(solve)
    

    def solve_view(self, solve: Solution) -> None:
        """ Masala yechimini ekranga chiqaradigan funksiya """
        new_window = tk.Tk()
        new_window.title("Masala yechimi")
        matrix = solve.get_matrix()
        item_list = solve.get_items()
        _i, _j = len(matrix), len(matrix[0])        
        width: int = 60 * _j + 100
        height: int = 40 * _i + 200
        position_y_fin = 40 * _i + 50
        new_window.geometry(f'{width}x{height}')
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                CustomButton(window=new_window, text=str(matrix[i][j]),width=60, height=40,position_x=70+j*60, position_y=50+i*40,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 13'))
        
        for i in range(_j):
            CustomButton(window=new_window, text=str(i),width=60, height=40,position_x=70+i*60, position_y=0,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 13'))

        for i in range(_i):
            CustomButton(window=new_window, text=str(i),width=60, height=40,position_x=0, position_y=40*i + 50,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 13'))
        
        CustomButton(window=new_window, text="N \\ W",width=60, height=40,position_x=0, position_y=0,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))
        CustomButton(window=new_window, text=self.profit_name,width=150, height=30, position_x=10, position_y=position_y_fin+20,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))
        CustomButton(window=new_window, text=self.weight_name,width=150, height=30, position_x=10, position_y=position_y_fin+60,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))
        CustomButton(window=new_window, text="indeks:",width=150, height=30, position_x=10, position_y=position_y_fin+100,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))
        CustomButton(window=new_window, text=f"{solve.sum_profit()}",width=60, height=30, position_x=180, position_y=position_y_fin+20,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))
        CustomButton(window=new_window, text=f"{solve.sum_weight()}",width=60, height=30, position_x=180, position_y=position_y_fin+60,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))

        item_list.reverse()

        for _ in range(len(item_list)):
            i = item_list[_]
            CustomButton(window=new_window, text=str(i.profit),width=60, height=30, position_x=270 + _*60, position_y=position_y_fin + 20,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))
            CustomButton(window=new_window, text=str(i.weight),width=60, height=30, position_x=270 + _*60, position_y=position_y_fin + 60,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))
            CustomButton(window=new_window, text=str(i.index + 1),width=60, height=30, position_x=270 + _*60, position_y=position_y_fin + 100,borderwidth=0.5, relief="ridge", state=tk.DISABLED,font=('Arial 11'))
        if width < 280 + len(item_list) * 60:
            new_window.geometry(f'{270 + len(item_list) * 60 + 10}x{height}')
        new_window.mainloop()

    def error_view(self, error: str) -> None:
        """ Dasturda xatolik yuz berganda chiqadigan oyna """
        new_window = tk.Tk()
        new_window.title(self.error_window_title)
        new_window.geometry('450x120+500+250')
        label = tk.Label(new_window, text=error, width=400, height=60, font=('Arial 12'), fg='red')
        label.place(relx=0.5, rely=0.5)
        label.pack()
        new_window.mainloop()