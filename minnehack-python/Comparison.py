import math
farm_list = []
target_farm = Farm("dfdsfs")

def main thing ():


# % of farms like urs in your area that were profitable/that lost money
# the average profit/loss for farms like urs/farms like urs in your area/for farms.


    #use bayes algo to compute the percentage likleyhood of a farm that is "close" to our target farm having each
#sorta crop

def get_farms_in_area():
    flist = []
    for farm in farm_list:
        if compute_distance(farm.get_loc(), target_farm.get_loc()) < 1500:
            flist.append(farm)
    return flist

def get_farms_like_target(flist):
    LIKE_PERCENT_CUTOFF = 25
    targetdict = {}
    #create a dictionary of the target farm and its crop percentages
    for crop in target_farm.getCroptypes():
        dict[crop] = get_percentage_of_crop(target_farm, crop)

    #create dictionaries of the farms and their crop percentages
    farm_dict ={}
    farm_list =[]
    for farm in flist:
        temp = {}
        for crop in farm.getCroptypes():
            temp[crop] = get_percentage_of_crop(farm, crop)
        farm_list.append(temp)

    blockdiff = 0
    for farmdict in farm_list:
        for n in targetdict.keys():
            if farmdict.has_key(n):
                # percent sim measurement prepblockdiff += max(farmdict.get(n), targetdict.get(n)) - min(farmdict.get(n), targetdict.get(n))
    #calc percent sim
    #return percent sim



def get_percentage_of_crop(farm, cro):
    totalblocks = 0
    totalcrop = 0
    for field in farm.get_fields():
        for block in field.get_blocks():
            totalblocks +=1
            if block.get_crop() == cro:
                totalcrop +=1
    return totalblocks/totalcrop



def compare_loc (farm):
     compute_distance(farm.get_loc(),target_farm.get_loc())


def compute_distance (loc1, loc2):
    R = 6371 # Radius of the earth in km
    dLat = deg2rad(loc1[0] - loc1[1]) # deg2rad below
    dLon = deg2rad(loc2[0] - loc2[1])#long then lat
    a = math.sin(dLat / 2) * math.sin(dLat / 2) +math.cos(deg2rad(loc1[1])) * math.cos(deg2rad(loc2[1])) \
        *math.sin(dLon / 2) * math.sin(dLon / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c # Distance in km
    return d


def deg2rad(deg):
    return deg * (math.pi / 180)


