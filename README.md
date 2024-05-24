# python-selenium
Basisframework für automatisiertes GUI-Testing mit selenium und pytest.

## Notwendige Softwarepakete
- sorge dafür, dass Python (min. v.3.10.x; [python.org](https://www.python.org/downloads/)) inklusive pip auf PATH installiert ist.
- sorge dafür, dass geckodriver ([download...](https://github.com/mozilla/geckodriver/releases)) und/oder chromedriver ([download...](https://chromedriver.chromium.org/downloads)) als WebDriver über PATH zur Verfügung stehen. Dafür kannst du die BATCH-Datei im Hauptverzeichnis zu Rate ziehen und entweder den dort verwendeten Pfad benutzen, um deinen Webdriver dort abzulegen oder einen anderen Pfad einstellen.
- sorge dafür, dass git installiert ist (ebenfalls auf PATH verfügbar, [git-scm.com](https://git-scm.com/download/win))

## Welche Python-Pakete werden benötigt?
- selenium
- pytest
- pytest-html
- *optional*: pytest-xdist
- *optional*: pytest-bdd


## Schritte zum eigenen Testframework
- klone das Repository in ein Verzeichnis auf deinem PC
- erstelle einen neuen Branch mit deinem Namen "VornameNachname" und mache einen checkout in diesen branch
- erstelle auf Basis des main-Repos __in deinem neuen Branch__ dein eigenes Testframework und implementiere deine Testfälle
- Logge dich auf unserem Jenkins Server ([zum Server](http://92.205.24.45:8080/)) mit deinen Userdaten ein und erstelle dort einen Buildjob. Diesen verknüpfst du mit einem Webhook und einem Zugriffstoken, sodass Jenkins jedes Mal, wenn du *deinen* Branch auf das Git-Repository pushst, dein pytest-Script durchläuft. (__*ggf. genauere Anleitung formulieren!*__)
