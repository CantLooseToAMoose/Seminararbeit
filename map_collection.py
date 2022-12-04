import pixelmap
import numpy as np


def GetTrainingsMap(tier):
    if tier == 1:
        return GetTraingsMap_Tier1()
    elif tier == 2:
        return GetTrainingsMap_Tier2()
    elif tier == 3:
        return GetTrainingsMap_Tier3()
    elif tier == 4:
        return GetTrainingsMap_Tier4()
    elif tier == 5:
        return GetTrainingsMap_Tier5()


def GetTestMap(tier):
    if tier == 1:
        return GetTestMap_Tier1()
    elif tier == 2:
        return GetTestMap_Tier2()
    elif tier == 3:
        return GetTestMap_Tier3()


def GetTraingsMap_Tier1():
    pm = pixelmap.Pixelmap(50, 50, 10)
    return pm


def GetTrainingsMap_Tier2():
    pm = pixelmap.Pixelmap(50, 50, 10)
    obstacle_1 = np.ones((5, 5))
    pm.set_obstacle(obstacle_1, (7, 7))
    pm.set_obstacle(obstacle_1, (22, 22))
    pm.set_obstacle(obstacle_1, (38, 7))
    pm.set_obstacle(obstacle_1, (7, 37))
    pm.set_obstacle(obstacle_1, (38, 38))
    return pm


def GetTrainingsMap_Tier3():
    pm = pixelmap.Pixelmap(50, 50, 10)
    obstacle_1 = np.ones((5, 36))
    obstacle_2 = np.ones((10, 5))
    pm.set_obstacle(obstacle_1, (7, 7))
    pm.set_obstacle(obstacle_1, (38, 7))
    pm.set_obstacle(obstacle_2, (20, 10))
    pm.set_obstacle(obstacle_2, (20, 35))
    pm.set_obstacle(obstacle_2, (10, 23))
    pm.set_obstacle(obstacle_2, (30, 23))
    return pm


def GetTrainingsMap_Tier4():
    pm = pixelmap.Pixelmap(80, 80, 10)
    obstacle_1 = np.ones((30, 5))
    obstacle_2 = np.ones((5, 30))
    pm.set_obstacle(obstacle_1, (5, 5))
    pm.set_obstacle(obstacle_2, (5, 5))
    pm.set_obstacle(obstacle_1, (45, 5))
    pm.set_obstacle(obstacle_2, (70, 5))
    pm.set_obstacle(obstacle_1, (5, 70))
    pm.set_obstacle(obstacle_2, (5, 45))
    pm.set_obstacle(obstacle_1, (45, 70))
    pm.set_obstacle(obstacle_2, (70, 45))
    obstacle_3 = np.ones((10, 5))
    obstacle_4 = np.ones((5, 10))
    pm.set_obstacle(obstacle_3, (20, 20))
    pm.set_obstacle(obstacle_4, (20, 20))
    pm.set_obstacle(obstacle_3, (50, 20))
    pm.set_obstacle(obstacle_4, (55, 20))
    pm.set_obstacle(obstacle_3, (20, 55))
    pm.set_obstacle(obstacle_4, (20, 50))
    pm.set_obstacle(obstacle_3, (50, 55))
    pm.set_obstacle(obstacle_4, (55, 50))
    obstacle_5 = np.ones((70, 3))
    obstacle_6 = np.ones((3, 70))
    pm.set_obstacle(obstacle_5, (5, 39))
    pm.set_obstacle(obstacle_6, (39, 5))

    return pm


def GetTrainingsMap_Tier5():
    pm = pixelmap.Pixelmap(80, 80, 10)
    r = np.random
    r.seed(42855347)
    obstacle_noise_1 = r.randint(0, 2, size=(78, 78))
    r.seed(3423)
    obstacle_noise_2 = r.randint(0, 2, size=(78, 78))
    obstacle_noise = np.subtract(obstacle_noise_2, obstacle_noise_1)
    # r.seed(5564764)
    # obstacle_noise_3 = r.randint(0, 2, size=(78, 78))
    # obstacle_noise = np.subtract(obstacle_noise, obstacle_noise_3)
    obstacle_noise[obstacle_noise < 0] = 0
    obstacle_1 = np.ones((70, 2))
    obstacle_2 = np.ones((2, 70))
    pm.set_obstacle(obstacle_noise, (1, 1))
    pm.set_obstacle(obstacle_1, (5, 39))
    pm.set_obstacle(obstacle_2, (39, 5))
    return pm


def GetTestMap_Tier1():
    pm = pixelmap.Pixelmap(50, 50, 10)
    obstacle_1 = np.ones((5, 30))
    obstacle_2 = np.ones((25, 5))
    pm.set_obstacle(obstacle_1, (22, 10))
    pm.set_obstacle(obstacle_2, (12, 10))
    pm.set_obstacle(obstacle_2, (12, 35))
    return pm


def GetTestMap_Tier2():
    pm = pixelmap.Pixelmap(50, 50, 10)
    obstacle_1 = np.ones((5, 40))
    obstacle_2 = np.ones((10, 5))
    obstacle_3 = np.ones((5, 5))
    pm.set_obstacle(obstacle_1, (10, 10))
    pm.set_obstacle(obstacle_2, (15, 30))
    pm.set_obstacle(obstacle_2, (30, 30))
    pm.set_obstacle(obstacle_3, (0, 30))
    pm.set_obstacle(obstacle_3, (5, 10))
    pm.set_obstacle(obstacle_3, (45, 30))
    obstacle_4 = np.ones((4, 15))
    pm.set_obstacle(obstacle_4, (33, 35))
    obstacle_5 = np.ones((30, 5))
    pm.set_obstacle(obstacle_5, (15, 20))
    obstacle_6 = np.ones((5, 20))
    pm.set_obstacle(obstacle_6, (40, 5))
    return pm


def GetTestMap_Tier3():
    pm = pixelmap.Pixelmap(100, 100, 10)
    r = np.random
    r.seed(42855323)
    obstacle_noise_1 = r.randint(0, 2, size=(98, 98))
    r.seed(3452323)
    obstacle_noise_2 = r.randint(0, 2, size=(98, 98))
    obstacle_noise = np.subtract(obstacle_noise_2, obstacle_noise_1)
    r.seed(5564764)
    obstacle_noise_3 = r.randint(0, 2, size=(98, 98))
    obstacle_noise = np.subtract(obstacle_noise, obstacle_noise_3)
    obstacle_noise[obstacle_noise < 0] = 0
    obstacle_1 = np.ones((90, 2))
    obstacle_2 = np.ones((2, 90))
    pm.set_obstacle(obstacle_noise, (1, 1))
    pm.set_obstacle(obstacle_1, (5, 49))
    pm.set_obstacle(obstacle_2, (49, 5))
    obstacle_3 = np.ones((40, 5))
    obstacle_4 = np.ones((5, 40))
    pm.set_obstacle(obstacle_3, (30, 20))
    pm.set_obstacle(obstacle_3, (30, 75))
    pm.set_obstacle(obstacle_4, (20, 30))
    pm.set_obstacle(obstacle_4, (75, 30))

    return pm
