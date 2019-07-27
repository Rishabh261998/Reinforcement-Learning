import numpy as np

import gym
env = gym.make('FrozenLake-v0')
n = env.action_space.n
m = env.observation_space.n
q = np.zeros([m,n])
V = np.zeros(m)
F = True
gamma= 0.99
#env.reset()
the = 1e-3 
max_episode = 10000
for i in range(max_episode):
	v_ep = np.copy(V)
	env.reset()
	for i in range(m):
		kk = []
		for a in range(n):
			val = 0
			for p, s_, r, _ in env.env.P[i][a]:
				val += p*(r + gamma * v_ep[s_])
			kk.append(val)
		V[i] = np.max(kk)
		#print(V)
	if max(V - v_ep) < the:
		print('Done!!')
		break

​

# testing
s = env.reset()
rewards=[]
for i in range(10000):
    s = env.reset()
    d = False
    R = 0
    #input()
    while d==False:
        a=np.argmax([sum ( [ p * ( r+gamma*V[s_] )  for p,s_,r,_ in env.env.P[s][k] ] ) for k in range(n)])
        input()
        env.render()
        s2,r,d,_=env.step(a)
        R=R*gamma+r
        s=s2
        if d:
            rewards.append(r)
            break
print(np.mean(rewards))