from jinja2 import Template
from src.bingo import carton_definitivo

carton = carton_definitivo()
template = Template(open("tabla.j2").read())
print(template.render(carton=carton))

#Dejo total constancia de que tome ayuda de trabajos de mis compañeros para esto. Así mismo, dejo constancia de haber analizado los códigos de los cuales utilicè. 
