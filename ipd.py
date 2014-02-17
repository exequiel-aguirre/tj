print "IPD";

import random;

#params
T=5;
R=3;
P=1;
S=0;


#line that will be modified(input)
p=[None,0.5,0.5,0.5,0.5];

#random strategy for Y player
random.seed(1);
q=[None,random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)];

#init a fake last iteration result
xy='cc'


for n in range(1, 10):
  #game begins
  xChoice=random.uniform(0,1);
  yChoice=random.uniform(0,1);

  if xy=='cc':
    if(0<= xChoice <=p[1]):
      xy='c';
    else:
      xy='d';
    
    if(0<= yChoice <=q[1]):
      xy=xy+'c';
    else:
      xy=xy+'d';
      
  elif xy=='cd':
    if(0<= xChoice <=p[2]):
      xy='c';
    else:
      xy='d';
    
    if(0<= yChoice <=q[2]):
      xy=xy+'c';
    else:
      xy=xy+'d';
  elif xy=='dc':
    if(0<= xChoice <=p[3]):
      xy='c';
    else:
      xy='d';
    
    if(0<= yChoice <=q[3]):
      xy=xy+'c';
    else:
      xy=xy+'d';
  elif xy=='dd':
    if(0<= xChoice <=p[4]):
      xy='c';
    else:
      xy='d';
    
    if(0<= yChoice <=q[4]):
      xy=xy+'c';
    else:
      xy=xy+'d';

  print xy;