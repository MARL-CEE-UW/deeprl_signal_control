# test
import os
import sys
import optparse
import random
import math
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa

# os.system(r'C:\Users\guoqq17\tensorflow\Scripts\activate')
def get_options(show_gui):
    optParser = optparse.OptionParser()
    if show_gui == 1:
        optParser.add_option("--nogui", action="store_true",
                             default=False, help="run the commandline version of sumo")
    else:
        optParser.add_option("--nogui", action="store_true",
                             default=True, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options

def start_sumo(show_gui):
    options = get_options(show_gui)
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "most.sumocfg"])

start_sumo(1)
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
traci.close(wait=False)
sys.stdout.flush()
