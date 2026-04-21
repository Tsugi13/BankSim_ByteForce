# brazil_geo.py
# States and their major cities with approximate lat/lng coordinates
# Coordinates are city centers used for fraud distance detection

STATES_CITIES = {
    "AC": {"name": "Acre", "cities": {
        "Rio Branco": (-9.9754, -67.8249),
        "Cruzeiro do Sul": (-7.6306, -72.6726),
        "Sena Madureira": (-9.0656, -68.6578),
    }},
    "AL": {"name": "Alagoas", "cities": {
        "Maceió": (-9.6658, -35.7350),
        "Arapiraca": (-9.7522, -36.6616),
        "Palmeira dos Índios": (-9.4088, -36.6252),
    }},
    "AM": {"name": "Amazonas", "cities": {
        "Manaus": (-3.1190, -60.0217),
        "Parintins": (-2.6267, -56.7358),
        "Itacoatiara": (-3.1431, -58.4442),
        "Tefé": (-3.3647, -64.7097),
    }},
    "AP": {"name": "Amapá", "cities": {
        "Macapá": (0.0349, -51.0694),
        "Santana": (-0.0583, -51.1783),
        "Laranjal do Jari": (-0.8017, -52.4572),
    }},
    "BA": {"name": "Bahia", "cities": {
        "Salvador": (-12.9714, -38.5014),
        "Feira de Santana": (-12.2664, -38.9663),
        "Vitória da Conquista": (-14.8661, -40.8444),
        "Camaçari": (-12.6997, -38.3246),
        "Ilhéus": (-14.7889, -39.0361),
        "Juazeiro": (-9.4272, -40.5014),
        "Porto Seguro": (-16.4447, -39.0642),
    }},
    "CE": {"name": "Ceará", "cities": {
        "Fortaleza": (-3.7319, -38.5267),
        "Caucaia": (-3.7361, -38.6531),
        "Juazeiro do Norte": (-7.2100, -39.3153),
        "Sobral": (-3.6886, -40.3497),
        "Maracanaú": (-3.8769, -38.6258),
    }},
    "DF": {"name": "Distrito Federal", "cities": {
        "Brasília": (-15.7801, -47.9292),
        "Ceilândia": (-15.8134, -48.1085),
        "Taguatinga": (-15.8308, -48.0569),
        "Samambaia": (-15.8761, -48.0764),
    }},
    "ES": {"name": "Espírito Santo", "cities": {
        "Vitória": (-20.3155, -40.3128),
        "Vila Velha": (-20.3297, -40.2919),
        "Serra": (-20.1289, -40.3078),
        "Cariacica": (-20.2636, -40.4197),
        "Cachoeiro de Itapemirim": (-20.8489, -41.1136),
    }},
    "GO": {"name": "Goiás", "cities": {
        "Goiânia": (-16.6864, -49.2643),
        "Aparecida de Goiânia": (-16.8233, -49.2436),
        "Anápolis": (-16.3281, -48.9531),
        "Rio Verde": (-17.7972, -50.9283),
        "Luziânia": (-16.2519, -47.9506),
    }},
    "MA": {"name": "Maranhão", "cities": {
        "São Luís": (-2.5297, -44.3028),
        "Imperatriz": (-5.5261, -47.4919),
        "São José de Ribamar": (-2.5578, -44.0653),
        "Timon": (-5.0947, -42.8369),
    }},
    "MG": {"name": "Minas Gerais", "cities": {
        "Belo Horizonte": (-19.9167, -43.9345),
        "Uberlândia": (-18.9186, -48.2772),
        "Contagem": (-19.9317, -44.0536),
        "Juiz de Fora": (-21.7642, -43.3503),
        "Montes Claros": (-16.7281, -43.8611),
        "Ribeirão das Neves": (-19.7681, -44.0828),
        "Uberaba": (-19.7481, -47.9319),
        "Governador Valadares": (-18.8514, -41.9494),
        "Ipatinga": (-19.4681, -42.5369),
        "Sete Lagoas": (-19.4658, -44.2469),
    }},
    "MS": {"name": "Mato Grosso do Sul", "cities": {
        "Campo Grande": (-20.4697, -54.6201),
        "Dourados": (-22.2211, -54.8056),
        "Três Lagoas": (-20.7511, -51.6783),
        "Corumbá": (-19.0078, -57.6508),
    }},
    "MT": {"name": "Mato Grosso", "cities": {
        "Cuiabá": (-15.5989, -56.0949),
        "Várzea Grande": (-15.6467, -56.1325),
        "Rondonópolis": (-16.4700, -54.6358),
        "Sinop": (-11.8647, -55.5039),
    }},
    "PA": {"name": "Pará", "cities": {
        "Belém": (-1.4558, -48.4902),
        "Ananindeua": (-1.3656, -48.3722),
        "Santarém": (-2.4428, -54.7081),
        "Marabá": (-5.3686, -49.1178),
        "Castanhal": (-1.2939, -47.9267),
    }},
    "PB": {"name": "Paraíba", "cities": {
        "João Pessoa": (-7.1195, -34.8450),
        "Campina Grande": (-7.2306, -35.8811),
        "Santa Rita": (-7.1128, -34.9772),
        "Patos": (-7.0228, -37.2814),
    }},
    "PE": {"name": "Pernambuco", "cities": {
        "Recife": (-8.0539, -34.8811),
        "Caruaru": (-8.2844, -35.9761),
        "Olinda": (-8.0089, -34.8553),
        "Petrolina": (-9.3975, -40.4978),
        "Paulista": (-7.9408, -34.8728),
        "Cabo de Santo Agostinho": (-8.2897, -35.0339),
        "Jaboatão dos Guararapes": (-8.1133, -35.0144),
        "Camarajibe": (-8.0211, -34.9783),
    }},
    "PI": {"name": "Piauí", "cities": {
        "Teresina": (-5.0892, -42.8019),
        "Parnaíba": (-2.9056, -41.7769),
        "Picos": (-7.0767, -41.4672),
    }},
    "PR": {"name": "Paraná", "cities": {
        "Curitiba": (-25.4297, -49.2711),
        "Londrina": (-23.3045, -51.1696),
        "Maringá": (-23.4253, -51.9382),
        "Ponta Grossa": (-25.0945, -50.1633),
        "Cascavel": (-24.9578, -53.4553),
        "São José dos Pinhais": (-25.5350, -49.2067),
        "Foz do Iguaçu": (-25.5478, -54.5882),
    }},
    "RJ": {"name": "Rio de Janeiro", "cities": {
        "Rio de Janeiro": (-22.9068, -43.1729),
        "São Gonçalo": (-22.8269, -43.0539),
        "Duque de Caxias": (-22.7856, -43.3117),
        "Nova Iguaçu": (-22.7594, -43.4511),
        "Niterói": (-22.8833, -43.1036),
        "Belford Roxo": (-22.7631, -43.3986),
        "Campos dos Goytacazes": (-21.7553, -41.3264),
        "Petrópolis": (-22.5050, -43.1786),
    }},
    "RN": {"name": "Rio Grande do Norte", "cities": {
        "Natal": (-5.7945, -35.2110),
        "Mossoró": (-5.1883, -37.3442),
        "Parnamirim": (-5.9147, -35.2631),
        "Caicó": (-6.4589, -37.0972),
    }},
    "RO": {"name": "Rondônia", "cities": {
        "Porto Velho": (-8.7619, -63.9039),
        "Ji-Paraná": (-10.8800, -61.9483),
        "Ariquemes": (-9.9111, -63.0367),
    }},
    "RR": {"name": "Roraima", "cities": {
        "Boa Vista": (2.8197, -60.6733),
        "Rorainópolis": (-0.9417, -60.4294),
    }},
    "RS": {"name": "Rio Grande do Sul", "cities": {
        "Porto Alegre": (-30.0346, -51.2177),
        "Caxias do Sul": (-29.1681, -51.1794),
        "Pelotas": (-31.7654, -52.3376),
        "Canoas": (-29.9178, -51.1839),
        "Santa Maria": (-29.6842, -53.8069),
        "Gravataí": (-29.9439, -51.0317),
        "Novo Hamburgo": (-29.6783, -51.1306),
    }},
    "SC": {"name": "Santa Catarina", "cities": {
        "Joinville": (-26.3044, -48.8487),
        "Florianópolis": (-27.5954, -48.5480),
        "Blumenau": (-26.9194, -49.0661),
        "São José": (-27.5936, -48.6350),
        "Chapecó": (-27.1006, -52.6156),
        "Criciúma": (-28.6775, -49.3697),
    }},
    "SE": {"name": "Sergipe", "cities": {
        "Aracaju": (-10.9472, -37.0731),
        "Nossa Senhora do Socorro": (-10.8539, -37.1239),
        "Lagarto": (-10.9153, -37.6522),
    }},
    "SP": {"name": "São Paulo", "cities": {
        "São Paulo": (-23.5505, -46.6333),
        "Guarulhos": (-23.4628, -46.5333),
        "Campinas": (-22.9056, -47.0608),
        "São Bernardo do Campo": (-23.6939, -46.5650),
        "Santo André": (-23.6644, -46.5350),
        "Ribeirão Preto": (-21.1775, -47.8103),
        "Osasco": (-23.5325, -46.7919),
        "Sorocaba": (-23.5015, -47.4526),
        "Mauá": (-23.6678, -46.4619),
        "Santos": (-23.9608, -46.3336),
        "São José dos Campos": (-23.1794, -45.8869),
        "Mogi das Cruzes": (-23.5228, -46.1869),
        "Bauru": (-22.3147, -49.0600),
    }},
    "TO": {"name": "Tocantins", "cities": {
        "Palmas": (-10.2491, -48.3243),
        "Araguaína": (-7.1919, -48.2044),
        "Gurupi": (-11.7256, -49.0694),
    }},
}

def get_states():
    """Returns list of (code, name) tuples sorted by name."""
    return sorted([(code, data["name"]) for code, data in STATES_CITIES.items()], key=lambda x: x[1])

def get_cities(state_code):
    """Returns list of city names for a given state code."""
    if state_code in STATES_CITIES:
        return sorted(STATES_CITIES[state_code]["cities"].keys())
    return []

def get_coords(state_code, city_name):
    """Returns (lat, lng) for a city, or None if not found."""
    try:
        return STATES_CITIES[state_code]["cities"][city_name]
    except KeyError:
        return None
