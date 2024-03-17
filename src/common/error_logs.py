import csv
import datetime
import os.path


class LogErrors:
    def __init__(self, filepath='generated/errors_{}.csv'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S')),
                 header=None):
        if header is None:
            header = ['Project', 'User', 'Asset', 'ProjectErrors', 'UserErrors', 'AssetErrors', 'Status']
        self.header = header
        self.filepath = filepath

    def create_writer(self):
        if not os.path.exists(os.path.dirname(self.filepath)):
            os.makedirs(os.path.dirname(self.filepath))
        self.fp = open(self.filepath, 'w')
        self.writer = csv.writer(self.fp)
        self.writer.writerow(self.header)

    def writer_logs(self, project):
        for user_id, user in project.users.items():
            for task_path, asset in user.assets.items():
                self.writer.writerow([project.project_id, user.user_id, asset.row.get_entity('Asset_Path'),
                                      project.get_error_str(), user.get_error_str(), asset.get_error_str(),
                                      'Approved' if user.approved and asset.approved else 'Rejected'])

