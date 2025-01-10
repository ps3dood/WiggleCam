import struct

def create_avi_header(width, height, frame_count, frame_rate=24):
    """Create a basic MJPG AVI header for the given parameters."""
    # Calculate bytes per second, assuming 24-bit color JPEGs.
    bytes_per_sec = width * height * 3 * frame_rate
    # AVI RIFF header
    header = b'RIFF' + struct.pack('<I4s', 4 + 56 + 8 + frame_count * (8 + 8 + len(frame_data[0])), b'AVI ')
    # AVI main header
    header += (
        b'LIST\x3c\x00\x00\x00hdrlavih' +
        struct.pack('<IiiIIIIIIIIII', 56, 1000000 // frame_rate, bytes_per_sec, 0, 0, 0, frame_count, 0, width * height * 3, width, height, 1, 0)
    )
    # Stream list
    header += (
        b'LIST\x74\x00\x00\x00strlstrh' +
        struct.pack('<4sI4s4sIIIIIIII', b'vids', 56, b'MJPG', b'\x00\x00\x00\x00', 0, 1000000 // frame_rate, 1000000 // frame_rate, 0, frame_count, 1, 0, 0) +
        b'strf' +
        struct.pack('<IiIHH', 40, width, height, 1, 24)
    )
    return header

def create_avi_from_jpegs(output_name, jpeg_files):
    """Create an MJPG AVI from the given list of JPEG file names."""
    global frame_data
    frame_data = [open(f, 'rb').read() for f in jpeg_files]
    # Get dimensions from the first JPEG
    # Assuming all JPEGs have the same dimensions
    height = 0
    width = 0
    with open(jpeg_files[0], 'rb') as f:
        data = f.read()
        pos = data.find(b'\xFF\xC0')
        if pos != -1:
            height, width = struct.unpack('>HH', data[pos + 5:pos + 9])
    # Write AVI
    with open(output_name, 'wb') as f:
        f.write(create_avi_header(width, height, len(jpeg_files)))
        for data in frame_data:
            f.write(b'00db' + struct.pack('<I', len(data)))
            f.write(data)

# Example use
jpeg_files = ['img01.jpg', 'img02.jpg', 'img03.jpg', 'img02.jpg', 'img01.jpg']
create_avi_from_jpegs('output.avi', jpeg_files)
