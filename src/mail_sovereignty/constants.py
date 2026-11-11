import re

MICROSOFT_KEYWORDS = [
    "mail.protection.outlook.com",
    "mail.protection.outlook.de",
    "mx.microsoft",
    "outlook.com",
    "outlook.de",
    "hotmail.com",
    "microsoft",
    "office365",
    "onmicrosoft",
    "spf.protection.outlook.com",
    "sharepointonline",
]
GOOGLE_KEYWORDS = [
    "google",
    "googlemail",
    "gmail",
    "_spf.google.com",
    "aspmx.l.google.com",
]
AWS_KEYWORDS = ["amazonaws", "amazonses", "awsdns"]

# Regional providers
ZONE_KEYWORDS = ["zone.eu", "zone.ee", "zoneit.eu", "zonemx.eu"]
TELIA_KEYWORDS = ["telia.ee", "telia.lt", "telia.lv", "telia.com"]
TET_KEYWORDS = ["tet.lv"]
ELKDATA_KEYWORDS = ["elkdata.ee"]
ZOHO_KEYWORDS = ["zoho.com", "zoho.eu", "zoho.in", "zohocorp.com"]
YANDEX_KEYWORDS = ["yandex.net", "yandex.ru"]

PROVIDER_KEYWORDS = {
    "microsoft": MICROSOFT_KEYWORDS,
    "google": GOOGLE_KEYWORDS,
    "aws": AWS_KEYWORDS,
    "zoho": ZOHO_KEYWORDS,
    "yandex": YANDEX_KEYWORDS,
    "zone": ZONE_KEYWORDS,
    "telia": TELIA_KEYWORDS,
    "tet": TET_KEYWORDS,
    "elkdata": ELKDATA_KEYWORDS,
}

FOREIGN_SENDER_KEYWORDS = {
    "mailchimp": ["mandrillapp.com", "mandrill", "mcsv.net"],
    "sendgrid": ["sendgrid"],
    "mailjet": ["mailjet"],
    "mailgun": ["mailgun"],
    "brevo": ["sendinblue", "brevo"],
    "mailchannels": ["mailchannels"],
    "smtp2go": ["smtp2go"],
    "nl2go": ["nl2go"],
    "hubspot": ["hubspotemail"],
    "knowbe4": ["knowbe4"],
    "hornetsecurity": ["hornetsecurity", "hornetdmarc"],
}

