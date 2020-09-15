import tkinter as tike 

window = tike.Tk()
window.title("Project Cupu")
window.geometry("400x400")

#LABEL
label1=tike.Label(text="Tampilin teks utama pake ini")
label1.grid()

label2=tike.Label(text="siapa kamu ? ")
label2.grid(column=0, row=2)


#ENTRI
entri1=tike.Entry()
entri1.grid(column=2, row=1)
entri1.grid()

#TOMBOL
tombol1=tike.Button(text="Pencet aku")
tombol1.grid(column=0, row=3)

window.mainloop()