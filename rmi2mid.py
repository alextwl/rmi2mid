# rmi2mid - Extract Standard MIDI file (.mid) from RIFF MIDI (RMID) file
#           (.rmi or .mid).
#
# This is a simple tool to extract minimal RMID chunk from RIFF file
# (*.rmi or *.mid) and write MIDI data to an independent .mid file.

import struct
import sys


def rmi2mid(rmi_file, mid_file):
    '''
    Extract Standard MIDI file from RIFF MIDI (RMID) file.

    :param rmi_file: Input RIFF MIDI (RMID) file path. (.rmi or .mid)
    :type rmi_file: str
    :param mid_file: Output Standard MIDI file path. (.mid)
    :type mid_file: str
    '''
    with open(rmi_file, 'rb') as frmi:
        chunk_id = frmi.read(4)
        if chunk_id == b'MThd':
            raise IOError("Already a Standard MIDI format file: %s" % rmi_file)
        elif chunk_id != b'RIFF':
            raise IOError("Not an RIFF file: %s" % rmi_file)

        chunk_size = struct.unpack_from('<L', frmi.read(4))[0]
        chunk_raw = frmi.read(chunk_size)
        (hdr_id, hdr_data, midi_size) = struct.unpack("<4s4sL", chunk_raw[0:12])

        if hdr_id != b'RMID' or hdr_data != b'data':
            raise IOError("Invalid or unsupported input file: %s" % rmi_file)
        try:
            midi_raw = chunk_raw[12:12+midi_size]
        except IndexError:
            raise IOError("Broken input file: %s" % rmi_file)

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
