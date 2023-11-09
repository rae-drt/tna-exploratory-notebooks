## Hello! This is a file with aditional data for the project.
## Its stored here so it can be easily imported to other files.
## Having it in the notebook would make it too long and messy - no-one likes to scroll through lines of just data. 
## Each set of data here will have an explanation of what it is, how it was obtained, and which notebook it was used in.

## Ship list
## This is a list of ships from the Wikipedia list found here -> https://en.wikipedia.org/wiki/Category:War_of_1812_ships_of_the_United_Kingdom
## The list is used in notebook x, where we automate the process of getting the data from the API. A for loop is created 
## that loops through this list, and calls the API for each ship.
## Note that, to keep the code manageable in the notebook, this list is restricted to ships with an HMS prefix, and only one word in the name.

ships = [
"Acasta",
"Aeolus",
"Aetna",
"Africa",
"Albion",
"Alceste",
"Anaconda",
"Asia",
"Avon",
"Ballahou",
"Bedford",
"Belle",
"Belvidera",
"Bold",
"Bonne",
"Borer",
"Boxer",
"Boyne",
"Bream",
"Bucephalus",
"Bulwark",
"Caledonia",
"Calliope",
"Carron",
"Centurion",
"Charybdis",
"Cherub",
"Childers",
"Chippeway",
"Colibri",
"Columbine",
"Confiance",
"Cornwallis",
"Cornwallis",
"Curlew",
"Cuttle",
"Cyane",
"Cydnus",
"Detroit",
"Detroit",
"Devastation",
"Diadem",
"Dictator",
"Diomede",
"Dominica",
"Dragon",
"Duke",
"Elephant",
"Endymion",
"Epervier",
"Erebus",
"Euryalus",
"Fairy",
"Fantome",
"Favourite",
"Forward",
"Fox",
"Frolic",
"Galatea",
"Garland",
"General",
"Goliath",
"Gorgon",
"Grecian",
"Guerriere",
"Havannah",
"Herald",
"Hermes",
"Herring",
"Horatio",
"Hydra",
"Java",
"La",
"Lady",
"Landrail",
"Laura",
"Leander",
"Leopard",
"Levant",
"Linnet",
"Little",
"Lord",
"Macedonian",
"Madagascar",
"Majestic",
"Manly",
"Marlborough",
"Medway",
"Menelaus",
"Moira",
"Moselle",
"Mosquidobit",
"Nemesis",
"Newcastle",
"Niemen",
"Norge",
"Nymphe",
"Orpheus",
"Pactolus",
"Pelican",
"Penguin",
"Peruvian",
"Phoebe",
"Pictou",
"Pictou",
"Pigmy",
"Plantagenet",
"Poictiers",
"Pomone",
"Prince",
"Princess",
"Psyche",
"Racoon",
"Ramillies",
"Recruit",
"Reindeer",
"Ringdove",
"Royal",
"Royal",
"Ruby",
"San",
"Sappho",
"Saturn",
"Sceptre",
"Seahorse",
"Severn",
"Shannon",
"Shelburne",
"Sir",
"Sophie",
"Southampton",
"Spartan",
"St",
"St",
"Starr",
"Statira",
"Success",
"Superb",
"Surprise",
"Terror",
"Thames",
"Thistle",
"Tonnant",
"Valiant",
"Vengeur",
"Victorious",
"Volcano",
"Whiting",
"Wolfe"
]

## Admiralty record series
## This list is used in notebook x, where we automate the process of getting the data from the API. 
## These series are series in the National Archives catalogue that represent sections of the Admiralty records. 
## They are formateed as sps.recordSeries=ADM%20xxx, where xxx is the number of the series. This is the format that the API uses.

admiralty_record_series = [
"sps.recordSeries=ADM%2050", # record_series_ADM_50
"sps.recordSeries=ADM%2051", # record_series_ADM_51
"sps.recordSeries=ADM%2052", # record_series_ADM_52
"sps.recordSeries=ADM%2053", # record_series_ADM_53
"sps.recordSeries=ADM%2054", # record_series_ADM_54
"sps.recordSeries=ADM%2055", # record_series_ADM_55
"sps.recordSeries=ADM%20101", # record_series_ADM_101
"sps.recordSeries=MT%2032" # record_series_MT_32
]


