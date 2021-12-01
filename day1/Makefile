ONE := puzzle1.out
TWO := puzzle2.out

NAME := $(ONE) $(TWO)

CFLAGS ?= -Wall -Werror -Wextra
ifdef DEBUG
CFLAGS := -g $(CFLAGS)
endif
OBJECTS_ONE := main_one.o
OBJECTS_ONE := $(addprefix obj/,$(OBJECTS_ONE))
OBJECTS_TWO := main_two.o
OBJECTS_TWO := $(addprefix obj/,$(OBJECTS_TWO))
INCLUDE := headers libft
INCLUDE := $(addprefix -I,$(INCLUDE))
HEADER_FILES := 
HEADER_FILES := $(addprefix headers/,$(HEADER_FILES))

all: $(NAME)

$(ONE): $(OBJECTS_ONE)
	$(MAKE) bonus -C ./libft
	$(CC) $(CFLAGS) $(OBJECTS_ONE) libft/libft.a -o $(ONE)

$(TWO): $(OBJECTS_TWO)
	$(MAKE) bonus -C ./libft
	$(CC) $(CFLAGS) $(OBJECTS_TWO) libft/libft.a -o $(TWO)

obj/%.o: src/%.c $(HEADER_FILES)
	@mkdir -p obj
	$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

clean:
	$(MAKE) clean -C ./libft
	rm -f $(OBJECTS_ONE)
	rm -f $(OBJECTS_TWO)
	@rm -rf obj

fclean: clean
	$(MAKE) fclean -C ./libft
	rm -f $(NAME)

re: fclean all

bonus: all

run: all
	./$(ONE) "`cat input`"
	./$(TWO) "`cat input`"

debug:
	$(MAKE) DEBUG=1

.PHONY: all clean fclean re bonus run debug
