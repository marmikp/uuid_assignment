import traceback
import logging

from sqlalchemy import and_
from sqlalchemy.orm import class_mapper

from entities.asset_entities import DBAsset, UUIDEntity, PhraseEntity
from models.asset_model import AssetModel, UUIDMapping, PhraseMapping


class DBAssetRepository:
    def __init__(self, session_factory) -> None:
        self.log = logging.getLogger(f'{__name__}.{self.__class__.__name__}')
        self.session_factory = session_factory

    def get_all(self):
        with self.session_factory() as session:
            return session.query(AssetModel).all()

    def get_entity_by_project_and_asset_name(self, project_id, asset_name):
        with self.session_factory() as session:
            asset = session.query(AssetModel).filter_by(Project_ID=project_id, Asset_Name=asset_name).first()
            return asset

    def get_non_delivered_data(self):
        with self.session_factory() as session:
            assets = session.query(AssetModel).filter_by(delivery_status=False, user_approved=True,
                                                         asset_approved=True).all()
            return [DBAsset(**asset.__dict__) for asset in assets]

    def add_asset(self, assetEnt: DBAsset):
        try:
            with self.session_factory() as session:
                asset = session.query(AssetModel).filter_by(Project_ID=assetEnt.Project_ID,
                                                            Asset_Name=assetEnt.Asset_Name).first()
                if asset is None:
                    asset = AssetModel(**assetEnt.__dict__)
                    session.add(asset)
                else:
                    for key, value in assetEnt.__dict__.items():
                        if key.startswith("__") or key in ['id']:
                            continue
                        setattr(asset, key, value)
                session.commit()
                return asset
        except:
            traceback.print_exc()

    def get_speakerId_by_uuid(self, uuid):
        try:
            with self.session_factory() as session:
                uuid_row = session.query(UUIDMapping).filter_by(Username=uuid).first()
                return uuid_row.speaker_id
        except:
            self.log.error(f'Unable to get the speaker with uuid={uuid}')
            raise

    def add_uuid(self, uuidEnt: UUIDEntity):
        with self.session_factory() as session:
            uuidmap_mapper = class_mapper(UUIDMapping)
            info = {k: v for k, v in uuidEnt.__dict__.items() if k in uuidmap_mapper.attrs.keys()}
            # self.log.info(info)
            uuid = UUIDMapping(**info)
            session.merge(uuid)
            session.commit()

    def add_phrase(self, phraseEnt: PhraseEntity):
        with self.session_factory() as session:
            phrase = PhraseMapping(**phraseEnt.__dict__)
            session.merge(phrase)
            session.commit()

    def get_phrase_id(self, phrase):
        try:
            with self.session_factory() as session:
                phrase_row = session.query(PhraseMapping).filter_by(phrase=phrase).first()
                return phrase_row.phraseId
        except Exception as e:
            self.log.error('Unable to reterive phrase %s', phrase)
            raise e

    def update_delivery_status(self, asset: DBAsset):
        try:
            with self.session_factory() as session:
                session.query(AssetModel).filter(AssetModel.id == asset.id).update({'delivery_status': True})
                session.commit()
        except Exception as e:
            self.log.error('Unable to update delivery status')
            raise e
