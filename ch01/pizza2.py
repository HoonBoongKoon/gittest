#로그인 하지 않은 ChatGPT 4o mini

import tkinter as tk
from tkinter import messagebox

class PizzaOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("조각 피자 주문 프로그램")
        
        # 가격 설정
        self.pizza_prices = {
            "Small": 8,
            "Medium": 10,
            "Large": 12
        }
        
        self.create_widgets()

    def create_widgets(self):
        # 피자 크기 선택
        self.size_label = tk.Label(self.root, text="피자 크기 선택:")
        self.size_label.pack()

        self.size_var = tk.StringVar()
        self.size_var.set("Medium")  # 기본값

        self.size_menu = tk.OptionMenu(self.root, self.size_var, "Small", "Medium", "Large")
        self.size_menu.pack()

        # 피자 조각 수 입력
        self.slices_label = tk.Label(self.root, text="피자 조각 수 (1~8):")
        self.slices_label.pack()

        self.slices_var = tk.IntVar()
        self.slices_var.set(1)  # 기본값

        self.slices_spinbox = tk.Spinbox(self.root, from_=1, to=8, textvariable=self.slices_var)
        self.slices_spinbox.pack()

        # 주문 버튼
        self.order_button = tk.Button(self.root, text="주문하기", command=self.calculate_total)
        self.order_button.pack()

        # 결과 출력
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def calculate_total(self):
        size = self.size_var.get()
        slices = self.slices_var.get()

        # 피자 크기에 따른 가격 계산
        price = self.pizza_prices[size] * slices / 8  # 8조각 기준으로 가격 계산

        # 결과 출력
        total_price = round(price, 2)
        self.result_label.config(text=f"총 가격: {total_price}원")
        
        # 가격 계산 후 알림
        messagebox.showinfo("주문 완료", f"{size} 피자 {slices}조각을 주문하셨습니다.\n총 가격: {total_price}원")

# 프로그램 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaOrderApp(root)
    root.mainloop()
