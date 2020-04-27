#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *instance = list;
	int n = 0;

	while (list)
	{
		if (list->next == instance)
			return (1);
		list = list->next;
		n++;
	}

	return (0);

}
