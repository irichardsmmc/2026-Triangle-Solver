import math

# Functions
def calculations(opp, adj, hyp, theta):

    if theta is not None:

        theta = math.radians(theta)

    while any(item is None for item in [opp, adj, hyp, theta]):

        num_known_sides = sum(side is not None for side in [opp, adj, hyp])

        if num_known_sides >= 2:
            if hyp is None:
                hyp = math.sqrt(opp ** 2 + adj ** 2)
            if opp is None:
                opp = math.sqrt(hyp ** 2 - adj ** 2)
            if adj is None:
                adj = math.sqrt(hyp ** 2 - opp ** 2)

        if theta is None:
            if hyp is not None:
                if opp is not None:
                    theta = math.asin(opp / hyp)
                elif adj is not None:
                    theta = math.acos(adj / hyp)
            elif opp is not None and adj is not None:
                theta = math.atan(opp / adj)

        else:
            if opp is None:
                if adj is not None:
                    opp = adj * math.tan(theta)
                if hyp is not None:
                    opp = hyp * math.sin(theta)

            if adj is None:
                if hyp is not None:
                    adj = hyp * math.cos(theta)
                if opp is not None:
                    adj = opp / math.tan(theta)

            if hyp is None:
                if opp is not None:
                    hyp = opp / math.sin(theta)
                if adj is not None:
                    hyp = adj / math.cos(theta)

    return opp, adj, hyp, theta
        
