#로그인 후 만든 ChatGPT

import tkinter as tk
from tkinter import messagebox

# 피자 종류와 가격
PIZZA_PRICES = {
    "치즈 피자": 5000,
    "페퍼로니 피자": 6000,
    "하와이안 피자": 7000,
    "베지터블 피자": 5500
}

# 주문 총 가격 계산 함수
def calculate_total():
    total_price = 0
    for pizza, var in quantities.items():
        try:
            quantity = int(var.get())
            if quantity < 0:
                raise ValueError
            total_price += quantity * PIZZA_PRICES[pizza]
        except ValueError:
            messagebox.showerror("입력 오류", f"{pizza}의 수량은 0 이상의 정수를 입력해주세요.")
            return
    
    messagebox.showinfo("총 가격", f"총 주문 금액은 {total_price}원입니다.")

# 프로그램 초기화
root = tk.Tk()
root.title("피자 주문 프로그램")

# 피자 선택 라벨
label = tk.Label(root, text="피자 종류와 수량을 선택하세요:")
label.pack(pady=10)

# 피자 수량 입력
def create_pizza_row(pizza_name):
    frame = tk.Frame(root)
    frame.pack(pady=5, padx=10, anchor="w")

    label = tk.Label(frame, text=f"{pizza_name} ({PIZZA_PRICES[pizza_name]}원):")
    label.pack(side="left")

    entry_var = tk.StringVar(value="0")
    entry = tk.Entry(frame, textvariable=entry_var, width=5)
    entry.pack(side="left", padx=5)

    quantities[pizza_name] = entry_var

quantities = {}
for pizza in PIZZA_PRICES:
    create_pizza_row(pizza)

# 주문 버튼
order_button = tk.Button(root, text="주문하기", command=calculate_total)
order_button.pack(pady=20)

# 프로그램 실행
root.mainloop()
