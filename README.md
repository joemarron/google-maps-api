
# Google Maps API

Testing and writing a simple Python function to call the Google Maps API to calculate a user given journey. This was part of experimentation with the API, which was later used to help enhance the employee expenses solution at my workplace at the time. This allowed employee claimed travel to be accurately measured, leading to an increase in the accuracy of carbon emissions reporting.

### Prerequisites
1. You will need a [Google Cloud Platform](https://developers.google.com/maps) account and to have generated an API key. 
2. The function utilises the very useful [googlemaps](https://github.com/googlemaps) package, which helps streamline requests sent to the API and avoids using the Requests package. To install you can run ```pip install googlemaps```.

## Example
Example usage can be achieved by using the `testing_gmaps.py` file, which takes the `test_journeys.csv` and calculates the mileages for each journey.
| origin                | destination | mode    | transit_mode | is_return |
| --------------------- | ----------- | ------- | ------------ | --------- |
| London                | Edinbrough  | transit | train        | FALSE     |
| Bowness-on-Windermere | Leeds       | driving |              | TRUE      |
| Cornwall              | Sheffield   | driving |              | FALSE     |
| Doncaster             | London      | transit | train        | TRUE      |
| SW1A 2AA              | DL12 8PR    | driving |              | TRUE      |

The code below from `testing_gmaps.py` shows usage of our gmaps function to calculate mileage for each record in above table.
```
# Import Libraries
import gmaps_calc as gm # Import gmaps function
import pandas as pd # for reading csv

# load example journeys csv
journeys = pd.read_csv('test_journeys.csv')
mileages = [] # define empty mileages list

# iterate through dataframe
for i, r in journeys.iterrows():
    # if transit_mode not specified, calc mileage using calc_distance function 
    if type(r['transit_mode']) != str:
        miles = gm.calc_distance(r['origin'], r['destination'], mode=r['mode'], is_return=bool(r['is_return']))
    # if transit_mode specified, calc mileage using calc_distance function using with transit_mode
    else:
        miles = gm.calc_distance(r['origin'], r['destination'], mode=r['mode'], transit_mode=r['transit_mode'], is_return=bool(r['is_return'])) 
    # append mileage calculated to mileages list
    mileages.append(miles)
    
# create mileage column and assign calculated milages
journeys['mileage'] = mileages
# print dataframe and save as csv
print(journeys)
journeys.to_csv('journeys_calculated.csv', index=False)
```
 The results can be seen below.
| origin                | destination | mode    | transit_mode | is_return | mileage |
| --------------------- | ----------- | ------- | ------------ | --------- | ------- |
| London                | Edinbrough  | transit | train        | FALSE     | 400.48  |
| Bowness-on-Windermere | Leeds       | driving |              | TRUE      | 233.75  |
| Cornwall              | Sheffield   | driving |              | FALSE     | 339.1   |
| Doncaster             | London      | transit | train        | TRUE      | 318.52  |
| SW1A 2AA              | DL12 8PR    | driving |              | TRUE      | 506.53  |