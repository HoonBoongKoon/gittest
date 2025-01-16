import tkinter as tk
from tkinter import messagebox

# 피자 종류와 크기별 가격
PIZZA_SIZES = {
    "치즈 피자": {"Small": 5000, "Medium": 7000, "Large": 9000},
    "페퍼로니 피자": {"Small": 6000, "Medium": 8000, "Large": 10000},
    "하와이안 피자": {"Small": 7000, "Medium": 9000, "Large": 11000},
    "베지터블 피자": {"Small": 5500, "Medium": 7500, "Large": 9500}
}

# 주문 총 가격 계산 함수
def calculate_total():
    total_price = 0
    for pizza, size_var in sizes.items():
        size = size_var.get()
        quantity = quantities[pizza].get()
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise ValueError
            total_price += quantity * PIZZA_SIZES[pizza][size]
        except ValueError:
            messagebox.showerror("입력 오류", f"{pizza}의 수량은 0 이상의 정수를 입력해주세요.")
            return
    
    messagebox.showinfo("총 가격", f"총 주문 금액은 {total_price}원입니다.")

# 프로그램 초기화
root = tk.Tk()
root.title("피자 주문 프로그램")

# 피자 선택 라벨
label = tk.Label(root, text="피자 종류, 크기, 수량을 선택하세요:")
label.pack(pady=10)

# 피자 크기 및 수량 입력
def create_pizza_row(pizza_name):
    frame = tk.Frame(root)
    frame.pack(pady=5, padx=10, anchor="w")

    label = tk.Label(frame, text=f"{pizza_name}:")
    label.pack(side="left")

    # 크기 선택
    size_var = tk.StringVar(value="Small")
    size_menu = tk.OptionMenu(frame, size_var, *PIZZA_SIZES[pizza_name].keys())
    size_menu.pack(side="left", padx=5)

    # 수량 선택
    quantity_var = tk.IntVar(value=0)
    quantity_spinbox = tk.Spinbox(frame, from_=0, to=20, textvariable=quantity_var, width=5)
    quantity_spinbox.pack(side="left", padx=5)

    sizes[pizza_name] = size_var
    quantities[pizza_name] = quantity_var

sizes = {}
quantities = {}
for pizza in PIZZA_SIZES:
    create_pizza_row(pizza)

# 주문 버튼
order_button = tk.Button(root, text="주문하기", command=calculate_total)
order_button.pack(pady=20)

# 프로그램 실행
root.mainloop()
