"""frameSizeData = {
    "FRAMESIZE_96X96": [[0x60, 0x00], [0x60, 0x00]],
    "FRAMESIZE_QQVGA": [[0xA0, 0x00], [0x78, 0x00]],
    "FRAMESIZE_QCIF": [[0xB0, 0x00], [0x90, 0x00]],
    "FRAMESIZE_HQVGA": [[0xF0, 0x00], [0xB0, 0x00]],
    "FRAMESIZE_240X240": [[0xF0, 0x00], [0xF0, 0x00]],
    "FRAMESIZE_QVGA": [[0x40, 0x01], [0xF0, 0x00]],
    "FRAMESIZE_CIF": [[0x90, 0x01], [0x28, 0x01]],
    "FRAMESIZE_HVGA": [[0xE0, 0x01], [0x40, 0x01]],
    "FRAMESIZE_VGA": [[0x80, 0x02], [0xE0, 0x01]],
    "FRAMESIZE_SVGA": [[0x20, 0x03], [0x58, 0x02]],
    "FRAMESIZE_XGA": [[0x00, 0x04], [0x00, 0x03]],
    "FRAMESIZE_HD": [[0x00, 0x05], [0xD0, 0x02]],
    "FRAMESIZE_SXGA": [[0x00, 0x05], [0x00, 0x04]],
    "FRAMESIZE_UXGA": [[0x40, 0x06], [0xB0, 0x04]],
    # 3MP Sensors
    "FRAMESIZE_FHD": [[0x80, 0x07], [0x38, 0x04]],
    "FRAMESIZE_P_HD": [[0xD0, 0x02], [0x00, 0x05]],
    "FRAMESIZE_P_3MP": [[0x60, 0x03], [0x00, 0x06]],
    "FRAMESIZE_QXGA": [[0x00, 0x08], [0x00, 0x06]],
    # 5MP Sensors
    "FRAMESIZE_QHD": [[0x00, 0x0A], [0xA0, 0x05]],
    "FRAMESIZE_WQXGA": [[0x00, 0x0A], [0x40, 0x06]],
    "FRAMESIZE_P_FHD": [[0x38, 0x04], [0x80, 0x07]],
    "FRAMESIZE_QSXGA": [[0x00, 0x0A], [0x80, 0x07]]
};

framesize = "FRAMESIZE_VGA"
framerate = 1

# create a bytearray
avi_header = bytearray([
  0x52, 0x49, 0x46, 0x46, 0xD8, 0x01, 0x0E, 0x00, 0x41, 0x56, 0x49, 0x20, 0x4C, 0x49, 0x53, 0x54,
  0xD0, 0x00, 0x00, 0x00, 0x68, 0x64, 0x72, 0x6C, 0x61, 0x76, 0x69, 0x68, 0x38, 0x00, 0x00, 0x00,
  0xA0, 0x86, 0x01, 0x00, 0x80, 0x66, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00,
  0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x80, 0x02, 0x00, 0x00, 0xe0, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4C, 0x49, 0x53, 0x54, 0x84, 0x00, 0x00, 0x00,
  0x73, 0x74, 0x72, 0x6C, 0x73, 0x74, 0x72, 0x68, 0x30, 0x00, 0x00, 0x00, 0x76, 0x69, 0x64, 0x73,
  0x4D, 0x4A, 0x50, 0x47, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0A, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x73, 0x74, 0x72, 0x66,
  0x28, 0x00, 0x00, 0x00, 0x28, 0x00, 0x00, 0x00, 0x80, 0x02, 0x00, 0x00, 0xe0, 0x01, 0x00, 0x00,
  0x01, 0x00, 0x18, 0x00, 0x4D, 0x4A, 0x50, 0x47, 0x00, 0x84, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x49, 0x4E, 0x46, 0x4F,
  0x10, 0x00, 0x00, 0x00, 0x6A, 0x61, 0x6D, 0x65, 0x73, 0x7A, 0x61, 0x68, 0x61, 0x72, 0x79, 0x20,
  0x76, 0x36, 0x30, 0x20, 0x4C, 0x49, 0x53, 0x54, 0x00, 0x01, 0x0E, 0x00, 0x6D, 0x6F, 0x76, 0x69])

avi_header[0x40:0x40+2] = frameSizeData[framesize][0]
avi_header[0xA8:0xA8+2] = frameSizeData[framesize][0]
avi_header[0x44:0x44+2] = frameSizeData[framesize][0]
avi_header[0xAC:0xAC+2] = frameSizeData[framesize][0]

avi_header[0x84] = framerate

avi_header[4:4+4] = [movi_size + 240 + 16 * frame_cnt + 8 * frame_cnt]
avi_header[0x20:0x20+4] = [us_per_frame]

avifile.seek( 0x24 , SeekSet);
print_quartet(max_bytes_per_sec, avifile);

avifile.seek( 0x30 , SeekSet);
print_quartet(frame_cnt, avifile);

avifile.seek( 0x8c , SeekSet);
print_quartet(frame_cnt, avifile);

avifile.seek( 0x84 , SeekSet);
print_quartet((int)iAttainedFPS, avifile);

avifile.seek( 0xe8 , SeekSet);
print_quartet(movi_size + frame_cnt * 8 + 4, avifile);

avifile.seek( current_end , SeekSet);
avifile.write(idx1_buf, 4)
print_quartet(frame_cnt * 16, avifile);

for (int i = 0; i < frame_cnt; i++) {
    size_t res = idxfile.readBytes( AteBytes, 8);
    size_t i1_err = avifile.write(dc_buf, 4);
    size_t i2_err = avifile.write(zero_buf, 4);
    size_t i3_err = avifile.write((uint8_t *)AteBytes, 8);
}

# open a file for writing in binary mode
with open('output.bin', 'wb') as f:
    # write the bytearray to the file
    f.write(avi_header)
"""

