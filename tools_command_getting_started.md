## Werken met een shell

Eén van de eerste basis-vaardigheden van een software-ontwikkelaar is het kunnen omgaan met een shell of command-line.  
Het kunnen omgaan met de command-line is meestal noodzakelijk builden en deployen van je software:

* Starten en compilen van je software
* Automatisaties
* Flashen van de software op een microcontroller (of ontwikkelbordje)
* Automatisatie (bijvoorbeeld in 1 maal compilen en flashen)
* ...

Voor vele microcontrollers en toolchains bestaan er grafische tools, maar deze steunen in de meeste gevallen op command-line-tools in de achtergrond.  

### Wat is een shell?

Een shell is een programma waarmee je rechtstreeks toegang hebt tot **systeem-operaties** via tekst-commando's.

* Opstarten van programma's
* Navigeren door een file-systeem
* Manipuleren files en folders
* Controleren en monitoren van processen
* Automatiseren van taken
* Communicatie over een seriele lijn
* ...

### Tekst-commando's ingeven

Deze tekst-commando's kunnen meestal ook **gebundeld** worden in een **script** (dat je dan kan uitvoeren van een CLI net zoals je programma's kan uitvoeren)   

Nadat zo'n commando/script/programma is uitgevoerd krijgt de gebruiker weer de kans om de shell of het programma aan te spreken door op de opdrachtregel een nieuwe opdracht op te geven.  

### Waarom werken met een shell

Om het kort te houden, het is een tool die moet gekend zijn als je wil programmeren omdat we deze vaardigheden nodig hebben om later met toolchains (compiler en linkers) om te gaan.  

Elke software-ontwikkelaar moet de beginselen kennen van het werken met command-line.  
Dit argument is nog sterker als je met embedded devices werkt die veelal enkel te besturen zijn via command-line.

### Vervolg...

We gaan nu dit bekijken voor 2 soorten shell-omgevingen

* Windows CMD
* Bash (Linux, Mac e.a. Posix-systemen)
