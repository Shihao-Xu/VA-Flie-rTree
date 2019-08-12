#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
import heapq

class VA_file():
    def __init__(self, b, d, N, K):
        self.b = b
        self.d = d
        self.N = N
        self.K = K
        
        self.ans_ssa = [] 
        self.dst_ssa = []
        
        self.ans = [] 
        self.dst = []
        
        self.a = []
        self.p = []
        
        self.b_vector = [0] * d
        
        self.q = []
        self.r = []
        self.block_num = 0

        
       
    
    def p_Synthesize(self):
        for i in range(self.N):
            self.p.append(np.random.uniform(0.00,1.00,self.d))
    
    '''def p_b_Example(self):
        self.p = [[0.9,0.1],[0.6,0.8],[0.1,0.4],[0.1,0.9],[0.3,0.7]]
        self.b_vector = [2,2]
        self.q = [0.7, 0.1]'''
    
    
    def get_b_vector(self):
        for j in range(self.d):
            if j < self.b%self.d:
                self.b_vector[j] = math.floor(self.b/self.d) + 1
            else:
                self.b_vector[j] = math.floor(self.b/self.d)
    
    def get_VA_file(self):
        for i in range(self.N):
            a_row = []
            for j in range(self.d):
                rij = math.floor(self.p[i][j]/(1/math.pow(2, self.b_vector[j])))
                a_row.append(rij)
            self.a.append(a_row)
        
        self.block_num = len(np.unique(self.a, axis=0))
    
    def q_generate(self):
        self.q = np.random.uniform(0.00,1.00,self.d)
        
    def get_r(self):
        for j in range(self.d):
            rqj = math.floor(self.q[j]/(1/math.pow(2, self.b_vector[j])))
            self.r.append(rqj)
    
    def GetBounds(self, i):                   
        li = []
        ui = []
        
        self.get_r()
        
        for j in range(self.d):
            if self.a[i][j] < self.r[j]:          
                li.append(self.q[j] - (self.a[i][j]+1) * (1/ math.pow(2, self.b_vector[j]))) 
            elif self.a[i][j] == self.r[j]:
                li.append(0)
            else:
                li.append(self.a[i][j] * (1/ math.pow(2, self.b_vector[j])) - self.q[j])
            
        for j in range(self.d):
            if self.a[i][j] < self.r[j]:
                ui.append(self.q[j] - self.a[i][j] * (1/ math.pow(2, self.b_vector[j])))
            elif self.a[i][j] == self.r[j]:
                ui.append(max( self.q[j] - self.a[i][j] * (1/ math.pow(2, self.b_vector[j])), (self.a[i][j]+1)*(1/ math.pow(2, self.b_vector[j])) - self.q[j]))
            else:
                ui.append((self.a[i][j]+1)*(1/ math.pow(2, self.b_vector[j])) - self.q[j])
         
        return np.linalg.norm(li), np.linalg.norm(ui)
    
    def InitCandidate(self):
        for j in range(self.K):
            self.dst.append(float('inf'))
            self.ans.append(-1)
        return float('inf')
    
    def Candidate(self, sigma, i):
        if sigma < self.dst[-1]:
            self.dst[-1], self.ans[-1]  = sigma, i
            #print(self.dst, self.ans)
            dst, ans = zip(*sorted(zip(self.dst, self.ans)))
            self.dst, self.ans = list(dst), list(ans)
            
            
            #print(self.dst, self.ans)
        return self.dst[-1]
    
    def Lp(self, i):
        return np.linalg.norm(self.p[i]-np.array(self.q))
    
    def VA_SSA(self):
        self.ans = [] 
        self.dst = []
        
        sigma = self.InitCandidate()
        visited_vec = 0
        visited_block = []
        for i in range(self.N):
            l, _ = self.GetBounds(i)
            #print(l)
            
            if l < sigma:
                visited_vec +=1
                visited_block.append(self.a[i])
                sigma = self.Candidate(self.Lp(i), i)                
                #print(self.dst, self.ans)
                
                
        #print(self.dst, self.ans)
        #visited_block = np.array(visited_block)
        #print(visited_vec, len(np.unique(visited_block, axis=0)))
        #print(visited_vec)
        return  len(np.unique(visited_block, axis=0))
    
    def VA_NOA(self):
        # i,
        # sigma
        # l, u
        # heap
        self.ans = [] 
        self.dst = []
        
        visited_vec = 0
        visited_block = []
        
        Heap = []
        
        visited_vec = 0
        visited_block = []
        
        # PHASE - ONE
        sigma = self.InitCandidate()
        for i in range(self.N):
            l, u = self.GetBounds(i)
            if l <= sigma:
                sigma = self.Candidate(u, i)
                heapq.heappush(Heap, (l, i) )
        
        # PHASE - TWO
        sigma = self.InitCandidate()    
        l, i = heapq.heappop(Heap)
        while l < sigma:
            visited_vec +=1
            visited_block.append(self.a[i])
            
            sigma = self.Candidate(self.Lp(i), i)
            l, i = heapq.heappop(Heap)
        
        #print(visited_vec)
        return  len(np.unique(visited_block, axis=0))     
            
            
