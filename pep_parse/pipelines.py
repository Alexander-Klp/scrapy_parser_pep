import csv
import datetime as dt

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = {}

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary__{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            f.write('Статус,Количество\n')
            for status, count in self.results.items():
                writer.writerow((status, count))
            f.write(f'Total,{sum(self.results.values())}')

    def process_item(self, item, spider):
        if item['status'] in self.results:
            self.results[item['status']] += 1
        else:
            self.results[item['status']] = 1
        return item
