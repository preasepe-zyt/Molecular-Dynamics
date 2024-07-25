import matplotlib.pyplot as plt
import matplotlib
import numpy
import sys
sys.path.append(r"C:\Users\79403\Desktop\Cal-MD-240623\PTGS2_calendoflaside")
from mean import mean
import os
from str_split import str_split
import pandas as pd
import seaborn as sns

# 使用seaborn的颜色循环
#colors = sns.color_palette('pastel', len(data.columns))

#matplotlib.use("TKAgg")
#字体
matplotlib.rcParams['font.family'] = 'Arial'
#plt.rcParams["font.family"] = "serif"
#plt.rcParams["font.serif"] = "Times New Roman"
path = r"C:\Users\79403\Desktop\Cal-MD-240623\PTGS2_calendoflaside"
# 定义颜色列表
colors = ['orange', 'green', 'blue',  'red', 'purple', "olive"]
index=0
# #skip legend
# list_rmsd = os.listdir(path)
# rmsd_name = [i for i in list_rmsd if "rmsd_" in i]
# with open(os.path.join(path, rmsd_name[0]), "r") as file:
#     x = []
#     y = []
#     for line in file:
#         if not line.startswith("@") and not line.startswith("#"):
#             t, rmsd = line.split()
#             x.append(float(t))
#             y.append(float(rmsd))

#RMSD
list_rmsd = os.listdir(path)
rmsd_name = [i for i in list_rmsd if "rmsd_" in i]
rmsd_legend = [str_split(i,"_",".") for i in rmsd_name]
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)
for index, i in enumerate(rmsd_name):
    t, rmsd = numpy.loadtxt(path + "\\" + i, unpack=True)
    t_m, rmsd_m = mean(rmsd)
    ax.plot(t/1000, rmsd, linestyle="-", alpha=0.2, color=colors[index])
    ax.plot(t_m/100, rmsd_m, linestyle="-", color=colors[index], label=rmsd_legend[index]) #
ax.set_xlabel("Time (ns)", fontsize=20)
ax.set_ylabel(r"RMSD (nm)", fontsize=20) #r"C$_\alpha$ RMSD (nm)"
ax.legend(loc='upper right', frameon=False, fontsize=13)
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
ax.set_yticks(numpy.arange(0, 0.5, 0.1))
plt.show()
fig.savefig(path+"\\"+"rmsd.png", dpi=300)

#rmsf
import matplotlib.pyplot as plt
import numpy as np
list_rmsf= os.listdir(path)
rmsf_name = [i for i in list_rmsf if "rmsf_" in i]
rmsf_legend = [str_split(i,"_",".") for i in rmsf_name]
# residue = ("LEU289", "VAL244", "ALA454", "LEU67",
#            "VAL27", "VAL111", "HIS131", "ILE127",
#            "ARG102", "GLN142")
# residue_lo = [list(range(3699, 3703)), list(range(2035, 2041)), list(range(2401, 2416)),  list(range(469, 476)),
#               list(range(196, 202)), list(range(900, 906)), list(range(1064, 1079)), list(range(1030, 1073))
#               , list(range(825, 835)), list(range(1167, 1175))]
#style = {'color': 'black', 'fontsize': 11, 'fontweight': 'bold'}
#resisue_h = [0.4, 0.42, 0.55, 0.4, 0.53, 0.68, 0.52, 0.3, 0.6, 0.73]

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

 # Load data (replace this with your actual data loading)
resid, rmsf = np.loadtxt(os.path.join(path, rmsf_name[index]), unpack=True)

# Plot the data
ax.plot(resid, rmsf, linestyle="-", linewidth=0.5, color=colors[index], label=rmsf_legend[index])
ax.set_xlabel("Residue number", fontsize=20)
ax.set_ylabel("RMSF (nm)", fontsize=20)
ax.tick_params(axis='both', labelsize=20)
ax.legend(loc='upper right',  frameon=False, fontsize=13)
#ax.set_xticks(numpy.arange(0, 25000, 5000))

for spine in ax.spines.values():
        spine.set_linewidth(2)

plt.show()
fig.savefig(path+"\\"+"rmsf.png", dpi=300)


#distance
import matplotlib.pyplot as plt
import numpy
list_dis = os.listdir(path)
dis_name = [i for i in list_dis if "dist_" in i]
dis_legend = [str_split(i,"_",".") for i in dis_name]
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)


t, d= numpy.loadtxt(path+"\\"+dis_name[0], unpack=True)
t_d, d_m = mean(d)
ax.plot(t/1000, d, linestyle="-", alpha=0.2, color=colors[index])
ax.plot(t_d/100, d_m, linestyle="-", color=colors[index], label=dis_legend[index])  #

ax.set_xlabel("Time (ns)", fontsize=20)
ax.set_ylabel("DISTANCE (nm)", fontsize=20)
ax.tick_params(axis='both', labelsize=20)
ax.legend(loc='upper right', frameon=False, fontsize=13)
for spine in ax.spines.values():
    spine.set_linewidth(2)
