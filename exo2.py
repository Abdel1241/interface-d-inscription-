import tkinter as tk

def valider_inscription():
    pseudo = pseudo_entry.get()
    mot_de_passe = mot_de_passe_entry.get()
    email = email_entry.get()
    
    print("Inscription validée !")
    print(f"Pseudo: {pseudo}")
    print(f"Mot de passe: {mot_de_passe}")
    print(f"Email: {email}")

# Créez la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Inscription")

# Étiquettes et champs de saisie pour le pseudo, le mot de passe et l'e-mail
pseudo_label = tk.Label(fenetre, text="Pseudo:")
pseudo_label.pack()
pseudo_entry = tk.Entry(fenetre)
pseudo_entry.pack()

mot_de_passe_label = tk.Label(fenetre, text="Mot de passe:")
mot_de_passe_label.pack()
mot_de_passe_entry = tk.Entry(fenetre, show="*")  # Pour masquer le mot de passe
mot_de_passe_entry.pack()

email_label = tk.Label(fenetre, text="E-mail:")
email_label.pack()
email_entry = tk.Entry(fenetre)
email_entry.pack()

# Bouton pour valider l'inscription
valider_bouton = tk.Button(fenetre, text="Valider", command=valider_inscription)
valider_bouton.pack()

# Lancez la boucle d'événements
fenetre.mainloop()
