import json
import glob
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def clean_json(json_file):
    conditions = [
        u'',
        u'brak uwag',
        u'brak zarzut\u00f3w',
        u'brak m\u0119\u017c\xf3w zaufania w obwodzie',
        u'brak zarz\u0105dze\u0144'
        ]
    clean_data_arr = []
    for obj in json_file[u'records']:
        clean_data = {k: v for k, v in obj.iteritems() if not v in conditions}
        clean_data_arr.append(clean_data)

    return clean_data_arr


def converter():
    jsons = []
    for file_name in glob.glob('./*.json'):
        jsons.append(open(file_name, "r+b"))

    # single_json_file = open('sejmik_warszawa.json', 'r+b')
    # destined_file = open('sejmik_warszawa_json.json', 'r+b')

    for json_file in jsons:
        json_to_clean = json.load(json_file)
        json_to_clean = clean_json(json_to_clean)
        json_converted = json.dumps(json_to_clean, ensure_ascii=False, indent=4).encode('utf-8')
        json_file.seek(0)
        json_file.truncate()
        json_file.write(unicode(json_converted))


converter()
