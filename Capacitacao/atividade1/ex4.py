carlos_height = 1.5  
artur_height = 1.1  
carlos_growth = 0.03  
artur_growth = 0.04  

years = 0

while artur_height <= carlos_height:

    carlos_height += carlos_growth
    artur_height += artur_growth
    
    years += 1

print(f"Em {years} anos o Artur ficará da mesma altura ou mais alto que Carlos.")
