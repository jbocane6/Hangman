#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * main - main function
 * @argc: Amount of arguments received
 * @argv: Pointer to an array to char received 
 * Return: 0
*/

int main(int argc, char *argv[])
{
    int valRead = 0;
	char character = 0;
    write(1, "$ ", 2);
    valRead = read(STDIN_FILENO, &character, 1);
 return (0);
}