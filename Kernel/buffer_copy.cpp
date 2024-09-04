#include <stdint.h>
#include <stddef.h>
#include <string.h> // For memcpy

typedef struct {
    uint8_t *data;       // Pointer to data buffer
    size_t size;         // Size of the buffer
} Buffer;

/**
 * Copies data from src to dest buffer securely.
 * 
 * @param dest Destination buffer.
 * @param src Source buffer.
 * @return The number of bytes copied.
 */

size_t secure_buffer_copy(Buffer dest, Buffer src) {
    // Determine the minimum of dest.size and src.size
    size_t copy_size = dest.size < src.size ? dest.size : src.size;

    // Copy the data securely
    memcpy(dest.data, src.data, copy_size);

    // Return the number of bytes copied
    return copy_size;
}
