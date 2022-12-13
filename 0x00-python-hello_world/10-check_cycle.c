#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *f;
	listint_t *s;

	f = list;
	s = list;
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if(s == f)
			return (1);
	}

	return (0);
}
