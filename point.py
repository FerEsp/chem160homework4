class point:        
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def scale(self, x):
        for i in range(self.dim):
            self.data[i]*=x
    def dot(self, apoint):
        sum=0
        for i in range(self.dim):
            sum+=self.data[i]*apoint.data[i]
        return sum
    def dist(self, p2):
        d=0
        for i in range(self.dim):
            d += ((self.data[i]-p2.data[i])**2)
        distance=(d**0.5)
        return distance
    def mirror(self):
        for j in range(self.dim):
            self.data[j] = -self.data[j]
        