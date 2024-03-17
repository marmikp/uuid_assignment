import csv
import json

from sklearn.cluster import DBSCAN


class UUIDs:
    def __init__(self, embedding_filepath):
        self.clusters = None
        self.embedding_filepath = embedding_filepath
        self.embedding_dict = None

    def load_embeddings(self):
        self.embedding_dict = json.load(open(self.embedding_filepath, 'r'))

    def create_clusters(self, eps=0.5, min_samples=2):
        embeddings = list(self.embedding_dict.values())
        self.clusters = DBSCAN(eps=eps, min_samples=min_samples).fit(embeddings).labels_

    def save_uuids(self, output_path):
        self.load_embeddings()
        self.create_clusters()
        fp = open(output_path, 'w')
        writer = csv.writer(fp)
        writer.writerow(['Filename', 'UUIDs'])
        filename_dict = {}
        for i, emb_file in enumerate(self.embedding_dict.keys()):
            filename = emb_file.split("_")[0]
            if filename not in filename_dict:
                filename_dict[filename] = []
            filename_dict[filename].append(str(self.clusters[i]))
        for filename, uuids in filename_dict.items():
            writer.writerow([filename, ", ".join(uuids)])
