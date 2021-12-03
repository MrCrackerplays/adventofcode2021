/**
 * file reading code taken from nodejs api example
 * https://nodejs.org/api/readline.html#readline_example_read_file_stream_line_by_line
 * and made sync using the readline example (which uses the same code example as from the api) from
 * https://geshan.com.np/blog/2021/10/nodejs-read-file-line-by-line/
 */
const fs = require('fs');
const events = require('events');
const readline = require('readline');

const rl = readline.createInterface({
	input: fs.createReadStream('input'),
	crlfDelay: Infinity
});

//https://stackoverflow.com/a/16155417
function dec2bin(dec) {
	return (dec >>> 0).toString(2);
  }

(async function processLineByLine() {
	try {
		const epsilon_map = new Map();
		let	width = 0;
		let	count = 0;
		rl.on('line', (line) => {
			for (let i = 0; i < line.length; i++) {
				if (line[i] == '1') {
					if (epsilon_map.has(i) == false) {
						epsilon_map.set(i, 1);
						width++;
					}
					else
						epsilon_map.set(i, epsilon_map.get(i) + 1);
				}
			}
			count++;
		});

		await events.once(rl, 'close');

		const	mask = (1 << width) - 1; // width number of 1's (e.g. width=4 -> 01111) in order to not have trouble with the bits beyond the width leading to a large negative number
		let	epsilon_rate = 0;
		for (let i = 0; i < width; i++) {
			//I love myself some bitwise operations
			epsilon_rate <<= 1;
			if (epsilon_map.get(i) > (count / 2))
				epsilon_rate |= 1;
		}
		let	inverse_epsilon_rate = ~epsilon_rate & mask;
		console.log("epsilon rate:", epsilon_rate, "(" + dec2bin(epsilon_rate) +")", "inverse epsilon rate:", inverse_epsilon_rate, "(" + dec2bin(inverse_epsilon_rate) +")", "power consumption:", epsilon_rate * inverse_epsilon_rate, "(" + dec2bin(epsilon_rate * inverse_epsilon_rate) +")")
	} catch (err) {
		console.error(err);
	}
})();
