import datetime
import time

heute = datetime.date.today()
print(heute)
x = 0

datei = open("berichtsheft.txt", "a")
datei.write("\n")
datei.write(str(heute))
datei.write("\n")
datei.close()

while x != 1:
    eingabe = input("Bitte gib die nächste Tätigkeit ein: ")
    if eingabe == "x":
        break
    else:
        datei = open("berichtsheft.txt", "a")
        datei.write(eingabe)
        datei.write("\n")
        datei.close()


print("Das Berichtsheft wurde erfolgreich bearbeitet.")
time.sleep(2)
