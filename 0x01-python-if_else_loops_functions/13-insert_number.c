#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * insert_node - inserts new node into a sorted linked list
  * @head: pointer to pointer of first node
  * @number: integer
  * Return: address of new element or NULL
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c_head = *head, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}

	for (; c_head != NULL; c_head = c_head->next)
	{
		if (number <= c_head->n)
		{
			*head = new;
			new->next = c_head;
			return (new);
		}
		if (number >= c_head->n && c_head->next == NULL)
		{
			new->next = NULL;
			c_head->next = new;
			return (new);
		}
		if (number >= c_head->n && number <= c_head->next->n)
		{
			new->next = c_head->next;
			c_head->next = new;
			return (new);
		}
	}

	return (NULL);
}
