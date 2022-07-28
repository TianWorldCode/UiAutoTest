import yaml
import config


def detail_yaml(file):
    with open(file, encoding='utf-8') as allData:
        case_data = yaml.load(allData.read(), Loader=yaml.FullLoader)
        case_data_list = []
        for data in case_data:
            case_data_list.append(data)
        return case_data_list