ax.set_yticks(numpy.arange(0, 20, 1))
plt.show()
fig.savefig(path+"\\"+"dis.png", dpi=300)

#Radius of gyration
import matplotlib.pyplot as plt
import numpy
list = os.listdir(path)
gyrate_name = [i for i in list if "gyrate_" in i]
gyrate_legend = [str_split(i,"_",".") for i in gyrate_name]
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

for index, i in enumerate(gyrate_name):
    t, data, x, y, z = numpy.loadtxt(path+"\\"+i, unpack=True)
    t_m, data_m = mean(data)
    ax.plot(t / 1000, data, linestyle="-", color=colors[index], alpha=0.2)
    ax.plot(t_m / 100, data_m, linestyle="-", color=colors[index], label=gyrate_legend[index])
ax.set_xlabel("Time (ns)", fontsize=20)#$s$ 可以斜体
ax.set_ylabel(r"RoG (nm)", fontsize=20)# _\mathrm{hb} 可以把字体下标
ax.legend(loc='upper right', frameon=False, fontsize=13)
#ax.set_yticks(numpy.arange(2.40, 3.80, 0.10))
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
plt.show()
fig.savefig(path+"\\"+"rgyr.png", dpi=300)

#fig.savefig("rgyr.svg")
#fig.savefig("rgyr.pdf")


#hbond
import matplotlib.pyplot as plt
import numpy
list = os.listdir(path)
hbnum_name = [i for i in list if "hbnum_" in i]
hbnum_legend = [str_split(i,"_",".") for i in hbnum_name]
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体
#plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# Load data (replace this with your actual data loading)
t, hnum, hnum2 = np.loadtxt(os.path.join(path, hbnum_name[0]), unpack=True)
# Plot the data
ax.bar(t / 1000, hnum, color=colors[index], label=hbnum_legend[index])
ax.set_xlabel("Time (ns)", fontsize=20)
ax.set_ylabel("Number of Hbond", fontsize=20)
ax.tick_params(axis='both', labelsize=20)
ax.legend(loc='upper right', frameon=False, fontsize=13)

ax.set_yticks(numpy.arange(0, 8, 1))
# ax.set_xticks(numpy.arange(0, 110, 10))
for spine in ax.spines.values():
        spine.set_linewidth(2)
plt.show()

fig.savefig(path+"\\"+"hbond.png", dpi=300)
#
'tab:blue'
'tab:orange'
'tab:green'
'tab:red'
'tab:purple'
'tab:brown'
'tab:pink'
'tab:gray'
'tab:olive'
'tab:cyan'

#绘制二级结构
import numpy as np
import matplotlib.pyplot as plt
# color_map = ["总结构 (Structure)", "区卷 (Coil)", "β-折叠 (B-Sheet)","β-桥 (B-Bridge)", "弯曲 (Bend)",
#               "转弯 (Turn)", "α-螺旋 (A-Helix)", "5-螺旋 (5-Helix)", "分链器 (3-Helix)"]
color_map = ["Structure", "Coil", "B-Sheet", "B-Bridge", "Bend",
              "Turn", "A-Helix", "5-Helix", "3-Helix"]
list = os.listdir(path)
psc_name = [i for i in list if "scount_" in i]
psc_legend = [str_split(i,"_",".") for i in psc_name]
# 替换为你的 DSSP 输出文件路径
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)
#plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体
#plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

data = np.loadtxt(path + "\\" + psc_name[0] , unpack=True, skiprows=1)
for a in range(1, 10):
   ax.plot(data[0]/1000, data[a], linestyle="-", label=color_map[a-1], linewidth=4)
   ax.set_xlabel("Time (ns)", fontsize=20)
   ax.set_title(psc_legend[index], fontsize=15)
   ax.set_ylabel("Number Of Residue", fontsize=20)
   ax.tick_params(axis='both', labelsize=20)
for spine in ax.spines.values():
        spine.set_linewidth(2)
#ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.45), frameon=False, title="Second Structure", ncol=3)
# ax.set_xticks(numpy.arange(0, 110, 10))
ax.legend(loc='upper center', frameon=False, fontsize=13, ncol=3, bbox_to_anchor=(0.5, 1.18))
# ax.set_yticks(numpy.arange(0, 800, 100))
plt.show()
fig.savefig(path+"\\"+"second_structure.png", dpi=300)


#溶剂可及面积 SASA
list = os.listdir(path)
area_name = [i for i in list if "area_" in i]
area_legend = [str_split(i,"_",".") for i in area_name]
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

for index, i in enumerate(area_name):
    t, sasa = numpy.loadtxt(path+"\\"+i, unpack=True)
    t_m, sasa_m = mean(sasa)
    ax.plot(t/1000, sasa, linestyle="-", color=colors[index], alpha=0.2)
    ax.plot(t_m / 100, sasa_m, linestyle="-", color=colors[index], label=area_legend[index])

