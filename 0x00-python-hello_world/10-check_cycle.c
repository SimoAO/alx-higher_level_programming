#include "lists.h"

/**
 * check_cycle - a function that checks if a singly linked
 * list has a cycle in it
 * @list: linked list input
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *sw = list;
	listint_t *ft = list;

	if (!list)
	return (0);
	while (ft && ft->next)
	{
	sw = sw->next;
	ft = ft->next->next;
	if (sw == ft)
	return (1);
	}
	return (0);
}
