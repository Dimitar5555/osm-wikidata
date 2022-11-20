import re

from . import model

countries = {
    16: ["Canada", "Canadian", "Kanada", "canada"],
    17: ["Japan", "Japanese", "Japon", "japon"],
    20: [
        "Kingdom of Norway",
        "Norsk",
        "Noruega",
        "Norvegian",
        "Norway",
        "Norwegian",
        "Reino de Noruega",
        "norsk",
    ],
    27: [
        "Ireland",
        "Irish",
        "Irland",
        "Irlanda",
        "Republic of Ireland",
        "Republik Irland",
        "République d'Irlande",
        "the Republic of Ireland",
    ],
    28: ["Hongarije", "Hungarian", "Hungary", "Ungheria"],
    29: [
        "España",
        "Español",
        "Kingdom of Spain",
        "Royaume d'Espagne",
        "Spain",
        "Spanien",
        "Spanish",
        "Кралство Испания",
    ],
    30: [
        "ASV",
        "American",
        "Americana",
        "Amerika",
        "Amérique",
        "EUA",
        "Estados Unidos",
        "Etats-Unis",
        "States",
        "The United States",
        "U.S",
        "US",
        "USA",
        "United States",
        "United States Of America",
        "United States of America",
        "estados unidos",
        "the US",
        "the United States",
        "u.s.",
        "États-Unis d'Amérique",
        "США",
        "الولايات المتحدة",
    ],
    31: [
        "Belgian",
        "Belgica",
        "Belgie",
        "Belgien",
        "Belgique",
        "Belgische",
        "Belgium",
        "Bélgica",
        "Kingdom of Belgium",
        "Reino de Bélgica",
    ],
    32: [
        "Gran Ducado de Luxemburgo",
        "Gran Ducat de Luxemburg",
        "Grand Duchy of Luxembourg",
        "Grand-Duché",
        "Großherzogtum Luxemburg",
        "Luxembourg",
        "Luxemburg",
        "Luxemburgo",
    ],
    33: [
        "Finland",
        "Finlande",
        "Finlandia",
        "Finn",
        "Finnish",
        "Finnland",
        "Republic of Finland",
        "Republik Finnland",
        "República de Finlandia",
    ],
    34: [
        "Kingdom of Sweden",
        "Reino de Suecia",
        "Svedese",
        "Svensk",
        "Sverige",
        "Sweden",
        "Swedish",
    ],
    35: [
        "Danimarca",
        "Danish",
        "Danmark",
        "Dansk",
        "Danske",
        "Denmark",
        "Dinamarca",
        "Kingdom of Denmark",
        "Reino de Dinamarca",
        "dansk",
    ],
    36: [
        "Poland",
        "Polen",
        "Polish",
        "Polonia",
        "Republic Of Poland",
        "Republic of Poland",
        "Republica de Polonia",
        "República da Polônia",
        "República de Polonia",
        "República de Polònia",
    ],
    37: [
        "Lithuania",
        "Lithuanian",
        "Lituania",
        "Republic of Lithuania",
        "República de Lituania",
    ],
    38: [
        "Italia",
        "Italian",
        "Italian Republic",
        "Italiana",
        "Italiane",
        "Italiano",
        "Italie",
        "Italy",
        "Repubblica Italiana",
        "República Italiana",
        "italian",
        "italiano",
        "italie",
    ],
    39: [
        "Confédération Suisse",
        "Eidgenossenschaft",
        "Schweizer",
        "Suisse",
        "Swiss",
        "Switzerland",
    ],
    40: [
        "Austria",
        "Austriaco",
        "Austrian",
        "Osztrák",
        "Republic of Austria",
        "Republik Österreich",
        "República de Austria",
        "Österreich",
    ],
    41: ["Grec", "Greece", "Greek", "Hellenic Republic", "República Helénica"],
    43: [
        "Republic of Turkey",
        "República da Turquia",
        "República de Turquía",
        "Turc",
        "Turco",
        "Turk",
        "Turkey",
        "Turkish",
        "Turquia",
        "Türk",
        "Türkiye Cumhuriyeti",
        "turkey",
    ],
    45: [
        "PORTUGUESA",
        "Portugal",
        "Portuguese",
        "Portuguese Republic",
        "República Portuguesa",
    ],
    55: [
        "Dutch",
        "Holanda",
        "Hollanda",
        "Nederland",
        "Netherlands",
        "The Netherlands",
        "los Paises Bajos",
        "los Países Bajos",
        "the Netherlands",
    ],
    77: ["República Oriental del Uruguay", "Uruguay", "Uruguayan"],
    79: [
        "Arab Republic of Egypt",
        "EGYPTE",
        "Egipto",
        "Egypt",
        "Egypte",
        "Egyptian",
        "Repubblica Araba d'Egitto",
        "Republic of Egypt",
        "egypt",
        "Арабска република Египет",
        "جمهورية مصر العربية",
    ],
    96: ["MEXICO", "Mexican", "Mexico", "México", "United Mexican States", "mexicano"],
    114: ["Kenia", "Kenya", "Kenyan", "Republic of Kenya", "Republik Kenia"],
    115: [
        "Ethiopia",
        "Ethiopian",
        "Ethiopie",
        "Etiopia",
        "Federal Democratic Republic of Ethiopia",
    ],
    117: ["Ghana", "Ghanaian", "Republic of Ghana"],
    142: [
        "FRANCE",
        "FRANCIA",
        "France",
        "Francese",
        "Francia",
        "Frankreich",
        "Frankrijk",
        "França",
        "Français",
        "French",
        "Republic of France",
        "Republique Francaise",
        "República Francesa",
        "fra",
        "france",
        "francese",
        "française",
        "la France",
    ],
    145: [
        "Brit",
        "Britain",
        "British",
        "Brittiska",
        "Great Britain",
        "Großbritannien",
        "UK",
        "United Kingdom",
        "Велика Британија",
    ],
    148: [
        "China",
        "Chine",
        "Chine Populaire",
        "Chinese",
        "Chino",
        "Cinese",
        "Kínai",
        "PRC",
        "People's Republic of China",
        "VR China",
        "china",
        "chinese",
        "КНР",
        "الصين",
    ],
    155: [
        "Brasil",
        "Brasileira",
        "Brazil",
        "Brazilian",
        "Federative Republic of Brazil",
        "República Federativa de Brasil",
        "República Federativa del Brasil",
    ],
    159: [
        "Federación Rusa",
        "Federazione Russa",
        "Rus",
        "Rusia",
        "Russe",
        "Russia",
        "Russian",
        "Russian Federation",
        "Russian federation",
        "Russische Föderation",
        "Russo",
        "russia",
        "Руски",
    ],
    183: [
        "Bondsrepubliek Duitsland",
        "Bundesrepublik Deutschland",
        "Deutsche",
        "Deutschland",
        "Federal Republic of Germany",
        "German",
        "Germany",
        "República Federal da Alemanha",
        "República Federal de Alemania",
        "République fédérale d'Allemagne",
        "Германия",
        "ФРГ",
    ],
    184: [
        "Belarus",
        "Belarusian",
        "Bélarus",
        "Republic of Belarus",
        "Weißrußland",
        "Беларусь",
        "Република Беларус",
    ],
    189: ["Iceland", "Island", "Republic of Iceland"],
    191: [
        "Estland",
        "Estonia",
        "Estonian",
        "Republic of Estonia",
        "Republik Estland",
        "República de Estonia",
        "République d’Estonie",
    ],
    211: [
        "Latvia",
        "Latvian",
        "Letonia",
        "Lettland",
        "Republic of Latvia",
        "republic of Latvia",
    ],
    212: ["UCRAINA", "Ucraina", "Ukraine", "Ukrainian", "the Ukraine"],
    213: ["CZECH REPUBLIC", "Ceca", "Czech", "Czech Republic", "República Checa"],
    214: ["República Eslovaca", "République Slovaque", "Slovak", "Slovakia"],
    215: ["Republic of Slovenia", "Republik Slowenien", "Slovenia", "Slovenian"],
    217: [
        "Moldavia",
        "Moldavie",
        "Moldova",
        "Republic of Moldova",
        "Republica Moldova",
        "Republik Moldau",
        "Молдова",
    ],
    218: ["Romania", "Romanian", "Romenia", "Rumania", "Rumanía"],
    219: [
        "Bulgaria",
        "Bulgarian",
        "Bulgarie",
        "Bulgarien",
        "Republic of Bulgaria",
        "República de Bulgaria",
        "България",
    ],
    221: [
        "Macedonia",
        "Macedonian",
        "Macédoine",
        "Makedonien",
        "Republic of Macedonia",
        "The former Yugoslav Republic of Macedonia",
        "the former Yugoslav Republic of Macedonia",
    ],
    222: [
        "Albania",
        "Albanian",
        "Albanie",
        "Republic of Albania",
        "Republik Albanien",
        "Shqipërisë",
        "Албанія",
    ],
    224: ["Croacia", "Croatia", "Croatian", "Republic of Croatia", "Republik Kroatien"],
    225: ["Bosnia", "Bosnia and Herzegovina"],
    227: ["Azerbaijan", "Republic of Azerbaijan"],
    228: ["Principality of Andorra"],
    229: ["Cypriot", "Cyprus", "Republic of Cyprus", "Zypern"],
    230: ["Georgia", "Georgian"],
    232: [
        "Kazakhstan",
        "Kazakstan",
        "REPUBLIC OF KAZAKHSTAN",
        "Republic of Kazakhstan",
        "República de Kazajistán",
    ],
    233: ["Malta", "Máltai", "Republic of Malta", "República de Malta"],
    235: [
        "Monaco",
        "Principado de Mónaco",
        "Principality of Monaco",
        "Principauté de Monaco",
    ],
    236: ["Montenegro"],
    237: [
        "Estado de la Ciudad del Vaticano",
        "Vatican",
        "Vatican City",
        "Vatikan",
        "the Vatican",
    ],
    238: ["République de Saint-Marin", "San Marino"],
    241: [
        "CUBA",
        "Cuba",
        "Cuban",
        "Kuba",
        "Republic of Cuba",
        "Republica de Cuba",
        "República de Cuba",
    ],
    242: ["Belize"],
    244: ["Barbadian", "Barbados"],
    252: [
        "INDONESIAN",
        "Indonesia",
        "Indonesian",
        "Indonéz",
        "Republic Of Indonesia",
        "Republic of Indonesia",
        "Republik Indonesia",
        "República de Indonesia",
    ],
    258: [
        "RSA",
        "Republic of South Africa",
        "República de Sudáfrica",
        "South Africa",
        "South African",
        "Sudafrica",
        "south african",
        "ЮАР",
    ],
    262: ["Algeria", "Algerian", "Algériai", "People’s Democratic Republic of Algeria"],
    265: [
        "Repubblica dell'Uzbekistan",
        "Republic of Uzbekistan",
        "Uzbekistan",
        "Uzbekistani",
    ],
    298: [
        "Chile",
        "Chilean",
        "Chilei",
        "Republic of Chile",
        "Republik Chile",
        "República de Chile",
    ],
    334: ["Republic of Singapore", "Singapore", "Singaporean"],
    347: ["Liechtenstein", "Principality of Liechtenstein"],
    398: [
        "Bahrain",
        "Bahraini",
        "Bahrein",
        "Kingdom of Bahrain",
        "kingdom of Bahrain",
        "مملكة البحرين",
    ],
    399: ["Armenia", "Armenian", "Republic of Armenia"],
    403: ["Republic of Serbia", "República de Serbia", "Serbia", "Serbian"],
    408: ["Australia", "Australian", "Australie", "Commonwealth of Australia"],
    414: [
        "Argentina",
        "Argentine",
        "Argentine Republic",
        "Argentinian",
        "Argentino",
        "República Argentina",
        "argentina",
    ],
    419: ["Peru", "Peruvian", "Republic of Peru", "República del Perú"],
    423: [
        "Democratic People's Republic of Korea",
        "North Korea",
        "República Popular Democrática de Corea",
        "КНДР",
        "공화국",
    ],
    424: ["Cambodia", "Cambodian", "Kingdom of Cambodia", "cambodia"],
    458: ["EU", "European Union", "Union Europea"],
    574: [
        "Democratic Republic of Timor-Leste",
        "East Timor",
        "Timor Leste",
        "Timor-Leste",
    ],
    657: ["Chad", "Chadian", "Republic of Chad", "Tchad", "Tschad"],
    664: ["New Zealand"],
    668: ["India", "Indiai", "Indian", "Indien", "Republic of India", "İndian"],
    672: ["Tuvalu"],
    678: ["Kingdom of Tonga", "Tonga"],
    683: ["Independent State of Samoa", "Samoa"],
    685: ["Solomon Islands"],
    686: ["Republic of Vanuatu"],
    691: [
        "Independent State of Papua New Guinea",
        "Papua New Guinea",
        "Papua New Guinean",
        "Papua New guinea",
    ],
    695: ["Republic of Palau"],
    697: ["Republic of Nauru"],
    702: ["Federated States of Micronesia"],
    709: ["Marshall Islands", "Republic of the Marshall Islands"],
    710: ["Republic of Kiribati"],
    711: ["Mongolia", "Mongolian"],
    712: ["Fiji", "Republic of Fiji"],
    717: [
        "Bolivarian Republic of Venezuela",
        "Venezuela",
        "Venezuelan",
        "Vénézuela",
        "Vénézuéla",
        "la República Bolivariana de Venezuela",
    ],
    730: ["Republic of Suriname", "Suriname"],
    733: ["Paraguay", "Republic of Paraguay", "República del Paraguay"],
    734: [
        "Co-operative Republic of Guyana",
        "Guiana",
        "Guyana",
        "Guyanese",
        "Republic of Guyana",
        "republic of Guyana",
    ],
    736: [
        "Ecuador",
        "Ecuadorian",
        "Republic of Ecuador",
        "Republik Ecuador",
        "República del Ecuador",
        "l'Equador",
    ],
    739: [
        "COLOMBIA",
        "Colombia",
        "Colombian",
        "Colombiano",
        "Republic of Colombia",
        "Republica de Colombia",
        "República de Colombia",
    ],
    750: [
        "Bolivia",
        "Bolivian",
        "Estado Plurinacional de Bolivia",
        "Plurinational State of Bolivia",
    ],
    754: [
        "Republic of Trinidad and Tobago",
        "República de Trinidad y Tobago",
        "Trinidad and Tobago",
    ],
    757: ["Saint Vincent", "Saint Vincent and the Grenadines", "St. Vincent"],
    760: ["Saint Lucia"],
    763: ["Saint Kitts and Nevis"],
    766: ["Jamaica", "Jamaican"],
    769: ["Grenada"],
    774: ["Guatemala", "Guatemalan", "Republik Guatemala", "República de Guatemala"],
    778: ["Bahamas", "Bahamian", "Commonwealth of the Bahamas", "the Bahamas"],
    781: ["Antigua and Barbuda"],
    783: ["Honduran", "Honduras", "Republic of Honduras", "República de Honduras"],
    784: ["the Commonwealth of Dominica"],
    786: ["Dominican Republic", "Dominicana", "República Dominicana"],
    790: ["Haiti", "Haitian", "Haïti", "República de Haití", "République d'Haïti"],
    792: [
        "El Salvador",
        "Republic of El Salvador",
        "República de El Salvador",
        "Salvador",
        "Salvadoran",
        "Эль-Сальвадор",
    ],
    794: [
        "Iran",
        "Iranian",
        "Islamic Republic Of Iran",
        "Islamic Republic of Iran",
        "Republic of Iran",
        "República Islámica de Irán",
        "République Islamique d'Iran",
        "iran",
        "İran",
        "الجمهورية الاسلامية الايرانية",
    ],
    796: [
        "Irak",
        "Iraq",
        "Iraqi",
        "Republic Of Iraq",
        "Republic of Iraq",
        "República de Irak",
        "iraq",
        "İraq",
        "العراق",
    ],
    800: ["Costa Rica", "Costa Rican", "Republic of Costa Rica", "Republik Costa Rica"],
    801: ["Israel", "Israeli", "Israelin", "State of Israel"],
    804: [
        "Panama",
        "Panamanian",
        "Panamá",
        "Republic of Panama",
        "República de Panamá",
    ],
    805: ["Jemeni", "Republic of Yemen", "Yemen", "الجمهورية اليمنية"],
    810: ["Hashemite Kingdom of Jordan", "Jordan", "Jordanian", "jordan"],
    811: ["Nicaragua", "Nicaraguan", "República de Nicaragua"],
    813: ["Kyrgyz", "Kyrgyzstan"],
    817: [
        "KUWAIT",
        "Koweit",
        "Kuwait",
        "Kuweit",
        "State of Kuwait",
        "state of Kuwait",
        "دولة الكويت",
        "کویت",
    ],
    819: ["Lao", "Lao People's Democratic Republic", "Laos"],
    822: ["Lebanese", "Lebanese Republic", "Lebanon", "Libano", "Republic of Lebanon"],
    826: ["Maldives", "Republic of Maldives"],
    833: ["Malasia", "Malaysia", "Malaysian"],
    836: [
        "Myanmar",
        "Republic Of The Union Of Myanmar",
        "Republic of the Union of Myanmar",
        "Union von Myanmar",
        "republic of the union of Myanmar",
    ],
    837: [
        "Federal Democratic Republic of Nepal",
        "NEPAL",
        "Nepal",
        "República Federal Democrática de Nepal",
    ],
    842: ["Oman", "Ománi Szultánság", "Sultanat d'Oman", "Sultanate of Oman"],
    843: [
        "Islamic Republic of Pakistan",
        "PAKISTAN",
        "Pakistan",
        "république islamique du Pakistan",
    ],
    846: [
        "Estado de Catar",
        "Katar",
        "Qatar",
        "Qatari",
        "State Of Qatar",
        "State of Qatar",
        "دولة قطر",
    ],
    851: [
        "Arabia Saudí",
        "Arabie Saoudite",
        "Saudi",
        "Saudi Arabia",
        "Saudita",
        "Saudite",
        "saudi",
        "the Kingdom of Saudi Arabia",
        "السعوديه",
        "المملكة",
        "المملكة العربية",
        "سعودي",
    ],
    854: ["Democratic Socialist Republic of Sri Lanka", "Sri Lanka", "Sri Lankan"],
    858: ["Syria", "Syrian", "Syrie"],
    863: ["Republic of Tajikistan", "Tajikistan"],
    865: [
        "Republic of China",
        "Taiwan",
        "Taiwanese",
        "republic of china",
        "جمهورية الصين",
        "Taipei",
    ],
    869: [
        "Kingdom of Thailand",
        "Reino de Tailandia",
        "Tailandia",
        "Thai",
        "Thaiföldi Királyság",
        "Thailand",
        "Thailandese",
        "thailand",
    ],
    874: ["Turkmen", "Turkmenistan"],
    878: [
        "Emirates",
        "Emirati",
        "Emiratos Árabes Unidos",
        "Förenade Arabemiraten",
        "The United Arab Emirates",
        "UAE",
        "United Arab Emirates",
        "the UAE",
        "the United Arab Emirates",
        "ОАЭ",
        "دولة الإمارات العربية المتحدة",
    ],
    881: ["Socialist Republic of Vietnam", "Viet", "Vietnam", "Vietnamese", "Việt Nam"],
    884: [
        "Korea Republic",
        "Koreai Köztársaság",
        "ROK",
        "Rep. Korea",
        "Republic Of Korea",
        "Republic of Korea",
        "Republica de Corea",
        "Republik Korea",
        "República de Corea",
        "South Korea",
        "South Korean",
        "republic of Korea",
        "republic of korea",
    ],
    889: [
        "Afghan",
        "Afghanistan",
        "Islamic Republic of Afghanistan",
        "República Islámica de Afganistán",
        "islamic republic of Afghanistan",
        "Афганістан",
    ],
    902: ["Bangladesh", "Bangladeshi"],
    912: ["Mali", "Malian", "Republic of Mali", "mali"],
    916: ["Angola", "Angolai", "Republic of Angola", "Republic of angola"],
    917: ["Bhutan", "Kingdom of Bhutan", "Königreich Bhutan"],
    921: ["Brunei", "Nation of Brunei, the Abode of Peace"],
    924: [
        "Tansania",
        "Tanzania",
        "Tanzanian",
        "United Republic Of Tanzania",
        "United Republic of Tanzania",
    ],
    928: [
        "Filipina",
        "Fülöp-szigeteki",
        "Philippine",
        "Philippines",
        "Republic of the Philippines",
        "República de Filipinas",
        "The Philippines",
        "philippine",
        "the Philippines",
    ],
    929: ["Centrafrique", "Central African Republic", "République Centrafricaine"],
    945: ["République Togolaise", "Togo", "Togolese"],
    948: ["Republic of Tunisia", "Tunisia", "Tunisian", "Tunisie"],
    953: ["Republic of Zambia", "Zambia", "republic of Zambia"],
    954: ["Republic of Zimbabwe", "Simbabwe", "Zimbabwe", "Zimbabwé"],
    958: ["Republic of South Sudan", "South Sudan", "Southern Sudan"],
    962: ["Benin", "Bénin", "Republic of Benin", "la République du Bénin"],
    963: ["Botswana", "Republic of Botswana"],
    965: ["Burkina Faso"],
    967: ["Burundi", "Republic of Burundi"],
    970: ["Comores", "Comoros", "Union of the Comoros"],
    971: [
        "Congo Brazzaville",
        "Congo-Brazzaville",
        "Kongo-Brazzaville",
        "Republic of Congo",
        "Republic of the Congo",
        "République du Congo",
        "republic of Congo",
    ],
    974: [
        "DRC",
        "Democratic Republic Of Congo",
        "Democratic Republic of Congo",
        "Democratic Republic of the Congo",
        "République Démocratique du Congo",
        "République démocratique du Congo",
        "Zaire",
        "république démocratique du Congo",
        "الكونغو",
    ],
    977: ["Djibouti", "Republic of Djibouti"],
    983: [
        "Equatorial Guinea",
        "Republic of Equatorial Guinea",
        "República de Guinea Ecuatorial",
    ],
    986: ["Eritrea", "Eritrean"],
    1000: ["Gabon", "Gabonese Republic"],
    1005: ["Gambia", "Gambian", "Republic of The Gambia", "The Gambia", "the Gambia"],
    1006: ["Guinea", "Guinean", "Republic of Guinea", "República de Guinea", "guinea"],
    1007: ["Guinée Bissau"],
    1008: [
        "Cote d'Ivoire",
        "Côte d'Ivoire",
        "Côte d’Ivoire",
        "Ivory Coast",
        "Republic of Côte d'Ivoire",
        "République de Côte d'Ivoire",
        "République de côte d'ivoire",
    ],
    1009: ["Cameroon", "Cameroun", "Republic of Cameroon", "República de Camerún"],
    1011: ["Cabo Verde", "Cape Verde", "Republic of Cape Verde", "Republik Kap Verde"],
    1013: ["Kingdom of Lesotho", "Lesotho"],
    1014: ["Liberia", "Liberian", "Libéria", "Republic of Liberia"],
    1016: ["Libya", "Libyan", "Libyen", "State of Libya", "الليبية"],
    1019: ["Madagascar", "Madagaskar", "Republic of Madagascar"],
    1020: ["Malawi", "Republic of Malawi"],
    1025: [
        "Islamic Republic of Mauritania",
        "Mauritania",
        "Mauritanie",
        "الجمهورية الإسلامية الموريتانية",
    ],
    1027: ["Maurice", "Mauritius", "Republic of Mauritius", "Île Maurice"],
    1028: [
        "Kingdom Of Morocco",
        "Kingdom of Morocco",
        "Maroc",
        "Marocco",
        "Marokkói",
        "Marruecos",
        "Moroccan",
        "Morocco",
        "Reino de Marruecos",
        "Royaume du Maroc",
        "المغرب",
    ],
    1029: ["Mozambique", "Moçambique", "Republic of Mozambique"],
    1030: [
        "Namibia",
        "Namibie",
        "Republic of Namibia",
        "Republik Namibia",
        "République de Namibie",
    ],
    1032: ["Niger", "Republic of Niger", "Republic of the Niger"],
    1033: ["Federal Republic of Nigeria", "NIGERIA", "Nigeria", "Nigerian", "Nigéria"],
    1036: ["Republic of Uganda", "Uganda"],
    1037: ["Republic of Rwanda", "Rwanda", "République Rwandaise"],
    1039: ["Democratic Republic of São Tomé and Príncipe", "Sao Tome and Principe"],
    1041: [
        "Republic of Senegal",
        "Senegal",
        "Senegalese",
        "Sénégal",
        "la République du Sénégal",
        "senegal",
    ],
    1042: ["Republic of Seychelles", "Republik Seychellen", "Seychelles"],
    1044: ["Republic of Sierra Leone", "Sierra Leone"],
    1045: ["Federal Republic of Somalia", "Somali", "Somalia", "Somalian", "Somalie"],
    1049: [
        "Republic of Sudan",
        "Republic of the Sudan",
        "Republik Sudan",
        "República de Sudán",
        "Sudan",
        "Sudanese",
        "the Sudan",
        "جمهورية السودان",
    ],
    1050: ["Kingdom of Eswatini", "Kingdom of Swaziland", "Swaziland"],
    1065: ["Nações Unidas", "ONU", "UN", "UNO", "Un", "United Nations"],
    1183: ["Puerto Rico", "puerto rico"],
    1246: ["Kosovo", "Republic of Kosovo", "Republik Kosovo"],
    4628: ["Faroe"],
    8646: ["Hong Kong"],
    9648: ["Falkland"],
    21203: ["Aruba"],
    25279: ["Curaçao"],
    26988: ["Cook Islands", "the Cook Islands"],
    35086: ["de Georgia"],
    219060: [
        "Estado de Palestina",
        "Palestina",
        "Palestine",
        "Palestinian",
        "Palästina",
        "State of Palestine",
        "palestina",
        "state of Palestine",
        "État de Palestine",
    ],
}


def from_name(name):
    """Look for an embassy by name."""
    reverse_map = {}
    for i in model.Embassy:
        for name in i.names:
            reverse_map[name] = i
            reverse_map[name.lower()] = i

    longest_first = sorted(reverse_map.keys(), key=len, reverse=True)

    name_pattern = (
        r"(?:\b|')(" + "|".join(re.escape(n) for n in longest_first) + r")s?\b"
    )
    re_name = re.compile(name_pattern, re.I)

    m = re_name.search(name)
    if not m:
        return
    lc_match = m.group(1).lower()
    return reverse_map[m] if m in reverse_map else reverse_map[lc_match]
