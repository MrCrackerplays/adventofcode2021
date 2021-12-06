import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Puzzle2 {
	static void	add_line_to_bingo_card(List<List<Integer>> card, String line) {
		card.add(Arrays.stream(line.split("\\s+")).filter(str-> !str.isEmpty()).mapToInt(Integer::parseInt).boxed().collect(Collectors.toList()));
	}

	static boolean	has_bingo(boolean[][]found, int x, int y) {
		for (int i = 0; i < 5; i++) {
			if (!found[y][i])
				break;
			if (i == 4)
				return (true);
		}
		for (int i = 0; i < 5; i++) {
			if (!found[i][x])
				break;
			if (i == 4)
				return (true);
		}
		return (false);
	}

	public static Bingo	bingo(int[] drawn_numbers, List<List<List<Integer>>> bingo_cards, boolean[][][] found) {
		List<Integer>	winners = new ArrayList<>();
		for (int number : drawn_numbers) {
			for (int i = 0; i < bingo_cards.size(); i++) {
				if (winners.contains(i))
					continue;
				for (int y = 0; y < 5; y++) {
					for (int x = 0; x < 5; x++) {
						if (number == bingo_cards.get(i).get(y).get(x)) {
							found[i][y][x] = true;
							if (has_bingo(found[i], x, y)) {
								winners.add(i);
								if (winners.size() == bingo_cards.size())
									return (new Bingo(i, number));
							}
						}
					}
				}
			}
		}
		return (new Bingo(-1, -1));
	}

	public static void main(String args[]) {
		int[]						drawn_numbers = {};
		List<List<List<Integer>>>	bingo_cards = new ArrayList<>();
		try (BufferedReader br = new BufferedReader(new FileReader("input"))) {
			for (String line; (line = br.readLine()) != null; ) {
				if (drawn_numbers.length == 0)
					drawn_numbers = Arrays.stream(line.split(",")).map(String::trim).mapToInt(Integer::parseInt).toArray();
				else {
					if (line.length() == 0)
						bingo_cards.add(new ArrayList<>());
					else
						add_line_to_bingo_card(bingo_cards.get(bingo_cards.size() - 1), line);
				}
			}
			boolean[][][]	found = new boolean[bingo_cards.size()][5][5];
			Bingo	last_win = bingo(drawn_numbers, bingo_cards, found);
			System.out.println("Congratulations on your win card number " + last_win.getCardNumb());
			int	score = 0;
			for (int y = 0; y < 5; y++) {
				for (int x = 0; x < 5; x++) {
					if (found[last_win.getCardNumb()][y][x] == false)
						score += bingo_cards.get(last_win.getCardNumb()).get(y).get(x);
				}
			}
			System.out.println("score:"+ score + " winning number:" + last_win.getWinningNumb() + " total:" + score * last_win.getWinningNumb());
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	final static class Bingo {
		private final int cardNumb;
		private final int winningNumb;
	
		public Bingo(int cardNumb, int winningNumb) {
			this.cardNumb = cardNumb;
			this.winningNumb = winningNumb;
		}
	
		public int getCardNumb() {
			return cardNumb;
		}
	
		public int getWinningNumb() {
			return winningNumb;
		}
	}
}