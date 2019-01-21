#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>

#define THREAD_COUNT 4

int test(void *arg)
{
    int result = (int)arg;
    for (int i = 0; i < 2000000000; ++i)
        result = result * result - i;
    return result;
}

void foobar(const float m[], const int length)
{
    printf("%lu\n", sizeof(m));
    for (int i = 0; i < length; ++i)
        printf("%f ", m[i]);
    printf("\n");
    // pthread_t list_pthread[THREAD_COUNT];
    // int results[THREAD_COUNT];
    // for (int i = 0; i < THREAD_COUNT; ++i)
    //     pthread_create(&list_pthread[i], NULL, test, (void *)i);
    // for (int i = 0; i < THREAD_COUNT; ++i)
    //     pthread_join(list_pthread[i], (void *)(&results[i]));
    // for (int i = 0; i < THREAD_COUNT; ++i)
    //     printf("%d is %d\n", i, results[i]);
    // printf("m is %d\n", m);
}