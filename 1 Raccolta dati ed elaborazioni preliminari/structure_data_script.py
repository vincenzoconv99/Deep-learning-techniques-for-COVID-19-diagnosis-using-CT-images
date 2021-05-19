import json

def get_value_in_range(value):
    trend_val = value.split('&#')
    if len(trend_val) == 1:
        return trend_val[0], 0
    else:
        if trend_val[1] == '8593;':
            return trend_val[0], 1
        elif trend_val[1] == '8595;':
            return trend_val[0], -1
        else:
            return trend_val[0], None

dict_patients = {}
key_overview = ['Hospital', 'Age', 'Gender', 'Body temperature', 
                'Underlying diseases', 'SARS-CoV-2 nucleic acids', 
                'Computed tomography (CT)', 'Morbidity outcome', 'Mortality outcome']
key_cl = ['Clinical feature', 'Abbreviation', 'Value', 'Normal range', 'Value in range'] # Value in range: 0 in range, 1 up, -1 down

with open('patient.txt', encoding="utf8") as f:
    for line in f:
        patient_id = line.split('\t')[0]
        dict_patients[patient_id] = {}
        text = line.split('\t')[9]
        if text.find("&basic_info&")>-1:
            new_item = text.split("&basic_info&")[1]
            dict_patients[patient_id]['basic_info'] = dict(zip(key_overview, 
                                                               [s.strip() for s in new_item.split('$')]))
        if text.find("&ct&")>-1:
            new_item = text.split("&ct&")[1]
            dict_patients[patient_id]['ct'] = [s.strip() for s in new_item.split('@')]

        if text.find("&cf&")>-1:
            new_item = text.split("&cf&")[1]
            clinical_features = [s.strip() for s in new_item.split('$#$')[2:]]
            dict_patients[patient_id]['cf'] = {}
            for cf in clinical_features:
                cf_row = cf.split('$')
                cf_id = cf_row[0].strip()
                l_values = []
                for val in cf.split('$')[2:]:
                    val_split = [s.strip() for s in val.split('@')]
                    if len(val_split)>2:
                        val_split[2], in_range = get_value_in_range(val_split[2])
                        val_split += [in_range]
                        l_values.append(dict(zip(key_cl, val_split)))
                dict_patients[patient_id]['cf'][cf_id] = l_values
        if text.find("&cp&")>-1:
            # Actually not found &cp& 
            new_item = text.split("&cp&")[1]
            dict_patients[patient_id]['cp'] = [s.strip() for s in new_item]
            
with open('patient.json', 'w') as fp:
    json.dump(dict_patients, fp,  indent=4)