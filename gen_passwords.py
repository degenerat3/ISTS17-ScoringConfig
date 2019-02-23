import random
import string

TEAM_LOW = 1
TEAM_HIGH = 13
for team in range(TEAM_LOW, TEAM_HIGH+1):
    password = "team{}-{}".format(team, ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)))
    print('"{}"'.format(password))
