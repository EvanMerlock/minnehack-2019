farm_list
target_farm

def main thing ():

    #use bayes algo to compute the percentage likleyhood of a farm that is "close" to our target farm having each
sorta crop

def get_farms_in_area():
    flist = []
    for Farm: farm_list:
        if compute_distance(farm.get_loc(), target_farm.get_loc()) < 1500:
            flist.append(farm)
return flist

def get_farms_like_target(flist):
    targetdict = {}
    #create a dictionary of the target farm and its crop percentages
    for crop in target_farm.getCroptypes():
        dict[crop] = get_percentage_of_crop(target_farm, crop)

    #create dictionaries of the farms and their crop percentages
    farm_dict
    for Farm in flist:
        temp = {}
        for crop in farm.getCroptypes():
            dict[crop] = get_percentage_of_crop(farm, crop)
        dict [farm.get_ID()]=temp


def get_percentage_of_crop(farm, cro):
    totalblocks = 0
    totalcrop = 0
    for field in farm.get_fields():
        for block in field.get_blocks()
            totalblocks++
            if block.get_crop() = cro:
                totalcrop ++
    return totalblocks/totalcrop

#% of farms like urs in your area that were profitable/that lost money
#% the average profit/loss for farms like urs/farms like urs in your area/for farms.

def compare_loc (farm):
     compute_distance(farm.get_loc(),target_farm.get_loc())


def compute_distance (loc1, loc2):
    R = 6371 # Radius of the earth in km
    dLat = deg2rad(lat2 - lat1) # deg2rad below
    dLon = deg2rad(lon2 - lon1)
    a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *Math.sin(dLon / 2) * Math.sin(dLon / 2)

    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
    d = R * c # Distance in km
    return d


def deg2rad(deg):
    return deg * (Math.PI / 180)


