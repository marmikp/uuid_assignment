import traceback


class AssetLevelValidations:
    def __init__(self, asset, db_asset_repo):
        self.asset = asset
        self.db_asset_repo = db_asset_repo

    def check_sample_rate(self, condition_value=16000):
        if self.asset.metadata['sample_rate'] != condition_value:
            self.asset.errors.append(
                f"Sample rate is not valid. Expected {condition_value} got {self.asset.metadata['sample_rate']}")
            self.asset.approved = False

    def check_bit_depth(self, condition_value=16):
        if self.asset.metadata['bit_depth'] != condition_value:
            self.asset.errors.append(
                f"Bit Depth is not valid. Expected {condition_value} got {self.asset.metadata['bit_depth']}")
            self.asset.approved = False

    def check_channels(self, condition_value=1):
        if self.asset.metadata['channels'] != condition_value:
            self.asset.errors.append(
                f"Channels is not valid. Expected {condition_value} got {self.asset.metadata['channels']}")
            self.asset.approved = False

    def check_format(self, condition_value=1):
        if self.asset.metadata['format'] != condition_value:
            self.asset.errors.append(
                f"Bit Depth is not valid. Expected {condition_value} got {self.asset.metadata['format']}")
            self.asset.approved = False

    def check_phrase_id(self):
        try:
            if self.db_asset_repo.get_phrase_id(self.asset.row.get_entity('script')) is None:
                self.asset.errors.append(f"Phrase is not valid, Phrase={self.asset.row.get_entity('script')}")
                self.asset.approved = False
        except:
            # traceback.print_exc()
            self.asset.errors.append(f"Phrase is not valid, Phrase={self.asset.row.get_entity('script')}")
            self.asset.approved = False
            print(f"Asset is rejected, approved value is {self.asset.approved}")

    def __call__(self):
        self.check_format()
        self.check_channels()
        self.check_sample_rate()
        self.check_bit_depth()
        self.check_phrase_id()
        self.asset.row.set_entity('asset_approved', self.asset.approved)
        self.asset.row.set_entity('tech_rejection_reason', self.asset.get_error_str())


class UserLevelValidations:
    def __init__(self, user):
        self.user = user

    def get_approved_assets_counts(self):
        approved_counts = 0
        for task_path, asset in self.user.assets.items():
            if asset.approved:
                approved_counts += 1
        return approved_counts

    def check_assets_counts(self, min_condition_value=200, max_condition_value=235):
        approved_counts = self.get_approved_assets_counts()
        if approved_counts > max_condition_value or approved_counts < min_condition_value:
            self.user.errors.append(
                f'Assets counts are not valid. Expected counts between {min_condition_value} and {max_condition_value} got {approved_counts}')
            self.user.approved = False

    def __call__(self):
        self.check_assets_counts()
        for task_map, asset in self.user.assets.items():
            asset.row.set_entity('user_approved', self.user.approved)


class ProjectLevelValidations:
    def __init__(self, project):
        self.project = project

    def __call__(self):
        pass


class ValidationRule:
    def is_applicable(self, entity):
        raise NotImplementedError()

    def apply(self, entity):
        raise NotImplementedError()

    def get_error(self, entity):
        raise NotImplementedError()


class ModelValidation(ValidationRule):
    def __init__(self, model):
        self.model = model

    def is_applicable(self, entity):
        return isinstance(entity, self.model)

    def apply(self, entity):
        return isinstance(entity, self.model)

    def get_error(self, entity):
        return f'entity is not instance of model {type(self.model)}'
