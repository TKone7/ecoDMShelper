# Archive GMail attachments

Dieses einfache Tool erlaubt es mithilfe von QmailAgent Anhänge von Google-Mails herunterzuladen und in den Scaninput-Ordner von ecoDMS zu verschieben.

# Setup
## Vorausetzung
Zuerst muss QmailAgent so eingerichtet sein, dass die Attachments unabhängig von den Mails in einem Verzeichnis abgelegt werden. Das Verzeichnis kann frei gewählt werden, muss aber im Pythonskript angegeben werden. Die Ordnerstruktur sieht dann wiefolgt aus.
- Gewhählter Pfad
  - QmailAgent_xyz@gmail.com
    - attachment
      - 2019
      - 2018
      - 2017
      - ...


## Platzieren des Shell-Scripts
Um das Python-Skript via Cron-Job zu starten, muss ein Wrapper-Shell-Skript erstellt werden. Dieses hat lediglich eine Zeile und führt Python aus:

```
#!/bin/sh

python path_to_script # e.g. .../my_att.py

```

## Pfade

`src` = Pfad zum attachment Verzeichnis (siehe oben)
`dest` = Scaninput-Verzeichnis des ecoDMS
`path_to_shell` = Pfad zum Shell-Skript
`path_to_script` = Pfad zum Python-Skript

## Platzieren des Python-Skripts
Das Skript `mv_att.py` kann an einen beliebigen Ort gespeichert werden. Die beiden Variabeln `src` und `dest` müssen vorher korrekt gesetzt werden.

## Cron-Job
Um das Python-Skript in einem Intervall laufen zu lassen definieren wir einen Cron-Job.
__WICHTIG:__ Diese Anleitung bezieht sich auf QNAP NAS Systeme. Auf anderen Servern können die Befehle abweichen.

Definiert einen Cron-Job der alle 5 Minuten läuft.
```
# echo "*/5 * * * * path_to_shell"  >> /etc/config/crontab
```
Cron-Job Daemon muss neugestartet werden.
```
 # crontab /etc/config/crontab && /etc/init.d/crond.sh restart
```