SPARQL_URL = "https://query.wikidata.org/sparql"
# Not used — municipalities are loaded from seed JSON files
SPARQL_QUERY = ""

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
TYPO3_RE = re.compile(r"linkTo_UnCryptMailto\(['\"]([^'\"]+)['\"]")
SKIP_DOMAINS = {
    "example.com",
    "example.ee",
    "example.lv",
    "example.lt",
    "example.no",
    "example.se",
    "example.de",
    "example.dk",
    "example.ad",
    "example.lu",
    "example.be",
    "example.at",
    "example.cz",
    "example.is",
    "example.es",
    "example.fr",
    "example.pl",
    "example.pt",
    "example.it",
    "example.nl",
    "example.ie",
    "example.bg",
    "example.sk",
    "example.si",
    "example.uk",
    "example.hr",
    "example.cy",
    "example.gr",
    "example.hu",
    "example.mt",
    "example.ro",
    "example.al",
    "example.me",
    "example.ba",
    "example.au",
    "example.com.au",
    "example.gov.au",
    "example.nz",
    "example.govt.nz",
    "example.co.nz",
    "gov.uk",
    "gov.au",
    "govt.nz",
    "go.id",
    "gov.pg",
    "gov.my",
    "go.th",
    "gov.kh",
    "gov.ph",
    "kommune.no",
    # South America
    "example.ar",
    "example.bo",
    "example.br",
    "example.cl",
    "example.co",
    "example.ec",
    "example.gy",
    "example.pe",
    "example.py",
    "example.sr",
    "example.uy",
    "example.ve",
    "gob.ar",
    "gov.br",
    "gob.cl",
    "gov.co",
    "gob.ec",
    "gob.pe",
    "gov.py",
    "gub.uy",
    "gob.ve",
    # Mexico
    "example.mx",
    "gob.mx",
    # Canada + Central America
    "example.ca",
    "gc.ca",
    "example.bz",
    "example.gt",
    "example.hn",
    "example.sv",
    "example.ni",
    "example.cr",
    "example.pa",
    "gob.gt",
    "gob.hn",
    "gob.sv",
    "gob.ni",
    "go.cr",
    "gob.pa",
    # Africa
    "example.dz",
    "example.eg",
    "example.ly",
    "example.ma",
    "example.tn",
    "example.sd",
    "example.bj",
    "example.bf",
    "example.cv",
    "example.ci",
    "example.gm",
    "example.gh",
    "example.gn",
    "example.gw",
    "example.lr",
    "example.ml",
    "example.mr",
    "example.ne",
    "example.ng",
    "example.sn",
    "example.sl",
    "example.tg",
    "example.cm",
    "example.cf",
    "example.td",
    "example.cg",
    "example.cd",
    "example.gq",
    "example.ga",
    "example.st",
    "example.bi",
    "example.km",
    "example.dj",
    "example.er",
    "example.et",
    "example.ke",
    "example.mg",
    "example.mw",
    "example.mu",
    "example.mz",
    "example.rw",
    "example.sc",
    "example.so",
    "example.ss",
    "example.tz",
    "example.ug",
    "example.ao",
    "example.bw",
    "example.sz",
    "example.ls",
    "example.na",
    "example.za",
    "example.zm",
    "example.zw",
    "gov.dz",
    "gov.eg",
    "gov.gh",
    "gov.ng",
    "gov.za",
    "gov.ke",
    "go.ke",
    "go.tz",
    "go.ug",
    "gov.et",
    "gov.mz",
    "gouv.bj",
    "gouv.ci",
    "gouv.sn",
    "gouv.ml",
    "gouv.cm",
    # Caribbean
    "example.cu",
    "example.ht",
    "example.do",
    "example.jm",
    "example.tt",
    "example.bs",
    "example.bb",
    "example.ag",
    "example.dm",
    "example.gd",
    "example.kn",
    "example.lc",
    "example.vc",
    "gob.cu",
    "gov.jm",
    "gov.tt",
    "gov.bs",
    "gov.bb",
    "gov.ag",
    "gov.dm",
    "gov.gd",
    "gov.kn",
    "gov.lc",
    "gov.vc",
    # Asia (additional)
    "example.af",
    "example.sg",
    "example.ye",
    "example.sy",
    "example.ps",
    "example.tj",
    "example.tm",
    "example.mv",
    "example.bt",
    "gov.af",
    "gov.sg",
    "gov.ye",
    "gov.sy",
    "gov.ps",
    "gov.tj",
    "gov.tm",
    "gov.mv",
    "gov.bt",
    # Oceania (additional)
    "example.sb",
    "example.mh",
    "example.fm",
    "example.ki",
    "example.tv",
    "gov.sb",
    "gov.mh",
    "gov.fm",
    "gov.ki",
    "gov.tv",
    "sentry.io",
    "w3.org",
    "gstatic.com",
    "googleapis.com",
    "schema.org",
}

