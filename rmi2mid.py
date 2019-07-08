# rmi2mid - Extract Standard MIDI file (.mid) from RIFF MIDI (RMID) file
#           (.rmi or .mid).
#
# This is a simple tool to extract minimal RMID chunk from RIFF file
# (*.rmi or *.mid) and write MIDI data to an independent .mid file.

import chunk
import struct
import sys


def rmi2mid(rmi_file, mid_file):
    with open(rmi_file, 'rb') as frmi:
        root = chunk.Chunk(frmi, bigendian=False)

        chunk_id = root.getname()
        if chunk_id == b'MThd':
            raise IOError("Already a Standard MIDI format file: %s" % rmi_file)
        elif chunk_id != b'RIFF':
            raise IOError("Not an RIFF file: %s" % rmi_file)

        chunk_size = root.getsize()
        chunk_raw = root.read(chunk_size)
        (hdr_id, hdr_data, midi_size) = struct.unpack("<4s4sL", chunk_raw[0:12])

        if hdr_id != b'RMID' or hdr_data != b'data':
            raise IOError("Invalid or unsupported input file: %s" % rmi_file)
        try:
            midi_raw = chunk_raw[12:12+midi_size]
        except IndexError:
            raise IOError("Broken input file: %s" % rmi_file)

        root.close()

    with open(mid_file, 'wb') as fmid:
        fmid.write(midi_raw)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: %s <.rmi or .mid> <.mid>\n" % sys.argv[0])
        sys.exit(0)

    rmi_filename, mid_filename = sys.argv[1:3]

    try:
        rmi2mid(rmi_filename, mid_filename)
    except IOError as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(22)
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)

    print("%s -> %s" % (rmi_filename, mid_filename))
    sys.exit(0)
