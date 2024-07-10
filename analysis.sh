source /usr/local/gromacs/bin/GMXRC
## 获取用户输入
read -p "请输入一个值: " user_input

echo 4 4 | gmx rms -s  ../md_0_1.tpr -f  ../md_0_1.xtc -o rmsd_$user_input.xvg -fit rot+trans -xvg none
echo 1 | gmx rmsf -s ../md_0_1.tpr -f ../md_0_1.xtc  -o rmsf_$user_input.xvg -fit -xvg none
echo 1 | gmx gyrate -s ../md_0_1.tpr -f ../md_0_1.xtc -o gyrate_$user_input.xvg -xvg none
echo 1 | gmx sasa -s ../md_0_1.tpr -f ../md_0_1.xtc -o area_$user_input.xvg -or resarea.xvg -oa atomarea.xvg -xvg none
gmx distance -s ../md_0_1.tpr -f ../md_0_1.xtc -select 'com of group 1 plus com of group 13' -oav distave.xvg -oall dist_$user_input.xvg -dt 10 -xvg none
gmx mdrun -rerun ../md_0_1.trr -s ../md_0_1.tpr -o rerun.trr -c rerun.gro
#提取xtc文件
gmx  trjconv -f rerun.trr -o  mdreturn.xtc
##矫正
echo 1 0 | gmx trjconv -s ../md_0_1.tpr -f mdreturn.xtc -ur rect -pbc mol -center -o md_center.xtc
echo 1 13 | gmx hbond  -s ../md_0_1.tpr -f md_center.xtc -n ../index.ndx -num hbnum_$user_input.xvg  -xvg none

#氢键频率
echo 1 13 | gmx hbond  -s ../md_0_1.tpr -f md_center.xtc -n ../index.ndx -num -hbn -hbm
bash gmx_hbdat.bsh -s ../md_0_1.tpr  -n hbond.ndx  -m hbmap.xpm


#自由能景观
source ~/miniconda3/bin/activate md-davis
md-davis landscape_xvg -T 300 -x rmsd_$user_input.xvg -y gyrate_$user_input.xvg -n "$user_input" -l "$user_input"  -o $user_input.html --axis_labels 'dict(x="RMSD (nm)",y=" ROG (nm)",z="Free Energy (kJ mol)")'  --font_size  20

source ~/miniconda3/bin/activate gmxMMPBSA
#分子动力学相关矩阵
python DCCM.py ../md_0_1.gro md_center.xtc


#蛋白质二级结构
echo 1 | gmx do_dssp -f  md_center.xtc -s ../md_0_1.tpr -n ../index.ndx -o ss.xpm -sc scount_$user_input.xvg  -xvg none
# 设置变量
START_FRAME=1
END_FRAME=5000
INTERVAL=5
VERBOSE=2
FORCEFIELDS="oldff/leaprc.ff99SB,leaprc.gaff"
IGB=5
SALTCON=0.150

# 创建 mmpbsa.in 文件
cat <<EOF > mmpbsa.in
&general
startframe=1, endframe=5000, interval=5, verbose=2, 
forcefields="oldff/leaprc.ff99SB,leaprc.gaff"
/
&gb
igb=5, saltcon=0.150
/
&decomp
idecomp=2, dec_verbose=3,
print_res="within 4"
/
EOF

# 运行 gmx_MMPBSA
mpirun -np 10 gmx_MMPBSA MPI -O -i mmpbsa.in -cs ../md_0_1.tpr -ci  ../index.ndx -cg 1 13 -ct md_center.xtc -cp ../topol.top -o FINAL_RESULTS_MMPBSA.dat -eo FINAL_RESULTS_MMPBSA.csv
cp FINAL_RESULTS_MMPBSA.dat $user_input.dat
name=$(cat FINAL_RESULTS_MMPBSA.csv  | grep -n Delta | cut -d':' -f1)
final=$(awk -v line=$name "NR>line" FINAL_RESULTS_MMPBSA.csv > mmpbsa_$user_input.csv) 
cat scount_$user_input.xvg | grep -n SS > sc_$user_input.csv)
echo '分析完成'




