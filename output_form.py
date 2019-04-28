from tkinter import *

def display_form(labels, results, top_k):
    w = Tk()
    Label(w, text="The Animal Is:").pack()
    
    res1 = Label(w)
    res1.pack()
    res2 = Label(w)
    res2.pack()
    res3 = Label(w)
    res3.pack()
    res4 = Label(w)
    res4.pack()
    res5 = Label(w)
    res5.pack()
    
    all_res = [res1, res2, res3, res4, res5]
    x = 0
    
    
    for i in top_k:
        all_res[x].configure(text = labels[i].capitalize() + ' :' + '               ' + str(results[i] * 100))
        x = x + 1
    
    w.mainloop()