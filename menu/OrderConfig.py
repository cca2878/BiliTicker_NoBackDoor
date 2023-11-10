import tkinter as tk
from tkinter import ttk
import json


class OrderConfigWindow:
    def __init__(self, master, order_config):
        self.master = master
        self.master.title("复制你得配置")
        self.displayed_info_label = tk.Label(master, text="复制你的配置, 放入抢票app里面")
        self.displayed_info_label.grid(row=2, column=0, pady=10)
        # Format the order_config as a JSON string with indentation
        formatted_order_config = json.dumps(order_config, indent=2, ensure_ascii=False)

        # Create a non-editable text widget
        self.text_widget = tk.Text(master, wrap="none", height=10, width=40)
        self.text_widget.insert(tk.END, formatted_order_config)
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.grid(row=0, column=0, padx=10, pady=10)

        # Create a copy button
        self.copy_button = ttk.Button(master, text="点我复制", command=self.copy_to_clipboard)
        self.copy_button.grid(row=1, column=0, pady=10)

    def copy_to_clipboard(self):
        # Copy the content of the text widget to the clipboard
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text_widget.get(1.0, tk.END))
        self.master.update()


if __name__ == "__main__":
    # Sample order_config, replace this with your actual order_config
    order_config = {
        "count": 2,
        "screen_id": 123,
        "project_id": 456,
        "sku_id": 789,
        "token": "your_token",
        "pay_money": 50.0,
        "timestamp": "202311090900",
        "buyer_info": {"name": "John Doe", "email": "john@example.com"}
    }

    root = tk.Tk()
    order_config_window = OrderConfigWindow(root, order_config)
    root.mainloop()