from pep_parse.constants import EXPECTED_STATUS


def get_status_code(status_code):
    if len(status_code) == 2:
        for key, values in EXPECTED_STATUS.items():
            if status_code[1] in key:
                return values
    else:
        return ''
