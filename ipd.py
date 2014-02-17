print "IPD";

import random;

#params
scores={'T':5,'R':3,'P':1,'S':0};
N=100000;


#line that will be modified(input)
#[p1,p2,p3,p4];

#p={'cc':0.9,'cd':0.8,'dc':0.05,'dd':0.0};#strategy to set s_y=1

phi=0.11;#1/5
chi=2.0;#extortion coefficient, (Ji)

p={'cc':1.0-2.0*phi*(chi-1.0),'cd':1.0-phi*((4.0*chi)+1.0),'dc':phi*(chi+4.0),'dd':0.0};#strategy to set s_x-1=chi* (s_y - 1)


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
    xScore+=scores['R'];
    yScore+=scores['R'];
  elif xy=='cd':
    xScore+=scores['S'];
    yScore+=scores['T'];
  elif xy=='dc':
    xScore+=scores['T'];
    yScore+=scores['S'];
  elif xy=='dd':
    xScore+=scores['P'];
    yScore+=scores['P'];
  
  #print xy;

print xScore/float(N);
print yScore/float(N);