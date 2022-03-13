# everything is idealized.
allstops={
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
} # container for all bus stops.
charge=1.8 # pay 1.8 per stop.


def stops_interval(startstop,endstop):
    v=allstops[startstop]-allstops[endstop]
    if v>0:
        c=(13-abs(v))*charge
    else:
        c=abs(v)*charge
    return c
'''     I assume its routine is a loop. If endstop is somewhere before startstop on the routine,
        passenger might go to the bottom stop and take a new one starts from the top stop.
'''
print("Welcome to take bus.")
start=input("Your start stop is:")
end=input("Your end stop is:")
print("The charge is:"+str(stops_interval(start,end))+".")
