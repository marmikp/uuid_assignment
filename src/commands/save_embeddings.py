import json
import os

from common.embeddings_helper import get_diarization, get_embeddings
from tqdm import tqdm


class Segment:
    def __init__(self, audioPath, segment):
        self.embedding = None
        self.audioPath = audioPath
        self.segment = segment

    def generate_embedding(self):
        self.embedding = get_embeddings(self.audioPath, self.segment)


class AudioFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.segments = []

    def get_segments(self):
        return get_diarization(self.filepath)

    def generate_embeddings(self):
        for segment in self.get_segments():
            segment_ = Segment(self.filepath, segment)
            self.segments.append(segment_)
            segment_.generate_embedding()

    def get_filename(self):
        return os.path.basename(self.filepath)


class Embeddings:
    def __init__(self, dir_path, emb_output_path):
        self.dir_path = dir_path
        self.emb_output_path = emb_output_path
        self.audioFiles = []

    def collect_files(self):
        for file in os.listdir(self.dir_path):
            self.audioFiles.append(AudioFile(os.path.join(self.dir_path, file)))

    def generate_embeddings(self):
        for audioFile in self.audioFiles:
            audioFile.generate_embeddings()

    def save_embeddings(self):
        self.collect_files()
        with open(self.emb_output_path, 'w') as fp:
            self.generate_embeddings()
            embeddings_dict = {}
            for file in tqdm(self.audioFiles, desc='Generating Embeddings'):
                for i, segment in enumerate(file.segments):
                    embeddings_dict[(file.get_filename()+"_"+str(i))] = segment.embedding.tolist()
            json.dump(embeddings_dict, fp)

    def __call__(self):
        self.save_embeddings()
