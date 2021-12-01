/* ************************************************************************** */
/*                                                                            */
/*                                                        ::::::::            */
/*   main_two.c                                         :+:    :+:            */
/*                                                     +:+                    */
/*   By: pdruart <pdruart@student.codam.nl>           +#+                     */
/*                                                   +#+                      */
/*   Created: 2021/12/01 12:08:38 by pdruart       #+#    #+#                 */
/*   Updated: 2021/12/01 13:31:05 by pdruart       ########   odam.nl         */
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

int	arr_size(char **arr)
{
	int	i;

	i = 0;
	while (arr[i] != NULL)
		i++;
	return (i);
}

void	fill_windows(int **windows, char **arr)
{
	int	i;

	i = 0;
	while (arr[i] != NULL)
	{
		(*windows)[i] = ft_atoi(arr[i]);
		i++;
	}
}

int	count_ups(char **arr)
{
	int		i;
	int		*windows;
	int		diff;
	int		ups;
	int		size;

	size = arr_size(arr);
	if (size < 4)
		return (0);
	windows = ft_calloc(size, sizeof(int));
	if (windows == NULL)
		return (0);
	fill_windows(&windows, arr);
	i = 1;
	ups = 0;
	while (i < size - 2)
	{
		diff = windows[i + 2] - windows[i - 1];
		if (diff > 0)
			ups++;
		i++;
	}
	free(windows);
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
