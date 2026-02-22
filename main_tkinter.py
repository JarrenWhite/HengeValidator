import tkinter as tk
from tkinter import messagebox
from character import Character, Attributes, Skills


class CharacterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Character Creator")

        # --- Attributes Frame ---
        attr_frame = tk.LabelFrame(root, text="Attributes", padx=10, pady=10)
        attr_frame.pack(padx=10, pady=5, fill="x")

        self.attrs = {}
        for i, attr in enumerate(["Power", "Finesse", "Mind", "Heart"]):
            tk.Label(attr_frame, text=attr).grid(row=i, column=0, sticky="w")
            self.attrs[attr] = tk.Entry(attr_frame, width=5)
            self.attrs[attr].grid(row=i, column=1)

        # --- Skills Frame ---
        skills_frame = tk.LabelFrame(root, text="Skills", padx=10, pady=10)
        skills_frame.pack(padx=10, pady=5, fill="x")

        self.skills_entries = {}
        for i, lvl in enumerate(["Lvl 3", "Lvl 2", "Lvl 1"]):
            tk.Label(skills_frame, text=f"Number of {lvl} skills:").grid(row=i, column=0, sticky="w")
            self.skills_entries[lvl] = tk.Entry(skills_frame, width=5)
            self.skills_entries[lvl].grid(row=i, column=1)

        # --- Other Details ---
        other_frame = tk.LabelFrame(root, text="Other Details", padx=10, pady=10)
        other_frame.pack(padx=10, pady=5, fill="x")

        tk.Label(other_frame, text="Attunement:").grid(row=0, column=0, sticky="w")
        self.attunement_entry = tk.Entry(other_frame, width=5)
        self.attunement_entry.grid(row=0, column=1)

        tk.Label(other_frame, text="Feats of Light:").grid(row=1, column=0, sticky="w")
        self.feats_entry = tk.Entry(other_frame, width=5)
        self.feats_entry.grid(row=1, column=1)

        # --- Buttons ---
        tk.Button(root, text="Create Character", command=self.create_character).pack(pady=10)

        # --- Output Text ---
        self.output = tk.Text(root, height=20, width=50)
        self.output.pack(padx=10, pady=5)

    def create_character(self):
        try:
            # Get attributes
            attr_values = {k: int(v.get()) for k, v in self.attrs.items()}
            attributes = Attributes(attr_values["Power"], attr_values["Finesse"],
                                    attr_values["Mind"], attr_values["Heart"])

            # Get skills
            skills_list = (
                [3] * int(self.skills_entries["Lvl 3"].get()) +
                [2] * int(self.skills_entries["Lvl 2"].get()) +
                [1] * int(self.skills_entries["Lvl 1"].get())
            )
            skills = Skills(skills_list)

            # Other details
            attunement = int(self.attunement_entry.get())
            feats = int(self.feats_entry.get())

            # Create character
            character = Character(attributes, skills, attunement, feats)

            # Display results
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, "=============== Character Details ===============\n\n")
            self.output.insert(tk.END, f"{'Level:':15} {character.get_level()}\n")
            self.output.insert(tk.END, f"{'Spent EXP:':15} {character.get_spent_exp()}\n")
            self.output.insert(tk.END, f"{'Focus Roll:':15} {character.get_focus_roll()}\n")
            self.output.insert(tk.END, f"{'River Limit:':15} {character.get_river()}\n\n")
            self.output.insert(tk.END, f"{'Health:':15} {character.get_health()}\n\n")

            light_levels = character.get_light()
            colors = ['Red', 'Green', 'Blue', 'Gold']
            self.output.insert(tk.END, "Light Levels:\n")
            for color, value in zip(colors, light_levels):
                self.output.insert(tk.END, f"{color:10} {value:<5}\n")

            self.output.insert(tk.END, "\n=================================================\n")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for all fields.")


def main():
    root = tk.Tk()
    app = CharacterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
