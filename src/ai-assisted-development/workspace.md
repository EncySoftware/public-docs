# Organisation des Arbeitsbereichs

Der Assistent beginnt jede Sitzung ohne Erinnerung an die vorherige. Er weiß nicht mehr, was Sie gestern vereinbart haben, welche Steuerung im letzten Monat Ärger gemacht hat und warum der Interpreter ein bestimmtes Wort genau so liest. Er weiß, was in Ihrem Arbeitsordner steht; was nur im Chatverlauf geblieben ist, existiert für ihn nicht.

Deshalb ist der Arbeitsordner keine Ordnung um der Ordnung willen, sondern das Gedächtnis des Assistenten. Einige Stunden, die Sie einmal darauf verwenden, ersparen Ihnen dieselben Erklärungen in jeder folgenden Sitzung.

## Was hineingehört

Ein Ordner, der in Visual Studio Code geöffnet ist:

```text
work\
├── AGENTS.md         was der Assistent jedes Mal wissen muss
├── interpreters\     Quellen der Interpreter, ein Ordner pro Interpreter
├── programs\         echte NC-Programme der Maschine und erwartete Ergebnisse
├── projects\         Projekte des CAM-Systems mit der Maschine
├── manuals\          Programmierhandbuch der Steuerung
└── notes\            Ihre Erfahrungen und gelöste Fälle
```

Die Namen sind nicht wichtig, wichtig ist die Trennung: Quellen getrennt von Testdaten, Ihr Wissen getrennt von der offiziellen Dokumentation.

## Programme und Maschine

