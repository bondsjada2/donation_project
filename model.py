def address(zipcode):
    # print(type(zipcode))
    if int(zipcode) == 11201:
        # print("running")
        return "Adams Street Library: 135 Plymouth Street Brooklyn, NY 11201"
    if int(zipcode) == 11428:
        # print("running")
        return "Queens Village: 94-11 217 Street, Queens Village, NY 11428" 
    if int(zipcode) == 10467:
        # print("running")
        return "Allerton Library: 2740 Barnes Avenue, Bronx, NY 10467"
    if int(zipcode) == 10035:
        # print("running")
        return "125th Street Library: 224 East 125th Street, New York, NY 10035" 
    if int(zipcode) == 10304:
        # print("running")
        return "Dongan Hill Library: 1617 Richmond Road, Staten Island, NY 10304" 
    if int(zipcode) == 29440:
        # print("running")
        return "405 Cleland St, Georgetown, SC 29440"  

# def donation(center):
#     if center.lower() == "goodwill":
#         return "Here are goodwills near you"

# def SetPic(month):
#     if month.lower() == "august":
#         return "static/img/peridot.png"