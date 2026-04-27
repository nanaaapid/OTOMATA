import tkinter as tk

def cek_string(s):
    state = "S"
    path = ["S"]
    rejected = False

    for char in s:
        if char not in ['0', '1']:
            return "Input hanya boleh 0 dan 1!"

        if state == "S":
            state = "B" if char == "1" else "A"

        elif state == "A":
            if char == "1":
                state = "B"
            else:
                state = "C"
                rejected = True

        elif state == "B":
            state = "B" if char == "1" else "A"

        elif state == "C":
            state = "C"
            rejected = True

        path.append(state)

    if rejected or state != "B":
        return f"{'-'.join(path)} → Ditolak"
    else:
        return f"{'-'.join(path)} → Diterima"


def proses():
    input_str = entry.get()
    hasil = cek_string(input_str)
    label_hasil.config(text=hasil)

root = tk.Tk()
root.title("FSM Checker")
root.geometry("400x250")

label_judul = tk.Label(root, text="Cek String FSM", font=("Comic Sans MS", 20))
label_judul.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn = tk.Button(root, text="Cek", command=proses)
btn.pack(pady=10)

label_hasil = tk.Label(root, text="", wraplength=450)
label_hasil.pack(pady=10)

root.mainloop()