SUBPAGES = [
    "/kontakt",
    "/contact",
    "/kontaktid",  # Estonian
    "/kontakti",  # Latvian
    "/kontaktai",  # Lithuanian
    "/kontakt/",
    "/contact/",
    "/meist",  # Estonian: "About us"
    "/par-mums",  # Latvian: "About us"
    "/apie-mus",  # Lithuanian: "About us"
    "/struktuur",  # Estonian: "Structure"
    "/struktura",  # Lithuanian: "Structure"
    "/impressum",  # German
    "/service/kontakt",  # German
    "/hafa-samband",  # Icelandic: "Contact"
    "/um-sveitarfelagid",  # Icelandic: "About the municipality"
    "/contacto",  # Spanish
    "/contacta",  # Spanish (Catalan)
    "/sede-electronica",  # Spanish: "Electronic office"
    "/nous-contacter",  # French: "Contact us"
    "/contactez-nous",  # French: "Contact us"
    "/mentions-legales",  # French: "Legal notice"
    "/kontakt",  # Polish: "Contact" (same as German)
    "/bip",  # Polish: "Public Information Bulletin"
    "/contactos",  # Portuguese: "Contacts"
    "/contacte-nos",  # Portuguese: "Contact us"
    "/municipio",  # Portuguese: "Municipality"
    "/contatti",  # Italian: "Contacts"
    "/amministrazione-trasparente",  # Italian: "Transparent administration"
    "/amministrazione",  # Italian: "Administration"
    "/over-de-gemeente",  # Dutch: "About the municipality"
    "/contact-us",  # Irish English
    "/your-council",  # Irish: council info
    "/kontakti",  # Bulgarian: "Contacts"
    "/za-nas",  # Bulgarian: "About us"
    "/kontakt",  # Slovenian: "Contact" (same as German/Polish)
    "/o-obcini",  # Slovenian: "About the municipality"
    "/obcina",  # Slovenian: "Municipality"
    "/contact-us",  # UK English
    "/about-the-council",  # UK council info
    "/kontakt",  # Croatian: "Contact" (same as German)
    "/o-nama",  # Croatian: "About us"
    "/epikoinonia",  # Greek: "Contact"
    "/kapcsolat",  # Hungarian: "Contact"
    "/elerhetosegek",  # Hungarian: "Contact details"
    "/contact",  # Romanian/Maltese/Cypriot (already present but explicit)
    "/despre-noi",  # Romanian: "About us"
    "/kontakt",  # Bosnian/Montenegrin: "Contact" (same as Croatian)
    "/kontakti",  # Albanian: "Contacts"
    # South America (Spanish/Portuguese)
    "/contactenos",  # Spanish: "Contact us"
    "/contato",  # Brazilian Portuguese: "Contact"
    "/fale-conosco",  # Brazilian Portuguese: "Talk to us"
    "/alcaldia",  # Spanish: "Mayor's office"
    "/transparencia",  # Spanish/Portuguese: "Transparency"
]

GATEWAY_KEYWORDS = {
    "seppmail": ["seppmail.cloud", "seppmail.com"],
    "barracuda": ["barracudanetworks.com", "barracuda.com"],
    "trendmicro": ["tmes.trendmicro.eu", "tmes.trendmicro.com", "trendmicro.eu", "trendmicro.com"],
    "hornetsecurity": ["hornetsecurity.com"],
    "proofpoint": ["ppe-hosted.com", "pphosted.com"],
    "sophos": ["hydra.sophos.com"],
    "fortimail": ["fortimail", "fortimailcloud.com"],
    "secmail": ["secmail.com"],
    "d-fence": ["d-fence.eu"],
    "edelkey": ["edelkey.net"],
    "ippnet": ["ippnet.fi"],
    "garmtech": ["garmtech.com", "garmtech.net"],
    "cisco-ironport": ["iphmx.com"],
    "staysecure": ["staysecuregroup.com"],
    "mailanyone": ["mailanyone.net", "electric.net"],
    "comendo": ["comendosystems.com"],
    "heimdal": ["heimdalsecurity.com"],
    "messagelabs": ["messagelabs.com"],
    "nospamproxy": ["nospamproxy.de", "nospamproxy.com", "as-scan.de"],
    "secumail": ["secumail.de"],
    "mailspamprotection": ["mailspamprotection.com"],
    "mailguard": ["mailguard.com.au"],
    "mimecast": ["mimecast.com"],
    "smxemail": ["smxemail.com"],
    "securemx": ["securemx.biz"],
    "cloudflare-email": ["mx.cloudflare.net"],
    "antispameurope": ["antispameurope.com"],
    "retarus": ["retarus.com"],
    "psmanaged": ["psmanaged.com"],
    "simnet": ["simnet.is"],
    "skyggnir": ["skyggnir.is"],
    "siminn": ["spamvorn.internet.is"],
    "telefonica": ["correolimpio.telefonica.es"],
    "cdmon": ["cdmon.net", "cdmon.com"],
    "vadesecure": ["vadesecure.com"],
    "mailinblack": ["mailinblack.com"],
    "mimecast": ["mimecast.com"],
    "mailcontrol": ["mailcontrol.com"],
    "security-mail": ["security-mail.net"],
    "topsec": ["topsec.com"],
    "tstechnology": ["tstechnology.net"],
    "mailchannels": ["mailchannels.net"],
    "spamexperts": ["spamexperts.eu", "spamexperts.net", "spamexperts.com"],
    "mpssec": ["mpssec.net"],
    "spambusters": ["spambusters.email"],
    "mxthunder": ["mxthunder.net"],
    "mx-hub": ["mx-hub.cz", "mx-hub.sk", "mx-hub.net", "mx-hub.eu"],
    "dsidata": ["dsidata.sk"],
    "spamtador": ["spamtador.com"],
    "jellyfish": ["jellyfish.systems"],
    "anti-spam-premium": ["anti-spam-premium.com"],
    "suantispam": ["suantispam.com"],
    "spamhero": ["spamhero.net", "spamhero.com"],
}

