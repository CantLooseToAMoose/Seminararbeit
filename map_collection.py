import pixelmap

def GetTrainingsMap(tier):
    if tier==1:
        return GetTraingsMap_Tier1()


def GetTraingsMap_Tier1():
    pm = pixelmap.Pixelmap(50, 50, 10)