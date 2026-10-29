# Schutz-Schnittstelle

Liegt im Container mit dem Interpreter die Datei **Name_der_Interpreterbibliothek.dat** (im Folgenden: Datei mit geheimen Daten), wird einem solchen Interpreter bei der Initialisierung zusätzlich die Schnittstelle **INCT_Connect** übergeben.

**INCT_Connect** - Schnittstelle, die dem Interpreter den Zugriff auf die Daten aus der Datei mit geheimen Daten ermöglicht. Die Datei wird dabei nicht aus dem Container entpackt und ist deshalb nur über die dem Interpreter übergebene Schnittstelle lesbar.

Der Interpreter muss so entwickelt werden, dass er erst nach erfolgreicher Prüfung der über die Schnittstelle **INCT_Connect** erhaltenen Daten arbeitet. Stellen, Anzahl und Algorithmus der Prüfungen legt der Entwickler selbst fest.

**Beschreibung der Schnittstellenmethoden:**

<table>
<thead>
<tr><th>Methode</th><th>Beschreibung der Methode</th><th>Verwendung</th></tr>
</thead>
<tbody>
<tr><td><strong>Get_Count<br></strong></td><td>Die Funktion gibt die Anzahl der Bytes in der Datei mit geheimen Daten zurück (Ganzzahl).</td><td rowspan="3"><p>Mit diesen Methoden müssen die Daten, die der Entwickler des Interpreters im Container abgelegt hat, mit den Daten verglichen werden, die das CAM-System dem Interpreter übergibt (sie müssen übereinstimmen).</p><p>Hat der Entwickler im Container die Datei sample.dat (die Bibliothek des Interpreters heißt sample.dll) mit einer Größe von 5 Bytes und folgenden Daten abgelegt: 12345</p><p>Die Funktion <strong>Get_Count</strong> gibt den Wert 5 zurück.</p><p>Die Funktion <strong>Get_Data</strong>(0) gibt den Wert 1 zurück, <strong>Get_Data</strong>(2) den Wert 3, <strong>Get_Data</strong>(4) den Wert 5.</p><p>Die Methode <strong>Get_SCData</strong> gibt einen Zeiger auf den Speicher mit den Daten 12345 zurück.</p></td></tr>
<tr><td><strong>Get_Data<br></strong></td><td><p>Die Funktion gibt das Byte aus der Datei mit geheimen Daten zurück, dessen Nummer im Eingabeparameter angegeben ist.</p><p>Eingabeparameter: <strong>Index</strong> (Ganzzahl) - Nummer des zurückgegebenen Bytes. Die Nummerierung der Bytes beginnt bei 0.</p><p>Ausgabeparameter: Byte aus der Datei mit geheimen Daten mit der im Parameter <strong>Index</strong> angegebenen Nummer.</p></td></tr>
<tr><td><strong>Get_SCData<br></strong></td><td><p>Die Methode gibt einen Zeiger auf die geheimen Daten aus der Datei zurück.</p><p>Ausgabeparameter: <strong>Data</strong> (Zeiger) - Zeiger auf die geheimen Daten.</p></td></tr>
</tbody>
</table>
