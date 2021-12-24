# %% [markdown]
# c- customer no.
# 
# i-interarrival time
# 
# s-simulation clock at arrival
# 
# b-busy status of server (str)
# 
# l-queue length (length)
# 
# q-queue time(non sim time)
# 
# p-processing time(non sim time)
# 
# ps-process start
# 
# pe-process end
# 
# t-time spend in system(non sim time)
# 
# w-idle time of server(non sim time)
# 
# wl=time limit

# %%
import numpy as np
import pandas as pd
import random as rand
c,i,b,l,q,p,ps,pe,t,w,s=[],[],[],[],[],[],[],[],[],[],[]
x=0
y=1
wl=480
a=0
qt=0
pt=0
di=0
while x<wl:
    c.append(y)
    i.append(int(rand.uniform(4,8)))
    a=sum(i)
    s.append(a)
    p.append(int(rand.uniform(2,9)))
    #Arrival
    if y==1:
        b.append("IDLE")
        l.append(0)
        q.append(0)
        w.append(i[0])
    else:
        if s[y-1]<pe[y-2]:
            
            b.append("BUSY")
            di=len(pe)
            dm=0
            z=0
            while dm<di:
                if s[y-1]<pe[dm]:
                    z+=1
                dm+=1
            l.append(z)
            qt=pe[y-2]-s[y-1]
            q.append(qt)
            pt=s[y-1]+q[y-1]
            ps.append(pt)
            pt+=p[y-1]
            pe.append(pt)
            w.append(0)
            ts=pe[y-1]-s[y-1]
            t.append(ts)
            y+=1
            continue
        else:
            b.append("IDLE")
            l.append(0)
            q.append(0)
    pt=s[y-1]+q[y-1]
    ps.append(pt)
    pt+=p[y-1]
    pe.append(pt)
    if s[y-1]>pe[y-2]:
        lt=s[y-1]-pe[y-2]
        w.append(lt)
    else:
        if y>1:
            w.append(0)    
    ts=pe[y-1]-s[y-1]
    t.append(ts)
    x=w[y-1]+pe[y-1]
    y+=1
df=pd.DataFrame(list(zip(c,i,s,b,l,q,p,ps,pe,t,w)),columns=["Cust_no.","Inter_arr","Simu_clock","Busy status","Queue length","Queue time","Process time","Process start","Process end","Time spent in system","Idle time"])
print(df)
df.to_csv (r'exportpath', index = False, header=True)
