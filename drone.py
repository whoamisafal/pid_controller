

class Drone:
    
    def __init__(self,weight) -> None:
        self.weight = weight
        self.altitude  = 0 
        self.velocity = 0 
        self.__gravity = 9.8

    def update(self,thrust,dt):
        print(thrust)
        thrust = max(0,min(100,thrust))
        gravity = self.weight*self.__gravity
        accelerate = (thrust-gravity)/self.weight
        self.velocity += accelerate*dt 
        self.altitude += self.velocity * dt 

