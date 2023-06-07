#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insert a number to a sorted list
 * @head: pointer to the pointer of the linked list
 * @number: the number to be inserted
 *
 * Return: address to the new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *ptr = NULL, *new_node = NULL;


	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		free(new_node);
		return (NULL);
	}
	if ((*head)->n > number)
	{
		new_node->next = (*head)->next;
		*head = new_node;
		return (new_node);
	}

	ptr = *head;

	while (ptr != NULL)
	{
		temp = ptr;
		ptr = ptr->next;

		if (ptr->n > number)
		{
			new_node->next = ptr;
			temp->next = new_node;
			return (new_node);
		}
	}
	ptr = new_node;
	return (new_node);
}
