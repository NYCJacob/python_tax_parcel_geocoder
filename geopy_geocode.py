import pandas as pd
from geopy.geocoders import GoogleV3
from geopy.extra.rate_limiter import RateLimiter

geolocator = GoogleV3(format_string="%s, Marbletown NY")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# create new csv file to save data
new_csv_file= open('geocoded_data.csv', 'w')

# process original csv file
df_csv = pd.read_csv('tmarble_export.csv', nrows=2)
for row in df_csv.itertuples(index=True, name='Pandas'):
    row_add_number= getattr(row, "ADDRESS_NU")
                                                # isnan throws typeerror against row_add_number even though a float??
    if type(row_add_number) is float:
        print("nan")
    else:
        row_objid= getattr(row, "OBJECTID")
        row_add_name= getattr(row, "ADDRESS_NA")
        not_geocoded_full_address= str(row_add_number) + " " + str(row_add_name) + " Marbletown, NY"
        #print(not_geocoded_full_address)
        address, (latitude, longitude) = geolocator.geocode(not_geocoded_full_address)
        print(row_objid, address, latitude, longitude)
        # write geocoded address and object id to csv file
        new_csv_file.write(str(row_objid) + "," + address + "," + str(latitude) + "," + str(longitude) + '\n')

# close open file stream
new_csv_file.close()