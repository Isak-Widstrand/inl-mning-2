import numpy as np
import matplotlib.pyplot as plt

while True:
    grader = input("Ange grader: ")
    grader = float(grader)
    V0 = input("Ange utgångshastigheten: ")
    plt.figure(figsize=(5, 4))
    plt.ion()
    plt.xlabel("Längd (m)")
    plt.ylabel("Höjd (m)")
    plt.title("Kastparabel")
    plt.grid(True)
    V0 = float(V0)
    g = 9.81
    alfa = np.radians(grader)
    airtime = 2 * V0 * np.sin(alfa) / g
    tid = np.arange(0, airtime, 0.005)
    x_distans = V0 * tid * np.cos(alfa)
    y_distans = V0 * tid * np.sin(alfa) - g / 2 * tid ** 2

    plt.plot(x_distans, y_distans)
    plt.vlines (x=15, ymin=0, ymax=5)
    plt.draw()
    plt.show()

    bra = input("Är du nöjd med resultatet? (ja/nej): ").strip().lower()
    if bra == "ja":
        break
    else: 
        print("ange nya värden.")

#grader=40 och hastighet = 15.8