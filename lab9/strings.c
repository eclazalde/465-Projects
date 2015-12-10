/* strings.c */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	// Print out memory locations on the stack
	char variable[10];
	
    printf("%08x %08x %08x %08x %08x\n");
    
    // Change the value of a variable on the stack
    int i = 100000000;
    
    printf("%d\n", i);
    
    printf("12345%n\n", &i);
    
    printf("%d\n",i);
    
    // Print out chunks of memory from a specific address.
    printf("printing chunks\n"); 
    printf("\x10\x01\x48\x08_%08x.%08x.%08x.%08x.%08x|%s|\n");
    
    // Make the program crash
    printf("crashing\n");
    printf("%s%s%s%s%s%s%s%s%s%s%s%s");
    
    return 1;
}
