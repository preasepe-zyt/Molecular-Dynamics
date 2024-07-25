
#!/bin/bash

for i in {1..85};                        #脚本循环数
do
  t=$(awk -v i=$i 'BEGIN{print 1*i}')     #0.05表示抽取的时间间隔（ps）
                                             #本例运行了50ps，因此最多有1000个间隔，循环数不能超过1000
                                             #这些参数可以根据自己的需求更改，这只是示例，随便设的。
  echo $t
  name=pull_$t
  echo 0 | gmx trjconv -s ../pull.tpr -f ../pull.xtc -dump $t -o $name.gro
  gmx grompp -f um.mdp -p ../topol.top -c $name.gro -o $name.tpr -maxwarn 99
  gmx mdrun -s $name.tpr -pf ${name}_pf.xvg 
  rm -f *.edr *.log *.trr *.cpt *.xtc *.gro
  rm \#*
done
