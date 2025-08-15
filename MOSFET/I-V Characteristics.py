import matplotlib.pyplot as plt
import numpy as np

Vgs_vals = [0.2,0.4,0.5,0.6,0.7,0.8,0.9,1]      //Test values for Gate-Source Voltage
Vt = 0.2      #(V) Threshold Voltage
Bn = 1        #(ma/V^2) MOSFET Gain = u_n * C_ox * W/L

Vds_vals = np.linspace(0, 1, 100)    //Vds positive for NMOS

def linear_id(Vov, Vds):
  return Bn*(Vov*Vds - (Vds**2)/2)    //Eqn in Triode mode

def satn_id(Vov):
  return Bn/2*Vov**2                  //Eqn in Saturation Mode

for Vgs in Vgs_vals:
  Vov = Vgs-Vt      //Overdrive Voltage

  Id_vals = [linear_id(Vov, Vds) if Vds < Vov else satn_id(Vov) for Vds in Vds_vals]        //If Vov < Vds, triode mode. If Vov >= Vds, saturation.
  #all Ids are in mA since Bn=1mA/V^2

  plt.plot(Vds_vals, Id_vals, label=f'Vgs={Vgs} V')

plt.xlabel("Vds [V]")
plt.ylabel("Id [mA]")
plt.legend()
plt.title("Id vs Vds characteristics")
plt.show()