Legen Sie in `programs\` mehrere echte NC-Programme dieser Maschine, nicht nur eines: von ihrem Postprozessor erzeugte, von Hand geschriebene, aus anderen CAM-Systemen. Die Schreibweise der Wörter übernimmt der Assistent aus ihnen: Dieselbe Achse kann als `B90`, `B=90` und `B1=90` vorkommen, und der Interpreter muss jede Schreibweise verstehen, die in Ihren Programmen vorkommt. Wenn es einen Postprozessor gibt, der diese Programme erzeugt, legen Sie auch ihn dazu: An ihm sieht man, welche Varianten der Wörter auftreten werden.

Legen Sie daneben das Projekt des CAM-Systems mit dieser Maschine (`*.stcp`) und, falls vorhanden, das erwartete Ergebnis: was die Maschine mit dem Programm macht. Das Handbuch der Steuerung in `manuals\` ist die wichtigste Quelle für die Bedeutung der Wörter; ohne es wird der Assistent raten.

Bitten Sie den Assistenten, eine Liste der Wörter aus allen Programmen zu erstellen — das erledigt der Skill `inspect-nc-programs`. Die Liste zeigt, welche Wörter der Interpreter bereits versteht und welche nicht, und dient als Liste dessen, was nach jeder Änderung zu prüfen ist.

## AGENTS.md — kurze dauerhafte Merkhilfe

Diese Datei wird zu Beginn jeder Sitzung gelesen, halten Sie sie daher kurz — nicht mehr als eine Seite — und lagern Sie Details in `notes\` aus. Was darin Platz verdient:

- Maschine, Steuerung und deren Version, welcher Interpreter sie bedient;
- Versionen des CAM-Systems und von ENCY Tuner, in denen der Interpreter arbeiten muss;
- wo was liegt: Programme, Projekte, Handbuch, Notizen;
- Arbeitsregeln — zuerst Programme und Handbuch lesen, Änderungen minimal halten, nach jeder Änderung alle Programme durchlaufen lassen und mit dem vorherigen Ergebnis vergleichen;
- Einschränkungen, die Sie bereits einmal formuliert haben — so aufgeschrieben, wie Sie sie gesagt haben. Sonst schlägt der Assistent in einem Monat erneut eine Idee vor, die Sie begründet verworfen haben.

Bitten Sie den Assistenten, einen Entwurf zu erstellen, und korrigieren Sie ihn — das geht schneller, als mit einer leeren Datei anzufangen.

## notes — wo sich Ihre Erfahrung sammelt

Nach jedem gelösten Fall eine kurze Datei: was falsch war, wie es gefunden wurde, was geholfen hat **und warum genau so**. Gerade das „Warum“ spart später Zeit.

- **Ein Thema — eine Datei**, nicht eine wachsende: Eine kleine Datei ist leicht zu finden und günstig zu lesen.
- **Beschreiben Sie den aktuellen Stand.** Anmerkungen wie „früher war es anders“ veralten mit der Zeit; steht der Ordner unter Versionskontrolle, gibt es den Verlauf ohnehin.

Führen Sie in `notes\` auch eine schriftliche Liste der Wünsche und Entscheidungen zur aktuellen Aufgabe. Ein langes Gespräch fasst der Assistent zusammen, und Details gehen dabei verloren; die Liste nicht. Bevor er „fertig“ meldet, bitten Sie den Assistenten, sie Punkt für Punkt durchzugehen und für jeden Punkt einen Nachweis zu zeigen.

Wenn sich ein Arbeitsablauf zu wiederholen beginnt — dieselbe Prüfung, dieselbe Reihenfolge für eine Familie von Steuerungen —, schreiben Sie ihn als eigenen Skill auf: einen Ordner mit einer Datei `SKILL.md`, wie bei den mitgelieferten Skills. Der Client findet Skills nur in seinem Skills-Ordner, legen Sie Ihren Skill daher dorthin, wo auch die übrigen installiert sind (siehe [erweiterte Einrichtung](advanced-setup.md#skills-in-verschiedenen-ki-clients)); eine Datei in `notes\` liest der Assistent nur, wenn Sie ihn darauf hinweisen. Einen Skill, in dem Kunden oder Besonderheiten genau Ihrer Maschinen genannt sind, geben Sie nicht zusammen mit dem Interpreter weiter und veröffentlichen ihn nicht.

## Zwei Arten, den Verlauf zu führen

### Ordner und Kopien — den Verlauf führen Sie selbst

Vor einer wesentlichen Änderung kopieren Sie den Ordner des Interpreters, neben den Programmen bewahren Sie die Ergebnisse früherer Durchläufe auf, und als Verlauf dienen Ordner mit Datum. Auch so lässt sich arbeiten. Der Preis dafür: Der Verlauf hängt an Ihrem Gedächtnis — vergessen Sie eine Kopie, ist der vorherige Stand verloren.

### Git — den Verlauf führt das Werkzeug

Derselbe Ordner, aber für die Vergangenheit ist ein Werkzeug zuständig, das genau dafür gemacht ist. Es nimmt auch die größte Sorge bei der Arbeit mit einem Assistenten: Jeder Stand ist gespeichert, deshalb kostet eine missglückte Änderung eine Minute für das Zurücksetzen und nicht einen funktionierenden Interpreter.

Git müssen Sie dafür nicht lernen. Sie bitten in Worten, und der Assistent führt es aus:

- „committe, Achse B1 wird gelesen“ — er committet die Änderung mit einer Nachricht, wozu sie dient;
- „vergleiche mit dem Stand vom Freitag“ — er zeigt, was sich geändert hat;
- „finde heraus, seit wann der Zyklus G83 nicht mehr simuliert wird“ — er sucht im Verlauf;
- „stelle den Stand vor der letzten Änderung wieder her“ — er stellt ihn aus dem Verlauf wieder her, statt ihn neu zu schreiben.

Ist git nicht installiert, bitten Sie den Assistenten, es zu installieren — der offizielle Download ist unter [git-scm.com](https://git-scm.com/downloads). Bitten Sie ihn dabei auch, Build-Ergebnisse (`bin`, `obj`) und Protokolle vom Verlauf auszuschließen.

## Wenn der geöffnete Ordner der Ordner des Interpreters sein muss

Für einen Interpreter in C# muss Visual Studio Code auf dem Ordner des Interpreters selbst geöffnet sein — so funktionieren Bauen und Debuggen mit der Taste `F5`. Merkhilfe und Notizen liegen dann oberhalb des geöffneten Ordners. Zwei Kniffe genügen:

- **Halten Sie alles in einem Repository.** Das Repository sei der ganze Ordner `work\`, und die Ordner der Interpreter liegen darin. Git funktioniert aus jedem Unterordner, und der Verlauf bleibt einer.
- **Machen Sie die Merkhilfe aus dem Ordner des Interpreters sichtbar.** Claude Code liest die Anweisungsdateien in den Ordnern oberhalb des geöffneten selbst, er braucht nichts weiter. Kilo Code liest nur den geöffneten Ordner: Geben Sie die Merkhilfe in seinen Einstellungen an oder legen Sie in den Ordner des Interpreters eine kurze `AGENTS.md` mit zwei Zeilen: Regeln — in `..\..\AGENTS.md`, Notizen — in `..\..\notes\`. Ausführlich in der [erweiterten Einrichtung](advanced-setup.md#anweisungsdatei-des-arbeitsordners).

Installieren Sie die Skills für den Benutzer, nicht für den Arbeitsordner: Dann stehen sie bei jedem geöffneten Ordner zur Verfügung, und es genügt, sie einmal abzulegen.

## Was nicht hineingehört

Passwörter, Token, Lizenzdateien, Kundenarchive, die nichts mit dem Interpreter zu tun haben, und fremde Repositorys. Alles, was im Arbeitsordner liegt, darf der Assistent lesen, und wenn Sie einen Verlauf führen, bleibt es darin. Wenn ein Programm des Kunden nur als Beispiel benötigt wird, geben Sie eine gekürzte Fassung: einige Sätze mit dem zu prüfenden Wort und den Programmkopf.
