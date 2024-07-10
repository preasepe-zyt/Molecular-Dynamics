import numpy as np

def mean(rmsd):
    i = 0
    t_m = []
    rmsd_m = []
    while i < 50:
        i += 1
        time = i * 100
        rmsd_raw = sum(rmsd[(time - 100):time]) / 100
        rmsd_m.append(rmsd_raw)
        t_m.append(time)
    rmsd_m = np.array(rmsd_m)
    t_m = np.array(t_m)
    return t_m, rmsd_m
