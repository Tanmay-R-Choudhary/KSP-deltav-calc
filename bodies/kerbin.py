import pandas as pd

class Kerbin:
    # row names: kerbin orbit, intercept, low orbit, land
    dfNormal = pd.DataFrame({
        "Mun": [3400, 860, 310, 580],
        "Minmus": [3400, 1270, 160, 180],
        "Eeloo": [3400, 3420, 1370, 620],
        "Moho": [3400, 4230, 2410, 870],
        "Eve": [3400, 1470, 1410, 8000],
        "Duna": [3400, 1090, 610, 1450],
        "Dres": [3400, 2570, 1290, 430],
        "Jool": [3400, 2200, 2970, 14000]
    }, index=["Kerbin Orbit", "Intercept", "Low Orbit", "Land"])

    dfCumulative = pd.DataFrame({
        "Mun": [3400, 860, 310, 580],
        "Minmus": [3400, 1270, 160, 180],
        "Eeloo": [3400, 3420, 1370, 620],
        "Moho": [3400, 4230, 2410, 870],
        "Eve": [3400, 1470, 1410, 8000],
        "Duna": [3400, 1090, 610, 1450],
        "Dres": [3400, 2570, 1290, 430],
        "Jool": [3400, 2200, 2970, 14000]
    }, index=["Kerbin Orbit", "Intercept", "Low Orbit", "Land"])

    def __init__(self):
        for i in range(1, len(self.dfCumulative.index)):
            self.dfCumulative.iloc[i] += self.dfCumulative.iloc[i-1]

    def to_orbit(self):
        return 3400

    def to_keostationary_orbit(self):
        return self.to_orbit + 1115

    def show_stages(self):
        print("Stages: ")
        print(self.dfCumulative.index)

    def destination(self, name, stage, mode):
        if mode == "normal":
            print("Delta-v levels")
            print(self.dfNormal[name]["Kerbin Orbit": stage])
        if mode == "cumulative":
            print("Cumulative delta-v levels")
            print(self.dfCumulative[name]["Kerbin Orbit": stage])