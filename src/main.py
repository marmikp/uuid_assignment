"""Update Bhasha JSON Files"""

import typer
from dependency_injector.wiring import inject
from container import ApplicationContainer
from commands.get_uuids import UUIDs
from commands.save_embeddings import Embeddings

app = typer.Typer()


@inject
def save_embedding_command(dir_path, output_path):
    emb = Embeddings(dir_path, output_path)
    emb()


@inject
def get_uuid_command(embedding_filepath, output_path):
    uuids = UUIDs(embedding_filepath)
    uuids.save_uuids(output_path)


@app.command('save-embedding')
def save_embedding(dir_path, output_path):
    save_embedding_command(dir_path, output_path)


@app.command('get-uuid')
def get_uuid(embedding_path, uuid_output_path):
    get_uuid_command(embedding_path, uuid_output_path)


if __name__ == '__main__':
    app_container = ApplicationContainer()
    app_container.init_resources()
    app_container.wire(modules=[__name__])
    app()
