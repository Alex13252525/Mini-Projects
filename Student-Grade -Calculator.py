import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def find_grade(average):
    if average >= 90:
        return "A (You're killing it)"
    elif average >= 75:
        return "B (Awesome work)"
    elif average >= 60:
        return "C (Solid effort)"
    elif average >= 40:
        return "D (Keep pushing)"
    else:
        return "Fail (Let's study harder)"

def show_results():
    try:
        scores = []
        for i, entry in enumerate(subject_entries):
            score_text = entry.get().strip()
            if not score_text:
                raise ValueError(f"Hey, you forgot to enter marks for {subjects[i]}!")
            score = float(score_text)
            if score < 0 or score > 100:
                raise ValueError(f"Oops, {subjects[i]} marks should be between 0 and 100.")
            scores.append(score)

        total_score = sum(scores)
        average_score = total_score / len(scores)
        grade = find_grade(average_score)

        results.set(
            f"Student: {name_entry.get().strip()}\n"
            f"Total: {total_score}\n"
            f"Average: {average_score:.2f}\n"
            f"Grade: {grade}"
        )
    except ValueError as error:
        messagebox.showerror("Oops!", str(error))
    except ZeroDivisionError:
        messagebox.showerror("Hold on!", "Please fill in all subject marks.")

window = tk.Tk()
window.title("🌟 Grade Calculator 🌟")
window.geometry("400x550")
window.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Arial', 10), foreground='#333')
style.configure('TButton', font=('Arial', 12, 'bold'), background='#007bff', foreground='white')
style.map('TButton', background=[('active', '#0056b3')])

main_frame = ttk.Frame(window, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(main_frame, text="Your Name:", font=('Arial', 11, 'bold')).pack(pady=(10, 5))
name_entry = ttk.Entry(main_frame, width=30)
name_entry.pack(pady=(0, 10))

subjects = ["Math", "Science", "English", "History", "Computer"]
subject_entries = []

for subject in subjects:
    ttk.Label(main_frame, text=f"{subject} Marks (0-100):", font=('Arial', 10)).pack(pady=2)
    entry = ttk.Entry(main_frame, width=10)
    entry.pack()
    subject_entries.append(entry)

ttk.Button(main_frame, text="Get My Grade!", command=show_results).pack(pady=20)

result_box = ttk.Frame(main_frame, relief=tk.GROOVE, borderwidth=2, padding="10")
result_box.pack(pady=10, fill=tk.X)

results = tk.StringVar()
ttk.Label(result_box, textvariable=results, font=("Arial", 12, 'bold'), foreground="darkblue", wraplength=300).pack()

window.mainloop()