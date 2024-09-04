#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/in.h>
#include <netinet/if_ether.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <netinet/udp.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

#define BUFFER_SIZE 65536

void process_packet(unsigned char *, int);

int main(int argc, char *argv[]) {
    int sock_raw;
    int saddr_size, data_size;
    struct sockaddr saddr;
    unsigned char *buffer = (unsigned char *)malloc(BUFFER_SIZE);

    printf("Packet Sniffer Started...\n");

    // Create a raw socket to sniff packets
    sock_raw = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    if (sock_raw < 0) {
        perror("Socket Error");
        return 1;
    }

    // Main packet sniffing loop
    while (1) {
        saddr_size = sizeof saddr;
        // Receive a packet
        data_size = recvfrom(sock_raw, buffer, BUFFER_SIZE, 0, &saddr, (socklen_t *)&saddr_size);
        if (data_size < 0) {
            perror("Recvfrom error , failed to get packets");
            return 1;
        }
        // Process the received packet
        process_packet(buffer, data_size);
    }
    close(sock_raw);
    return 0;
}

void process_packet(unsigned char *buffer, int size) {
    // Implement packet processing here
    // Extract Ethernet, IP, and TCP/UDP headers
    // Print relevant information about each packet
    // You can refer to the structures defined in the headers included above
    struct ethhdr *eth = (struct ethhdr*) buffer;
    if(ntohs(eth->h_proto) !=ETH_P_IP){
        
    }

}
