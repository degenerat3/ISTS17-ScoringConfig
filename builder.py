# Turn all those pesky configs into a massive giant config
import random
import string

TEAM_LOW = 1
TEAM_HIGH = 13

checks = [
    # Local net
    "Alexander",
    "Julius",
    "Churchhill",
    "Leonidas",
    "Attila",
    "Xerxes",
    "Ashoka",
    # Cloud net
    "Gandhi",
    "Bonaparte",
    "Ataturk"
    ]

team_passwords = [
    "team0-0000",
    "team1-DBKW",
    "team2-ZX5T",
    "team3-PB5J",
    "team4-OL1T",
    "team5-BUFV",
    "team6-503C",
    "team7-XJ91",
    "team8-A45T",
    "team9-XI0L",
    "team10-4Y5A",
    "team11-4LIQ",
    "team12-5QPE",
    "team13-GTPI"
]

def build_team(team):
    """Build a team for the given team number
    """
    output = ""
    with open("base_team.yml") as inf:
        data = inf.read().rstrip()
        output = data.replace("$TEAM", str(team)) # Change the team number
        output = output.replace("$PASSWORD", team_passwords[team])
        output += "\n"

    for check in checks:
        check = check.lower()+".yml"
        with open("check_configs/"+check) as inf:
            data = inf.read().rstrip()
            data = data.replace("$TEAM", str(team)) # Change the team number
            output += data + "\n"
    return output
            

def build_all():
    """ Build all the config"""
    with open("competition.yml", "w") as ofil:
        # Load the base config and write it to the outfile
        with open("base.yml") as inf:
            ofil.write(inf.read().rstrip())
            ofil.write("\n")
        # Iterate all the teams and add them to the outfile
        for team in range(TEAM_LOW, TEAM_HIGH+1):
            ofil.write(build_team(team))
        
    print("Config written to competition.yml")

if __name__ == "__main__":
    build_all()