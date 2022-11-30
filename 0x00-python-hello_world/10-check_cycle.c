#include "lists.h"

/**
 * check_cycle - function checks if a linked list contains a cycle
 * @list: pointer to the list
 * Return: Returns 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *post;
	listint_t *prev;

	post = list;
	prev = list;
	while (list && post && post->next)
	{
		list = list->next;
		post = post->next->next;

		if (list == post)
		{
			list = prev;
			prev =  post;
			while (1)
			{
				post = prev;
				while (post->next != list && post->next != prev)
				{
					post = post->next;
				}
				if (post->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
