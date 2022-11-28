#include "lists.h"
#include "stdio.h"

/**
 * check_cycle - Checks if a linked list contains a cycle
 * @list: linked list to check from
 * Return: 1 if cycle is present, 0 if absent
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (!list)
		return (0);

	while (1)
	{
		if (a->next != NULL && a->next->next != NULL)
		{
			a = a->next->next;
			b = b->next;

			if (a == b)
				return (1);
		}
		else
			return (0);
	}
}
