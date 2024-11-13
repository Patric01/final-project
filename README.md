# final-project
Project
# Proiect Final - Automatizare cu Docker și Ansible

Acest proiect implementează un sistem de automatizare utilizând Docker, Docker Compose și Ansible. Scopul este să automatizeze rularea scripturilor într-un mediu containerizat și să faciliteze implementarea acestora pe diferite mașini.

## Cerințe preliminare

Pentru a rula acest proiect, trebuie să ai instalate următoarele pe sistemul tău:
- **Git**: pentru clonarea repository-ului
- **Python și pip**: pentru rularea scriptului Python
- **Docker și Docker Compose**: pentru gestionarea containerelor Docker
- **Ansible**: pentru implementarea automatizării pe alte servere

---

## Clonarea repository-ului

1. **Instalează Git** (dacă nu este deja instalat):
   ```bash
   sudo apt update
   sudo apt install git -y
git clone https://github.com/Patric01/final-project.git
cd final-project
##  Script bash
# Acest script rulează o buclă infinită și afișează informații despre sistem la fiecare câteva secunde.
chmod +x script_bash.sh
# Rulează scriptul
./script_bash.sh
## Script Python
# Asigură-te că Python este instalat:
sudo apt install python3 -y
# Instalează biblioteca psutil necesară
pip install psutil
# Rulează scriptul:
# Acest script rulează o buclă infinită și afișează informații despre sistem la fiecare câteva secunde.
python3 script_python.py
## Rularea containerelor individual
# Construiește imaginea Docker pentru scriptul Bash:
docker build -t bash_service -f Dockerfile_bash .
# Rulează containerul Bash
docker run -d --name container_bash bash_service
# Verifică output-ul containerului Bash:
docker logs container_bash
## Container Python
# Construiește imaginea Docker pentru scriptul Python
docker build -t python_service -f Dockerfile_python .
# Rulează containerul Python:
docker run -d --name container_python python_service
# Verifică output-ul containerului Python:
docker logs container_python
## Rularea deployment-ului Docker Compose
# Construiește și rulează serviciile definite în docker-compose.yml
docker-compose up -d
# Verifică dacă ambele containere rulează:
docker ps
# Verifică log-urile serviciilor:
# Pentru serviciul Bash
docker-compose logs bash_service
# Pentru serviciul Python
docker-compose logs python_service
# Oprește toate serviciile
docker-compose down
## Deploy cu Ansible
# Instalează Ansible:
sudo apt update
sudo apt install -y ansible
# Configurați inventarul Ansible: Creează un fișier hosts în directorul proiectului cu următorul conținut:
[docker_servers]
192.168.1.100 ansible_user=your_user
# Înlocuiește 192.168.1.100 cu adresa IP a serverului tău de destinație și your_user cu utilizatorul pe care îl folosești pentru accesul SSH la server.
# Configurează conexiunea SSH:
# Asigură-te că ai configurate cheile SSH pentru a te conecta la serverul de destinație.
# Testează conexiunea Ansible
ansible -i hosts docker_servers -m ping
# Rulează playbook-ul Ansible:
ansible-playbook -i hosts docker_deploy.yml --ask-become-pass
# Exemplu de Output
# Docker Compose
patric_cali@DESKTOP-PDM0H0U:~/final-project$ docker-compose up -d
Creating container_bash   ... done
Creating container_python ... done
# Ansible
patric_cali@DESKTOP-PDM0H0U:~/final-project$ ansible-playbook -i hosts docker_deploy.yml --ask-become-pass
BECOME password:

PLAY [Deploy Docker Compose Services] ******************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Creează directorul de deploy] ********************************************
ok: [localhost]

TASK [Copiază fișierul docker-compose.yml] *************************************
ok: [localhost]

TASK [Copiază Dockerfile_bash] *************************************************
ok: [localhost]

TASK [Copiază Dockerfile_python] ***********************************************
ok: [localhost]

TASK [Copiază scriptul Bash] ***************************************************
ok: [localhost]

TASK [Copiază scriptul Python] *************************************************
ok: [localhost]

TASK [Rulează serviciile Docker Compose] ***************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0





