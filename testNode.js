const fs = require('fs');

function writeUInt32(buffer, value, offset) {
    buffer[offset] = value & 0xFF;
    buffer[offset + 1] = (value >> 8) & 0xFF;
    buffer[offset + 2] = (value >> 16) & 0xFF;
    buffer[offset + 3] = (value >> 24) & 0xFF;
}

function createAviHeader(framesLength, frameRate) {
    const buffer = Buffer.alloc(175);

    // RIFF header
    buffer.write('RIFF', 0);
    writeUInt32(buffer, 2048 - 8, 4); // Placeholder for file size
    buffer.write('AVI ', 8);

    // HDRL - AVI Header Chunk
    buffer.write('LIST', 12);
    writeUInt32(buffer, 188, 16); // Size of this chunk
    buffer.write('hdrl', 20);

    // AVIH - AVI Main Header
    buffer.write('avih', 24);
    writeUInt32(buffer, 56, 28); // Size of this sub-chunk
    writeUInt32(buffer, Math.round(1000000 / frameRate), 32); // Microseconds per frame
    writeUInt32(buffer, 0, 36); // Max bytes per sec
    writeUInt32(buffer, 0, 40); // Padding
    writeUInt32(buffer, 0, 44); // Flags
    writeUInt32(buffer, framesLength, 48); // Total frames
    writeUInt32(buffer, 0, 52); // Initial frames
    writeUInt32(buffer, 1, 56); // Streams
    writeUInt32(buffer, 0, 60); // Buffer size
    writeUInt32(buffer, 640, 64); // Width (assuming 640)
    writeUInt32(buffer, 480, 68); // Height (assuming 480)

    // STRL - Stream Header List
    buffer.write('LIST', 72);
    writeUInt32(buffer, 116, 76); // Size of this chunk
    buffer.write('strl', 80);

    // STRH - Stream Header
    buffer.write('strh', 84);
    writeUInt32(buffer, 56, 88); // Size of this sub-chunk
    buffer.write('vids', 92); // fccType
    buffer.write('MJPG', 96); // fccHandler
    writeUInt32(buffer, 0, 100); // Flags
    writeUInt32(buffer, 0, 104); // Reserved
    writeUInt32(buffer, 0, 108); // Initial frames
    writeUInt32(buffer, 1, 112); // Scale
    writeUInt32(buffer, frameRate, 116); // Rate
    writeUInt32(buffer, 0, 120); // Start
    writeUInt32(buffer, framesLength, 124); // Length
    writeUInt32(buffer, 0, 128); // Buffer size

    // STRF - Stream Format
    buffer.write('strf', 132);
    writeUInt32(buffer, 40, 136); // Size of this sub-chunk
    writeUInt32(buffer, 40, 140); // Size
    writeUInt32(buffer, 640, 144); // Width (assuming 640)
    writeUInt32(buffer, 480, 148); // Height (assuming 480)
    buffer[152] = 1; // Planes
    buffer[153] = 0;
    buffer[154] = 24; // Bit count
    buffer.write('MJPG', 156); // Compression
    writeUInt32(buffer, 640 * 480 * 3, 160); // Image size

    return buffer;
}

function createFrameBuffer(jpegData) {
    const bufferSize = 8 + 4 + jpegData.length;
    const buffer = Buffer.alloc(bufferSize);
    buffer.write('00dc', 0); // 00dc indicates a video frame
    writeUInt32(buffer, jpegData.length, 4); // Data length
    jpegData.copy(buffer, 8);

    return buffer;
}

async function createMjpgAvi() {
    const aviHeader = createAviHeader(5, 30); // 30 fps
    const frames = [];

    for (let i = 0; i < 5; i++) {
        const jpegData = fs.readFileSync(`img0${i}.jpg`);
        const frameBuffer = createFrameBuffer(jpegData);
        frames.push(frameBuffer);
    }

    const aviData = Buffer.concat([aviHeader, ...frames]);
    aviData[4] = aviData.length - 8; // Update file size
    fs.writeFileSync('output_node.avi', aviData);
}

createMjpgAvi();