if __name__ == '__main__':     


    # In[ ]:

    d = np.array([2,4,6,8,10,14,18,20,22,26,30])
    #b = 40
    para = np.array([2,2,2,2,2, 2.5,3,3,3,3, 3])
    b = d * para
    print(b)

    N = 50000
    K = 10

    vb_ssa = []
    vb_ssa_percentage = []
    vb_noa = []
    vb_noa_percentage = []
    print(2)
    for i in range(11):
        X =VA_file(b[i],d[i],N,K)
        X.p_Synthesize()
        X.get_b_vector()
        X.get_VA_file()
        
        vb_s = 0
        vb_n = 0
        vst_pct_NOA = 0
        vst_pct_SSA = 0
        iter_time = 7
        
        for aver in range(iter_time):
            print(f'the {i+1}th and {aver+1} time')
            X.q_generate()
            X.get_r()
            vst_pct_SSA += X.VA_SSA() / X.block_num
            vst_pct_NOA += X.VA_NOA() / X.block_num
            vb_s += X.VA_SSA()
            vb_n += X.VA_NOA()
            
        vb_ssa.append(vb_s/iter_time)
        vb_noa.append(vb_n/iter_time)
        vb_ssa_percentage.append(vst_pct_SSA / iter_time)
        vb_noa_percentage.append(vst_pct_NOA / iter_time)
        
    print(vb_ssa)
    print(vb_noa)
    print(vb_ssa_percentage) 
    print(vb_noa_percentage)


    # # In[ ]:


    # '''b =  4
    # d =  2
    # N = 5 
    # K = 4
    # X =VA_file(b,d,N,K)
    # X.p_b_Example()
    # X.get_VA_file()
    # X.get_r()
    # vb = X.VA_SSA()'''


    # # In[ ]:


    # b =  120
    # d =  30
    # N = 50000
    # K = 10
    # X =VA_file(b,d,N,K)
    # X.p_Synthesize()
    # X.get_b_vector()
    # X.get_VA_file()

    # X.q_generate()
    # X.get_r()

    # #vb = X.VA_SSA()
    # #print(vb)
    # #t = np.unique(X.a, axis=0)
    # #print(len(t))
    # # 8,2,38/256
    # # 16, 4, 186/35052
    # # 24, 6, 170/49912
    # # 32, 8, 184/
    # # 56, 14  100/ 

    # # 100, 50. 18505

    # vb = X.VA_NOA()
    # print(vb)


    # # In[ ]:


    # # find the K nearest neighbors to self.q from self.p 

    # p_q = X.p - X.q


    # # In[ ]:


    # dist = np.linalg.norm(p_q, axis=1)


    # # In[ ]:


    # print(X.dst, X.ans)


    # # In[ ]:


    # np.argsort(dist)[:X.K]

    # #array([ 7541, 42560, 42529,  1812,  4801, 38745, 11343,  8934, 47664, 44101])


    # # In[ ]:


    # t = np.array([[2,2],[2,2],[2,2]])
    # print(np.unique(t, axis=0))


    # # In[ ]:




