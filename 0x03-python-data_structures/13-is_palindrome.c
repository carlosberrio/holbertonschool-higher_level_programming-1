#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: address of pointer to list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome,
 * An empty list is considered a palindrome
 */
int counter(listint_t *head)
{
	int c = 0;

	for ( ; head ; head = head->next, c++)
		;

	return (c);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: address of pointer to list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome,
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	int c = counter(*head), i = 0;
	int *numbers = malloc(sizeof(int) * c);

	for (  ; (*head) ; head = &(*head)->next, i++)
		numbers[i] = (*head)->n;

	i = 0;
	while(i < (c / 2))
	{
		if(numbers[i] != numbers[c-i-1])
		{
			free(numbers);
			return (0);
		}
		i++;
	}
	free(numbers);
	return (1);
}
