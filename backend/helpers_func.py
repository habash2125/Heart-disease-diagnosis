
def preproccess_biometrics(bio_json):

    str_mappings = {'True': 1, 'False': 0, 'Yes': 1, 'No': 0 , "0" : 0}

    print(dict(bio_json))
    bio_json = dict(bio_json)
    #bio_json = json.dump({bio_json})
    
    bio_json["sex"] = int(bio_json["sex"][0])
    bio_json["cp"] = int(bio_json["cp"][0])
    bio_json["fbs"] = str_mappings[bio_json["fbs"]]
    bio_json["restecg"] = int(bio_json["restecg"][0])
    bio_json["exang"] = str_mappings[bio_json["exang"]]
    bio_json["slope"] = int(bio_json["slope"][0])
    bio_json["thal"] = int(bio_json["thal"][0])

    bio_json.pop("fbs")
    bio_vector = [int(bio_json[x]) for x in bio_json.keys()]
    print("&&&&& ",bio_vector)
    return bio_vector
