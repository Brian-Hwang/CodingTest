#include <stdint.h>
#include <stdbool.h>
#include <pthread.h> // Include for mutex

typedef struct {
    uint32_t src_ip;   // Source IP address
    uint32_t dest_ip;  // Destination IP address
    uint16_t length;   // Length of the packet
    uint8_t data[1024];// Packet data
} NetworkPacket;

typedef struct PacketNode {
    NetworkPacket packet;
    struct PacketNode *next;
} PacketNode;

typedef struct {
    PacketNode *head;
    PacketNode *tail;
    pthread_mutex_t lock; // Mutex for thread safety
} PacketQueue;


void init_queue(PacketQueue *queue) {
    queue->head = NULL;
    queue->tail = NULL;
    pthread_mutex_init(&queue->lock, NULL);
}

void enqueue_packet(PacketQueue *queue, NetworkPacket packet) {
    // Your code here: Safely add a packet to the queue
    PacketNode *newNode = (PacketNode*)malloc(sizeof(PacketNode));
    if (newNode == NULL){
        return;
    }
    newNode->packet = packet;
    newNode->next = NULL;

    pthread_mutex_lock(&queue->lock);
    if (queue->head == NULL){
        queue->head = newNode;
        queue->tail = newNode;
    }
    else{
        queue->tail->next = newNode;
        queue->tail = queue->tail->next;
    }
    pthread_mutex_unlock(&queue->lock);
}

NetworkPacket dequeue_packet(PacketQueue *queue) {
    // Your code here: Safely remove and return a packet from the queue
    // Note: Consider what to return if the queue is empty
    if (queue->tail==NULL){
        return NetworkPacket{0};
    }
    else{
        pthread_mutex_lock(&queue->lock);
        PacketNode* temp_node = queue->head;
        NetworkPacket temp_packet = temp_node->packet;

        queue-> head = queue->head->next;
        if (queue->head == NULL){
            queue->tail = NULL;
        }
        free(temp_node);

        pthread_mutex_unlock(&queue->lock);

        return temp_packet;
    }
}


