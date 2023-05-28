

class Item:
    """ Bitta yechimni o'z ichida saqlovchi sinf """
    def __init__(self, index: int, profit: float, weight: float) -> None:
        self.index = index
        self.profit = profit
        self.weight = weight
    
    def __str__(self) -> str:
        return f'{self.profit} {self.weight}'


class Solution:
    """ Knapsack muammosini yechim uchun sinf modeli. \n
    Bunda profit, weight va W qiymatlari berilishi kerak. 
    n = len(profit) sifatida hisoblanadi. \n    Qo'shimcha yechimlar metodlar 
    orqali aniqlanadi
    """

    def __init__(self, profit: list[float], weigth: list[float], W: float) -> None:
        self.profit: list[float] = profit
        self.weigth: list[float] = weigth
        self.n = len(profit)
        self.W = W
        self.matrix = Solution._solution(self.W, self.weigth, self.profit, self.n)
    
    def get_max_solve(self) -> float:
        """ Maksimal yechimni olish uchun metod """
        return self.matrix[self.n][self.W]

    def get_items(self) -> list[Item]:
        """ Har bir tanlangan obyektni olish metodi\n
        Bunda har bir yechim 'Item' sinfi orqali yuboriladi. \n
        Sinf vakillari index :int, profit :float, weight :float.
        """
        item_list: list[Item] = []
        w = self.W
        res = self.matrix[self.n][self.W]
        for i in range(self.n, 0, -1):
            if res <= 0:
                break
            if res == self.matrix[i - 1][w]:
                continue
            else: 
                item_list.append(Item(index=i-1, profit=self.profit[i-1], weight=self.weigth[i-1]))
                res = res - self.profit[i - 1]
                w = w - self.weigth[i - 1]
        return item_list

    def sum_weight(self) -> float:
        """ Umumiy og'irlikni olish funksiyasi """
        s = 0
        for i in self.get_items():
            s += i.weight
        return s
    
    def sum_profit(self) -> float:
        """ umumiy foydani olish funksiyasi """
        return self.get_max_solve()

    def get_matrix(self) -> list[list[float]]:
        """ Yechim matritsasini qaytaradigan metod """
        return self.matrix    

    def _solution(W, wt, val, n):
        """ Yechim va yechim matritsasini aniqlash funksiyasi """
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                
                elif wt[i-1] <= w:
                    K[i][w] = max(val[i-1]+ K[i-1][w-wt[i-1]], K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]
        return K