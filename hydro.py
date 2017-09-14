import numpy as np

#1D euler equation solver. Let's see how this goes.
#shape of u is (3,N) where N is the number of cells.
#shape of f is (3,N+1). f(i,n) corresponds to the ith flux at the left endpoint of cell n

def L(u,f): 
	for j in range(ncells):
		u(:,j) = (f(:,j)-f(:,j+1))*ncells #We assume the interval we care about is (0,1), and dx = 1/ncells so 1/dx = ncells
	
	
def evolve(u0,f0,nsteps,dt):
	ncells = len(u0[1,:])
	u = u0
	f = f0
	unew = u
	for i in range(nsteps):
		unew = u + dt*L(u,f)
