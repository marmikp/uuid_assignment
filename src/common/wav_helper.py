import io
import struct

from scipy.io.wavfile import _read_riff_chunk, _read_fmt_chunk, _skip_unknown_chunk


def read_data_size(fid, is_big_endian):
    if is_big_endian:
        fmt = '>'
    else:
        fmt = '<'

    # Size of the data subchunk in bytes
    size = struct.unpack(fmt + 'I', fid.read(4))[0]
    return size


def fread(fid):
    file_size, is_big_endian = _read_riff_chunk(fid)
    fmt_chunk_received = False
    data_chunk_received = False
    while fid.tell() < file_size:
        # read the next chunk
        chunk_id = fid.read(4)
        if not chunk_id:
            if data_chunk_received:
                break
            else:
                raise ValueError("Unexpected end of file.")
        elif len(chunk_id) < 4:
            msg = f"Incomplete chunk ID: {repr(chunk_id)}"
            # If we have the data, ignore the broken chunk
            if fmt_chunk_received and data_chunk_received:
                pass
            else:
                raise ValueError(msg)
        if chunk_id == b'fmt ':
            fmt_chunk_received = True
            fmt_chunk = _read_fmt_chunk(fid, is_big_endian)
            # print(fmt_chunk)
            format_tag, channels, fs = fmt_chunk[1:4]
            block_align = fmt_chunk[5]
            bit_depth = fmt_chunk[6]
        elif chunk_id == b'fact':
            _skip_unknown_chunk(fid, is_big_endian)
        elif chunk_id == b'data':
            data_chunk_received = True
            size = read_data_size(fid, is_big_endian)
            _skip_unknown_chunk(fid, is_big_endian)
        elif chunk_id == b'LIST':
            _skip_unknown_chunk(fid, is_big_endian)
        elif chunk_id in {b'JUNK', b'Fake'}:
            _skip_unknown_chunk(fid, is_big_endian)
        else:
            try:
                _skip_unknown_chunk(fid, is_big_endian)
            except:
                pass  # Ignore

    headers = ['sample_rate', 'duration', 'format', 'channels', 'bit_depth']
    row = [fs, (size / (fs * (bit_depth / 8))), format_tag, channels, bit_depth]
    return {k: v for k, v in zip(headers, row)}


if __name__ == '__main__':
    fid = io.BytesIO(open('/home/marmik/Downloads/A000002_t1_1.wav', 'rb').read())
    print(fread(fid))
