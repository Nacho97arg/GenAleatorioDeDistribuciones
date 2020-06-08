class ranGen:

    def randGCL(self, seed, rep): #Linear congruential generator
        val = []
        a=25214903917
        c=11
        m=2**64
        for i in range(0,rep):
            
            if i==0:
                x = (seed * a + c) % m
                val.append(x)
            else:
                x = (val[i-1] * a + c) % m
                val.append(x)
        for i in range(len(val)):
            val[i] = val[i] / m
        return val