# Local ISP ASNs (replaces SWISS_ISP_ASNS)
LOCAL_ISP_ASNS: dict[int, str] = {
    # Estonia
    3249: "Telia (EE/LT)",
    2586: "Elisa Eesti",
    3327: "Telia Eesti",
    49604: "Telia Eesti",
    3212: "EENET",
    216263: "Radicenter (EE)",
    # Latvia
    5518: "TET (Lattelecom)",
    12578: "Lattelecom",
    12993: "LVRTC",
    2847: "LATNET",
    5538: "SigmaNet (LV)",
    43513: "Nano IT (LV)",
    29600: "Latvenergo/IVIKS (LV)",
    206111: "LINKIT (LV)",
    # Lithuania
    8764: "Telia Lietuva",
    43811: "Telia Lietuva",
    13194: "Bite Lietuva",
    33922: "Cgates",
    15440: "Baltneta",
    61272: "Init (LT)",
    6769: "LITNET",
    15419: "LRTC (LT)",
    212531: "Interneto Vizija (LT)",
    # Multi-country
    2588: "Elisa",
    # Finland
    719: "Elisa (FI)",
    1759: "Cinia/SecMail",
    39699: "Lounea",
    198024: "Istekki",
    16086: "Ratkaisutalo",
    215722: "Lapit Oy",
    199087: "KaseNet Oy",
    29240: "LanMail",
    3238: "Ålands Telekommunikation",
    # Norway
    29492: "Eidsiva/Hedmark IKT (NO)",
    199900: "BedSys (NO)",
    8542: "Eviny (NO)",
    210615: "Alta Kommune (NO)",
    207464: "Varanger Kraft (NO)",
    29695: "Altibox (NO)",
    # Sweden
    3301: "Telia Sweden",
    28954: "Fiberstaden (SE)",
    12552: "GlobalConnect (SE)",
    29672: "Stockholm stad (SE)",
    198568: "Atea (SE)",
    202780: "Advania (SE)",
    60053: "Habo kommun (SE)",
    206387: "BLL (SE)",
    205574: "Borås stad (SE)",
    206114: "Hofors kommun (SE)",
    25417: "Ljusnet (SE)",
    1257: "Tele2 (SE)",
    6782: "Bdnet (SE)",
    # Germany
    553: "BelWü (DE)",
    680: "DFN (DE)",
    3209: "Vodafone (DE)",
    3320: "Deutsche Telekom (DE)",
    6687: "communelink (DE)",
    8560: "IONOS/1&1 (DE)",
    8767: "M-net (DE)",
    8881: "Versatel/1&1 (DE)",
    9063: "Saarland IT (DE)",
    9145: "EWE TEL (DE)",
    9197: "ekom21 (DE)",
    12693: "DIKOM Brandenburg (DE)",
    13045: "KDO Niedersachsen (DE)",
    13101: "TNG Stadtnetz (DE)",
    16097: "TELEPORT (DE)",
    20810: "ekom21 (DE)",
    21473: "Pfalzkom (DE)",
    24940: "Hetzner (DE)",
    33846: "Dataport (DE)",
    34011: "AKDB Bayern (DE)",
    34928: "regio iT (DE)",
    42652: "eCube/Saarland IT (DE)",
    48049: "ITK Rheinland (DE)",
    50964: "Komm.ONE (DE)",
    61352: "KISA Sachsen (DE)",
    198435: "DVZ-MV (DE)",
    201318: "Südwestfalen IT (DE)",
    210849: "ITK Rheinland (DE)",
    24961: "nol-IS/myLoc (DE)",
    202577: "KDVZ Frechen (DE)",
    8351: "SIS Schwerin (DE)",
    60123: "WTnet Wuppertal (DE)",
    8422: "NetCologne (DE)",
    16024: "GELSEN-NET (DE)",
    12897: "ENTEGA (DE)",
    8319: "KGRZ Fulda (DE)",
    30238: "Trier-net (DE)",
    29014: "IN-Ulm (DE)",
    15598: "QSC/q.beyond (DE)",
    15817: "WOBCOM (DE)",
    34788: "NM-NET (DE)",
    8820: "TAL.de (DE)",
    # Denmark
    3292: "TDC/Nuuday (DK)",
    3308: "TDC NET (DK)",
    # Andorra
    6752: "Andorra Telecom (AD)",
    # Luxembourg
    6661: "POST Luxembourg (LU)",
    2602: "Restena (LU)",
    9008: "Cegecom (LU)",
    8632: "Proximus Luxembourg (LU)",
    34683: "LuxNetwork (LU)",
    # Belgium
    9208: "Proximus (BE)",
    5432: "Proximus/Skynet (BE)",
    15383: "Computerland (BE)",
    29222: "Infradata (BE)",
    6848: "Telenet (BE)",
    # Austria
    8447: "A1 Telekom Austria (AT)",
    8412: "Magenta Telekom (AT)",
    45012: "A1 Telekom Austria (AT)",
    8339: "Medialog (AT)",
    1764: "Next Layer (AT)",
    12605: "Salzburg AG (AT)",
    6830: "Liberty Global/UPC (AT)",
    29081: "OpenBusiness (AT)",
    1853: "ACOnet/ACONET (AT)",
    12762: "SPARDAT (AT)",
    25255: "Netway (AT)",
    51468: "one.com (AT/DK)",
    31543: "myNet (AT)",
    42572: "Nessus (AT)",
    47692: "Nessus (AT)",
    25575: "domainfactory (AT)",
    21013: "Stadtwerke Kufstein (AT)",
    199217: "Linz Strom GAS (AT)",
    6798: "SIL/Salzburg Internet (AT)",
    # Czechia
    16019: "Vodafone CZ",
    2852: "CESNET (CZ)",
    13036: "T-Mobile CZ",
    43542: "4ISP (CZ)",
    5610: "O2 CZ",
    21430: "Forpsi (CZ)",
    12570: "Czech On Line (CZ)",
    5577: "root.cz (CZ)",
    35592: "CZNIC/Coolhousing (CZ)",
    15685: "Casablanca INT (CZ)",
    # France
    16276: "OVH (FR)",
    12876: "Online/Scaleway (FR)",
    3215: "Orange (FR)",
    15557: "LDCom/SFR (FR)",
    5410: "Bouygues Telecom (FR)",
    16347: "Inherent (FR)",
    20756: "Nameshield (FR)",
    # Poland
    5617: "Orange Polska (PL)",
    12741: "Netia (PL)",
    8308: "NASK (PL)",
    197226: "NASK (PL)",
    21021: "Multimedia Polska (PL)",
    6714: "OPL/TP SA (PL)",
    15694: "Atman (PL)",
    29522: "Nazwa.pl (PL)",
    16138: "Interia.pl (PL)",
    50840: "home.pl (PL)",
    48850: "Zenbox (PL)",
    43939: "PERN (PL)",
    20804: "Exatel (PL)",
    61141: "AZ.pl (PL)",
    201053: "EPSI (PL)",
    12824: "home.pl (PL)",
    15967: "Netart Group (PL)",
    31229: "Beyond.pl (PL)",
    34360: "Ogicom (PL)",
    50599: "Dataspace (PL)",
    48896: "dhosting.pl (PL)",
    47544: "IQ.pl (PL)",
    60713: "TARRCI (PL)",
    203417: "LH.pl (PL)",
    8267: "Cyfronet (PL)",
    42503: "Oktawave (PL)",
    48707: "Aftermarket.pl (PL)",
    41079: "CF Gdańsk (PL)",
    13110: "INEA (PL)",
    28978: "webserwer.pl/COIG (PL)",
    41508: "webh.email/IWACOM (PL)",
    # Portugal
    3243: "MEO/Altice (PT)",
    2860: "NOS (PT)",
    12353: "Vodafone PT",
    8657: "PT Comunicações (PT)",
    15525: "MEO (PT)",
    39729: "Claranet PT",
    47787: "Ar Telecom (PT)",
    60729: "Nowo Communications (PT)",
    25291: "Adclick (PT)",
    24768: "CleanMX (PT)",
    # Spain
    3352: "Telefonica (ES)",
    200521: "SEAP-AGE/Gobierno (ES)",
    42612: "Dinahosting (ES)",
    16371: "Acens (ES)",
    25487: "DigitalValue (ES)",
    31577: "Prored/DNSxperta (ES)",
    198871: "Diputación Castellón (ES)",
    44280: "Diputació Girona (ES)",
    12430: "Vodafone España (ES)",
    50926: "Axarnet (ES)",
    15704: "Xtra Telecom (ES)",
    56958: "Raiola Networks (ES)",
    201446: "ProfesionalHosting (ES)",
    57910: "SCIP (ES)",
    198066: "Loading (ES)",
    57286: "Gigas (ES)",
    15954: "Tecnocratica (ES)",
    12338: "Euskaltel (ES)",
    203051: "Diputación Ávila (ES)",
    3262: "Sarenet (ES)",
    # Italy
    12874: "Fastweb (IT)",
    3269: "Telecom Italia/TIM (IT)",
    6762: "Telecom Italia Sparkle (IT)",
    12637: "Aruba.it (IT)",
    31034: "Aruba.it (IT)",
    5602: "Kyndryl Italia (IT)",
    8968: "BT Italia (IT)",
    6734: "INFN (IT)",
    137: "GARR (IT)",
    28716: "Retelit (IT)",
    20811: "Brennercom (IT)",
    8612: "Tiscali (IT)",
    29286: "Netsons (IT)",
    35574: "Lottomatica (IT)",
    30722: "Vodafone Italia (IT)",
    12779: "IT.Gate (IT)",
    34695: "E4A (IT)",
    49367: "Seeweb (IT)",
    44160: "SINet/Almaviva (IT)",
    15589: "Clouditalia (IT)",
    # Netherlands
    20857: "TransIP (NL)",
    15879: "i3D.net (NL)",
    49981: "WorldStream (NL)",
    25596: "Antagonist (NL)",
    43350: "NForce (NL)",
    20847: "Previder (NL)",
    286: "KPN (NL)",
    1136: "KPN (NL)",
    3265: "XS4ALL/KPN (NL)",
    33915: "Ziggo (NL)",
    15435: "CAIW (NL)",
    60781: "LeaseWeb (NL)",
    47541: "VK Hosting (NL)",
    12859: "BIT (NL)",
    39309: "Signet (NL)",
    57626: "Ezorg (NL)",  # Dutch municipal IT cooperative
    38915: "TransIP/Team.blue (NL)",
    # Ireland
    2128: "Hosting Ireland (IE)",
    39122: "Blacknight (IE)",
    31641: "Blacknight (IE)",
    34245: "Magnet Networks (IE)",
    13280: "Enet/Viatel (IE)",
    15502: "Vodafone Ireland (IE)",
    6830: "Virgin Media Ireland (IE)",
    25441: "Eir/eircom (IE)",
    35272: "Eir/eircom (IE)",
    60800: "GTI (IE)",
    # Bulgaria
    8717: "Spectra Net (BG)",
    42293: "Web Host Ltd (BG)",
    47453: "TerraHost (BG)",
    43205: "Bulsatcom (BG)",
    59466: "SZ IT (BG)",
    201200: "Hosting.bg (BG)",
    25374: "Netissat (BG)",
    44586: "SEGA.bg/e-Gov (BG)",
    42086: "RO-NI (BG)",
    34841: "Orbitel (BG)",
    8866: "BTC/Vivacom (BG)",
    # Iceland
    6677: "Simnet/Vist (IS)",
    29689: "Skyggnir (IS)",
    44925: "1984 Hosting (IS)",
    12969: "Síminn (IS)",
    # Slovakia
    6855: "Slovak Telekom (SK)",
    5578: "Orange Slovensko (SK)",
    29405: "SWAN (SK)",
    47232: "Websupport (SK)",
    51306: "Websupport (SK)",
    15962: "SANET (SK)",
    20940: "Akamai/SK",
    31588: "GTS Slovakia (SK)",
    196621: "EpixTechnology (SK)",
    43413: "MX-HUB (SK)",
    2607: "SANET (SK)",
    8290: "Slovanet (SK)",
    8778: "Slovanet (SK)",
    31117: "Energotel (SK)",
    35328: "DSI DATA (SK)",
    43451: "Slovanet Radiolan (SK)",
    44631: "CondorNet (SK)",
    49115: "E-MAX (SK)",
    51013: "Websupport (SK)",
    51653: "PresNet (SK)",
    57606: "Proxis (SK)",
    60895: "Lekos (SK)",
    208668: "Netspace (SK)",
    # United Kingdom
    20860: "IOMART (GB)",
    35425: "Bytemark (GB)",
    8468: "Entanet (GB)",
    20712: "ANS Group (GB)",
    24916: "Claranet UK (GB)",
    8683: "Fasthosts (GB)",
    34931: "UKFast/ANS (GB)",
    35662: "Heart Internet (GB)",
    21396: "NetSumo (GB)",
    5089: "Virgin Media (GB)",
    2856: "BT (GB)",
    6871: "Plusnet (GB)",
    13285: "TalkTalk (GB)",
    12576: "EE/Orange (GB)",
    60294: "JISC (GB)",
    786: "JANET (GB)",
    # Slovenia
    5603: "Telekom Slovenije (SI)",
    34779: "T-2 (SI)",
    21283: "A1 Slovenija (SI)",
    3212: "ARNES (SI)",
    47610: "Mega M (SI)",
    34803: "Telemach (SI)",
    12644: "AMIS (SI)",
    9119: "Softnet (SI)",
    198644: "Prenos podatkov (SI)",
    58046: "gov.si (SI)",  # Slovenian government shared mail
    # Croatia
    5391: "Hrvatski Telekom (HR)",
    13046: "A1 Croatia (HR)",
    34594: "Optima Telekom (HR)",
    15994: "Iskon (HR)",
    2108: "CARNET (HR)",
    31012: "Metronet (HR)",
    41336: "CDU/gov.hr (HR)",  # Croatian government shared mail
    # Cyprus
    6866: "CYTA (CY)",
    35432: "PrimeTel (CY)",
    # Greece
    6799: "OTE (GR)",
    1241: "Forthnet (GR)",
    5408: "GRNET (GR)",
    3329: "Vodafone GR (GR)",
    25472: "Wind Hellas (GR)",
    35506: "GRNET/gov.gr (GR)",  # Greek government mail
    34762: "GRNET (GR)",
    # Hungary
    5483: "Magyar Telekom (HU)",
    20845: "DIGI (HU)",
    12301: "Invitel (HU)",
    2547: "KIFU/NIIF (HU)",
    # Malta
    15735: "GO p.l.c. (MT)",
    12709: "Melita (MT)",
    # Romania
    8708: "RCS & RDS (RO)",
    9050: "Romtelecom (RO)",
    2614: "ROEDUNET (RO)",
    12302: "Vodafone RO (RO)",
    31313: "STS/gov.ro (RO)",  # Romanian government STS mail
    # Albania
    42313: "AKEP (AL)",
    29614: "Abissnet (AL)",
    # Kosovo
    21246: "IPKO (XK)",
    20773: "Kujtesa (XK)",
    # Montenegro
    8585: "Crnogorski Telekom (ME)",
    42159: "M-Tel (ME)",
    # Bosnia and Herzegovina
    9146: "BH Telecom (BA)",
    5564: "HT Eronet (BA)",
    31549: "Telekom Srpske (BA)",
    # Georgia
    49628: "SKYTEL/MRDI gov.ge (GE)",  # Government shared mail (edge.mrdi.gov.ge)
    47810: "ProService (GE)",
    57814: "Cloud9 (GE)",
    20545: "GRENA (GE)",
    35076: "NameService (GE)",
    35805: "Silknet (GE)",
    # Turkey
    209171: "ICISLERI/muhtar.gov.tr (TR)",  # Government shared mail (posta.muhtar.gov.tr)
    # Azerbaijan
    206977: "AZSTATENET/mail.gov.az (AZ)",  # Government shared mail (mmx.mail.gov.az)
    # Belarus
    60330: "BCT/g-cloud.by (BY)",  # Government cloud (mg.g-cloud.by)
    6697: "Belpak (BY)",
    25513: "nomessage.ru (RU)",  # Russian mail provider used by BY municipalities
    # Serbia
    8400: "Telekom Srbija (RS)",
    # Moldova
    28990: "Molddata (MD)",  # mx0.spamcloud.md
    # Australia
    1221: "Telstra (AU)",
    9290: "GoHosting (AU)",
    132321: "NT Government (AU)",
    10080: "Interconnect Networks (AU)",
    4764: "Aussie Broadband (AU)",
    # New Zealand
    4648: "Spark NZ (NZ)",
    2570: "Spark NZ (NZ)",
    9790: "Two Degrees (NZ)",
    # Pacific
    2764: "AAPT/PeaceSat (Pacific)",
    # Indonesia
    132634: "KOMINFO e-Gov (ID)",  # Government shared mail (mail.go.id)
    45313: "Pemda NAD (ID)",  # Aceh provincial government
    # Thailand
    4618: "Internet Thailand (TH)",
    # Germany — municipal IT cooperatives and regional ISPs
    12337: "Noris Network (DE)",  # rechennetz.de
    39835: "Goetel (DE)",  # kdgoe.de
    12611: "R-KOM Regensburg (DE)",
    28748: "AlphaCron (DE)",  # cm-system.de
    12360: "KTK/KEVAG (DE)",
    12923: "Wizard (DE)",  # brv.net, wizard.de
    203536: "FNOH (DE)",  # itv-gifhorn.de
    202680: "neu-itec (DE)",
    44973: "RZ Hassfurt (DE)",
    201035: "Lünecom (DE)",
    8937: "Salink (DE)",  # kirchberg-hunsrueck.de
    212587: "GKD-RE (DE)",
    12813: "Wornet (DE)",  # secumail.de
    51978: "Wemacom (DE)",
    199284: "Encoline (DE)",
    41955: "SerNet (DE)",
    25394: "MK-Netzdienste (DE)",
}

