#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include "../lib/memora.h"

int main()
{
    const char *server_address = "127.0.0.1";
    uint16_t port = 5000;
    int b = 1;

    // Connect to the MemoraDB server
    void *handle = NULL;
    int retries = 0;
    while (!handle && retries < 5)
    {
        handle = memora_connect(server_address, port);
        if (!handle)
        {
            retries++;
            fprintf(stderr, "Failed to connect to MemoraDB server at %s:%d (attempt %d)\n", server_address, port, retries);
            if (retries < 5)
            {
                // Wait for 6 seconds before retrying
                sleep(6);
            }
        }
    }

    if (!handle)
    {
        fprintf(stderr, "Failed to connect to MemoraDB server after 5 attempts\n");
        return 1;
    }
    
    printf("\n0=Exit, 1=Create, 2=Read, 3=Update, 4=Delete\n");

    while (b == 1)
    {
        printf("\n");
        int line;
        scanf("%d", &line);
        if (line == 0)
        {
            // Close the connection to the MemoraDB server
            if (memora_close(handle) == 0)
            {
                printf("Connection closed\n");
            }
            else
            {
                printf("Failed to close connection\n");
            }
        }
        else if (line == 1)
        {
            if (memora_create(handle, "key1", "value1") == 0)
            {
                printf("Create: key1 => value1\n");
            }
            else
            {
                printf("Failed to create key1\n");
            }
        }
        else if (line == 2)
        {
            char *value = memora_read(handle, "key1");
            if (value)
            {
                printf("Read: key1 => %s\n", value);
            }
            else
            {
                printf("Failed to read key1\n");
            }
        }
        else if (line == 3)
        {
            // Test update operation
            if (memora_update(handle, "key1", "new_value1") == 0)
            {
                printf("Update: key1 => new_value1\n");
            }
            else
            {
                printf("Failed to update key1\n");
            }
        }
        else if (line == 4)
        {
            if (memora_delete(handle, "key1") == 0)
            {
                printf("Delete: key1\n");
            }
            else
            {
                printf("Failed to delete key1\n");
            }
        }
    }
    return 0;
}
