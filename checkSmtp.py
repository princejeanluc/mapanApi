import smtplib

port = 587
try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', port)
    smtp_server.starttls()  # Si le serveur SMTP utilise le cryptage TLS
    smtp_server.login('princejeanluc.denteppe@gmail.com', '@Claireepety1999#')
    print("Connexion SMTP réussie")
except Exception as e:
    print("Erreur lors de la connexion SMTP :", e)

