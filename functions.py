import numpy as np


def alphaa(a, b):
    return np.dot(a, np.transpose(b))


def forward(alpha, observations, Rr, uR):
    rain = np.array([[0.5, 0.5]])
    for i, chance in enumerate(observations):
        r = Rr[0]
        ra = rain[i]
        PR = [np.add(np.multiply(r, ra[0]), np.multiply(np.flip(r, axis=0), ra[1]))]
        Rr = np.append(Rr, PR, axis=0)
        a = np.multiply(uR, PR)
        b = alphaa(a, PR)
        print(b)
        PRU = alpha * a
        rain = np.append(rain, PRU, axis=0)



