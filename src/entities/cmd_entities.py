from pydantic import BaseModel


class PrepareCsvsContext(BaseModel):
    directory: str
    to_directory: str
    output: str


class PrepareBatchCmdContext(BaseModel):
    csvpath: str
    batchno: int
    output: str
