#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
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