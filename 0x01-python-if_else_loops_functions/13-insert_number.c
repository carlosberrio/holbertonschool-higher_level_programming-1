#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @node: pointer to pointer of first node of listint_t list
 * @number: number to insert in the linked list
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **node, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!(*node) || new_node->n < (*node)->n)
	{
		new_node->next = (*node);
		return ((*node) = new_node);
	}

	while ((*node))
	{
		if (!(*node)->next || (*node)->next->n > number)
		{
			new_node->next = (*node)->next;
			(*node)->next = new_node;
			return ((*node));
		}
		node = &(*node)->next;
	}

	return (NULL);
}
