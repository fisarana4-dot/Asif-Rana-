class FibonacciEngine:
    def levels(self,high,low):
        r=high-low
        return {0.0:high,0.236:high-r*0.236,0.382:high-r*0.382,0.5:high-r*0.5,0.618:high-r*0.618,0.786:high-r*0.786,1.0:low}
fibonacci_engine=FibonacciEngine()
