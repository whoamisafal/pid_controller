class PIDController:
    def __init__(self,Kp,Ki,Kd,setPoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd 
        self.setPoint = setPoint
        self.integral = 0 
        self.previous_error = 0
        

    def update(self,feedback,dt):
        error = self.setPoint - feedback # calculate the error 
        derivative = (error-self.previous_error)/dt 
        self.integral += error* dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return output