ax.set_xlabel("Time (ns)", fontsize=20)
ax.set_ylabel("SASA (nm²)", fontsize=20) #r"C$_\alpha$ RMSD (nm)"
ax.legend(loc='upper right',frameon=False, fontsize=13)
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
#ax.set_yticks(numpy.arange(260, 400, 10))
plt.show()
fig.savefig(path+"\\"+"area.png", dpi=300)

#结合自由能
list = os.listdir(path)
MMPBSA_name = [i for i in list if "mmpbsa_" in i]
MMPBSA_legend = [str_split(i,"_",".") for i in MMPBSA_name]

col_name = ['Frame #','VDWAALS', 'EEL','EGB', 'ESURF', 'TOTAL']
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

data = pd.read_csv(path + "\\" + MMPBSA_name [0], sep=",")
data = data[col_name]
for index2, i2 in enumerate(data.columns.drop('Frame #')):
        ax.plot((data.iloc[:,0]*50)/100, data[i2], linestyle="-", color=colors[index2], label=i2)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.9), frameon=False, title="Second Structure",
                             ncol=3)
        ax.set_yticks(numpy.arange(-50, 50, 10))
        # 在相应的子图中绘制数据]
ax.set_xlabel("Time (ns)", fontsize=20)
ax.set_ylabel("Binding Energy (kcal/mol)", fontsize=20)
ax.tick_params(axis='both', labelsize=20)
ax.legend(loc='upper center', frameon=False, fontsize=15, ncol=3, bbox_to_anchor=(0.5, 1.35))
for spine in ax.spines.values():
        spine.set_linewidth(2)
ax.set_title(MMPBSA_legend[index], fontsize=15)
ax.set_xticks(numpy.arange(0, 110, 10))

plt.show()
fig.savefig(path+"\\"+"MMPBSA.png", dpi=300)

import matplotlib.pyplot as plt
import numpy as np

# 数据

list = os.listdir(path)
total_name = [i for i in list if "total" in i]
data = pd.read_csv(path+"\\"+total_name[0], sep=",")
data.set_index("Frames",inplace=True)
x_pos = np.arange(len(data.columns))
fig, ax = plt.subplots(figsize=(10, 6))

for index2, i2 in enumerate(data.columns.values):
         bars = ax.bar(i2, data.loc["Average"].values[index2], yerr=data.loc["SEM"].values[index2], align='center',
                  alpha=0.7, capsize=10, edgecolor='black', label=data.columns[index2])

# 添加标签和标题
ax.set_xlabel(' ', fontsize=1, rotation=45)
ax.set_ylabel('kcal/mol', fontsize=20)
ax.set_title('Binding Free energy', fontsize=20)
ax.legend(loc='upper center', frameon=False, fontsize=15, ncol=3, bbox_to_anchor=(0.5, 1.0))
#ax.set_xticklabels(i2, rotation=45, fontsize=5)
ax.tick_params(axis='both', labelsize=20)
for spine in ax.spines.values():
        spine.set_linewidth(2)
ax.set_yticks(numpy.arange(-100, 110, 10))
# 显示图像
# plt.tight_layout()
plt.show()
fig.savefig(path+"\\"+"totalMMPBSA.png", dpi=300)

#smd
list = os.listdir(path)
pull_name = [i for i in list if "pull" in i]
pull_legend = [str_split(i,"_",".") for i in pull_name]
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)
for index, i in enumerate(pull_name):
    t, f = numpy.loadtxt(path + "\\" + i, unpack=True,comments=["#","@"])
    ax.plot(t, f, linestyle="-", color=colors[index], label=pull_legend[index],linewidth=1.5) #
ax.set_xlabel("Time (ps)", fontsize=20)
ax.set_ylabel(r"Force (kJ/mol/nm)", fontsize=20) #r"C$_\alpha$ RMSD (nm)"
ax.legend(loc='upper right', frameon=False, fontsize=13)
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
#ax.set_yticks(numpy.arange(0, 0.5, 0.1))
plt.show()
fig.savefig(path+"\\"+"pull.png", dpi=300)

#umbrella
list = os.listdir(path)
um_name = [i for i in list if "hist" in i]
um_legend = [str_split(i,"_",".") for i in um_name]
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)
for index, i in enumerate(um_name):
    a,  b= numpy.loadtxt(path + "\\" + i, unpack=True,comments=["#","@"])
    ax.plot(a, b, linestyle="-", color=colors[index], label=um_legend[index]) #
ax.set_xlabel("ξ", fontsize=20)
ax.set_ylabel(r"Energy (kcal mol$^{-1}$)", fontsize=20) #r"C$_\alpha$ RMSD (nm)"
ax.legend(loc='upper right', frameon=False, fontsize=13)
# 设置坐标轴刻度的大小
ax.tick_params(axis='both', labelsize=20)
# 设置坐标轴边框粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)
#ax.set_yticks(numpy.arange(0, 0.5, 0.1))
plt.show()
fig.savefig(path+"\\"+"pull.png", dpi=300)