def firm_name(df):
    import numpy as np
    import pandas as pd
    lolland_list = ['Aktieselskabet Lollands Bank',
    'A/S Lollands Bank Vordingborg Filial',
    'Lollands Bank',
    'LOLLANDS BANK']

    lundbeck_list = ['Lundbeck',
    'Lundbeckfonden',
    'lundbeck',
    'H. Lundbeck A/S',
    'Lundbeck Pharma A/S',
    'LUNDBECKFONDEN',
    'H. Lundbeck',
    'Lundbeck A/S',
    'Lundbeckfond Ventures',
    'Lundbeck Institute',
    'H LUNDBECK A/S',
    'Lundbeckfond Invest A/S',
    'Lundbeckfonden / LFI a/s']

    luxor_list = ['Investeringsselskabet Luxor A/S', ]

    laan_spar_list = ['Lån og Spar Bank']

    matas_list = ['Matas A/S',
    'Matas',
    'Matas Operations A/S',
    'MATAS',
    'Matas Padborg',
    'Matas 18465',
    'Matas, Støvring',
    'Matas Højbjerg',
    'Matas Hornbæk',
    'Matas Støvring',
    'Matas 11789',
    'Matas Nakskov',
    'StyleBox by Matas',
    'MATAS 17797',
    'Allerød Matas',
    'Matas Frederiksværk',
    'Matas Bjerringbro',
    'Matas Ryesgade',
    'Matas Skanderborg',
    'Matas Købmagergade 55',
    'Matas 16810',
    'matas',
    'Matas Nexø',
    'Matas Vanløse',
    'Matas Ølgod',
    'MATAS 16756',
    'Matas v/Tina Bille Christensen',
    'Stylebox by Matas',
    'Matas søger nye elever',
    'Matas Værløse',
    'Matas i Aars',
    'MATAS 18538 SØNDERCENTRET',
    'Matas Gågaden',
    'MATAS 10537',
    'Matas i Esbjerg Storcenter',
    'Matas Torvet',
    'Matas 14616',
    'MATAS 10022',
    'Matas A/S (alle)',
    'Matas Materialisten',
    'Matas 12600',
    'Matas A/S Bytorv Horsens',
    'MATAS 10760',
    'Matas Waterfront',
    'MATAS V/PEDER FRØLUND HANSEN',
    'Matas 11258',
    'MATAS 12734',
    'MATAS A/S',
    'MATAS 18635',
    'Matas Aalborg Storcenter',
    'Matas Matrialisten',
    'Matas Kennedy Arkaden',
    'MATAS SLANGERUP',
    'MATAS 18481',
    'MATAS 17027',
    'MATAS 17574',
    'MATAS 11665',
    'Matas, Nørrebro Bycenter',
    'Matas Nordborg Aps',
    'Matas Rødding',
    'MATAS 17019',
    'MATAS 18570',
    'Matas v/Arne Hansen',
    'Matas herning centret',
    'MATAS 18589',
    'Matas 10073',
    'MATAS 10278',
    'MATAS SÆBY',
    'Matas 18589',
    'MATAS 15350',
    'HERM L MELSKENS A/S MATAS',
    'MATAS, Lyngby Storcenter',
    'Matas-Materialisten',
    'Matas, Herm. L. Melskens A/S',
    'Matas, City Nord',
    'MATAS MATERIALISTEN',
    'Materialisten Matas',
    'MATAS Glostrup Storcenter',
    'Matas v/Storetorv',
    'Matas Ro´s Torv',
    'MATAS - PETER LILLELUND SØRENSEN ApS',
    'MATAS I HILLERØD',
    'Matas Vejen',
    'Matas Ramsherred',
    'MATAS STØVRING V/FINN LAUERSEN',
    'Matas Veri Center',
    'Matas Nordborg',
    'Matas Løvemagasinet',
    'Matas Espergærde',
    'Matas - Søndercentret',
    'Matas City Nord',
    'Matas Frederiks Allé',
    'Matas Herning centret',
    'MATAS, NørreportcentretV/JENS KONGSGAARD',
    'Matas Storcenter Nord',
    'MATAS 18643',
    'Matas, Randers Storcenter',
    'MATAS 16896',
    'matas herning centret',
    'MATAS 10040',
    'MATAS 14044',
    'Matas Galten',
    'Matas Jægersborg Midtpunkt']

    miga_list = ['Migatronic A/S',
    'Migatronic Automation A/S',
    'Svejsemaskinfabrikken Migatronic A/S',
    'Migatronic',
    'Migatronic A/s',
    'SVEJSEMASKINEFABRIKKEN MIGATRONIC A/S',
    'Svejsemaskinefabrikken Migatronic A/S',
    'MIGATRONIC AUTOMATION A/S']

    mt_hojgaard_list = ['MT Højgaard A/S',
    'Mt Højgaard A/S',
    'MT Højgaard',
    'MT HØJGAARD A/S',
    'MT Højgaard A/S, KHV',
    'MT Højgaard a/s','Enemærke & Petersen A/S',
    'Enemærke & Petersen a/s',
    'Enemærke & Petersen',
    'ENEMÆRKE & PETERSEN A/S','Ajos A/S', 'Ajos A/s', 'Ajos', 'Ajos a/s', 'AJOS']

    mon_bank_list = ['Møns Bank A/S',
    'Møns Bank',
    'MØNS BANK',
    'MØNS BANK PRÆSTØ FILIAL',
    'A/S Møns Bank']

    netcompany_list = ['Netcompany',
    'Netcompany A/S',
    'NETCOMPANY A/S']

    nilfisk_list = ['Nilfisk A/S',
    'Nilfisk',
    'Nilfisk Group',
    'Nilfisk-Advance Nordic A/S',
    'Nilfisk Advance A/S',
    'Nilfisk-Advance',
    'Nilfisk-Advance Group',
    'Nilfisk Advance',
    'Nilfisk-Advance A/S',
    'Nilfisk-ALTO Food Division',
    'Nilfisk Outdoor Division',
    'Nilfisk Outdoor',
    'Nilfisk-Egholm A/S',
    'Nilfisk ALTO Food Division',
    'Nilfisk - Advance A/S',
    'Nilfisk-ALTO A/S',
    'Nilfisk-ALTO',
    'Nilfisk - ALTO']

    NKT_list = ['NKT (Denmark) A/S',
    'NKT A/S',
    'NKT Photonics',
    'NKT Photonics A/S',
    'NKT Holding A/S',
    'NKT Cables a/s',
    'NKT Holding',
    'NKT HOLDING A/S',
    'NKT CABLES A/S',
    'NKT PHOTONICS A/S',
    'NKT Cables'
    'NKT CABLES ULTERA A/S',
    'NKT Research & Innovation A/S'
    ]

    nnit_list = ['NNIT',
    'NNIT A/S', 'SCALES A/S',
    'Scales A/S']

    nordea_list = ['NORDEA FINANS DANMARK A/S',
    'Nordea',
    'Nordea-fonden',
    'Nordea Bank AB',
    'Nordea Bank Danmark A/S',
    'Nordea Bank Danmark',
    'Nordea Kredit Realkreditaktieselskab',
    'Nordea Bank Danmark A/S Glostrup Afd. & Erhverv',
    'Nordea Bank Danmark A/S Roskilde & Erhverv',
    'Nordea Bank',
    'Nordea Liv & Pension',
    'Nordea Bank Danmark A/S Ballerup Afd.',
    'Nordea Bank AB S.A.',
    'Nordea Bank Danmark A/S Centerfilial',
    'Nordea Ejendomsinvestering A/S',
    'Nordea Invest Fund Management A/S',
    'NORDEA BANK DANMARK A/S',
    'Nordea Danmark',
    'Nordea Bank Danmark A/s',
    'Nordea Bank Danmark A/s Ballerup Afd.',
    'Nordea Bank Danmark A/s Birkerød Afd. & Erhvervsafd.',
    'Nordea Bank Danmark A/s Edb Afdeling',
    'Nordea Operations Centre',
    'Nordea Bank - Copenhagen',
    'Nordea Bank Denmark',
    'Nordea Markets',
    'Nordea Wealth Management',
    'Nordea Ejendomme',
    'Nordea Bank Danmark A/S, Thisted',
    'Nordea ',
    'Nordea Bank A/S',
    'Nordea A/S',
    'Nordea Savings and Asset Management',
    'Nordea Invest',
    'NORDEA LIV & PENSION',
    'NORDEA PENSION DANMARK, LIVSFORSIKRINGSSELSKAB A/S',
    'NORDEA',
    'Nordea Finans Danmark A/S',
    'Nordea Danmark-fonden',
    'Nordea, Sædding afdeling',
    'Nordea, Oksbøl afdeling',
    'Nordea, Ribe afdeling',
    'NORDEA BANK',
    'NORDEA, MARKETS DIVISION']

    nordfyns_list = ['Nordfyns Finans',
    'Nordfyns Bank',
    'Nordfyns Finans A/S',
    'Aktieselskabet Nordfyns Bank',
    'A/S Nordfyns Bank Kerteminde afd']

    northmedia_list = ['North Media Online A/S', 'North Media A/S', 'NORTH MEDIA A/S', 'North Media',
      'Ofir A/S',
    'ofir A/S',
    'Ofir',
    'Ofir.dk - Marketing',
    'Ofir Services A/S',
    'OFiR Danmark a-s',
    'OFiR a-s',
    'OFIR DANMARK A/S',
       'Forbruger-Kontakt',
    'Forbruger-kontakt A/s',
    'Forbruger-Kontakt A/S',
    'Forbruger-kontakt',
    'forbruger-kontakt','BEKEY',
    'Bekey',
    'BEKEY A/S',
    ' BEKEY A/S']

    novozym_list = ['Novozymes A/S',
    'Novozymes',
    'NOVOZYMES A/S',
    'NovoZymes',
    'Novozymes A/S,']

    ntg_list = ['NTG Nordic Transport Group',
    ' NTG Nordic Transport Group',
    'NTG Continent A/S',
    'NTG Nordic A/S',
    'NTG - Nordic Transport Group',
    'NTG Frigo A/S',
    'NTG Projects A/S',
    'NTG Global',
    'NTG East A/S',
    'NTG Nielsen & Sørensen A/S',
    'NTG Global A/S',
    'NTG NORDIC A/S',
    'NTG TERMINALS A/S']

    ntr_list = ['Daniamant ApS', 'Daniamant Aps']

    novo_list = ['Novo Nordisk',
    'Novo Nordisk Fonden',
    'Novo Nordisk A/S',
    'Novo Holdings',
    'NOVO NORDISK A/S',
    'NOVO NORDISK FONDEN',
    'Novo Holdings A/S',
    'Novo Nordisk A/S Region Europe',
    'Novo Nordisk Foundation',
    'Novo Nordisk Fonden, LIFE',
    'Novo Nordisk Foundation Center for Protein Research',
    'Novo Nordisk Foundation Center for Basic Metabolic Research',
    'NovoNordisk Pharma GmbH',
    'Novo Nordisk Pharma GmbH',
    'Novo Nordisk A/s',
    'Novo Nordisk AS',
    'Novo Nordisk RD',
    'The Novo Nordisk Foundation Center for Protein Research',
    'The Novo Nordisk Foundation Center for Basic Metabolic Research',
    'The Novo Nordisk Foundation Center for Metabolic Research',
    'Novo NOrdisk',
    'Novo Nordisk Scandinavia',
    'Novonordisk',
    'Novo Nordisk A/S,',
    'Novo Nordisk Scandinavia AB',
    'Xellia Pharmaceuticals ApS', 'Xellia', 'Xellia Pharmaceuticals',
    'Sonion A/S', 'SONION A/S','Sonion'
    ]

    orphazyme_list = ['Orphazyme A/S', 'Orphazyme', 'Orphazyme ApS']

    pandora_list = ['PANDORA A/S',
    'Pandora Jewelry',
    'Pandora Group',
    'PANDORA',
    'Pandora',
    'Pandora A/S',
    'Pandora CWE',
    'PANDORA CWE',
    'pandora',
    'Pandora Store',
    'PANDORA Jewelry A/S',
    'PANDORA Jewelry GmbH',
    'PANDORA CEW',
    'PANDORA Jewelry',
    'KasiGroup / Pandora Jewelry',
    'Pandora Jewelry A/S',
    'KasiGroup / PANDORA Jewelry']

    nordicom_list = ['Park Street Nordicom A/S', 'Nordicom A/S']

    aarslef_list = ['Per Aarsleff A/S',
    'Aarsleff Rail',
    'Aarsleff Rail A/S',
    'Per Aarsleff Holding A/S',
    'Per Aarsleff',
    'AARSLEFF RAIL A/S',
    'Aarsleff Fundering ',
    'Aarsleff',
    'Per Aarsleff A/S-øst', 'VG ENTREPRENØR A/S', 'VG Entreprenør A/S', 'VG Entreprenør',
    'Danpipe A/S', 'DANPIPE A/S', 'Vandfax A/S',
    'Hansson & Knudsen A/S',
    'HANSSON & KNUDSEN A/S',
    'Petri & Haugsted A/S',
    'PETRI OG HAUGSTED A/S',
    'Petri & Haugsted',
    'Petri & Haugsted AS',
    'Petri & Haugsted as',
    'Petri & Hagusted AS',
    'Entreprenørfirmaet Østergaard A/S',
    'Entreprenørfirmaet Østergaard, Vejle A/S',
    'Entreprenørfirmaet Østergaard A/S, Vejle',
    'Entreprenørfirmaet Østergaard',
    'ENTREPRENØRFIRMAET ØSTERGAARD, VEJLE A/S',
    'Centrum Pæle A/S', 'Centrum Pæle', 'CENTRUM PÆLE', 'CENTRUM PÆLE A/S',
    'Wicotec Kirkebjerg A/S',
    'WICOTEC KIRKEBJERG',
    'Wicotec Kirkebjerg',
    'WICOTEC KIRKEBJERG A/S',
    'WICOTEC A/S',
    'AARSLEFF-WICOTEC J.V. I/S',
    'Wicotec A/S',
    'Aarsleff Wicotec Jernbaneanlæg','DANJORD A/S', 'Danjord A/S'
    ]

    rias_list = ['RIAS A/S',
    'Rias A/S',
    'RIAS']

    ringbank_list = ['Ringkjøbing Landbobank - Nordjyske Bank',
    'Ringkjøbing Landbobank ? Nordjyske Bank',
    'Ringkjøbing Landbobank \x96 Nordjyske Bank',
    'Ringkjøbing Landbobank',
    'Ringkjøbing Landbobank ',
    'Ringkjøbing Landbobank A/S - Aarhus Afd.',
    'Ringkjøbing Landbobank, Aktieselskab',
    'Ringkjøbing Landbobank. Aktieselskab',
    'Ringkjøbing Landbobank A/S',
    'Ringkjøbing Landbobank - via JydskeVestkysten',
    'Ringkjøbing Landbobank - via De Bergske Blade',
    'Ringkjøbing landbobank',
    'RINGKJØBING LANDBOBANK']

    roblon_list = ['Roblon',
    'ROBLON AKTIESELSKAB Industrial Fiber',
    'Roblon Aktieselskab',
    'ROBLON AKTIESELSKAB',
    'Roblon A/S',
    'Roblon Industrial Fiber Division',
    'Roblon Lighting Division',
    'Roblon Nordhavnsvej',
    'Roblon Engineering Division',
    'Roblon Fiber Optics']

    rockwool_list = ['ROCKWOOL International A/S',
    'ROCKWOOL A/S',
    'ROCKWOOL Technical Insulation',
    'Rockwool Technical Insulation',
    'ROCKWOOL Firesafe Insulation',
    'Rockwool A/S',
    'ROCKWOOL Nordics A/S',
    'ROCKWOOL Scandinavia',
    'Rockwool',
    'ROCKWOOL International',
    'Rockwool Group',
    'Rockwool International A/S',
    'ROCKWOOL Nordics',
    'ROCKWOOL',
    'Rockwool International',
    'ROCKWOOL INTERNATIONAL A/S',
    'The Rockwool Group']

    rovsing_list = ['Rovsing A/S',
    'SSBV-Rovsing A/S',
    'Rovsing',
    'Rovsing Dynamics A/S',
    'Rovsing Dynamics']

    royal_list = ['Royal Unibrew A/S',
    'ROYAL UNIBREW A/S Lager',
    'Royal Unibrew',
    'ROYAL UNIBREW A/S',
    'Royal Unibrew - Terminal Nordjylland',
    'ROYAL UNIBREW A/S ALBANI BRYGGERIERNE A/S',
    'Royal Unibrew - Vejle Depot v/Holger Rud',
    'Albani/Royal Unibrew',
    'ROYAL UNIBREW A/S FAXE BRYGGERI',
    'ROYAL UNIBREW A/S CERES BRYGGERIERNE',
    'Royal Unibrew, Faxe Depot Roskilde']

    rtx_list = ['RTX A/S',
    'RTX',
    'RTX Telecom A/S',
    'RTX TELECOM A/S']

    sani_list = ['Sanistål A/S',
    'Sanistål',
    'Sanistål A/s',
    'Sanistål A/S - Aalborg',
    'Sanistål A/S TCL',
    'Sanistål A/S i Aalborg',
    'Sanistål A/S i Billund',
    'Sanistål A/S BCL',
    'Sanistål, Markman',
    'Serman & Tipsmark A/S', 'Serman & Tipsmark']

    sas_list = ['Scandinavian Airlines System',
    'Scandinavian Airlines',
    'SAS Ground Handling Denmark A/S',
    'Scandinavian Airlines System (SAS)',
    'SAS Danmark A/S',
    'SAS Institute',
    'SAS Cargo Group A/S',
    'SAS',
    'SAS Group',
    'SAS Scandinavian Airlines Danmark A/S',
    'SAS EuroBonus',
    'SAS COMPONENT GROUP A/S',
    'SAS Human Resources Services',
    'SAS Ground Services',
    'SAS Group IT',
    'SAS Group Human Resources Services AB',
    'SAS group Corp. HR Development',
    'SAS Component Group A/S',
    'SAS Technical Services Denmark C/O Manpower Solutions',
    'SAS Technical Services Denmark',
    'SAS Ground Services Denmark A/S',
    'SAS Cargo A/S',
    'SAS Group SAS Technical Services Denmark',
    'SAS / Scandinavian Airlines System',
    'SAS Scandinavian Airlines Danmark',
    'SAS Flight Academy AB',
    'SAS Flight Academy',
    'SAS Technical Services',
    'SAS Component A/S',
    'SAS Cargo',
    'Radisson SAS Limfjord Hotel',
    'SAS Group Scandinavian Airlines Danmark A/S',
    'SAS Group SAS Ground Equipment Denmark A/S',
    'SAS Ground Equipment Denmark A/S',
    'SAS Human Ressource Services A/S',
    'SAS Ground Equipment Denmark A/S (SGE)',
    'SAS Group Scandinavian Airlines']

    brakesystem_list = ['Scandinavian Brake Systems A/S',
    'Scandinavian Brake Systems AS',
    'Scandinavian Brake Systems A/S, Svendborg',
    'Scandinavian Brake Systems']

    scandinavian_list = ['Scandinavian Tobacco Group A/S',
    'Scandinavian Tobacco Group Denmark A/S',
    'Scandinavian Tobacco Group',
    'Scandinavian Tobacco Group Nykøbing ApS',
    'SCANDINAVIAN TOBACCO GROUP A/S',
    'Scandinavian Tobacco Group Assens A/S',
    'SCANDINAVIAN TOBACCO GROUP HOLSTEBRO A/S',
    'Scandinavian Tobacco Group Holstebro A/S']

    schouw_list =  ['Schouw & Co.', 'Aktieselskabet Schouw & Co.']

    skako_list = ['SKAKO Concrete A/S',
    'SKAKO CONCRETE A/S',
    'SKAKO A/S',
    'Skako Concrete A/S',
    'SKAKO Vibration A/S',
    'SKAKO VIBRATION',
    'SKAKO CONCRETE',
    'SKAKO Concrete',
    'SKAKO CONRETE',
    'Skako A/S']

    skjern_list = ['Skjern Bank A/S',
    'Skjern Bank',
    'Skjern Bank - via JydskeVestkysten',
    'Aktieselskabet Skjern Bank',
    'SKJERN BANK']

    solar_list = ['Solar Danmark A/S',
    'Solar A/S',
    'Solar Group',
    'Solar',
    'Solar - Group',
    'Solar Danmark',
    'SOLAR A/S',
    'Solar Invest A/S',
    'Solar A/S Coporate',
    'Solar A/S, Corporate',
    'Solar A/S, Group',]

    sp_group_list = ['Ulstrup Plast A/S',
    'SP MOULDING A/S - Juelsminde afdelingen',
    'SP Moulding A/S',
    'SP MOULDING A/S Stoholm Afdeling',
    'SP MOULDING A/S - Juelsminde afdeling',
    'SP MOULDING A/S - Stoholm Afdeling',
    'SP MOULDING A/S - Stoholm afdelingen',
    'SP Moulding',
    'SP MOULDING A/S',
    'Ergomat A/S', 
    'Ergomat Danmark A/S',
    'ERGOMAT A/S',
    'Tinby A/S', 'TINBY A/S',
    'MM Composite A/S',
    'MedicoPack A/S', 'Medicopack A/S',
    'Gibo Plast A/S Spentrup',
    'GIBO PLAST A/S', 'Accoat A/S', 'ACCOAT A/S']


    sparnord_list = ['Spar Nord Bank A/S',
    'Spar Nord Lyngby',
    'Spar Nord',
    'Spar Nord Holstebro',
    'Spar Nord Hillerød',
    'Spar Nord Esbjerg',
    'Spar Nord Bank',
    'Spar Nord Helsingør',
    'Spar Nord Svendborg',
    'SPAR NORD BANK A/S',
    'Spar Nord Århus',
    'Spar Nord Horsens',
    'Spar Nord Kolding',
    'Spar Nord A/S',
    'SPAR NORD BANK A/S STORVORDE AFD',
    'Spar Nord Hobro',
    'Spar Nord Bolig',
    'Spar Nord København',
    'Spar Nord Vejle',
    'Spar Nord Odense',
    'Spar Nord Herning']

    sparekassen_list = ['Sparekassen Sjælland-Fyn A/S',
    'Sparekassen Sjælland-Fyn',
    'Sparekassen Sjælland-Fyn A/S, Dalum afd.',
    'Sparekassen Sjælland',
    'SPAREKASSEN SJÆLLAND HOLBÆK AFDELING',
    'Sparekassen Fyn A/S',
    'Sparekassen Fyn',
    'Sparekassen Fyn (det tidligere Sparekassen Faaborg)']

    sydbank_list = ['Sydbank',
    'Sydbank A/S',
    'Sydbank Esbjerg',
    'Sydbank Århus',
    'Sydbank Aarhus',
    'SYDBANK A/S',
    'SYDBANK SØNDERJYLLAND',
    'Sydbank Herning',
    'Sydbanks Odense, Odense',
    'SYDBANK']

    tcm_list = ['TCM Group A/S', 'TCM Group', 'TCM Group ', ]

    tivoli_list = ['Tivoli Hotel & Congress Center',
    'Tivoli A/S',
    'Tivoli Hotel og Tivoli Congress Center',
    'Arp-Hansen Tivoli Hotel & Congress Center',
    'Tivoli Hotel og Congress Center',
    'Tivoli Invest AS',
    'TIVOLI',
    'TIVOLI A/S',
    'Tivoli',
    'Tivoli Congress Center']

    topdanmark_list = ['Topdanmark Forsikring A/S',
    'Topdanmark',
    'Topdanmark Forsikring og Pension',
    'TopDanmark',
    'Topdanmark Forsikring, Ballerup',
    'Topdanmark Forsikring, Køge',
    'Topdanmark Forsikring, Odense',
    'Topdanmark Forsikring, Herning',
    'Topdanmark Forsikring, Viby J',
    'Topdanmark Forsikring, Aalborg',
    'TopDanmark Forsikring',
    'Topdanmark Forsikring',
    'Topdanmark A/S',
    'Top Danmark']

    torm_list = ['TORM A/S',
    'Torm',
    'TORM',
    'Torm A/S',
    'Torm Dampskibsselskabet A/S',
    'Dampskibsselskabet Torm',
    'A/S Dampskibsselskabet TORM',
    'Dampskib Torm',
    'Dampskibsselskabet TORM']

    totalbanken_list = ['Total Banken', 
    'Totalbanken A/S',
    'Totalbanken',
    'TOTALBANKEN A/S']

    tryg_list = ['Tryg Forsikring A/S',
    'TryghedsGruppen',
    'Tryg',
    'TrygFonden',
    'Tryghedsgruppen',
    'Tryg A/S',
    'TRYG',
    'Fondsmæglerselskabet Investering & Tryghed A/S',
    'Tryghedshotel Randers / Kollektivhuset',
    'TryghedsGruppen smba',
    'Fondsmæglerselskabet Investering & Tryghed',
    'Tryg Forsikring',
    'TrygVesta',
    'TrygVesta A/S',
    'TRYG FORSIKRING A/S',
    'Tryg i Danmark smba',
    'TRYG FORSIKRING A/S Inkassoafdelingen',
    'TrygVesta Forsikring A/S',
    'Tryg Vesta',
    'Tryg forsikring']

    vestas_list = ['Vestas Wind Systems A/S',
    'MHI Vestas Offshore Wind A/S',
    'MHI Vestas Offshore Wind',
    'MHI VESTAS OFFSHORE WIND A/S',
    'MHI Vestas',
    'Vestas',
    'Vestas Technology R&D',
    'Vestas Blades A/S',
    'Vestas Nacelles A/S',
    'Vestas Towers A/S',
    'Vestas ',
    'Vestas Offshore A/S',
    'Vestas Spare Parts & Repair A/S',
    'Vestas Control Systems A/S',
    'Vestas Northern Europe A/S',
    'Vestas Assembly A/S',
    'Vestas Towers',
    'Vestas Group Finance & Operations']

    vestjysk_list = ['vestjyskBANK', 'Vestjysk Bank A/S']

    zealand_pharma_list = ['Zealand Pharma A/S']

    oersted_list = ['Ørsted Bioenergy & Thermal Power',
    'Ørsted Distribution & B2C',
    'Ørsted Group Functions',
    'Ørsted Wind Power ? EPC',
    'Ørsted Wind Power ? Operations',
    'Ørsted Wind Power',
    'Ørsted Customer Solutions',
    'Ørsted Wind Power ? Strategy, Development & Regulatory',
    'Ørsted Distribution & Customer Solutions',
    'Ørsted',
    'Ørsted Wind Power - EPC',
    'Ørsted Wind Power - Operations',
    'Ørsted Vind A/S',
    'Ørsted Wind Power \x96 Operations',
    'Ørsted Wind Power \x96 HSE',
    'Ørsted Wind Power \x96 QHSE Wind',
    'Ørsted Wind Power \x96 EPC',
    'Ørsted Wind Power - Strategy, Development & Regulatory',
    'Ørsted Wind Power - QHSE Wind',
    'Ørsted Wind Power \x96 Strategy, Development & Regulatory',
    'Ørsted Master Thesis',
    'Ørsted A/S',
    'Ørsted Wind Power \x96 Partnerships & Asset Management',
    'Ørsted ? IT- Infrastructure, Operation and Support',
    'Ørsted Wind Power - Partnerships & Asset Management',
    'Ørsted Wind Power ? Cost of Electricity & Procurement',
    'Ørsted Wind Power ? QHSE Wind',
    'Ørsted ? Distribution & B2C',
    'Ørsted ? Wind Power ? EPC',
    'Ørsted ? Group Functions',
    'Ørsted Markets & Bioenergy',
    'Ørsted Radius, B2C & CityLight',
    'Ørsted Wind Power ? Partnerships & Asset Management',
    'Ørsted ? Radius, B2C & CityLight']

    Københavns_Lufthavne_list = ['Københavns Lufthavne A/S'
                         ,'Københavns Lufthavn'
                         ,'Københavns Lufthavne (CPH)'
                         ,"Københavns lufthavne"
                         ,'Copenhagen Airport Hotels A/S'
                         ,'COPENHAGEN AIRPORT HOTEL ApS'
                         ,"COPENHAGEN AIRPORTS INTERNATIONAL A/S"
                         ,"Københavns Lufthavne A/S, Hrm"]

    Kreditbanken_list = ['Kreditbanken A/S'
               ,'Kreditbanken A/S Sønderborg'
               ,'Kreditbanken A/S Tønder'
               ,'Kreditbanken'
               ,'Kreditbanken i Sønderborg'
               ,'KREDITBANKEN A/S']


    Jyske_Bank_list = ['Jyske Bank'
                  ,'Jyske Finans'
                  ,'JYSKE FINANS A/S'
                  ,'Jyske Invest']

    Jutlander_Bank_list = ['Jutlander Bank A/S'
                      ,'Jutlander Bank'
                      ,'Jutlander Bank AS'
                      ,'JUTLANDER BANK A/S'
                      ,' Jutlander Bank A/S']

    Jeudan_list = ['Jeudan A/S'
              ,'Jeudan'
              ,'JEUDAN A/S'
              ,'Jeudan Servicepartner A/S'
              ,'JEUDAN SERVICEPARTNER A/S'
              ,'Jeudan Servicepartner']

    ISS_list = ['ISS A/S'
           ,'ISS World Services A/S'
           ,'ISS World'
           ,'ISS Facility Services A/S'
           ,'ISS Facility Services AS'
           ,'Personalehuset - Part of ISS Facility Services A/S'
           ,'HR afd. i ISS Facility Services A/S'
           ,'Medarbejderfond for ansatte i ISS Facility Services A/S'
           ,'ISS FACILITY SERVICES A/S'
           ,'ISS Facility Services A/S Fredericia Sygehus'
           ,'ISS Facility Services'
           ,'ISS Facility Service'
           ,'ISS Facility Service A/S Rexam Galss Holmegaard A/S'
           ,'Iss Facility Services A/S'
          ,'ISS Facility Services A/S Rødby Færge'
         ,'ISS Facility Services A/S CSC Scandihealth A/S'
         ,'ISS Facility Services A/S Rexam Glass Holmegaard A/S'
         ,'ISS Facility Services A/S Salg'
         ,'ISS Facility Services A/S - El-Partners'
         ,'ISS Facility Services A/S Kolding Sygehus'
         ,'ISS Facility Services A/S Ringsted Sygehus'
         ,'Hørsholm Hospital, ISS Facility Services'
        ,'Hørsholm Hospital, ISS Facility Services'
         ,'ISS Facility Services A/S Office Support'
         ,'ISS Facillity Services A/S'
         ,'ISS Facility Service A/S'
         ,'ISS Facility Services A/S Sønderborg Sygehus'
         ,'ISS Facility Services A/S Aabenraa Sygehus'
         ,'ISS Facility Services A/S Bilka'
         ,'ISS Facility Services A/S Haderslev sygehus'
         ,'Iss Facility Services'
           ,'ISS Services A/S']

    InterMail_list = ['Intermail Danmark A/S'
                 ,'InterMail'
                 ,'InterMail A/S'
                 ,'InterMail Solutions A/S'
                 ,'Intermail Solutions']

    Hvidbjerg_Bank_list = ['Hvidbjerg Bank'
                      ,'Hvidbjerg Bank Aktieselskab'
                      ,'Hvidbjerg Bank Holstebro'
                      ,'HVIDBJERG BANK'
                      ,'HVIDBJERG BANK A/S'
                      ,'Hvidbjerg bank']

    HusCompagniet_list = ['HusCompagniet A/S'
                    ,'Huscompagniet Midt- og Nordjylland A/S'
                     ,'HusCompagniet'
                     ,'HusCompagniet Sjælland A/S'
                     ,'HusCompagniet Midt- og Nordjylland A/S'
                     ,'HusCompagniet Fyn A/S'
                     ,'Huscompagniet Sjælland A/S'
                     ,'Huscompagniet A/S'
                     ,'HusCompagniet as'
                     ,'HusCompagniet Midt- og Nordjylland'
                     ,'HusCompagniet Sønderjylland as']

    Harboes_Bryggeri_list = ['Harboes Bryggeri A/S'
                          ,'HARBOES BRYGGERI A/S']

    H_H_International_list = ['H+H International A/S'
                         ,'H+H Danmark A/S'
                         ,'H+H EJENDOMME A/S']

    Gyldendal_list = ['Gyldendals Bogklubber'
                 ,'Gyldendal A/S'
                 ,'Gyldendal'
                 ,'GYLDENDAL'
                 ,'GYLDENDAL A/S'
                 ,'Forlaget Gyldendal A/S'
                 , 'Gyldendal Uddannelse'
                 , 'Gyldendal Business'
                 ,'Gyldendal Akademisk A/S'
                 ,'Gyldendal Akademisk'
                 ,'Gyldendal Digital']

    Grønlandsbanken_list = ['Grønlandsbanken A/S'
                 ,'Grønlandsbanken Qaqortoq afdeling'
                 ,'GrønlandsBANKEN'
                 ,'Grønlandsbanken'
                 ,'GrønlandsBANKEN A/S']


    GreenMobility_list = ['GreenMobility'
                      ,'GreenMobility A/S'
                     ,'Green Mobility A/S']

    GN_Store_Nord_list = ['GN Store Nord',
                     'GN Store Nord A/S',
                     'GN STORE NORD A/S',
                     'GN Store Nord as',
                     'Gn Store Nord A/S'
                     'GN AUDIO A/S', 'GN Audio A/S', 'GN Audio'
                     'GN FalCom'
                     'GN Hearing A/S', 'GN HEARING A/S', 'GN Hearing DK A/S', 'GN Hearing',
                     'Dansk HøreCenter',
                     'Dansk Hørecenter',
                     'DANSK HØRETEKNIK A/S']

    Glunz_and_Jensen_Holding_list = ['Glunz & Jensen A/S',
    'Glunz & Jensen Microflex A/S',
    'Glunz & Jensen',
    'GLUNZ & JENSEN A/S',
    'GLUNZ & JENSEN MICROFLEX A/S']

    Genmab_list = ['Genmab A/S', 'Genmab', 'Genmab AS', 'Genmab A/S,']

    Gabriel_Holding_list = ['GABRIEL A/S','Gabriel A/S','Gabriel'] 

    G4S_plc_list = ['G4S Security Services A/S',
    'G4S',
    'G4S SECURITY SERVICES A/S',
    'G4S Security Services',
    'G4S SECURITY SERVICES A/S - Århus',
    'G4S SECURITY SERVICES A/S Billetbetaling',
    'G4S Vagt A/S',
    'G4S Vagt',
    'G4S vagt A/S',
    'G4S Security Service A/S',
    'G4S VAGT A/S']

    Fynske_Bank_list = ['Fynske Bank A/S',
    'Fynske Bank Nyborg Afd.',
    'Fynske Bank Assens Afd.',
    'Fynske Bank Fredericia Afd.',
    'Fynske Bank',
    'Fynske Bank Assens',
    'Fynske Bank Børkop',
    'Fynske Bank Svendborg',
    'Leasing Fyn Bank A/S',
    'Leasing Fyn',
    'LEASING FYN BANK A/S',
    'Leasing Fyn & Factoring Bankaktieselskab',
    'LEASING FYN & FACTORING BANKAKTIESELSKAB',
    'LEASING FYN & FACTORING BANKAKTIESELSKAB.']

    Flügger_group_list = ['Flügger A/S','FLÜGGER FARVER',
    'Flügger','Flügger Farver',
    'Flügger farver Årslev',
    'Flügger A/s',
    'Flügger A/S, Salgsafdeling A086 Ringkøbing',
    'FLÜGGER A/S, SALGSAFDELING',
    'FLüGGER A/S, SALGSAFDELING',
    'FLÜGGER A/S',
    'Flügger farver',
    'Flügger i Ørbæk v/Mette Marie Stokholm',
    'FLÜGGER FARVER V/MALERMESTER PAUL ISVIK',
    'Flügger HR',
    'Flügger farver, Frank Kristensen, Ringparkens Butikstorv',
    'Flügger farver A/S',
    'FLÜGGER A/S SALGSAFDELING',
    'Flügger Group',
    'FLÜGGER A/S Salgsafdeling',
    'Flügger farvehandel',
    'FLÜGGER Farver']

    FLSmidth_list = ['FLSmidth',
    'FLSmidth, Inc.',
    'FLSmidth Private Limited',
    'FLSMIDTH & CO. A/S',
    'FLSmidth & Co. A/S',
    'flsmidth-inc',
    'Flsmidth A/s',
    'Flsmidth & Co. A/s',
    'FLSmidth HAMBURG GmbH',
    'FLSmidth A/S',
    'FLSmidth Group Communications',
    'Flsmidth A/S',
    'FLSMIDTH A/S',
    'FLSmidth Airtech',
    'FLSmidth Airloq',
    'FLSmidth Automation',
    'FLSmidth Airloq A/S',
    'FLSmidth Minerals A/S']

    FirstFarms_list = ['FirstFarms A/S']

    Fast_Ejendom_Danmark_list = ['Fast Ejendom Danmark A/S']

    DSV_Panalpina_list = ['DSV',
    'DSV Transport A/S',
    'DSV Road A/S',
    'DSV A/S',
    'DSV Brøndby',
    'DSV Esbjerg',
    'DSV Miljø A/S',
    'DSV Solutions',
    'DSV Miljø',
    'DSV Road',
    'DSV Group IT',
    'DSV Air & Sea A/S',
    'DSV ROAD A/S',
    'DSV Road Holding A/S',
    'Støvring Biltransport DSV Road A/S',
    'DSV Air & Sea',
    'DSV Road A/S, Carlsberg',
    'DSV TRANSPORT A/S',
    'DSV Solutions A/S']


    Drilling_Company_of_1972_list = ['Maersk Drilling A/S',
    'Maersk Drilling',
    'A.P. Møller - Mærsk A/S (Maersk Drilling)',
    'Maersk Drilling Services A/S',
    'Mærsk Drilling',
    'A. P. Møller Mærsk Drilling',
    'A.P. Møller - Mærsk - Drilling SAP',
    'A.P. Møller - Mærsk - Drilling',
    'Maersk Drilling Norge A/S',
    'MÆRSK Drilling']

    Djurslands_Bank = ['Djurslands Bank',
    'Djurslands Bank A/S',
    'DJURSLANDS BANK',
    'DJURSLANDS BANK A/S ALLINGAABRO AFD.',
    'DJURSLANDS BANK A/S GRENAA AFDELING',
    'DJURSLANDS BANK A/S KOLIND AFDELING',
    'DJURSLANDS BANK A/S']


    DFDS_list = ['DFDS',
    'DFDS A/S',
    'DFDS AS',
    'Dfdsseaways',
    'DFDS Group',
    'DFDS a/s',
    'DFDS House',
    'DFDS Canal Tours',
    'DFDS Canal Tours A/S',
    'DFDS Seaways A/S',
    'DFDS Seaways',
    'DFDS Transport A/S, dsv',
    'DFDS TRANSPORT A/S',
    'DFDS Transport A/S',
    'DFDS CANAL TOURS A/S',
    'DFDS Tor Line']

    Demant_list = ['Demant',
    'William Demant Group',
    'William Demant',
    'William Demant Holding A/S',
    'WILLIAM DEMANT HOLDING A/S',
    'William Demant Holding',
        'Interacoustics A/S', 'INTERACOUSTICS A/S',
          'Oticon',
    'Oticon Medical',
    'Oticon A/S',
    'OTICON A/S',
          'Audika',
          'Bernafon', 'Bernafon - Phonic Ear A/S'
    ]

    Dantax_list = [
    'Dantax Radio A/S',
    'Dantax',
    'Dantax Radio',
    'Dantax Steuerberatungsgesellschaft mbH',
    'Dantax Steuerberatungsgesellschaft mbh',
    'DANTAX Steuerberatungsgesellschaft mbH']

    Danske_Bank_list = ['Danske Bank',
    'Danske Bank A/S',
    'Danske Bank A/s',
    'Danske Bank-koncernen',
    'Danske Bank Group',
    'DANSKE BANK A/S',
    'Danske Bank IT',
    'Danske Bank (.com)',
    'Den Danske Bank A/S',
    'Den Danske Bank','Danske Invest Administration A/S', 'Danske Invest',
              'Realkredit Danmark','Realkredit Danmark A/S','home a/s','home a/s',
    'Home A/S',
    'Home A/s','Danica Pension','MobilePay', 'Mobilepay']


    Danske_Andelskassers_Bank_list = ['Danske Andelskassers Bank A/S',
    'Danske Andelskassers Bank AS',
    'Danske Andelskassers Bank A/S - Augustenborg',
    'Danske Andelskassers Bank',
    'DANSKE ANDELSKASSERS BANK A/S']


    D_S_Norden_list = ['Dampskibsselskabet NORDEN A/S',
    'Dampskibsselskabet NORDEN',
    'Dampskibsselskabet Norden A/S',
    'DAMPSKIBSSELSKABET NORDEN A/S',

                  'Norient Product Pool ApS']


    Copenhagen_Capital_list = ['Copenhagen Capital A/S']


    Columbus_list = ['Columbus A/S',
    'Columbus Danmark A/S',
    'Columbus',
    'COLUMBUS A/S',
    'Columbus A/s']

    Coloplast_B_list = ['Coloplast A/S',
    'Coloplast Danmark A/S',
    'Coloplast',
    'Coloplast Ltd',
    'COLOPLAST A/S',
    'Coloplast Denmark and Emerging Markets']


    Chr_Hansen_Holding_list = ['Chr. Hansen Holding A/S']

    ChemoMetec_list = ['ChemoMetec A/S', 'CHEMOMETEC A/S', 'Chemometech', 'Chemometec A/S']

    cBrain_list = ['cBrain A/S',
    'cBrain',
    'CBrain A/S',
    'CBRAIN',
    'cBrain Technology',
    'cBrain Technology Copenhagen']

    Carlsberg_list = ['Carlsberg Danmark',
    'Carlsberg Breweries A/S',
    'Carlsberg Group',
    'Carlsberg Group A/S',
    'Carlsberg Danmark A/S',
    'Visit Carlsberg',
    'Carlsberg',
    'Carlsberg Group Procurement AG',
    'Carlsberg A/S Ejendomme',
    'CARLSBERG EJENDOMME HOLDING A/S',
    'Carlsberg Danmark AS',
    'CARLSBERG BREWERIES A/S',
    'Carlsbergfondet',
    'Carlsberg IT A/S',
    'CARLSBERG DANMARK A/S C/O PERSONALE',
    'Carlsberg A/S',
    'Carlsberg Group HR',
    'Carlsberg Danmark A/S Tuborg FB/Terminal Vest/Fredericia',
    'Carlsberg Danmarks',
    'CARLSBERG Danmark A/S Depot Holstebro',
    'CARLSBERG DANMARK A/S Depot Århus',
    'CARLSBERG Danmark A/S Depot Næstved']

    Brøndby_IF_list = ['Brøndby IF Arrangementer','Brøndbyernes IF'] # dobbeltjek

    brdr_hartmann_list = ['Brødrene Hartmann A/S', 'Brødrene Hartmann', 'BRØDRENE HARTMANN A/S']

    Brødrene_A_O_Johansen_list = ['Brødrene A & O Johansen A/S',
    'Brødrene A&O Johansen A/S',
    'Brødrene A. & O. Johansen A/S',
    'Brødrene A&O Johansen',
    'BRØDRENE A. & O. JOHANSEN A/S',
    'Brødrene A & O Johansen A/S, Hovedstaden',
    'Brødrene A. & O. Johansen A/s',
    'AO - Brødrene A & O Johansen A/S',
    'Brødrene A & O Johansen',
    'Brødrene A & O Johansen A/S Nykøbing F',
    'BRØDRENE A & O JOHANSEN A/S',
    'Brødrene Ao Johansen',
    ]



    Boozt_list = ['Boozt Fashion',
    'Boozt',
    'Boozt Fashion AB',
    'Boozt.com']

    Boliga_Gruppen_list = ['Boliga Gruppen A/S','Boliga','Boliga ApS','Boliga Aps', 'Boliga.dk']

    blue_vision_list = ['Contra A/S','CONTRA A/S','Contra - Hillerød',
    'Contra - Helsingør','ConTra International','Contra - Viborg','ConTra Denmark','Contra','ConTra']

    BioPorto_list = ['BioPorto A/S',
    'BioPorto Diagnostics A/S',
    'BioPorto Diagnostics',
    'Bioporto Diagnostics A/S',
    'BIOPORTO A/S',
    'Bioporto A/S']

    Bavarian_Nordic_list = ['Bavarian Nordic A/S', 'Bavarian Nordic', 'BAVARIAN NORDIC A/S']

    BankNordik_list = ['BankNordik',
    'P/F Banknordik',
    'P/F Banknordik Lyngby',
    'Banknordik',
    'BANKNORDIK']

    Bang_Olufsen_list = ['Bang & Olufsen A/S',
    'Bang & Olufsen America Inc.',
    'Bang & Olufsen a/s',
    'Bang & Olufsen Operations',
    'Bang & Olufsen Operations a/s','B&O PLAY']

    Atlantic_Petroleum = ['Atlantic Petroleum P/F']

    Ambu_list = ['Ambu A/S','Ambu',
    'Ambu Denmark','Ambu A/s','AMBU A/S']


    Alm_Brand_list = ['Alm. Brand',
    'Alm. Brand A/S',
    'Alm. Brand Forsikring A/S',
    'Alm. Brand Forsikring A/s',
    'Alm. Brand A/s',
    'Alm. Brand Forsikring',
    'Alm. Brand Bank A/S',
    'Alm. Brand Leasing A/S',
    'Alm. Brand Bank',
    'Alm. Brand Markets',
    'Alm. Brand Asset Management',
    'Alm. Brand BANK',
    'ALM. BRAND A/S',
    'Alm. Brand Region Syd',
    'ALM. BRAND FINANS A/S',
    'ALM. BRAND BANK',
    'ALM. Brand',
    'Alm. Brand Finans',
    'ALM. BRAND',
    'Alm. Brand Henton',
    'ALM. BRAND REGION SYD']


    ALK_Abello_list =['ALK-Abelló A/S',
    'Alk-Abelló A/S',
    'ALK-Abelló',
    'ALK-Abelló Arzneimittel GmbH',
    'ALK-abelló','ALK Abello'
    'ALK-Abello',
    'Alk-Abello A/S',
    'ALK-Abello A/S']

    AGF_list = ['AGF A/S', 'AGF','AGF Fodbold','AGF Håndbold','AGF Svømning','AGF Tennis']

    AaB_list = ['AaB esport', 'AaB A/S','Aalborg Boldspilklub A/S', 'AALBORG BOLDSPILKLUB AF 1885']

    A_P_Møller_Mærsk_list = ['Mærsk Container Industri',
    'Mærsk Container Industry A/S',
    'A.P. Møller - Mærsk A/S',
    'A.P. Møller - Mærsk A/S (Maersk Tankers)',
    'A.P. Møller - Mærsk',
    'A.P. Møller - Mærsk A/S (Maersk Drilling)',
    'Mærsk Line',
    'Maersk Group - A.P. Møller Mærsk',
    'A.P. MØLLER - MÆRSK A/S',
    'Mærsk Mc-Kinney Møller Videncenter',
    'A.P. Møller-Mærsk',
    'MÆRSK OLIE OG GAS A/S',
    'Mærsk',
    'Mærsk Drilling',
    'A. P. Møller Mærsk SAP',
    'A. P. Møller Mærsk Supply Service',
    'A. P. Møller Mærsk FPSOs',
    'A. P. Møller-Mærsk',
    'A. P. Møller Mærsk Oil Gas',
    'A.P. Møller Mærsk Line',
    'A. P. Møller Mærsk Damco',
    'Mærsk Olie og Gas AS',
    'Mærsk Oil Trading',
    'Mærsk Olie og Gas A/S (Esbjerg)',
    'A. P. Møller Mærsk Headquarters',
    'A. P. Møller Mærsk Tankers',
    'A. P. Møller Mærsk LNG',
    'Mærsk Oil',
    'Mærsk Olie og Gas',
    'Mærsk Tankers',
    'A.P. Møller Mærsk',
    'A.P. Møller - Mærsk Gruppen',
    'MÆRSK OLIE OG GAS',
    'A.P. Møller - Mærsk - Headquarters',
    'A.P. Møller - Mærsk - Oil Gas',
    'A.P. Møller - Mærsk - Line',
    'A.P. Møller - Mærsk - Drilling',
    'A.P. Møller - Mærsk - Ship Management',
    'Mærsk A/S',
    'A. P. Møller Mærsk',
    'A.P. Møller - Mærsk - Damco',
    'A.P. Møller - Mærsk - Tankers',
    'A.P. Møller - Mærsk - Oil gas',
    'A.P.Møller-Mærsk',
    'A. P. Møller - Mærsk A/S',
    'Mærsk Olie og GAS AS',
    'A. P. Møller Mærsk Container Industry',
    'Mærsk Line (Container Business)',
    'Mærsk Oil Qatar',
    'A.P. Møller-Mærsk Gruppen',
    'Mærsk Container Industri AS',
    'Mærsk Olie og Gas A/S',
    'AP Møller-Mærsk A/S',
    'A.P. Møller - MÆRSK OLIE OG GAS A/S',
    'Mærsk Contractors',
    'Maersk Oil, Mærsk Olie og Gas',
    'MÆRSK CONTAINER INDUSTRI A/S',
    'Mærsk Olie & Gas A/S',

    'A.P. Møller ? Maersk A/S',
    'A.P. Møller - Maersk A/S',
    'Maersk Container Industry (MCI)',
    'Maersk Supply Service',
    'Maersk Tankers',
    'Maersk Broker',
    'Maersk Training A/S',
    'A.P. Møller - Mærsk A/S (Maersk Tankers)',
    'Maersk Line',
    'Maersk',
    'A.P. Møller \x96 Maersk A/S',
    'Maersk Oil Trading',
    'A.P. Møller ? Maersk',
    'Sealand ? A Maersk Company',
    'Maersk Management Consulting',
    'Maersk Drilling',
    'Maersk Procurement',
    'Maersk Oil',
    'Maersk Management Consulting, A.P. Moller',
    'MAERSK CONTAINER INDUSTRY A/S',
    'Maersk Digital',
    'MAERSK',
    'Maersk Line A/S',
    'A.P. Møller Maersk A/S',
    'A.P. Moeller - Maersk A/S',
    'A.P. Møller - Maersk',
    'Maersk Group Functions'
    'Maersk Training',
    'Maersk Oil Trading Lubricants',
    ' Maersk Oil Trading',
    ' Maersk Management Consulting',
    'Maersk Group - A.P. Møller Mærsk',
    'Maersk Training Svendborg',
    'Maersk Group',
    'Maersk Maritime Technology',
    'Maersk FPSOs',
    'Maersk Line ',
    'Maersk H2S Safety Services',
    'Maersk Training Esbjerg',
    'Maersk FPSO',
    'Maersk In-house Consulting',
    'MAERSK TRAINING SVENDBORG A/S',
    'MAERSK LINE',
    'Maersk Container Industry',
    'A.P. Moller - Maersk',
    'Maersk Fluid Technology',
    'Maersk A/S',
    'AP MOLLER MAERSK',
    'Maersk Training Svendborg A/S',
    'Maersk Broker Agency',
    'Maersk Oil A/S',
    'Maersk Drilling Services A/S',
    'A.P. Moller - Maersk A/S',
    'Maersk Broker K/S',
    'MAERSK TRAINING ESBJERG A/S',
    'MAERSK OIL',
    'K.T. Maersk-Net v/ Tino Kristian Mærsk',
    'Maersk Supply Service A/S',
    'A.P. Moller/Maersk',
    'A.P. Moller - Maersk Group',
    'Maersk Tankers A/S',
    'A. P. Møller Maersk',
    'Maersk Oil Trading A/S',
    'Maersk Training Centre, Esbjerg',
    'Maersk Training Centre',
    'PSDM Modell Builder - Maersk Oil',
    'Maersk Container Industry AS',
    'Maersk Training, Svendborg',
    'Maersk Broker K/S Agency',
    'Maersk Maritime Officer',
    'Maersk LNG',
    'A.P. Møller Maersk',
    'Maersk Container Industry AS (MCI)',
    'Maersk Group - Corporate Headoffice',
    'MAERSK BROKER K/S',
    'Maersk Logistisk/Damco',
    'Maersk Ship Management',
    'Maersk Container Industri AS',
    'A.P. Moller-Maersk Group',
    'MAERSK TRAINING CENTRE A/S',
    'Maersk Procurement Singapore',
    'Maersk Tankers & Maersk Oil Trading',
    'Maersk Crew Management',
    'A.P M ¸ller Maersk',
    'A.P. Moller Maersk Group',
    'A. P. Moller - Maersk Group',
    'Maersk Logistics',
    'K.T. Maersk-Net v/ Kristian Tino Mærsk',
    'Maersk Training Centre A/S',
    'Maersk Contractors',
    'A.P.Moller-Maersk',
    'Maersk MITAS',
    'Maersk Contractors Norge AS',
    'A.P.Moller-Maersk Group',
    'Maersk Oil Qatar AS',
    'Maersk Drilling Norge A/S',
    'Maersk Training Centre A / S',
    'Maersk Oil, Mærsk Olie og Gas',
    'Maersk Line, Maersk Logistics',
    'Maersk Line og Maersk Logistics i Århus',
    'Maersk Oil Qatar as',
    'Maersk Broker A/S',
    'Maersk Line and Maersk Logistics',
    'A.P. Møller-Maersk Group',
    'esbjerg@maerskoil.dk',
    'Maersk Oil Qatar A/S',
    'Maersk Construction Consultants']

    list_of_names = ['Ørsted', 'Zealand Pharma', 'Vestjysk Bank', 'Vestas Wind Systems', 'Tryg', 'Totalbanken', 'TORM A', 'Topdanmark', 'Tivoli A/S', 'TCM Group', 'Sydbank', 
    'Sparekassen Sjælland-Fyn', 'Spar Nord Bank', 'SP Group', 'Solar B', 'Skjern Bank', 'SKAKO', 'Schouw & Co.', 'Scandinavian Tobacco Group', 'Scandinavian Brake Systems',
    'SAS', 'Sanistål', 'RTX', 'Royal UNIBREW', 'Rovsing', 'Rockwool Int. B', 'Roblon B', 'Ringkjøbing Landbobank', 'Rias B', 'Per Aarsleff Holding B',
    'Park Street Nordicom A', 'Pandora', 'Orphazyme', 'Novo Nordisk B', 'NTR Holding B', 'NTG Nordic Transport Group', 'Novozymes B', 'North Media', 'Nordfyns Bank',
    'Nordea Bank Abp','NNIT', 'NKT', 'Nilfisk Holding', 'Netcompany Group', 'Møns Bank', 'MT Højgaard Holding', 'Migatronic B', 'Matas', 'Lån og Spar Bank', 'Luxor B',
    'Lundbeck', 'Lollands Bank', "Københavns Lufthavne",'Kreditbanken',"JyskeBank",'Jutlander Bank','Jeudan','ISS',"InterMail",'Hvidbjerg Bank','HusCompagniet','Harboes Bryggeri B',
                'H+H International','Gyldendal B','Grønlandsbanken','GreenMobility','GN Store Nord','Glunz & Jensen Holding','Genmab','Gabriel Holding'
                ,'G4S plc','Fynske Bank','Flügger group B','FLSmidth & Co.','FirstFarms','Fast Ejendom Danmark','DSV Panalpina','Drilling Company of 1972',
                'Djurslands Bank','DFDS','Demant','Dantax','Danske Bank','Danske Andelskassers Bank','D/S Norden','Copenhagen Capital','Columbus','Coloplast B',
                'Chr. Hansen Holding', 'ChemoMetec','CBRAIN','Carlsberg','Brøndby IF','Brdr.Hartmann','Brdr. A & O Johansen præf.','Boozt','Boliga Gruppen',
                'Blue Vision A','BioPorto','Bavarian Nordic','BankNordik','Bang & Olufsen','Atlantic Petroleum','Ambu','Alm. Brand','ALK-Abelló B','AGF B',
                'AaB','A.P. Møller - Mærsk B']
    
    list_of_lists = [oersted_list, zealand_pharma_list, vestjysk_list, vestas_list, tryg_list, totalbanken_list, torm_list, topdanmark_list, tivoli_list, tcm_list, sydbank_list,
    sparekassen_list, sparnord_list, sp_group_list, solar_list, skjern_list, skako_list, schouw_list, scandinavian_list, brakesystem_list, sas_list, sani_list, rtx_list,
    royal_list, rovsing_list, rockwool_list, roblon_list, ringbank_list, rias_list, aarslef_list, nordicom_list, pandora_list, orphazyme_list, novo_list,ntr_list,
    ntg_list, novozym_list, northmedia_list, nordfyns_list, nordea_list, nnit_list, NKT_list,nilfisk_list, netcompany_list, mon_bank_list, mt_hojgaard_list,miga_list, matas_list,
    laan_spar_list,luxor_list,lundbeck_list,lolland_list,Københavns_Lufthavne_list,Kreditbanken_list,Jyske_Bank_list,Jutlander_Bank_list,Jeudan_list,ISS_list,InterMail_list,Hvidbjerg_Bank_list,HusCompagniet_list,
                Harboes_Bryggeri_list,H_H_International_list,Gyldendal_list,Grønlandsbanken_list, GreenMobility_list,GN_Store_Nord_list,Glunz_and_Jensen_Holding_list,
                Genmab_list,Gabriel_Holding_list,G4S_plc_list,Fynske_Bank_list,Flügger_group_list,FLSmidth_list,FirstFarms_list,Fast_Ejendom_Danmark_list,DSV_Panalpina_list,
                Drilling_Company_of_1972_list,Djurslands_Bank,DFDS_list,Demant_list,Dantax_list,Danske_Bank_list,Danske_Andelskassers_Bank_list,D_S_Norden_list,Copenhagen_Capital_list,
                Columbus_list,Coloplast_B_list,Chr_Hansen_Holding_list,ChemoMetec_list,cBrain_list ,Carlsberg_list,Brøndby_IF_list,brdr_hartmann_list,Brødrene_A_O_Johansen_list,Boozt_list,
                Boliga_Gruppen_list,blue_vision_list,BioPorto_list,Bavarian_Nordic_list,BankNordik_list,Bang_Olufsen_list,Atlantic_Petroleum,Ambu_list,Alm_Brand_list,
                ALK_Abello_list,AGF_list,AaB_list]

    list_of_dfs = []
    
    for list_, name_ in zip(list_of_lists, list_of_names):
        temp = df.copy()
        
        temp['real_firm_name'] = np.where(temp.firma.isin(list_) == True
                                   , name_
                                   , 'delete')

        temp = temp[temp.real_firm_name != 'delete'].drop_duplicates('ID')
        
        list_of_dfs.append(temp)
    
    return pd.concat(list_of_dfs)