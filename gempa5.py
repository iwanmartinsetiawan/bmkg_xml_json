import xmltodict, json, requests

def gempa_dirasakan_m5():
    """
    Data gempa bumi dirasakan English.
    """

    url = "https://data.bmkg.go.id/en_autogempa.xml"

    data = requests.get(url)
    xpars = xmltodict.parse(data.text)
    res = json.dumps(xpars)
    return res

def gempa_m_5():
    """
    Data gempa bumi dirasakan 60 English.
    """

    url = "https://data.bmkg.go.id/en_gempaterkini.xml"

    data = requests.get(url)
    xpars = xmltodict.parse(data.text)
    res = json.dumps(xpars)
    return res

def tsunami_terkini():
    """
    Data tsunami terkini.
    """

    url = "https://data.bmkg.go.id/lasttsunami.xml"

    data = requests.get(url)
    xpars = xmltodict.parse(data.text)
    res = json.dumps(xpars)
    return res

gempa_m5 = gempa_dirasakan_m5()

print(gempa_dirasakan_m5())
# print(gempa_m_5())

# print(tsunami_terkini())

df = pd.read_json (gempa_m5)
export_csv = df.to_csv ('gempa5.csv', index = None, header=True)

# Normalizing data
# multiple_level_data = pd.json_normalize(gempa_m5, record_path =['data'], meta_prefix='id', record_prefix='dt_')


# Saving to CSV format
# multiple_level_data.to_csv('gempa5.csv', index=False)