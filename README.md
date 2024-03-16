# THM_agentsudo
try hack me ctf agendsudo
## CTF Report

### Information:
- IP: 10.10.188.104

### Step 1/2: Enumeration

#### Passive Enumeration:
- Utilisation d'un script d'enumeration de port par ChatGPT
  - Retour du script `hostenum.py` :
    ```
    Ports ouverts sur l'adresse IP 10.10.205.190:
    Port 21 est ouvert (Service : ftp)
    Port 22 est ouvert (Service : ssh)
    Port 80 est ouvert (Service : http)
    ```

#### Active Enumeration:
- Recuperation d'info sur le port 80
  - `$ curl http://10.10.205.190 > annex001.txt`
  - `$ curl -A "C" http://10.10.205.190` retourne un message secret, l'option -A specifie l'user-agent
- Recuperation d'info sur le port 21
  - `$ nmap -Pn -sV 10.10.188.104 -p 21`
    ```
    PORT   STATE SERVICE VERSION
    21/tcp open  ftp     vsftpd 3.0.3 Service Info: OS: Unix
    ```
- Recuperation d'info sur le port 22
  - `$ nmap -Pn -sV 10.10.188.104 -p 22`
    ```
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
    ```

### Step 3: Chercher une entrée

#### Recherche de vulnérabilité:
- `$ nmap -Pn --script="vuln" 10.10.188.104`
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)

#### Brute force:
- `$ hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://10.10.188.104`
[21][ftp] host: 10.10.188.104 login: chris password: crystal

### Step 4: Obtenir l'accès FTP de Chris

#### Les pièces numériques trouvées sur le serveur FTP se trouvent dans l'annex02.
#### Il se pourrait qu'un message soit caché dans les images
- Analyse du fichier `cutie.png`
- Utilisation de `exiftool` et `binwalk` pour découvrir une archive ZIP cachée.
- Extraction du fichier ZIP
- Utilisation de `zip2john` pour extraire le hash du mot de passe.
- Crackage du mot de passe avec `john`.
- Lecture du message caché dans le fichier `message.txt`.

### Step 5: Obtenir l'accès SSH de James

#### Accès SSH
- Connexion avec les informations trouvées.
- Récupération du flag utilisateur.

#### Privilège Escalation
- `sudo -l` montre les permissions de l'utilisateur James.
