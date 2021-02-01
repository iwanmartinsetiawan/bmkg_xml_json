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

print(gempa_dirasakan_m5())

print(gempa_m_5())

print(tsunami_terkini())
