# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


#Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".
#Test your function with the data stored in damages.
# write your update damages function here:

def damage_converter(damages) :
  numeric_damages = []
  for damage in damages :
    if damage == 'Damages not recorded' :
      numeric_damages.append(damage)
    elif damage[-1] == 'B' :
      temp = float(damage[:-1])*1000000000
      numeric_damages.append(temp)
    elif damage[-1] == 'M' :
      temp = float(damage[:-1])*1000000
      numeric_damages.append(temp)
  return numeric_damages

print(damage_converter(damages))

#Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.
# write your construct hurricane dictionary function here:
# Defining an empty dictionary

def create_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths) :
  hurricanes_dict = {}
  for i in range(len(names)) :
    inner_dict = {}
    inner_dict['Name'] = names[i]
    inner_dict['Month'] = months[i]
    inner_dict['Year'] = years[i]
    inner_dict['Max Sustained Wind'] = max_sustained_winds[i]
    inner_dict['Areas Affected'] = areas_affected[i]
    inner_dict['Damage'] = damages[i]
    inner_dict['Deaths'] = deaths[i]
    hurricanes_dict[names[i]] = inner_dict
  return hurricanes_dict

hurricanes_dict = create_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

#print(hurricanes_dict)

#Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
# write your construct hurricane by year dictionary function here:

def hurricanes_by_year(years, names, hurricanes_dict) :
  year_dict = {}
  for i in range(len(years)) :
    if years[i] in year_dict :
      year_dict[years[i]].append(hurricanes_dict[names[i]])
    else :
      temp_list = []
      temp_list.append(hurricanes_dict[names[i]])
      year_dict[years[i]] = temp_list
  return year_dict

print(hurricanes_by_year(years, names, hurricanes_dict))

#Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.
# write your count affected areas function here:

def vulnerability_finder(areas_affected) :
  area_vulnerability = {}
  for areas in areas_affected :
    for area in areas :
      if area in area_vulnerability :
        area_vulnerability[area] += 1
      else :
        area_vulnerability[area] = 1
  return area_vulnerability

area_vulnerability = vulnerability_finder(areas_affected)
print(area_vulnerability)

#Write a function that finds the area affected by the most hurricanes, and how often it was hit.
# write your find most affected area function here:

def most_affected_finder(area_vulnerability) :
  max_count = 0
  for area in area_vulnerability :
    if area_vulnerability[area] > max_count :
      max_count = area_vulnerability[area]
      worst_affected_area = area
  return max_count, worst_affected_area

print(most_affected_finder(area_vulnerability))


#Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.
# write your greatest number of deaths function here:

def max_deaths_finder(hurricanes_dict) :
  max_deaths = 0
  for hurricane in hurricanes_dict :
    if hurricanes_dict[hurricane]['Deaths'] > max_deaths :
      max_deaths = hurricanes_dict[hurricane]['Deaths']
      worst_hurricane = hurricanes_dict[hurricane]['Name']
  return worst_hurricane, max_deaths

print(max_deaths_finder(hurricanes_dict))

#Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.
# write your catgeorize by mortality function here:

def mortality_rater(hurricanes_dict) :
  ratings_dict = {}
  for hurricane in hurricanes_dict :
    if hurricanes_dict[hurricane]['Deaths'] > 10000 :
     rating = 5
    elif hurricanes_dict[hurricane]['Deaths'] > 1000 :
     rating = 4
    elif hurricanes_dict[hurricane]['Deaths'] > 500 :
     rating = 3
    elif hurricanes_dict[hurricane]['Deaths'] > 100 :
     rating = 2
    elif hurricanes_dict[hurricane]['Deaths'] > 0 :
     rating = 1
    else :
       rating = 0
    if rating in ratings_dict :
      ratings_dict[rating].append(hurricane)
    else :
      temp_list = []
      temp_list.append(hurricane)
      ratings_dict[rating] = temp_list
  return ratings_dict

print(mortality_rater(hurricanes_dict))
