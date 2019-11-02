import random
import string
import numpy as np

class Population:
    populationSize = 1000
    population = []
    mutationRate = .01
    generation = 1
    target = 'arya kaustava mishra'
    fitness = []
    wheel = []

    def setup(self):
        letters = string.ascii_lowercase+' '
        for n in range(self.populationSize):
            dna=[]
            for i in range(len(self.target)):
                dna.append(random.choice(letters))
            self.population.append(dna)
            self.fitness.append(0)
    
    def calculateFitness(self):
        for n in range(self.populationSize):
            self.fitness[n] = self.individualFitness(self.population[n],self.target)

    def setupWheel(self):
        top_2_idx = np.argsort(self.fitness)[-2:]
        for i in top_2_idx:
            self.wheel.append(i)
        #for n in range(self.populationSize):
        #    for x in range(self.fitness[n]):
        #        self.wheel.append(n)

    @staticmethod
    def individualFitness(src, trg):
        count=0
        for i in range(len(trg)):
            if trg[i] == src[i]:
                count=count+1
                #print(self.target, '  :  ',''.join(self.population[n]))
        return count

    def selection(self):
        results = []
        while len(results) < 1:
            choice = random.randint(0, sum(self.fitness))
            for index, value in enumerate(self.fitness):
                choice -= value
                if choice < 0:
                    results.append(self.population[index])
                    #print(choice, ' ',len(results))
            
        return results[0]


    def pickParent(self):
        #index = self.wheel[random.randrange(0,len(self.wheel))]
        index  = self.fitness.index(max(self.fitness))
        return self.population[index]

    def nextGeneration(self):
        newPop=[]
        self.generation+=1
        for n in range(self.populationSize):
            parent1 = self.pickParent()
            parent2 = self.pickParent()
            child = self.crossOver(parent1, parent2)
            child  = self.mutate(child)
            newPop.append(child)
        self.population=newPop

    def crossOver(self,p1, p2):
        mid = random.randrange(len(self.target))
        child = []
        for i in range(len(self.target)):
            if i < mid:
                child.append(p1[i])
            else:
                child.append(p2[i])
        return child

    def mutate(self,child):
        letters = string.ascii_lowercase+' '
        if self.mutationRate > random.random():
        #for i in range(self.mutationRate):
            pos = random.randrange(len(self.target))
            child[pos]= random.choice(letters)
        return child
    
    def validate(self):
        index  = self.fitness.index(max(self.fitness))
        print(''.join(self.population[index]),' ',self.generation, ' ',self.fitness[index])
        if(''.join(self.population[index])==self.target):
            return True
        else:
            return False

def run():
    p=Population()
    p.setup()
    p.calculateFitness()
    while not p.validate():
        p.setupWheel()
        p.nextGeneration()
        p.calculateFitness()
run()
#print(Population.individualFitness('methinkc it is like a weasel',Population.target))
