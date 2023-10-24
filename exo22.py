import tkinter as tk

def valider_inscription():
    pseudo = pseudo_entry.get()
    mot_de_passe = mot_de_passe_entry.get()
    email = email_entry.get()
    
    # Affichage des données sur le terminal
    print("Inscription validée !")
    print(f"Pseudo: {pseudo}")
    print(f"Mot de passe: {mot_de_passe}")
    print(f"Email: {email}")

# Créez la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Inscription")

# Couleurs
background_color = "#f0f0f0"
label_color = "#333"
button_color = "#007acc"
button_text_color = "white"

# Configurez le style
fenetre.configure(bg=background_color)
fenetre.geometry("400x300")

# Étiquettes et champs de saisie
pseudo_label = tk.Label(fenetre, text="Pseudo:", bg=background_color, fg=label_color)
pseudo_label.pack()
pseudo_entry = tk.Entry(fenetre, bg="white")
pseudo_entry.pack()

mot_de_passe_label = tk.Label(fenetre, text="Mot de passe:", bg=background_color, fg=label_color)
mot_de_passe_label.pack()
mot_de_passe_entry = tk.Entry(fenetre, show="*", bg="white")
mot_de_passe_entry.pack()

email_label = tk.Label(fenetre, text="E-mail:", bg=background_color, fg=label_color)
email_label.pack()
email_entry = tk.Entry(fenetre, bg="white")
email_entry.pack()

# Bouton de validation
valider_bouton = tk.Button(fenetre, text="Valider", bg=button_color, fg=button_text_color, command=valider_inscription)
valider_bouton.pack()

# Lancez la boucle d'événements
fenetre.mainloop()
