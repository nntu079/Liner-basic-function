import numpy as np
import matplotlib.pyplot as plt

def small_phi(x,N):
  res=np.array([]);
  for i in range(0,N):
    res=np.append(res,pow(x,i));
  #print(res);
  return res;
def big_phi(X,N):
  res =np.empty((0,N), float);
  for x in X:
    temp=small_phi(x,N);
    res=np.append(res,np.array([temp]),axis=0);
  #print(res);
  return res;


def find_w(X,N,y):
  phi=big_phi(X,N);
  x=phi.T.dot(phi)
  x = np.linalg.inv(x)
  x=x.dot(phi.T);
  x=x.dot(np.array(y));
  return x
def curve(x,w):
  res=0;
  count=0;
  for i in w:
    res+=pow(x,count)*i;
    count+=1;
  return res;


X = [1, 2, 3, 4, 5, 8, 10]
y = [1.1, 3.8, 8.5, 16, 24, 65, 99.2]

for i in range(2,5):
  N=i;
  w=find_w(X,N,y);
  
  x = np.linspace(0, 10, 1000)
  plt.plot(x, curve(x,w));

  plt.plot(X,y,'ro');
  
  plt.title('curve with degree ='+str(N))
  plt.show();
