import re, glob, pandas
from matplotlib import pyplot
import numpy

def loadParallelCSVSeries(name):
  l = [(re.search("dt(\d+)_", s).group(1), s) for s in glob.glob(f"{name}.dt*_*.csv")]
  return pandas.concat([pandas.read_csv(file, sep=";").assign(dt=dt) for dt, file in l], ignore_index=True)

data = loadParallelCSVSeries("preCICE-output/Fluid-Mesh-Fluid")

# convert all columns of DataFrame to floats
data = data.apply(pandas.to_numeric)

# Extract final timestep data
final_data = data.loc[data["dt"] == max(data["dt"])]

# Sort by Posx
final_data = final_data.sort_values("PosX")

theta = (temp-300)/(310-300)
pyplot.figure(1)
pyplot.cla()
pyplot.plot(posx,theta)
pyplot.grid()
pyplot.xlabel("PosX (m)")
pyplot.ylabel("Theta")
pyplot.ylim([0.220, 0.425])
pyplot.title("Time: " + str(dt) + " ms")
pyplot.savefig("Final_Theta")