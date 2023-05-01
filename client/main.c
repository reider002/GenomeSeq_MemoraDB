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

    printf("\n0=Close Connection, 1=Create, 2=Read, 3=Update, 4=Delete, 5=Reconnect\n");

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
            printf("Give me a key: ");
            char kv[31];
            scanf("%s", kv);
            printf("\nGive me a value: ");
            char value[63];
            scanf("%s", value);
            if (memora_create(handle, kv, value) == 0)
            {
                printf("Create: %s => %s\n", kv, value);
            }
            else
            {
                printf("Failed to create key1\n");
            }
            line = 5;
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
            printf("Give me a key: ");
            char kv[31];
            scanf("%s", kv);
            printf("\nGive me a value: ");
            char value[63];
            scanf("%s", value);
            if (memora_update(handle, kv, value) == 0)
            {
                printf("Update: %s => %s\n", kv, value);
            }
            else
            {
                printf("Failed to update %s\n", kv);
            }
        }
        else if (line == 4)
        {
            printf("Give me a key: ");
            char kv[31];
            scanf("%s", kv);
            if (memora_delete(handle, kv) == 0)
            {
                printf("Delete: %s\n", kv);
            }
            else
            {
                printf("Failed to delete %s\n", kv);
            }
        }
        else if (line == 9)
        {
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
        }
    }
    return 0;
}
