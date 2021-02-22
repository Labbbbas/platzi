def average_temps(temps):
    
    sum_of_temps=0
    
    for temp in temps:
        sum_of_temps+=temp

    return sum_of_temps/len(temps)

if __name__ == "__main__":
    temps=[21,24,24,22,20,23,24]

    average=round(average_temps(temps),2)

    print("La temperatura promedio es: {}".format(average))