finalOutputBytes = bytearray()

def appendInt(number):
    finalOutputBytes.append(number & 0xFF)
    finalOutputBytes.append((number >> 8) & 0xFF)
    finalOutputBytes.append((number >> 16) & 0xFF)
    finalOutputBytes.append((number >> 24) & 0xFF)

def appendShort(number):
    finalOutputBytes.append(number & 0xFF)
    finalOutputBytes.append((number >> 8) & 0xFF)

def appendString(string):
    for char in string:
        finalOutputBytes.append(ord(char))

def modifyQuartet(offset, number):
    finalOutputBytes[offset] = number & 0xFF
    finalOutputBytes[offset + 1] = (number >> 8) & 0xFF
    finalOutputBytes[offset + 2] = (number >> 16) & 0xFF
    finalOutputBytes[offset + 3] = (number >> 24) & 0xFF


images = ["img00.jpg", "img01.jpg", "img02.jpg", "img03.jpg"]
bytearrays = []

for image in images:
    with open(image, 'rb') as file:
        bytearrays.append(bytearray(file.read()))

width = 528
height = 654
frameRate = 1
numFrames = len(images)
framesBytesSize = 0
for ba in bytearrays:
    framesBytesSize += len(ba)

appendString("RIFF")
appendInt(0) # The remaining size in bytes: (file size - 8) bytes (little endian).
appendString("AVI ")
appendString("LIST")
appendInt(294)
appendString("hdrl")
appendString("avih")
appendInt(56)
appendInt(int(1000000/frameRate))
appendInt(236213)
appendInt(0)
appendInt(0) # flags
appendInt(numFrames) # total frames
appendInt(0) # This specifies the initial frame. Noninterleaved files should use 0.
appendInt(1) # Number of streams in the file - here, just the video stream.
appendInt(0) # suggested buffer size for reading the file
appendInt(width)
appendInt(height)
appendInt(0) # 16 reserved bytes
appendInt(0)
appendInt(0)
appendInt(0)
appendString("LIST")
appendInt(116)
appendString("strl")
appendString("strh")
appendInt(56)
appendString("vids")
appendString("MJPG") # FOURCC
appendInt(0) # flags
appendInt(0) # priority
appendInt(0) # initial frame
appendInt(1) # scale
appendInt(frameRate) # rate # check rates and scales around here if not working
appendInt(0) # start
appendInt(numFrames) # length
appendInt(0) # suggested buffer size
appendInt(0) # quality
appendInt(0) # sample size
appendString("strf")
appendInt(40) # size
appendInt(40) # size again
appendInt(width)
appendInt(height)
appendShort(1) # planes
appendShort(24) # bits per pixel
appendString("MJPG") # compression
appendInt(230400) # "image size", not sure what is, just copied from myavi.avi
appendInt(0) # x pixels per meter
appendInt(0) # y pixels per meter
appendInt(0) # colors used
appendInt(0) # colors important
appendString("LIST") # list of frames
appendInt(framesBytesSize)
appendString("movi")
for i in range(numFrames):
    appendString("00dc")

    jpeg_size = len(bytearrays[i])
    remnant = (4 - (jpeg_size & 0x00000003)) & 0x00000003
    jpeg_size_rem = jpeg_size + remnant
    appendInt(jpeg_size_rem) # size of frame

    finalOutputBytes.extend(bytearrays[i])
    bytesLeft = 0
    for j in range(i, numFrames):
        bytesLeft += len(bytearrays[j])
    appendInt(bytesLeft)

modifyQuartet(4, len(finalOutputBytes) - 8)

with open('output.avi', 'wb') as f:
    # write the bytearray to the file
    f.write(finalOutputBytes)