#include "lists.h"

/**
 * is_palindrome - a function that checks if listint_t sll is
 * a palindrome
 * @head: pointer to the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head)
{
	listint_t *ft = *head, *sl = *head, *tp = NULL;

	if (!(head && *head))
		return (1);
	while (ft->next && ft->next->next)
	{
	ft = ft->next->next;
	sl = sl->next;
	}
	sl = reverse_list(&sl);
	ft = *head;
	tp = sl;
	while (ft && sl)
	{
	if (ft->n != sl->n)
	return (0);
	sl = sl->next;
	ft = ft->next;
	}
	reverse_list(&tp);
	return (1);
}

/**
 * reverse_list - a function that reverses a linked list
 * @head: pointer to the linked list
 *
 * Return: pointer to the first node
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *pv = NULL, *nx = NULL;

	while (*head != NULL)
	{
	nx = (*head)->next;
	(*head)->next = pv;
	pv = *head;
	*head = nx;
	}
	*head = pv;
	return (*head);
}
