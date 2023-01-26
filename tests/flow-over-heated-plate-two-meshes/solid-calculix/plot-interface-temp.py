import re, glob, pandas
from matplotlib import pyplot
import matplotlib
matplotlib.use('Agg') # To prevent figure plotting
import numpy
from optparse import OptionParser	# use a parser for configuration

def loadParallelCSVSeries(name):
  l = [(re.search("dt(\d+)_", s).group(1), s) for s in glob.glob(f"{name}.dt*_*.csv")]
  return pandas.concat([pandas.read_csv(file, sep=";").assign(dt=dt) for dt, file in l], ignore_index=True)

def loadSerialCSVSeries(name):
  l = [(re.search(".dt(\d+).", s).group(1), s) for s in glob.glob(f"{name}.dt*.csv")]
  return pandas.concat([pandas.read_csv(file, sep=";").assign(dt=dt) for dt, file in l], ignore_index=True)

def main():
  parser=OptionParser()
  parser.add_option("-t", "--timestep", dest="dt", help="Timestep to plot", default=None)
  parser.add_option("-m", "--mpi-active", dest="mpi", help="MPI = t, Serial = f", default="t")

  (options, args) = parser.parse_args()
  dt = options.dt

  data = 0
  try:
    if options.mpi == "t":
      data = loadParallelCSVSeries("preCICE-output/Fluid-Mesh-Solid")
    else:
      data = loadSerialCSVSeries("preCICE-output/Fluid-Mesh-Solid")
  except:
    print("Improper setting of whether parallel or serial was used")
    return
  # convert all columns of DataFrame to floats
  data = data.apply(pandas.to_numeric)

  # Extract timestep data
  try:
    if dt == None:
      dt = max(data["dt"])
    final_data = data.loc[data["dt"] == float(dt)]
  except:
    print("Invalid timestep input")
    print("Valid timesteps are: " + str(data["dt"]))
    return

  # Sort by Posx
  final_data = final_data.sort_values("PosX")

  posx = final_data["PosX"].to_numpy()
  temp = final_data["Temperature"].to_numpy()

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


# -------------------------------------------------------------------
#  Run Main Program
# -------------------------------------------------------------------

# this is only accessed if running from command prompt
if __name__ == '__main__':
    main()