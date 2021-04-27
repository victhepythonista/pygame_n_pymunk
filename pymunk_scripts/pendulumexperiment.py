from app import App
from pendulum import Pendulum
    
    
app = App(name = "Pendulum Stimulation by Leting")

Pendulum(app.space,(200,20),(20,20))

Pendulum(app.space,(240,20),(240,200))

Pendulum(app.space,(280,20), (280, 200))

Pendulum(app.space,(320,20), (320,200))
app.run()