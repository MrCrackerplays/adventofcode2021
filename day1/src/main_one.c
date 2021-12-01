/* ************************************************************************** */
/*                                                                            */
/*                                                        ::::::::            */
/*   main.c                                             :+:    :+:            */
/*                                                     +:+                    */
/*   By: pdruart <pdruart@student.codam.nl>           +#+                     */
/*                                                   +#+                      */
/*   Created: 2021/12/01 12:08:38 by pdruart       #+#    #+#                 */
/*   Updated: 2021/12/01 12:46:39 by pdruart       ########   odam.nl         */
/*                                                                            */
/* ************************************************************************** */

#include <libft.h>
#include <stdlib.h>

int	clean_arr(char ***arr)
{
	size_t	i;

	i = 0;
	while ((*arr)[i] != NULL)
	{
		free((*arr)[i]);
		i++;
	}
	free(*arr);
	return (1);
}

int	count_ups(char **arr)
{
	int		i;
	int		prev;
	int		curr;
	char	*numb;
	int		ups;

	prev = 0;
	i = 1;
	ups = 0;
	numb = arr[0];
	while (numb != NULL)
	{
		curr = ft_atoi(numb);
		if (prev != 0 && curr > prev)
			ups++;
		prev = curr;
		numb = arr[i];
		i++;
	}
	return (ups);
}

int	main(int argc, char **argv)
{
	char	**arr;
	char	separator;

	if (argc < 2 || argc > 3)
		return (1);
	separator = '\n';
	if (argc == 3)
		separator = argv[2][0];
	arr = ft_split(argv[1], separator);
	if (arr == NULL)
		return (2);
	ft_putnbr_fd(count_ups(arr), 1);
	clean_arr(&arr);
	ft_putchar_fd('\n', 1);
	return (0);
}
