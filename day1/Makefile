NAME := puzzle1.out

CFLAGS ?= -Wall -Werror -Wextra
ifdef DEBUG
CFLAGS := -g $(CFLAGS)
endif
OBJECTS := main.o
OBJECTS := $(addprefix obj/,$(OBJECTS))
INCLUDE := headers libft
INCLUDE := $(addprefix -I,$(INCLUDE))
HEADER_FILES := 
HEADER_FILES := $(addprefix headers/,$(HEADER_FILES))

PHIL_COUNT ?= 2
DIE_TIME ?= 310
EAT_TIME ?= 200
SLEEP_TIME ?= 200

all: $(NAME)

$(NAME): $(OBJECTS)
	$(MAKE) bonus -C ./libft
	$(CC) $(CFLAGS) $(OBJECTS) libft/libft.a -o $(NAME)

obj/%.o: src/%.c $(HEADER_FILES)
	@mkdir -p obj
	$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
	$(MAKE) clean -C ./libft
	rm -f $(OBJECTS)
	@rm -rf obj

fclean: clean
	$(MAKE) fclean -C ./libft
	rm -f $(NAME)

re: fclean all

bonus: all

run: all
	./$(NAME) "$(cat input)"

debug:
	$(MAKE) DEBUG=1

.PHONY: all clean fclean re bonus run debug
