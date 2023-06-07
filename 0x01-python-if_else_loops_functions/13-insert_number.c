#include "lists.h"

/**
 * inset_node - a function that inserts a number into
 * a sorted singly linked list
 * @head: the head of the list
 * @number: number of nodes
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c = *head;
	listint_t *nn = NULL;

	nn = malloc(sizeof(listint_t));
	if(!n)
	return (NULL);
	nn->n = number;
	nn->next = NULL;
	if (!*head)
	*head = nn;
	return (nn);
	if (nn->n < c->next->n)
	nn->next = *head;
	*head = nn;
	return (nn);
	while (c->next != NULL && c->next->n < nn->n)
	c = c->next;
	nn->next = c->next;
	c->next = nn;
	return (nn);
}
