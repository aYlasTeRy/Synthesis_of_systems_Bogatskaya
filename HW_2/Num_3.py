# https://www.codewars.com/kata/57d001b405c186ccb6000304

def i_tri(s):
    swim = 2.4
    bicycle = 112
    marathon = 26.2
    distance = swim + bicycle + marathon

    if s == 0:
        return 'Starting Line... Good Luck!'
    elif s <= swim:
        return {"Swim": f'{distance - s:2.2f} to go!'}
    elif swim < s <= bicycle + swim:
        return {"Bike": f'{distance - s:2.2f} to go!'}
    elif distance - s <= 10 and bicycle + swim < s < distance:
        return {"Run": "Nearly there!"}
    elif distance - s > 10 and bicycle + swim < s < distance:
        return {"Run": f'{distance - s:2.2f} to go!'}
    elif s >= distance:
        return "You're done! Stop running!"