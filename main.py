import subprocess
import shutil


def run_subprocess_with_command(command):
    """Runs a subprocess with the given command line.

    Args:
      command: The command line to execute.
    """
    try:
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Error running command: {command}")
            print(f"stderr: {stderr.decode()}")
        else:
            print(f"Command executed successfully: {command}")
            print(f"stdout: {stdout.decode()}")
    except Exception as e:
        print(f"Error running command: {command}")
        print(f"Exception: {e}")


wikis_to_get = [
    "overwatch",
    # "hades",
    # "elderscrolls",
    # "riskofrain2",
    # "helldivers",
    # "deeprockgalactic",
    # "terraria",
    # "minecraft",
    # "fortnite",
    # "divinity",
    # "baldursgate",
    # "wowpedia",
    # "diablo",
    # "eldenring",
    # "darksouls"
]

for wiki in wikis_to_get:
    command = f"python ScrapeFandom/ScrapeFandom.py {wiki}"
    run_subprocess_with_command(command)

    command = f"wikiextractor {wiki}.xml --no-templates -l --json -o {wiki}"
    run_subprocess_with_command(command)

    command = f"python3 ScrapeFandom/json2jsonl.py {wiki} {wiki}.jsonl"
    run_subprocess_with_command(command)

    command = "zip -r " + wiki + ".zip " + wiki
    run_subprocess_with_command(command)

for wiki in wikis_to_get:
    shutil.copytree(wiki, "out/" + wiki, dirs_exist_ok=True)

run_subprocess_with_command("zip -r wikis.zip out")
