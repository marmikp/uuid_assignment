from common import readers
from common.fs_helper import FsHelper
from entities.asset_entities import CsvAssetRow


class CsvAssetsRepository:
    def __init__(self, local_fs_helper: FsHelper):
        self.local_fs_helper = local_fs_helper

    def get_assets(self, asset_csv):
        reader = self.local_fs_helper.get_reader(asset_csv, encoding='utf-8')
        rows = readers.CsvReader(reader).get_rows()
        return [CsvAssetRow(**row) for row in rows if row['Job_Status'] == 'ready_for_delivery' and row['Asset_Path'] not in [None, '']]
