__author__ = 'yaxxu'
from scipy import stats
import numpy as np
import MySQLdb
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import sys,os
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estimation_tool.settings")
from django.db import models
import random
class Combine(models.Model):
    part_number = models.CharField(db_column='Part_number', max_length=80, primary_key=True) # Field name made lowercase.
    part_name = models.CharField(db_column='Part Name', max_length=300) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_days = models.FloatField(db_column='Total Days', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_width = models.FloatField(db_column='Board Width', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    board_height = models.FloatField(db_column='Board Height', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    metal_to_metal_thickness = models.FloatField(db_column='Metal to Metal Thickness', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    sequential_lam = models.CharField(db_column='Sequential Lam', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_buried = models.CharField(db_column='Via Type:Buried', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    via_type_blind = models.CharField(db_column='Via Type:Blind', max_length=3, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_layers = models.IntegerField(db_column='Total Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_layers = models.IntegerField(db_column='Plane Layers', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    pins = models.IntegerField(db_column='Pins', blank=True, null=True) # Field name made lowercase.
    connections = models.IntegerField(db_column='Connections', blank=True, null=True) # Field name made lowercase.
    components = models.IntegerField(db_column='Components', blank=True, null=True) # Field name made lowercase.
    total_nets = models.IntegerField(db_column='Total Nets', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    bga_lgas = models.IntegerField(db_column='BGA/LGAs', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    dimms = models.IntegerField(db_column='DIMMs', blank=True, null=True) # Field name made lowercase.
    pin_density = models.FloatField(blank=True, null=True)
    component_density = models.FloatField(blank=True, null=True)
    buses = models.IntegerField(db_column='Buses', blank=True, null=True) # Field name made lowercase.
    constraintsets = models.IntegerField(db_column='Constraintsets', blank=True, null=True) # Field name made lowercase.
    diffpairs = models.IntegerField(db_column='Diffpairs', blank=True, null=True) # Field name made lowercase.
    matchgroups = models.IntegerField(db_column='Matchgroups', blank=True, null=True) # Field name made lowercase.
    netclasses = models.IntegerField(db_column='Netclasses', blank=True, null=True) # Field name made lowercase.
    net_with_constraints = models.IntegerField(db_column='Net with Constraints', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    pinpairs = models.IntegerField(db_column='Pinpairs', blank=True, null=True) # Field name made lowercase.
    xnets = models.IntegerField(db_column='Xnets', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'combine'
        app_label = 'BET'
conn = MySQLdb.connect(host='localhost', user='root',passwd='%f3vFc29')
#get the cursor
cursor = conn.cursor()
conn.select_db('Pcb_design_data')
#test the linear regression
# x = np.random.random(10)
# y = np.random.random(10)
# slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
# print slope, intercept
#fetch a row
# cursor.execute("SELECT * FROM Combine")
# row = cursor.fetchone()
# while row is not None:
#     print(row)
#     row = cursor.fetchone()
Valid_combines = Combine.objects.filter(total_days__isnull=False)
X = []
Y = []
R = []
P = []
D_pin = []
D_component = []
T = []
Name = []
Area_inv = []
for data in Valid_combines:
    if data.total_days!=0 and (str(data.part_number)!='7020181-01' and str(data.part_number)!='7079664-01'and str(data.part_number)!='7053491-01'):
        X+=[data.board_width]
        Y+=[data.board_height]
        R+=[max(data.board_width/data.board_height,data.board_height/data.board_width)]
        P+=[data.pins]
        D_pin+=[data.pin_density]
        D_component+=[data.component_density]
        T+=[data.total_days]
        Name+=[data.part_number]
        Area_inv+=[1/(data.board_width*data.board_height)]
# print P
# print R
# print T
# print D_component

# # plot the parameters
# plt.figure(1)
# plt.plot(P,T,'ro')
# plt.ylabel('Total_days')
# plt.xlabel('Pins')
#
# plt.figure(2)
# plt.plot(R,T,'ro')
# plt.ylabel('Total_days')
# plt.xlabel('XY_Ratio')
#
# plt.figure(3)
# plt.plot(D_pin,T,'ro')
# plt.ylabel('Total_days')
# plt.xlabel('Pin_density')


# data =np.array(
# [[-0.042780748663101636, -0.0040771571786609945, -0.00506567946276074],
# [0.042780748663101636, -0.0044771571786609945, -0.10506567946276074],
# [0.542780748663101636, -0.005771571786609945, 0.30506567946276074],
# [-0.342780748663101636, -0.0304077157178660995, 0.90506567946276074]])
#
# coefficient = data[:,0:2]
# dependent = data[:,-1]
#
# print coefficient
# print dependent

def model(para,Ratio,Pins,Density_pin, Density_component,Area_inv, *args):
    a,b,c,d,e = para
    if len(args)>0:
        formula = 'a*Density_pin + c*(Ratio**d)*Pins'
        return formula
    return (a*Density_pin + c*(Ratio**d)*Pins)

def residuals(para,y, Ratio,Pins,Density_pin, Density_component,Area_inv):
    #a,b,c,d,e = para
    err = y - model(para,Ratio,Pins,Density_pin, Density_component,Area_inv)
    return err

p0 = np.array([1, 1, 0.01, 1, 1000]) #some initial guess
#perform RANSAC
error_count_optimal=1000
for jj in range(100):
# Randomly create the training set
    list = range(len(T))
    number_for_training = 12
    list_index = random.sample(list, number_for_training)
    T_train = []
    R_train = []
    P_train = []
    D_pin_train = []
    D_component_train = []
    Area_inv_train = []
    Name_train = []
    for index in list_index:
        T_train += [T[index]]
        R_train += [R[index]]
        P_train += [P[index]]
        D_pin_train += [D_pin[index]]
        D_component_train += [D_component[index]]
        Area_inv_train += [Area_inv[index]]
    # least square fit
    p = leastsq(residuals, p0, args=(np.array(T_train), np.array(R_train), np.array( P_train), np.array(D_pin_train), np.array(D_component_train), np.array(Area_inv_train) ) )[0]

    # output the iterated parameters
    T_est = []
    err = []

    #test our model get the error
    error_th = 0.2
    error_count = 0
    for i in range(len(R)):
        T_est += [model(p, R[i], P[i], D_pin[i], D_component[i], Area_inv[i])]
        err += [abs(T[i]-T_est[i])/T[i]]
        if err[i]>error_th:
            error_count += 1
    if error_count<error_count_optimal:
        error_count_optimal=error_count
        p_opt = p


# plot the performance of the model

for i in range(len(R)):
    T_est += [model(p_opt, R[i], P[i], D_pin[i], D_component[i], Area_inv[i])]
    err += [abs(T[i]-T_est[i])/T[i]]

plt.figure(4)
for i in list_index:
    plt.scatter(T[i], T_est[i], color='blue')
    plt.annotate(Name[i], (T[i], T_est[i]))
for i in set(range(len(T)))-set(list_index):
    plt.scatter(T[i], T_est[i], color='red')
    plt.annotate(Name[i], (T[i], T_est[i]))
plt.xlabel('Actual Time')
plt.ylabel('Estimated Time')
plt.ylim(ymin=0)
plt.plot([0,300],[0,300])
print error_count_optimal
print p_opt

# plt.figure(5)
# for i, txt in enumerate(Name):
#     print i
#     plt.scatter(T[i],T_est[i],color='blue')
#     plt.annotate(txt, (T[i], T_est[i]))
all_combines=Combine.objects.all()
for data in all_combines:
    X = data.board_width
    Y = data.board_height
    R = max(data.board_width/data.board_height,data.board_height/data.board_width)
    P = data.pins
    D_pin = data.pin_density
    D_component = data.component_density
    Area_inv = 1/(X*Y)
    partnumber = data.part_number
    est = model(p_opt,R,P,D_pin,D_component,X*Y)
    est = round(est,2)
    updatestmt = ("UPDATE BET_physicalboard SET Estimated_total_days=%s \
                    WHERE Part_number='%s'" %(est,partnumber) )
    cursor.execute(updatestmt)

def est_time(part_number):
    combine = Combine.objects.get(part_number=part_number)
    width = combine.board_width
    height = combine.board_height
    R = max(height/width, width/height)
    P = combine.pins
    D_pin = combine.pin_density
    D_component = combine.components
    Area_inv = 1/(width*height)
    estimation = model(p_opt, R, P, D_pin, D_component,Area_inv)
    return estimation


conn.commit()
cursor.close()
conn.close()
#plt.show()

