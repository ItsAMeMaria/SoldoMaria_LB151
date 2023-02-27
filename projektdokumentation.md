# Projekt-Dokumentation

Soldo

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|  13.02.2023     | 0.0.1   | Datei erstellt, Django eingebunden. Index.html gemacht|
|  19.02.2023     | 0.0.2   | Datei gelöscht, Django hat nicht richtig funktioniert.|
|  20.02.2023     | 0.0.3   | Neues Projekt erstellt, index.html gemacht.        |
|  21.02.2023     | 0.0.4   | Player_add() in index.html eingebunden             |
|  21.02.2023     | 0.0.5   | Django's admin interface eingebunden in die Applikation, mit einem Admin Login|
|  25.02.2023     | 0.0.6   | Models für die Datenbank gemacht, random_word() erstellt.   |
|  25.02.2023     | 0.0.7   | game.html gemacht (+ kleines css)
|  26.02.2023     | 0.0.7   | play_game() gemacht, in game.html eingebunden + random_word verfeinert. |

# 0 Ihr Projekt
In diesem Projekt, werde ich ein bekanntes Quizspiel, das Glücksrad, programmieren. Beim Glücksrad muss man ein Rad drehen, den richtigen Buchstaben auswählen und natürlich das Wort erraten.

# 1 Analyse
* Tier 1 (Presentation): 
  * Kategorie anzeigen
  * Spieler anzeigen
  * Anzahl Punkte anzeigen
  * Buchstaben (genommene und nicht genommene) anzeigen
  * Buchstaben angeben
  * Rad anzeigen
  * Rad drehen 
* Tier 2 (Webserver):
  * Buchstabe mit den Buchstaben im Wort vergleichen. 
* Tier 3 (Application Server):
  * Ausgewählten Buchstaben mit dem gegeben Wort vergeleichen.
  * Überprüfen ob der Buchstabe schon verwendet worden ist. 
* Tier 4 (Dataserver):
  * Kategorien und dessen Wörter gepseichert halten. 

# 2 Technologie
 * Tier 1: HTML / CSS
 * Tier 2: Python (Framework: Django)
 * Tier 3: Python 
 * Tier 4: SQLite

# 3 Datenbank
Die Datenbank wird mit dem Framework, Django, gesteurt und verwaltet. Für die SQLite DB gibt es schon standardmässig eine vordefinierte Einstellung in 'settings.py'. Dort stehen die Datenbankkonfigurationen.

# 4.1 User Stories

| US-№ | Verbindlichkeit |    Typ     | Beschreibung                       |
| ---- | --------------- | ---------- | ---------------------------------- |
| 1    |      Muss       | Funktional | Als ein Spieler möchte ich ein Buchstaben eintippen können, damit ich das Wort erraten kann|
| 2    |      Muss       | Funktional | Als ein Spieler möchte ich am Rad drehen, damit ich einen Betrag erhalte|
| 3    |      Muss       | Funktional | Als ein Spieler möchte ich auf "lösen" klicken, damit ich das Rätsel lösen kann|
| 4    |      Muss       | Funktional | Als ein Spieler möchte ich sehen, welche Buchstaben noch zur Verfügung stehen und welche nicht, damit es nicht zu wiederholungen kommt|
| 5    |       Muss      | Funktional | Als ein Spieler möchte die jetztige Zahl an Runden ansehen, damit ich weiss in welcher Runde ich mich befinde|
| 6    |       Muss      | Funktional | Als ein Spieler möchte ich jederzeit aufhören können, damit ich meinen Gewinn in der Highscore-Liste übernehmen kann.|
| 7    |       Muss      | Funktional | Als ein Spieler möchte ich meinen Namen eintragen können, damit dieser auf der Highscore-Liste erscheint|


# 4.2 Testfälle

| TC-№ | Vorbereitung | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  | Der Spieler muss einen Buchstaben auswählen| Der Spieler wählt einen Buchstaben aus | Der ausgewählte Buchstabe ist entweder im Wort vorhanden oder nicht|
| 4.1  | Das Spiel läuft | Der Spieler kann sehen welche Buchstaben noch zur verfügung stehen | Die zur Verfügung gestellten Buchstaben werden dann benutzt|
| 7.1  | Das Spiel is am laufen | Einen Namen eintragen | Wird in der Datenbank gespeichert|
| 7.2  | Das Spiel is am laufen | Der Name des Spielers, Beispiel: "Marko" | Ausgabe in der Highscore-Liste wird dann "Marko" sein|

# 5 Prototyp
#### Willkommensseite (Spielername eintragen oder sich als Admin einloggen)
![image](https://user-images.githubusercontent.com/69591610/213945317-f6497e4a-6edd-4b29-9c12-a68a262f55c8.png)

#### Quiz Seite
![image](https://user-images.githubusercontent.com/69591610/211218128-9900ad47-a268-4016-ae98-7a2515e62504.png)

#### Admin Seite (Admin Login und Adminseite)
![image](https://user-images.githubusercontent.com/69591610/213945488-03423f2b-abc0-489d-b9fb-8b9b2653d56a.png)
![image](https://user-images.githubusercontent.com/69591610/213946010-27bde3fe-e6ea-472f-8ef7-62244ae81487.png)


# 6 Implementation

| User Story | Datum | Beschreibung |
| ---------- | ----- | ------------ |
| 7    | 21.02.2023| Nur das man den Spielernamen eintragen kann.|
| 1    | 26.02.2023      |   play_game gemacht und in game.html eingebunden|
| 4    | 26.02.2023| play_game|


# 7 Projektdokumentation

| US-№ | Erledigt? | Entsprechende Code-Dateien oder Erklärung |
| ---- | --------- | ----------------------------------------- |
| 1    | ja  |    'game.html', 'views.py -> play_game()'     |
| 4 |  ja (teilweise)    |    Man sieht die nur die richtig vorgekommenen Buchstaben, 'views.play_game'   |
| 7| ja (teilweise)| Spielername kann eingetragen werden, wird aber nicht angezeigt. 'views.py -> add_player'

# 8 Testprotokoll
[![IMAGE ALT TEXT HERE](http://i3.ytimg.com/vi/rq_8SIujlYI/hqdefault.jpg)](https://youtu.be/rq_8SIujlYI)

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  | 27.02.2023 | OK  |  Maria Soldo      |
| 4.1  | 27.02.2023 |  OK/NOK  |    Maria Soldo    |
| 7.1  | 27.02.2023 |   OK  | Maria Soldo        |

#### Fazit
Man kann einen Namen eingeben, Buchstaben eintippen aber sonst nicht viel (Keine Highscoreliste, kein Gewinner/Verlierer etc.). 
Wenn man den richtigen Buchstaben eingetragen hat, wird der ja auch dann im Wort/Satz erscheinen, aber die die halt nicht richtig waren, erscheinen dann auch nicht, deswegen auch das OK/NOK.

# 9 `README.md`
https://github.com/ItsAMeMaria/SoldoMaria_LB151/blob/main/README.md

# 10 Allgemeines

- [ ] Ich habe die Rechtschreibung überprüft
- [ ] Ich habe überprüft, dass die Nummerierung von Testfällen und User Stories übereinstimmen
- [ ] Ich habe alle mit ✍️ markierten Teile ersetzt
