print "IPD";

import random;

#params
T=5;
R=3;
P=1;
S=0;
N=1000000;


#line that will be modified(input)
#[p1,p2,p3,p4];
#p={'cc':0.9,'cd':0.8,'dc':0.05,'dd':0.0};#strategy to set s_y=1

chi=1.0;#1.0 #extortion coefficient, (Ji)
phi=(P-S)/((P-S)+(chi*(T-P)))#0.1111;#0.2
p={'cc':1.0-phi*(chi-1.0)*((R-P)/((P-S))),'cd':1.0-phi*((((T-P)/(P-S))*chi)+1.0),'dc':phi*(chi+((T-P)/(P-S))),'dd':0.0};#strategy to set s_x-1=chi* (s_y - 1)



#random strategy for Y player
random.seed();
q={'cc':random.uniform(0,1),'cd':random.uniform(0,1),'dc':random.uniform(0,1),'dd':random.uniform(0,1)};#[q1,q2,q3,q4]

#init a fake last iteration result
xy='cc'
xScore=0;
yScore=0;


for n in range(1, N):
  #game begins
  xChoice=random.uniform(0,1);
  yChoice=random.uniform(0,1);
  
  #X chooses if cooperate or defect, based on last game iteration
  if(0<= xChoice <=p[xy]):
    choice='c';
  else:
    choice='d';
  
  #Y chooses if cooperate or defect, based on last game iteration
  if(0<= yChoice <=q[xy]):
    choice=choice+'c';
  else:
    choice=choice+'d';  
  
  xy=choice;
  ##TODO:CHECK THIS
  if xy=='cc':
    xScore+=R;
    yScore+=R;
  elif xy=='cd':
    xScore+=S;
    yScore+=T;
  elif xy=='dc':
    xScore+=T;
    yScore+=S;
  elif xy=='dd':
    xScore+=P;
    yScore+=P;
  
  #print xy;

print xScore/float(N);
print yScore/float(N);