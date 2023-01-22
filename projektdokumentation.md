# Projekt-Dokumentation

✍️ Soldo

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|       | 0.0.1   | ✍️ Jedes Mal, wenn Sie an dem Projekt arbeiten, fügen Sie hier eine neue Zeile ein und beschreiben in *einem* Satz, was Sie erreicht haben. |
|       | 0.0.2   |                                                              |
|       | 0.0.3   |                                                              |
|       | 0.0.4   |                                                              |
|       | 0.0.5   |                                                              |
|       | 0.0.6   |                                                              |
|       | 1.0.0   |                                                              |

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
✍️ Beschreiben Sie für dieselben Tiers, welche Programmiersprache bzw. Technologie Sie verwenden möchten.

 * Tier 1: HTML / CSS
 * Tier 2: Python oder Java (noch unsicher)
 * Tier 3: Python oder Java (noch unsicher)
 * Tier 4: SQL

# 3 Datenbank
✍️ Wie steuern Sie Ihre Datenbank an? Wie ist das Interface aufgebaut? 


# 4.1 User Stories

✍️ Formulieren Sie klare Anforderungen in der Form von User Stories (*„als … möchte ich … damit …“*) und zu jeder Anforderung mindestens einen dazugehörigen Testfall (in Kapitel 4.2). 

✍️ Formulieren Sie weitere, eigene Anforderungen und Testfälle, wie Sie Ihre Applikation erweitern möchten. Geben Sie diesen statt einer Nummer einen Buchstaben (`A`, `B`, etc.)

| US-№ | Verbindlichkeit |    Typ     | Beschreibung                       |
| ---- | --------------- | ---------- | ---------------------------------- |
| 1    |      Muss       | Funktional | Als ein Spieler möchte ich ein Buchstaben auswählen können, damit ich das Wort erraten kann|
| 2    |      Muss       | Funktional | Als ein Spieler möchte ich am Rad drehen, damit ich einen Betrag erhalte|
| 3    |      Muss       | Funktional | Als ein Spieler möchte ich auf "lösen" klicken, damit ich das Rätsel lösen kann|
| 4    |      Muss       | Funktional | Als ein Spieler möchte ich sehen, welche Bichstaben noch zur Verfügung stehen und welche nicht, damit es nicht zu wiederholungen kommt|
| 5    |       Muss      | Funktional | Als ein Spieler möchte die jetztige Zahl an Runden ansehen, damit ich weiss in welcher Runde ich mich befinde|
| 6    |       Muss      | Funktional | Als ein Spieler möchte ich jederzeit aufhören können, damit ich meinen Gewinn in der Highscore-Liste übernehmen kann.|
| 7    |       Muss      | Funktional | Als ein Spieler möchte ich meinen Namen eintragen können, damit dieser auf der Highscore-Liste erscheint|


✍️ Jede User Story hat eine ganzzahlige Nummer (1, 2, 3 etc. oder Zahl), eine Verbindlichkeit (Muss oder Kann?), und einen Typ (Funktional, Qualität, Rand). 



# 4.2 Testfälle

| TC-№ | Vorbereitung | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  | Der Spieler muss einen Buchstaben auswählen| Der Spieler wählt einen Buchstaben aus | Der ausgewählte Buchstabe ist entweder im Wort vorhanden oder nicht|
| 2.1  | Der Spieler muss am Rad drehen| Der Spieler wählt die funktion aus, bei dem man am Rad drehen muss| Rad dreht sich und gibt einen Betrag aus|
| 3.1  | Der Spieler kennt die Lösung| Der Spieler wählt die Funktion "lösen" aus| Der Spieler kann jetzt die Lösung eintragen|
| 3.2  | Der Spieler hat "lösen" gedrückt| Der Spieler tippt die mögliche Lösung ein. | Die Lösung wird entweder als Richtig oder Flasch angezeigt|
| 4.1  | Das Spiel läuft | Der Spieler kann ich sehen welche Buchstaben noch zur verfügung stehen | Die zur Verfügung gestellten Buchstaben werden dann benutzt|
| 5.1  | Das Spiel läuft | Die 3te Runde ist im gange | Der Rundenzähler zeigt "3" an|
| 6.1  | Das Spiel ist gespielt / wird noch gespielt | Der Spieler drückt auf "aufhören" | Der Gewinn des Spieler wird übernommen|
| 7.1  | Das Spiel is am laufen | Der Name des Spielers, Beispiel: "Marko" | Ausgabe in der Highscore-Liste wird dann "Marko" sein|

✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, die der Testfall abdeckt, und `m` von `1` an nach oben gezählt. Beispiel: Der dritte Testfall, der die zweite User Story abdeckt, hat also die Nummer `2.3`.

# 5 Prototyp

✍️ Erstellen Sie Prototypen für das GUI (Admin-Interface und Quiz-Seite).

Quiz Seite
![image](https://user-images.githubusercontent.com/69591610/211218128-9900ad47-a268-4016-ae98-7a2515e62504.png)


# 6 Implementation

✍️ Halten Sie fest, wann Sie welche User Story bearbeitet haben

| User Story | Datum | Beschreibung |
| ---------- | ----- | ------------ |
| ...        |       |              |

# 7 Projektdokumentation

| US-№ | Erledigt? | Entsprechende Code-Dateien oder Erklärung |
| ---- | --------- | ----------------------------------------- |
| 1    | ja / nein |                                           |
| ...  |           |                                           |

# 8 Testprotokoll

✍️ Fügen Sie hier den Link zu dem Video ein, welches den Testdurchlauf dokumentiert.

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |       |          |        |
| ...  |       |          |        |

✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

# 9 `README.md`

✍️ Beschreiben Sie ausführlich in einer README.md, wie Ihre Applikation gestartet und ausgeführt wird. Legen Sie eine geeignete Möglichkeit (Skript, Export, …) bei, Ihre Datenbank wiederherzustellen.

# 10 Allgemeines

- [ ] Ich habe die Rechtschreibung überprüft
- [ ] Ich habe überprüft, dass die Nummerierung von Testfällen und User Stories übereinstimmen
- [ ] Ich habe alle mit ✍️ markierten Teile ersetzt