## Ship record data
## This is a list of data pre-obtained from the API. It is used in notebook y, where we starto to visualise the data.
## The data are pre-downloaded to allow the work to be split into multiple notebooks without having to re-download the data each time.
## This also reduces the chance of the API rejecting calls for data (from too many calls in a short time period) and causing the notebook to crash.

ship_record_data = [
    {
        "records": [
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/08/1920",
                "id": "C1496966",
                "startDate": "01/07/1920"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/01/1914",
                "id": "C1496941",
                "startDate": "01/12/1913"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/05/1915",
                "id": "C1496945",
                "startDate": "10/04/1915"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/05/1913",
                "id": "C1480965",
                "startDate": "01/04/1913"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "30/01/1913",
                "id": "C1480963",
                "startDate": "30/11/1912"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "28/02/1917",
                "id": "C1496949",
                "startDate": "01/01/1917"
            },
            {
                "description": "<scopecontent><p>ACASTA.</p></scopecontent>",
                "digitised": False,
                "endDate": "31/05/1931",
                "id": "C1534145",
                "startDate": "01/05/1931"
            },
            {
                "description": "<scopecontent><p>ACASTA.</p></scopecontent>",
                "digitised": False,
                "endDate": "13/04/1930",
                "id": "C1534133",
                "startDate": "11/02/1930"
            },
            {
                "description": "<scopecontent><p>ACASTA.</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1932",
                "id": "C1534161",
                "startDate": "01/12/1932"
            },
            {
                "description": "<scopecontent><p>ACASTA.</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1934",
                "id": "C1534176",
                "startDate": "01/03/1934"
            },
            {
                "description": "<scopecontent><p>ACASTA.</p></scopecontent>",
                "digitised": False,
                "endDate": "30/06/1933",
                "id": "C1534167",
                "startDate": "01/06/1933"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1936",
                "id": "C1558833",
                "startDate": "01/03/1936"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "29/02/1936",
                "id": "C1558832",
                "startDate": "01/02/1936"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/01/1936",
                "id": "C1558831",
                "startDate": "01/01/1936"
            },
            {
                "description": "<scopecontent><p>ACASTA</p></scopecontent>",
                "digitised": False,
                "endDate": "30/09/1935",
                "id": "C1558827",
                "startDate": "01/09/1935"
            }
        ],
        "ship_name": "Acasta"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "30/05/1905",
                "id": "C1481046",
                "startDate": "09/06/1904"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "01/08/1908",
                "id": "C1481050",
                "startDate": "30/06/1908"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "07/09/1905",
                "id": "C1481047",
                "startDate": "31/05/1905"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1895",
                "id": "C1476643",
                "startDate": "08/01/1895"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "25/08/1893",
                "id": "C1476641",
                "startDate": "11/07/1893"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "18/06/1903",
                "id": "C1481044",
                "startDate": "16/09/1902"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "08/06/1904",
                "id": "C1481045",
                "startDate": "19/06/1903"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "03/10/1913",
                "id": "C1481054",
                "startDate": "01/05/1913"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "20/08/1901",
                "id": "C1481043",
                "startDate": "16/07/1901"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "17/08/1899",
                "id": "C1481042",
                "startDate": "11/07/1899"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "24/04/1897",
                "id": "C1476645",
                "startDate": "06/01/1897"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "05/01/1897",
                "id": "C1476644",
                "startDate": "01/01/1896"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "31/05/1907",
                "id": "C1481049",
                "startDate": "31/08/1906"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "30/08/1906",
                "id": "C1481048",
                "startDate": "08/09/1905"
            },
            {
                "description": "<scopecontent><p>AEOLUS</p></scopecontent>",
                "digitised": False,
                "endDate": "30/04/1913",
                "id": "C1481053",
                "startDate": "13/05/1912"
            }
        ],
        "ship_name": "Aeolus"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>Aetna (Etna) </p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1836",
                "id": "C1464685",
                "startDate": "23/10/1834"
            },
            {
                "description": "<scopecontent><p>Aetna (Etna) </p></scopecontent>",
                "digitised": False,
                "endDate": "13/11/1838",
                "id": "C1464686",
                "startDate": "01/01/1837"
            },
            {
                "description": "<scopecontent><p>Aetna (Etna) </p></scopecontent>",
                "digitised": False,
                "endDate": "10/09/1833",
                "id": "C1464683",
                "startDate": "27/05/1830"
            },
            {
                "description": "<scopecontent><p>Aetna (Etna) </p></scopecontent>",
                "digitised": False,
                "endDate": "25/04/1842",
                "id": "C1464687",
                "startDate": "08/02/1839"
            },
            {
                "description": "<scopecontent><p>Aetna (Etna) </p></scopecontent>",
                "digitised": False,
                "endDate": "11/03/1844",
                "id": "C6224063",
                "startDate": "11/06/1842"
            },
            {
                "description": "<scopecontent><p>Aetna (Etna)</p></scopecontent>",
                "digitised": False,
                "endDate": "24/05/1830",
                "id": "C6224062",
                "startDate": "12/12/1827"
            },
            {
                "description": "<scopecontent><p>Masters' logs: Aetna</p></scopecontent>",
                "digitised": False,
                "endDate": "18/11/1838",
                "id": "C16604172",
                "startDate": "15/03/1836"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Aetna (1778 May 14 - 1779 Feb 26). </p><p>Aetna (1779 Mar 4 - 1779 Aug 29). </p><p>Aetna (1780 Jan 17 - 1781 Mar 7). </p><p>Aetna (1781 July 12 - 1781 Dec 5)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1781",
                "id": "C2529962",
                "startDate": "01/01/1778"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Aetna (1804 Jan 4 - 1805 Jan 5). </p><p>Aetna (1805 Jan 17 - 1805 May 4). </p><p>Aetna (1805 Sept 19 - 1806 July 22). </p><p>Argo (1801 Sept 16 - 1804 Oct 27). </p><p>Atalante (1803 Jan 14 - 1803 Dec 31). </p><p>Atalante (1804 Jan 19 - 1805 Aug 21)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1806",
                "id": "C2529963",
                "startDate": "01/01/1801"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Aetna (1756 Dec 16 - 1757 July 31). </p><p>Aetna (1757 Aug 12 - 1758 May 20)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1758",
                "id": "C2529961",
                "startDate": "01/01/1756"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Aetna (1691/2 Feb 22 - 1693 Nov 25). </p><p>Aetna (1695 June 8 - 1696 June 27). </p><p>Eagle (1689/90 Feb 13 - 1695 Nov 19). </p><p>Eagle (1696 Sept 23 - 1697 Dec 7). </p><p>Eagle (1697/8 Feb 2 - 1699 May 22). </p><p>Eagle (1699/1700 Mar 11 - 1700/1 Feb 20)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1701",
                "id": "C2529959",
                "startDate": "01/01/1690"
            },
            {
                "description": "<scopecontent><p>Captains' logs, including: </p><p>AETNA  (1831 Oct 27-1832 Apr 30). </p><p>AETNA  (1833 Jan 1-1833 Sept 10). </p><p>AETNA  (1833 Dec 24-1836 Sept 30)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1836",
                "id": "C4458433",
                "startDate": "01/01/1831"
            },
            {
                "description": "<scopecontent><p>Captains' logs, including: </p><p>AETNA  (1824 May 8-1824 Oct 10). </p><p>AETNA  (1827 Dec 12-1830 Dec 31)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1830",
                "id": "C4458431",
                "startDate": "01/01/1824"
            },
            {
                "description": "<scopecontent><p>Captains' logs, including: </p><p>AETNA  (1778 May 14-1778 Dec 18). </p><p>AETNA  (1779 Aug 25-1780 Jan 16). </p><p>AETNA  (1780 Dec 28-1781 Dec 5). </p><p>ARIEL  (1777 July 14-1778 Feb 3). </p><p>ARIEL  (1778 Apr 28-1778 Sept 25). </p><p>ARIEL  (1781 Sept 13-1785 Nov 24)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1785",
                "id": "C4458424",
                "startDate": "01/01/1777"
            },
            {
                "description": "<scopecontent><p>Captains' logs, including: </p><p>AETNA  (1840 Jan 1-1842 Apr 25). </p><p>AETNA  (1842 June 11-1844 Mar 11). </p><p>ANSON  (1843 June 29-1843 Dec 31). </p><p>ANSON  (1844 Jan 30-1844 Apr 24). </p><p>ASP  (1845 Apr 1-1849 Nov 23)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1849",
                "id": "C4458435",
                "startDate": "01/01/1840"
            }
        ],
        "ship_name": "Aetna"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1918",
                "id": "C1497246",
                "startDate": "01/03/1918"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/05/1915",
                "id": "C1497213",
                "startDate": "01/05/1915"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/10/1917",
                "id": "C1497241",
                "startDate": "01/10/1917"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/07/1917",
                "id": "C1497238",
                "startDate": "01/07/1917"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1915",
                "id": "C1497220",
                "startDate": "01/12/1915"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1916",
                "id": "C1497232",
                "startDate": "01/12/1916"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/07/1916",
                "id": "C1497227",
                "startDate": "01/07/1916"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "30/04/1915",
                "id": "C1497212",
                "startDate": "01/04/1915"
            },
            {
                "description": "<scopecontent><p>Africa</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1809",
                "id": "C1464689",
                "startDate": "01/01/1808"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "30/06/1917",
                "id": "C1497237",
                "startDate": "01/06/1917"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1917",
                "id": "C1497243",
                "startDate": "01/12/1917"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1915",
                "id": "C1497211",
                "startDate": "01/03/1915"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/01/1916",
                "id": "C1497221",
                "startDate": "01/01/1916"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "30/11/1915",
                "id": "C1497219",
                "startDate": "01/11/1915"
            },
            {
                "description": "<scopecontent><p>AFRICA</p></scopecontent>",
                "digitised": False,
                "endDate": "31/01/1917",
                "id": "C1497233",
                "startDate": "01/01/1917"
            }
        ],
        "ship_name": "Africa"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1850",
                "id": "C2626188",
                "startDate": "01/01/1843"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "22/04/1913",
                "id": "C1481260",
                "startDate": "19/01/1913"
            },
            {
                "description": "<scopecontent><p>Albion</p></scopecontent>",
                "digitised": False,
                "endDate": "31/05/1851",
                "id": "C1464873",
                "startDate": "01/12/1850"
            },
            {
                "description": "<scopecontent><p>Albion</p></scopecontent>",
                "digitised": False,
                "endDate": "30/11/1850",
                "id": "C1464872",
                "startDate": "01/06/1850"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "16/06/1902",
                "id": "C1476726",
                "startDate": "25/06/1901"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "31/07/1917",
                "id": "C1497591",
                "startDate": "01/07/1917"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "31/08/1918",
                "id": "C1497604",
                "startDate": "01/08/1918"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "30/06/1918",
                "id": "C1497602",
                "startDate": "01/06/1918"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1916",
                "id": "C1497584",
                "startDate": "01/12/1916"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1917",
                "id": "C1497596",
                "startDate": "01/12/1917"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "17/05/1916",
                "id": "C1497579",
                "startDate": "01/05/1916"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1916",
                "id": "C1497577",
                "startDate": "01/03/1916"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "31/01/1916",
                "id": "C1497575",
                "startDate": "01/01/1916"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "30/11/1915",
                "id": "C1497573",
                "startDate": "01/11/1915"
            },
            {
                "description": "<scopecontent><p>ALBION</p></scopecontent>",
                "digitised": False,
                "endDate": "30/11/1916",
                "id": "C1497583",
                "startDate": "01/11/1916"
            }
        ],
        "ship_name": "Albion"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>Alceste</p></scopecontent>",
                "digitised": False,
                "endDate": "24/09/1815",
                "id": "C6224068",
                "startDate": "01/06/1814"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Alceste (1799 Nov 3 - 1800 Feb 26). </p><p>Alceste (1801 Aug 8 - 1802 Apr 15). </p><p>Alexandria (1801 Sept 12 - 1802 Apr 30)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1802",
                "id": "C2530063",
                "startDate": "01/01/1799"
            },
            {
                "description": "<scopecontent><p>Captains' logs, including: </p><p>ALCESTE  (1807 Apr 3-1808 Apr 30). </p><p>ALCESTE  (1809 May 1-1811 June 7). </p><p>ALCESTE  (1811 July 6-1812 June 6). </p><p>ALCESTE  (1812 July 2-1812 Aug 23). </p><p>ALCESTE  (1814 June 1-1817 Feb 18)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1817",
                "id": "C4458577",
                "startDate": "01/01/1807"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Albion (1813 Mar 18 - 1814 Jan 30). </p><p>Alceste (1809 Feb 19 - 1810 Nov 5). </p><p>Alceste (1811 Mar 3 - 1812 Sept 30). </p><p>Alceste (1815 May 31 - 1815 Dec 12). </p><p>Alert (1808 Mar 26 - 1810 Mar 13). </p><p>Alert (1815 Aug 25 - 1815 Oct 20)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1815",
                "id": "C2530052",
                "startDate": "01/01/1808"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Achille (1806 Jan 20 - 1808 Nov 30). </p><p>Acorn (1808 Apr 9 - 1808 Oct 8). </p><p>Alceste (1808 Apr 6 - 1808 Oct 6). </p><p>Arrow (1807 Apr 27 - 1807 Oct 26). </p><p>Assistance (1805 Oct 1 - 1806 Sept 30). </p><p>Audacious (1806 Nov 1 - 1808 Mar 28)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1808",
                "id": "C2529872",
                "startDate": "01/01/1805"
            },
            {
                "description": "<scopecontent><p>Captains' logs, including: </p><p>ALBION  (1770 Sept 21-1771 Sept 30). </p><p>ALBION  (1793 Oct 27-1794 Mar 9). </p><p>ALBION  (1794 Mar 24-1795 Mar 19). </p><p>ALCESTE  (1801 July 31-1802 Apr 15). </p><p>ALCIDE  (1793 Sept 9-1794 Dec 7). </p><p>ALCMENE  (1797 Nov 13-1799 Mar 7). </p><p>ALCMENE  (1808 Jan 1-1808 Aug 10). </p><p>ALERT  (1806 Aug 1-1807 July 31). </p><p>ALEXANDER  (1818 Nov 8-1818 Dec 17). </p><p>ALEXANDRIA  (1806 Mar 1-1807 Feb 28)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1818",
                "id": "C4458557",
                "startDate": "01/01/1770"
            },
            {
                "description": "<scopecontent><p>Captains' logs, including: </p><p>ACHILLE  (1799 Feb 27-1800 Feb 26). </p><p>AGINCOURT  (1799 Feb 5-1800 May 22). </p><p>ALCESTE  (1799 July 11-1800 Jan 27). </p><p>BARFLEUR  (1799 June 14-1799 Aug 21). </p><p>CENTAUR  (1799 Apr 1-1800 Mar 31). </p><p>DROMEDARY  (1799 Apr 21-1799 May 5). </p><p>DRUID  (1799 Mar 4-1800 Mar 3). </p><p>EXPEDITION  (1798 June 4-1800 Jan 18). </p><p>NAIADE  (1799 Mar 25-1799 Dec 11). </p><p>ROYAL OAK  (1799 Jan 8-1800 Jan 7). </p><p>STORK  (1799 July 1-1799 Dec 12). </p><p>VOLAGE  (1799 May 1-1799 Aug 3)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1800",
                "id": "C4458320",
                "startDate": "01/01/1798"
            }
        ],
        "ship_name": "Alceste"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Amphion (1810 Oct 4 - 1811 Jan 16). </p><p>Amphion (1813 July 3 - 1814 Dec 31). </p><p>Anaconda (1813 Nov 27 - 1815 Apr 22). </p><p>Anholt (1814 June 23 - 1814 Oct 11). </p><p>Antelope (1808 Dec 10 - 1811 Nov 8)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1815",
                "id": "C2530166",
                "startDate": "01/01/1808"
            },
            {
                "description": "<scopecontent><p>Captains' logs, including: </p><p>ALARM  (1811 Feb 13-1811 Oct 13). </p><p>AMBOYNA  (1796 Nov 20-1799 Aug 9). </p><p>AMSTERDAM  (1809 Sept 4-1811 Jan 26). </p><p>ANACONDA  (1813 Nov 20-1815 Apr 21). </p><p>ANN (Yacht)  (1809 Apr 26-1811 Apr 24). </p><p>ANN (Yacht)  (1812 Sept 9-1812 Nov 7). </p><p>ANN (Yacht)  (1812 Nov 23-1812 Dec 29). </p><p>ANN (Yacht)  (1813 Feb 1-1813 Mar 25). </p><p>APOLLO  (1821 Dec 28-1823 May 22)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1823",
                "id": "C4458527",
                "startDate": "01/01/1796"
            }
        ],
        "ship_name": "Anaconda"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "16/04/1879",
                "id": "C1465375",
                "startDate": "09/04/1878"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "05/04/1882",
                "id": "C1465378",
                "startDate": "02/04/1881"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "15/12/1871",
                "id": "C1465367",
                "startDate": "01/01/1871"
            },
            {
                "description": "<scopecontent><p>ASIA</p></scopecontent>",
                "digitised": False,
                "endDate": "27/02/1888",
                "id": "C1476871",
                "startDate": "16/03/1886"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "20/02/1850",
                "id": "C1465356",
                "startDate": "23/08/1849"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "22/08/1849",
                "id": "C1465355",
                "startDate": "22/02/1849"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "07/03/1839",
                "id": "C1465350",
                "startDate": "23/03/1836"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1862",
                "id": "C1465361",
                "startDate": "18/04/1861"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "24/05/1851",
                "id": "C1465359",
                "startDate": "20/02/1851"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "19/02/1851",
                "id": "C1465358",
                "startDate": "22/08/1850"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "23/02/1848",
                "id": "C1465352",
                "startDate": "26/08/1847"
            },
            {
                "description": "<scopecontent><p>ASIA</p></scopecontent>",
                "digitised": False,
                "endDate": "28/10/1891",
                "id": "C1476874",
                "startDate": "11/09/1890"
            },
            {
                "description": "<scopecontent><p>ASIA</p></scopecontent>",
                "digitised": False,
                "endDate": "10/09/1890",
                "id": "C1476873",
                "startDate": "01/10/1888"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "12/12/1872",
                "id": "C1465368",
                "startDate": "16/12/1871"
            },
            {
                "description": "<scopecontent><p>Asia</p></scopecontent>",
                "digitised": False,
                "endDate": "05/02/1830",
                "id": "C1465347",
                "startDate": "09/10/1826"
            }
        ],
        "ship_name": "Asia"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "05/04/1849",
                "id": "C2626203",
                "startDate": "13/06/1842"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "31/07/1914",
                "id": "C1498928",
                "startDate": "01/06/1914"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "30/09/1915",
                "id": "C1498935",
                "startDate": "01/08/1915"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1915",
                "id": "C1498932",
                "startDate": "01/02/1915"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1914",
                "id": "C1498926",
                "startDate": "01/02/1914"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "31/01/1914",
                "id": "C1498925",
                "startDate": "01/12/1913"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1916",
                "id": "C1498938",
                "startDate": "01/02/1916"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "31/03/1918",
                "id": "C1498946",
                "startDate": "01/02/1918"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "31/05/1914",
                "id": "C1498927",
                "startDate": "01/04/1914"
            },
            {
                "description": "<scopecontent><p>AVON</p></scopecontent>",
                "digitised": False,
                "endDate": "06/12/1889",
                "id": "C1476932",
                "startDate": "01/06/1889"
            },
            {
                "description": "<scopecontent><p>Avon</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1851",
                "id": "C1465491",
                "startDate": "15/11/1851"
            },
            {
                "description": "<scopecontent><p>Avon</p></scopecontent>",
                "digitised": False,
                "endDate": "07/06/1855",
                "id": "C1465498",
                "startDate": "07/01/1855"
            },
            {
                "description": "<scopecontent><p>Avon</p></scopecontent>",
                "digitised": False,
                "endDate": "05/04/1849",
                "id": "C1465488",
                "startDate": "07/01/1849"
            },
            {
                "description": "<scopecontent><p>Avon</p></scopecontent>",
                "digitised": False,
                "endDate": "14/08/1848",
                "id": "C1465486",
                "startDate": "11/04/1848"
            },
            {
                "description": "<scopecontent><p>Avon</p></scopecontent>",
                "digitised": False,
                "endDate": "06/01/1849",
                "id": "C1465487",
                "startDate": "15/08/1848"
            }
        ],
        "ship_name": "Avon"
    },
    {
        "records": [
            {
                "description": "<scopecontent><p>W. Bedford</p></scopecontent>",
                "digitised": False,
                "endDate": "13/05/1814",
                "id": "C6320274",
                "startDate": "02/04/1813"
            },
            {
                "description": "<scopecontent><p>BEDFORD</p></scopecontent>",
                "digitised": False,
                "endDate": "25/03/1909",
                "id": "C1482076",
                "startDate": "01/10/1908"
            },
            {
                "description": "<scopecontent><p>BEDFORD</p></scopecontent>",
                "digitised": False,
                "endDate": "30/09/1908",
                "id": "C1482075",
                "startDate": "05/08/1907"
            },
            {
                "description": "<scopecontent><p>BEDFORD</p></scopecontent>",
                "digitised": False,
                "endDate": "31/08/1910",
                "id": "C1482078",
                "startDate": "17/03/1910"
            },
            {
                "description": "<scopecontent><p>BEDFORD</p></scopecontent>",
                "digitised": False,
                "endDate": "16/03/1910",
                "id": "C1482077",
                "startDate": "25/03/1909"
            },
            {
                "description": "<scopecontent><p>BEDFORD</p></scopecontent>",
                "digitised": False,
                "endDate": "04/08/1907",
                "id": "C1482074",
                "startDate": "27/03/1906"
            },
            {
                "description": "<scopecontent><p>BEDFORD</p></scopecontent>",
                "digitised": False,
                "endDate": "29/11/1905",
                "id": "C1482072",
                "startDate": "08/12/1904"
            },
            {
                "description": "<scopecontent><p>BEDFORD</p></scopecontent>",
                "digitised": False,
                "endDate": "26/03/1906",
                "id": "C1482073",
                "startDate": "30/11/1905"
            },
            {
                "description": "<scopecontent><p>BEDFORD</p></scopecontent>",
                "digitised": False,
                "endDate": "07/12/1904",
                "id": "C1482071",
                "startDate": "11/11/1903"
            },
            {
                "description": "<scopecontent><p>Master's log(s): Bedford </p></scopecontent>",
                "digitised": False,
                "endDate": "17/07/1783",
                "id": "C2530408",
                "startDate": "30/08/1780"
            },
            {
                "description": "<scopecontent><p>Master's log(s): Bedford </p></scopecontent>",
                "digitised": False,
                "endDate": "29/08/1780",
                "id": "C2530407",
                "startDate": "30/08/1778"
            },
            {
                "description": "<scopecontent><p>Master's log(s): Bedford </p></scopecontent>",
                "digitised": False,
                "endDate": "05/03/1728",
                "id": "C2530404",
                "startDate": "07/05/1723"
            },
            {
                "description": "<scopecontent><p>Master's log(s): Bedford </p></scopecontent>",
                "digitised": False,
                "endDate": "05/07/1815",
                "id": "C2530416",
                "startDate": "04/11/1807"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Bedford (1757 Mar 1 - 1761 Sept 26). </p><p>Bedford (1762 July 2 - 1762 Dec 20)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1762",
                "id": "C2530406",
                "startDate": "01/01/1757"
            },
            {
                "description": "<scopecontent><p>Masters' logs, including: </p><p>Bedford (1699 May 5 - 1699 Aug 26). </p><p>Bedford (1700/1 Mar 6 - 1702 July 17). </p><p>Bedford (Galley) (1697 June 28 - 1699/1700 Jan 12). </p><p>Bideford (1695 Oct 25 - 1698 Nov 4). </p><p>Bristow (1692 Apr 15 - 1692 Oct 10). </p><p>Bristow (1693/4 Mar 19 - 1696 Sept 2). </p><p>Bristow (1697 May 9 - 1797 Oct 11)</p></scopecontent>",
                "digitised": False,
                "endDate": "31/12/1797",
                "id": "C2530402",
                "startDate": "01/01/1692"
            }
        ],
        "ship_name": "Bedford"
    }
]