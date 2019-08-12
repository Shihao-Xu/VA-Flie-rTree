import matplotlib.pyplot as plt 
import numpy as np
import math


class rtree():

    def __init__(self, dimension, number):
        self.dimension = dimension
        self.pointnumber = number
        self.number=self.dimension*self.pointnumber
        self.minsize = (8*1024) // (self.dimension * 8)
        self.divitime=int(math.ceil(math.log((self.pointnumber//self.minsize),2)))
        self.minNum=int(math.ceil(self.pointnumber/math.pow(2,self.divitime)))

    def create(self):
        lst = np.random.exponential(scale=1.0,size=1000)  # create points
        d1 = []
        #for i in range(self.number - self.dimension+1):
        #    if i==0 or i % self.dimension==0:
        #       
        #       d1.append(point_gen(lst[i : ], self.dimension ))
        for j in range(49999):
           point=[]
           for i in range(self.dimension):
            
              point.append(lst[np.random.randint(999,size=1)])
              p=tuple(point)
           d1.append(p)    
        return d1

    def sortlst(self, lst, mark):
        #sd1 = sorted(lst)
        for j in range(len(lst)):
            lst[j] = sorted(lst[j], key = lambda x: x[mark])
        #sd1 = sorted(lst, key=lambda x: x[mark])  # sort
        return lst

    def getNdimension(self, dn):
        blocks = []
        dn = [dn]
        for i in range (self.divitime):
            
            dn = self.sortlst(dn, i % self.dimension)
            dn = self.chunks(dn, self.pointnumber // np.power(2, i+1))
            blocks.append(dn)
        return blocks

    def chunks(self,lst, n):
        chunk = []
        for j in range(len(lst)):
            chunk.append(lst[j][0 : n])
            chunk.append(lst[j][n :])
    	
        return chunk
    		 
    def getmax(self,i):
    	a=[float('-Inf')]*i
    	return a
    
    def getmin(self,i):
    	a=[float('Inf')]*i
    	return a
    
    def getbounds(self,blocks):
    	bound=[]
    	bounds=blocks
    	top=()
    	bot=()
    	#mark=-1
    	for i in range (len(blocks)):  #[[(),()....],[],...]
    		for j in range (len(blocks[i])): #[(),()....]
    			#mark=mark+1
    			maxx=self.getmax(self.dimension)
    			minn=self.getmin(self.dimension)
    			for m in blocks[i][j]: # m is tuple
    			    for n in range(len(m)):
    			        if m[n]>maxx[n]:
    			        	maxx[n]=m[n]
    			        if m[n]<minn[n]:
    			        	minn[n]=m[n]
    			bounds[i][j]=[tuple(maxx),tuple(minn)]
    			#bounds.append([tuple(maxx),tuple(minn)])
    		#bounds.append(bound)
    	return bounds

def point_gen(list, n):
    points = ()
    for i in range(n):
        points= points + (list[i],)
    return points

def getBlockNumber(minNum,num):
	pointNum=num
	
	if minNum>num:
		return 1
	else: 
		#print(int(math.ceil(num/minNum)))
		return int(math.ceil(num/minNum))
def minDestince(point,block,dimension):
    dessqu=0
    for i in range (dimension):
        if point[i]<=block[1][i]:
        	mindes=block[1][i]-point[i]
        elif block[1][i]<point[i]<block[0][i]:
        	mindes=0
        else:
        	mindes=point[i]-block[0][i]
        dessqu=dessqu+mindes*mindes
    return np.sqrt(dessqu)
def maxDestince(point,block,dimension):
    dessqu=0
    for i in range (dimension):
        if point[i]<=block[1][i]:
        	maxdes=block[0][i]-point[i]
        elif block[0][i]>point[i]>block[1][i]:
        	if (point[i]-block[1][i])>(block[0][i]-point[i]):
        		maxdes=point[i]-block[1][i]
        	else:
        		maxdes=block[0][i]-point[i]
        else:
        	maxdes=point[i]-block[1][i]
        dessqu=dessqu+maxdes*maxdes
    return np.sqrt(dessqu)

def getCurrMax(destance):
    cmax=float('-Inf')
    for d in destance:
        if d[0]>cmax:
        	cmax=d[0]
    return cmax

def getCurrMin(destance):
    cmin=float('Inf')
    for d in destance:
        if d[1]<cmin:
        	cmin=d[1]
    return cmin
def takeSecond(elem):
    return elem[0]
def drop(allbounds,point,bounds,dimension,blockNum):
    destance=[]
    for j in range(allbounds):
            #if i<=j:
        a= maxDestince(point,bounds[j],dimension)
        b= minDestince(point,bounds[j],dimension)
        destance.append([a,b])
    destance.sort(key=takeSecond)
    #print (destance)
    destance=destance[0:blockNum]
    return destance
def KNN(point,num,minNum,bounds,dimension):
    blockNum=getBlockNumber(minNum,num)
    allbounds=len(bounds)
    
    destance=drop(allbounds,point,bounds,dimension,blockNum)
    
    cmax=getCurrMax(destance)
    cmin=getCurrMin(destance)
    
    l=len(bounds)
    for bound in bounds:
      
            if minDestince(point,bound,dimension)>cmax:
                l=l-1
    return l, l/allbounds
    
   		
if __name__ == '__main__':
    percentage = []
    block_visited = []
    dim = range(2, 20,2)
    for i in dim:
      if i%2==0:
        temp_num = []
        temp_percentage = []
        for n in range(10):
            print(f'{i} dimension, {n+1}th time')
            tree = rtree(i, 50000)
            t=tree.create()
            blocks=tree.getNdimension(t)
            bounds=tree.getbounds(blocks)
            blocks=tree.getNdimension(t)
        
            b=bounds[(tree.divitime-1)]
            lst = np.random.randint(100, size=tree.dimension)
       
            point = point_gen(lst, i)
        
            num_to_add, percentage_to_add = KNN(point,10,tree.minNum,b,tree.dimension)
            temp_num.append(num_to_add)
            temp_percentage.append(percentage_to_add)

        percentage.append(np.mean(temp_percentage))
        block_visited.append(np.mean(temp_num))
    print(percentage)
    print(block_visited)
    
    plt.plot(dim, percentage, 'b-', marker = 'o')
    plt.show()
    