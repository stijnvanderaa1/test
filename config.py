import gather_information

# Systeeminstellingen voor verbinding met z/OS via Zowe CLI
zos_id = "z58593"  # Dit is een unieke identifier voor je z/OS-systeem (bijv. een systeemnaam of IP-adres)
zos_user = "z58593"  # De gebruikersnaam die wordt gebruikt om in te loggen op het z/OS-systeem
zos_password = "LOT83DAM"  # Het wachtwoord voor de opgegeven gebruiker
zos_host = "204.90.115.200"  # Het hostadres van het z/OS-systeem
zos_port = 10443  # De poort waarop de Zowe API draait (meestal 443 voor HTTPS)

# Zowe CLI configuratie (optioneel als je Zowe CLI gebruikt)
zowe_cli_profile = "my_zowe_profile"  # Dit kan een profiel zijn dat is ingesteld in de Zowe CLI voor authenticatie

# Specifieke dataset of job naam voor z/OS
job_name = "SYSINFO"  # Dit is de naam van de JCL-job die we willen indienen
job_dataset = f"{zos_id}.PROJECT(SYSINFO)"  # Dit is de volledige datasetnaam, bijvoorbeeld voor het indienen van een job

# Verzamel systeeminformatie
cpu_info = gather_information.get_cpu_info()
memory_info = gather_information.get_memory_info()
disk_info = gather_information.get_disk_info()
network_info = gather_information.get_network_info()
system_info = gather_information.get_system_info()

log_level = "DEBUG"  # of een ander geschikt niveau zoals "INFO" of "ERROR"
