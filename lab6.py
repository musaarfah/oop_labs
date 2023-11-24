from random import randint

class Batsman:
    def __init__(self,name,country,total_matches=randint(10,20)):
        self.name=name
        self.country=country
        self.__total_matches=total_matches
        self.scores=[]
        randomscores=self._random_scores(total_matches)
        

    @property
    def total_matches(self):
        return self.__total_matches
    
    @total_matches.setter
    def total_matches(self,updated_matches):
        return updated_matches

    def _random_scores(self,total_match):
        rand=randint(0,10)
        if rand<7:
          for i in range(total_match):
            self.scores.append(randint(0,180))
        elif rand>7:
            self.scores.append(randint(350,500))

        return self.scores
    
    def calcTotal(self):
        sum=0
        for i in range(len(self.scores)):
            sum+=self.scores[i]
        return sum
    
    def calcAverage(self):
        sum=0
        for i in range(len(self.scores)):
            sum+=self.scores[i]
        avg=sum//(len(self.scores))
        return avg
    
    def max_score(self):
        max_score=max(self.scores)
        return max_score
    
    def count_50s(self):
        count_50=0
        for i in range(len(self.scores)):
            if self.scores[i]>=50 and self.scores[i]<100:
                count_50+=1
        return count_50
    
    def count_100s(self):
        count_100=0
        for i in range(len(self.scores)):
            if self.scores[i]>=100 and self.scores[i]<200:
                count_100+=1
        return count_100
    
    def show(self):
        print(f'Batsman : {self.name}')
        print(f'Country : {self.country}')
        print(f'Total Score : {self.calcTotal()}')
        print(f'Average Score : {self.calcAverage()}')
        print(f'No. of Matches : {self.total_matches}')
        print(f'scores :',end=' ')
        for score in self.scores:
            print(score,end=' ')
        print()
        print(f'Highest Score : {self.max_score()}')
        print(f'Fifties : {self.count_50s()}')
        print(f'Centuries : {self.count_100s()}')
        print()


        
      
    
    



def main():
  batsemen=[Batsman('Virat Kohli','Bharat',30),Batsman('Adam Gilchrist','Australia'),Batsman('Fakhar Zaman','Pakistan',20)]
  for batsman in batsemen:
      batsman.show()

main()