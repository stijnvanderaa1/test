import subprocess
import config


def submit_job():
    try:
        # De datasetnaam voor de JCL-job
        random_job = f"{config.zos_id}.PROJECT({config.job_name})"

        # Het Zowe CLI-commando om de job in te dienen
        random_command = f'zowe zos-jobs submit data-set "{random_job}"'

        # Voer het commando uit via subprocess
        result = subprocess.run(random_command, shell=True, check=True, capture_output=True, text=True)

        # Print de uitvoer van het commando (bijvoorbeeld voor debugging)
        print(f"Job submitted successfully. Output:\n{result.stdout}")

    except subprocess.CalledProcessError as e:
        # Foutafhandelingsblok voor eventuele fouten tijdens het uitvoeren van het commando
        print(f"Error occurred while submitting the job: {e.stderr}")
        print(f"Exit code: {e.returncode}")
        # Optioneel: voeg logging toe als je logbestanden gebruikt
        if config.log_level == "DEBUG":
            print(f"Command that failed: {e.cmd}")

    except Exception as e:
        # Algemene foutafhandeling voor andere onverwachte fouten
        print(f"An unexpected error occurred: {str(e)}")


