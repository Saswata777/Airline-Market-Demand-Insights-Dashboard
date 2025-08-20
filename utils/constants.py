CITIES = {
    "Sydney": {"iata": "SYD", "queries": ["Sydney to Melbourne flights", "flights to Sydney"]},
    "Melbourne": {"iata": "MEL", "queries": ["Melbourne to Sydney flights", "flights to Melbourne"]},
    "Brisbane": {"iata": "BNE", "queries": ["Brisbane to Sydney flights", "flights to Brisbane"]},
    "Perth": {"iata": "PER", "queries": ["Perth to Melbourne flights", "flights to Perth"]},
    "Adelaide": {"iata": "ADL", "queries": ["Adelaide to Sydney flights", "flights to Adelaide"]},
    "Cairns": {"iata": "CNS", "queries": ["Cairns to Sydney flights", "flights to Cairns"]},
    "Gold Coast": {"iata": "OOL", "queries": ["Gold Coast to Sydney flights", "flights to Gold Coast"]},
    "Hobart": {"iata": "HBA", "queries": ["Hobart to Melbourne flights", "flights to Hobart"]},
}

#  International Air Transport Association (iata) codes for cities

ROUTES = [
    ("Sydney", "Melbourne"), ("Sydney", "Brisbane"), ("Melbourne", "Brisbane"),
    ("Sydney", "Perth"), ("Melbourne", "Perth"), ("Sydney", "Adelaide"),
    ("Melbourne", "Hobart"), ("Brisbane", "Cairns"), ("Sydney", "Gold Coast"),
]