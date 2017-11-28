#smptlib obsluguje poczte w pythonie
#importujemy plik z loginem i haslem
#mailer moze byc wyslany do chmury, secrets jest tylko u mnie lokalnie

import smtplib
import dzien7.secrets

adresat = dzien7.secrets.login
nadawca = dzien7.secrets.login
haslo = dzien7.secrets.haslo

#tworze silnik mailera
#SMTP tworzy mi silnik
#podaje sciezke oraz port
mailer = smtplib.SMTP("smtp.gmail.com", 587)

#witam sie z serwerem, łąćze się
mailer.ehlo()
#szyfruje polaczenie
mailer.starttls()
#loguję się
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Monika\n"
wiadomosc = "To jest moja wiadomosc"
tresc = temat + wiadomosc

#wysylam
mailer.sendmail(nadawca, adresat, tresc)
print("Wysłano maila!")

mailer.close()

