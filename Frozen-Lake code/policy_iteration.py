import numpy as np
import gym

env = gym.make('FrozenLake-v0')
n=env.action_space.n
m=env.observation_space.n


po=np.random.randint(n,size = m)
Q=np.zeros((m,n))
v_po=np.zeros(m)
F=True

po=np.array(po)
s=env.reset()
gamma=0.995
print(po)


def value_function_solver(policy):
    v_po=np.zeros(m)
    T=True
    while T:
        c, d, v = 0, 0, 0

        for i in policy:
            v=v_po[c]

            v_po[c]=np.sum( [ p*(r+gamma*v_po[s_]) for p,s_,r,_ in env.env.P[c][i] ] )

            d=max(d,abs(v_po[c]-v))
            c+=1
        if d < 1e-20:
            T=False
    return v_po


def policy_eval(po,v_po,Q):
    T=True
    while T==True:
        d=0
        p=po
        v_po=value_function_solver(po)
        for i in range(m):
            for k in range(n):
                Q[i,k]=np.sum([ p*(r+gamma*v_po[s_]) for p,s_,r,_ in env.env.P[i][k]])
            po[i]=np.argmax(Q[i,:])
            d=max(d,p[i]-po[i])

        if(d<1e-15):
            T=False
            break
    return po


s=env.reset()
for _ in range(10):
    po = policy_eval(po,v_po,Q)
    print(po)



no_of_iteration=1
rewards=[]
for i in range(no_of_iteration):
    input('enter')
    s=env.reset()
    d=False
    R=0
    while d==False:
        input('')
    
        k=po[s]
        env.render()
        s2,r,d,_=env.step(k)
        R=R*gamma+r
        s=s2
        if d:
            rewards.append(r)
            break
print(np.mean(rewards))