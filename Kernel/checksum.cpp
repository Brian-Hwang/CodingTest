#include <stdint.h>
#include <stddef.h>

typedef struct {
    uint16_t packet_length; // Total length of the packet including header
    uint8_t source_id;      // Source identifier
    uint8_t destination_id; // Destination identifier
    uint8_t checksum;       // Checksum byte, initially zero during calculation
    uint8_t data[256];      // Data section of the packet, variable length
} SimplePacket;


void calculate_checksum(SimplePacket *packet) {
    // Your code goes here:
    // 1. Initialize checksum variable to 0
    // 2. Iterate over each byte in the packet excluding the checksum field
    // 3. Apply bitwise XOR of each byte with the current checksum value
    // 4. Store the final checksum value back into the packet's checksum field

    // Note: Remember to consider the packet_length field to determine the actual data length.
    // uint8_t checksum = 0;
    // uint8_t* packet_pointer = (uint8_t*)packet;

    // for (size_t i =0 ; i < packet->packet_length;i++){
    //     if (packet_pointer + i == &(packet->checksum)) continue;
    //     checksum ^= *(packet_pointer+i);
    // }

    // packet->checksum = checksum;








    uint8_t checksum = 0;
    u_int8_t* ptr = (uint8_t*) packet;

    for (size_t i =0 ; i < packet->packet_length; i++){
        if (ptr+i == &(packet->checksum)) continue;
        checksum ^= *(ptr+i);
    }

    packet->checksum = checksum;
    

}
