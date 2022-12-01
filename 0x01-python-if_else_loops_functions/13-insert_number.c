#include "lists.h"

/**
 * insert_number - inserts a number in a sorted
 * singly linked list.
 * @head: head of the node/linked list
 * @number: number to insert
 * Return: NULL if function fails, else pointer to new node
 */

listint_t *insert_number(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
