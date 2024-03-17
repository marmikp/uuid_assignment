from pyannote.audio import Model, Inference, Pipeline
from pyannote.core import Segment

huggingface_token = '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'

model = Model.from_pretrained("pyannote/embedding",
                              use_auth_token=huggingface_token)

inference = Inference(model, window="whole")

diarization_pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.0", use_auth_token=huggingface_token)


def get_embeddings(audio_file, segment: Segment):
    return inference.crop(audio_file, segment)


def get_diarization(audio_file):
    diarization = diarization_pipeline(audio_file)
    segments = []
    for segment, _, sp in diarization.itertracks(yield_label=True):
        segments.append(segment)
    return segments


if __name__ == '__main__':
    get_diarization("/home/marmik/[134Pincode.jpg]_Rajasthan-Bikaner-20230828054732805_881.wav")