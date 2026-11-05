# Entladen des Interpreters

**Das Entladen des Interpreters aus dem Speicher** besteht aus folgenden Schritten:

- Freigabe der Schnittstelle **INCT_Interpreter**;
- Freigabe des Speichers aller Objekte, die die Bibliothek selbst erstellt oder während der Arbeit vom CAM-System erhalten hat (Aufruf der Funktion **NCT_FreeMemory** der Bibliothek);
- Entladen der Bibliothek des Interpreters aus dem Speicher;
- Entladen der Eltern-Interpreter aus dem Speicher (falls vorhanden).

Danach ist der Speicher der erstellten Objekte freigegeben, und die Bibliothek des Interpreters sowie seine Eltern-Interpreter sind aus dem Speicher entladen.
