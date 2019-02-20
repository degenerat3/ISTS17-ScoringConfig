# Turn all those pesky configs into a massive giant config
import yaml

checks = ["Alexander", "Julius", "Churchhill", "Leonidas", "Attila", "Xerxes", "Ashoka",
          "Gandhi", "Bonaparte", "Ataturk"]

def build_team(team):
    """Build a team for the given team number
    """
    output = ""
    with open("base_team.yml") as inf:
        data = inf.read()
        output = data.replace("$TEAM", str(team)) # Change the team number
        output += "\n"
    for check in checks:
        check = check.lower()+".yml"
        with open("check_configs/"+check) as inf:
            data = inf.read()
            data = data.replace("$TEAM", str(team)) # Change the team number
            output += data
    return output
            

def build_all():
    with open("competition.yml", "w") as ofil:
        with open("base.yml") as inf:
            ofil.write(inf.read())
        for team in range(1, 14):
            ofil.write(build_team(team))
    print("Config written to competition.yml")

if __name__ == "__main__":
    build_all()