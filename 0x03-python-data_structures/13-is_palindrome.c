#include "lists.h"

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list
 * @head: first element of the list
 * @n: integer to copy
 * Return: Address of the new element, or NULL if it failed
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: address of pointer to list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome,
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed = NULL, *current = *head;

	while (current)
	{
		add_nodeint(&reversed, current->n);
		current = current->next;
	}
	while ((*head))
	{
		if ((*head)->n != reversed->n)
			return (0);

		head = &(*head)->next;
		reversed = reversed->next;
	}

	return (1);
}
