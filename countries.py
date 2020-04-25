
class Australia():
    state_dict = {"NSW": "New South Wales", "V": "Victoria", "Q": "Queensland",
                  "SA": "South Australia", "WA": "Western Australia", "T": "Tasmania",
                  "NT": "Northern Territory", "ACT": "Australian Capital Territory"}
    constraints = {"NSW": ["V", "Q", "SA", "ACT"], "V": ["SA", "NSW"],
                   "Q": ["NT", "SA", "NSW"], "SA": ["WA", "NT", "Q", "V", "NSW"],
                   "WA": ["SA", "NT"], "T": ["V"], "NT": ["WA", "SA", "Q"], "ACT": ["NSW"]}
    variables = ["NSW", "WA", "NT", "SA", "Q", "V", "T", "ACT"]
    geojson = 'geojson/australia.geojson'
    name = 'australia'


class Germany():
    state_dict = {"BB": "Brandenburg", "BE": "Berlin", "BW": "Baden-Württemberg",
                  "BY": "Bayern", "HB": "Bremen", "HE": "Hessen", "HH": "Hamburg",
                  "MV": "Mecklenburg-Vorpommern", "NI": "Niedersachsen",
                  "NW": "Nordrhein-Westfalen", "RP": "Rheinland-Pfalz",
                  "SH": "Schleswig-Holstein", "SL": "Saarland",
                  "SN": "Sachsen", "ST": "Sachsen-Anhalt", "TH": "Thüringen"}
    constraints = {"BB": ["BE", "MV", "SN", "NI", "ST"], "BE": ["BB"],
                   "BW": ["BY", "HE", "RP"], "BY": ["BW", "HE", "TH", "SN"],
                   "HB": ["NI"], "HE": ["NI", "NW", "RP", "BW", "BY", "TH"],
                   "HH": ["NI", "SH"], "MV": ["SH", "NI", "BB"],
                   "NI": ["SH", "HH", "HB", "NW", "HE", "TH", "ST", "BB", "MV"],
                   "NW": ["NI", "HE", "RP"], "RP": ["NW", "HE", "BW", "SL"],
                   "SH": ["NI", "HH", "MV"], "SL": ["RP"],
                   "SN": ["BB", "ST", "TH", "BY"], "ST": ["BB", "NI", "TH", "SN"],
                   "TH": ["ST", "NI", "HE", "BY", "SN"]}
    variables = ["BB", "BE", "BW", "BY", "HB", "HE", "HH", "MV", "NI", "NW", "RP", "SH", "SL", "SN", "ST", "TH"]
    geojson = 'geojson/germany.geojson'
    name = 'germany'