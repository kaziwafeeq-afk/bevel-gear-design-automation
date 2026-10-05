# DMS ASSIGNMENT 2 BEVEL GEAR
# STEP 0: Importing Relevent modules
import math
from tabulate import tabulate
# STEP 1: Select type of system.
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("Select the type of system:")
print("1. Closed System")
print("2. Open System")
SYSTEM_TYPE = input("Select type of system: ")
# STEP 2: Select type of teeth profile.
print("Select type of teeth profile:")
print("1. Involute teeth profile")
print("2. Cycoloidal teeth profile")
TEETH_TYPE = input("Select type of teeth profile: ")
# STEP 3: Assigning Pressure Angle and Angle at which the shafts intersect.
PRESSURE_ANGLE = int(input("Enter the pressure angle: "))
INTERSECTION_ANGLE = int(input("Enter the angle at which the shafts intersect: "))
# STEP 4: LAYOUT
# STEP 5: Determination of initial gear ratio.
INITIAL_SPEED = int(input("Initial speed in RPM: "))
FINAL_SPEED = int(input("Final speed in RPM: "))
INITIAL_GEAR_RATIO = INITIAL_SPEED / FINAL_SPEED
# STEP 6: Determination of cone angles.
COT_DELTA_1 = (INITIAL_GEAR_RATIO + math.cos(math.radians(INTERSECTION_ANGLE)))/math.sin(math.radians(INTERSECTION_ANGLE))
DELTA_1 = math.degrees(math.atan(1/COT_DELTA_1))
DELTA_2 = INTERSECTION_ANGLE - DELTA_1
# STEP 7: Number of teeth in gear and pinion.
PINION_TEETH = 18
GEAR_TEETH = math.ceil((PINION_TEETH*INITIAL_GEAR_RATIO)+1)
GEAR_RATIO = GEAR_TEETH/PINION_TEETH
# STEP 8: Virtual number of teeth in gear and pinion.
PINION_VIRTUAL_TEETH = math.ceil(PINION_TEETH/math.cos(math.radians(DELTA_1)))
GEAR_VIRTUAL_TEETH = math.ceil(GEAR_TEETH/math.cos(math.radians(DELTA_2)))
# STEP 9: Material Selection.
SIGMA_U_PINION = 720
SIGMA_Y_PINION = 380
SIGMA_U_GEAR = 570
SIGMA_Y_GEAR = 310
BHN_PINION = 241
BHN_GEAR = 187 
# STEP 10: Lewis form factor.
Yv1 = (0.154-(0.912/PINION_VIRTUAL_TEETH))*3.14
Yv2 = (0.154-(0.912/GEAR_VIRTUAL_TEETH))*3.14
# STEP 11: Determining if the pinion is the weakest element.
SIGMA_Y1 = SIGMA_Y_PINION*Yv1
SIGMA_Y2 = SIGMA_Y_GEAR*Yv2
# STEP 12: Determining the design torque.
MOTOR_POWER = input("Enter the power: ")
Mt = ((1.3*int(MOTOR_POWER)*1000*60)/(2*3.14*int(INITIAL_SPEED)))*1000
# STEP 13: Design bending stress.
SIGMA_B = ((1.4/3)*((0.35*SIGMA_U_PINION*10)+1200))*0.1
# STEP 14: Module.
Si = 10
Module = math.ceil(((Mt/(Yv1*SIGMA_B*Si*PINION_VIRTUAL_TEETH))**(1/3))*1.28*(6/5)*1.3)
# STEP 15: Checking wear.
DESIGN_COMPRESSIVE_STRESS = BHN_PINION*25*1*0.1
R = 0.5*Module*(((PINION_TEETH**2)+(GEAR_TEETH)**2)**(1/2))
B = R/3
E = 215000
INDUCED_COMPRESSIVE_STRESS = (0.72/(R-(0.5*B)))*(((E*Mt*((1+(GEAR_RATIO**2))**3)**(1/2))/(GEAR_RATIO*B))**(1/2))
# STEP 15: Results and conclusion.
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------BEVEL GEAR DESIGN--------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------")
Results =[[1,"Type of system selected is: ",SYSTEM_TYPE,"Used for industrial purposes."],
 [2,"Type of teeth profile selected is: ",TEETH_TYPE,"Easy to manufacture."],
 [3,"Pressure angle is: ", PRESSURE_ANGLE,"-"],
 [4,"Angle at which the shafts intersect each other is: ", INTERSECTION_ANGLE,"-"],
 [5,"Intitial speed is: ",INITIAL_SPEED," RPM"],
 [6,"Final speed is: ",FINAL_SPEED," RPM"],
 [7,"Delta 1: ",round(DELTA_1,2),"Degrees."],
 [8,"Delta 2: ",round(DELTA_2,2),"Degrees."],
 [9,"Number of teeth on pinion: ",PINION_TEETH,"Minimum number of theeth."],
 [10,"Number of teeth on gear: ", GEAR_TEETH,"Hunting teeth added."],
 [11,"Gear ratio: ",round(GEAR_RATIO,2),"-"],
 [12,"Virtual number of teeth on pinion: ",PINION_VIRTUAL_TEETH,"-"],
 [13,"Virtual number of teeth on gear: ",GEAR_VIRTUAL_TEETH,"-"],
 [14,"Pinion material: ","C-50","-"],
 [15,"Ultimate stress for pinion: ",round(SIGMA_U_PINION,2)," N/mm2"],
 [16,"Yeild stress for pinion: ",round(SIGMA_Y_PINION,2)," N/mm2"],
 [17,"Gear material: ","C-35","-"],
 [18,"Ultimate stress for gear: ",round(SIGMA_U_GEAR,2)," N/mm2"],
 [19,"Yeild stress for gear: ",round(SIGMA_Y_GEAR,2)," N/mm2"],
 [20,"Lewis form factor for pinion: ",round(Yv1,2),"-"],
 [21,"Lewis form factor for gear: ",round(Yv2,2),"-"],
 [22,"Input motor power: ", MOTOR_POWER," KW"],
 [23,"Design bending stress is: ",round(SIGMA_B,2)," N/mm2"],
 [24,"Design Motor torque is: ",round(Mt,2)," N/mm2"],
 [25,"Module: ",round(Module,2), " mm"],
 [26,"Cone Distance is: ",round(R,2)," mm"],
 [27,"Face width is: ",round(B,2)," mm"],
 [28,"Design compressive stress is: ",round(DESIGN_COMPRESSIVE_STRESS,2)," N/mm2"],
 [29,"Induced compressive stress is: ",round(INDUCED_COMPRESSIVE_STRESS,2)," N/mm2"]]
print (tabulate(Results, headers=["SrNo", "PARAMETERS", "VALUES","UNITS / REMARKS"]))
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("Conclusion: ")
if SIGMA_Y1 < SIGMA_Y2:
    print("Pinion is chosen / kept as a weaker element because it is easy to replace it incase of failure, Therefore its design is done.")
else:
    print("Change the material, pinion is taken as the weaker material as it can be easily changed")
if DESIGN_COMPRESSIVE_STRESS > INDUCED_COMPRESSIVE_STRESS:
    print("Design is Safe since induced compressive stress (",round(INDUCED_COMPRESSIVE_STRESS,2),
          ")is less than the design compressive stress.(",round(DESIGN_COMPRESSIVE_STRESS,2),")")
else:
    print("Design isnt safe, increase the modulus or hardness.")
print("-------------------------------------------------------------------------------------------------------------------------------------")
