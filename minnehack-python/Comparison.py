import math
import difflib
farm_list = []
#target_farm = set this to the target farm!

#i was going to create test farms to test this w. then realized that this should be implemented using database stuff things.
def test ():
    pass

#questions that should be answerable
# % of farms like urs in your area that were profitable/that lost money
# the average profit/loss for farms like urs/farms like urs in your area/for farms.
#"a farm like yours" means that the farm has a similar crop configuration.
#NOT implemnted: combining the fucntions below to give the ans to the above questions.
#needed to implement:
#get profitloss aveage from a group/list of farms.



def get_farms_in_area():
    flist = []
    for farm in farm_list:
        if compute_distance(farm.get_loc(), target_farm.get_loc()) < 1500:
            flist.append(farm)
    return flist

def get_farms_like_target(flist):
    LIKE_PERCENT_CUTOFF = 25
    finalfarmsliketarget = []
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



    for farmdict in farm_list:
        sother = []
        starget = []
        counter = 0
        #create int lists of percentages for each type of crop, in order (X1 in sother corresponds to X1 in starget
        #then these lists are compared using difflib, and if they are above the cuttoff, the farm is added to the final
        #farms list. Right now, I didn't bring the farm wiht the dictionary, so we don't have a link back to the farm to add
        #(my major bad) I belive that this would have to be rewritten using database accessers? either way,
        #adding in a way to compare one farm against all others would be a major boost for the functionality of the program
        #idk how long I'm going to sleep, but if this is possible to implement, id advice it.
        #also note this is not currently a class.
        for n in targetdict.keys():
            sother[counter] = farmdict.get(n)
            if farmdict.has_key(n):
                starget[counter] = targetdict.get(n)
            else:
                starget[counter] = 0
            counter +=1
        for n in farmdict.keys():
            if not targetdict.has_key(n):
                starget[counter] = targetdict.get(n)
                targetdict[counter] = 0
            counter +=1
        sumdif = difflib.SequenceMatcher(None, starget, sother)
        if sumdif.ratio() > LIKE_PERCENT_CUTOFF:
            finalfarmsliketarget.append(#FARM OF n) #I think I need to add the farm to the dict
    return finalfarmsliketarget
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



