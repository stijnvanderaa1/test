import socket
import paramiko
import time

import config
import gather_information
import run_job
from config import system_info


def send_data_to_mainframe(data):
    """Stuur gegevens naar het mainframe via SSH."""
    # Configuraties voor SSH-verbinding
    host = '204.90.115.200'  # Mainframe IP of hostnaam
    port = 22  # SSH poort (standaard 22)
    username = 'Z58593'  # Jouw SSH gebruikersnaam
    password = 'LOT83DAM'  # Jouw SSH wachtwoord

    # Maak verbinding met de mainframe via SSH
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Beveiliging voor onbekende sleutels
        client.connect(host, port, username, password)

        # Maak een bestand aan met de netwerkpoortinformatie die we zullen verwerken op het mainframe
        sftp = client.open_sftp()

        # Zet het bestand naar de juiste locatie op de mainframe server (bijv. /tmp)
        command = f"echo '{data}' > PROJECT/INFO"
        stdin, stdout, stderr = client.exec_command(command)
        # In dit geval slaan we de JCL-job stap over, zodat we geen REXX script starten
        print("Data succesvol naar het mainframe bestand gestuurd: /PROJECT/info.txt")

        # Sluit de verbinding met het mainframe
        sftp.close()
        client.close()

    except Exception as e:
        print(f"Fout bij het verbinden met het mainframe: {e}")


def main():
    # Verkrijg de open poorten


    # Stuur de open poorten naar het mainframe voor verwerking
    send_data_to_mainframe(gather_information.gather_system_info())
    run_job.submit_job()

if __name__ == "__main__":
    main()