import tkinter as tk

# Definē funkcijas, kas maina loga fona krāsu
def funkBalts():
    # Maina loga fona krāsu uz baltu
    window.config(bg="white")
    # Ja nepieciešams, varat arī mainīt iezīmes (Label) fona krāsu, lai tā būtu saskaņota
    teksts.config(bg="white")

def funkMelns():
    # Maina loga fona krāsu uz melnu
    window.config(bg="black")
    # Ja nepieciešams, varat arī mainīt iezīmes (Label) fona krāsu
    teksts.config(bg="black")

# Izveido galveno logu
window = tk.Tk()
window.title("Melnbalts ekrāns")
window.geometry("400x200")

# Izveido iezīmi ar norādi uz darbību
teksts = tk.Label(window, text="Klikšķini uz pogas, lai mainītu fona krāsu ...", 
                  fg="darkorange", font=("Verdana", 12))
teksts.pack(pady=20)

# Izveido rāmi pogām
frame = tk.Frame(window)
frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# Izveido pogas un sasaista tās ar attiecīgajām funkcijām
balts = tk.Button(frame, text="Balts", width=10, height=2, command=funkBalts)
balts.grid(row=0, column=0, padx=5)
melns = tk.Button(frame, text="Melns", width=10, height=2, command=funkMelns)
melns.grid(row=0, column=1, padx=5)

# Iecentrē pogas horizontāli, piešķirot kolonnu svaru
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Palaiž lietotāja interfeisu
window.mainloop()