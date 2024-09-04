#include <stdint.h>
#include <stdbool.h>

typedef struct {
    uint32_t src_ip;   // Source IP address in network byte order
    uint32_t dest_ip;  // Destination IP address in network byte order
    uint16_t length;   // Length of the packet
    uint8_t data[1024];// Packet data
} IPPacket;

typedef struct {
    uint32_t allowed_ips[10]; // List of allowed source IP addresses in network byte order
    int num_allowed;          // Number of allowed IP addresses
} FirewallSettings;


bool is_packet_allowed(const IPPacket *packet, const FirewallSettings *settings) {
    // Your code goes here:
    // 1. Iterate over the list of allowed IP addresses
    // 2. Compare each allowed IP with the packet's source IP
    // 3. Return true if a match is found
    // 4. Return false if no match is found after checking all allowed IPs

    // Note: Use appropriate functions to handle IP address comparison in network byte order.

    for (int i =0 ; i< settings->num_allowed; i++){
        if (ntohl(packet->dest_ip) == ntohl(settings->allowed_ips[i])){
            return 1;
        }
    }

    return 0;
}