DE_STATES = {
    "SH": "01", "HH": "02", "NI": "03", "HB": "04",
    "NW": "05", "HE": "06", "RP": "07", "BW": "08",
    "BY": "09", "SL": "10", "BE": "11", "BB": "12",
    "MV": "13", "SN": "14", "ST": "15", "TH": "16",
}

# Reverse mapping: state code → abbreviation (for display)
DE_STATE_CODES = {v: k for k, v in DE_STATES.items()}

# Countries that use partitioned DNS caches (keyed by state prefix in ID)
PARTITIONED_COUNTRIES = {"DE": lambda muni_id: muni_id[3:5]}

CONCURRENCY = 20
CONCURRENCY_POSTPROCESS = 20
CONCURRENCY_SMTP = 10
SCRAPE_TIME_BUDGET = 5400  # 90 minutes max for website scraping step

SMTP_BANNER_KEYWORDS = {
    "microsoft": [
        "microsoft esmtp mail service",
        "outlook.com",
        "protection.outlook.com",
        "mx.microsoft",
    ],
    "google": [
        "mx.google.com",
        "google esmtp",
    ],
    "zone": [
        "zone.eu",
        "zone.ee",
    ],
    "telia": [
        "telia.ee",
        "telia.lt",
    ],
    "aws": [
        "amazonaws",
        "amazonses",
    ],
    "elkdata": [
        "elkdata.ee",
    ],
    "zoho": [
        "zoho.com",
        "zoho.eu",
    ],
}
