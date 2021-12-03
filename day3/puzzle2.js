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

function get_life_support_rating(oxygen_generator_rating, co_scrubber_rating) {
	return (oxygen_generator_rating * co_scrubber_rating);
}

function get_most_common_bit_at_pos(arr, len, pos, width) {
	let	count = 0;
	for (let i = 0; i < len; i++) {
		if (((arr[i] >> (width - 1 - pos)) & 1) == 1)// 011: pos=0 -> 0, pos=2 -> 1
			count++;
	}
	return (count >= (len / 2) ? 1 : 0);
}

function has_bit_at(bit, pos, width) {
	return function(element) {
		return (((element >> (width - 1 - pos)) & 1) == bit);
	}
}

function get_oxygen_generator_rating(diagnostics, width) {
	let	arr = [...diagnostics];
	let	holder = [];
	let	pos = 0;
	let	bit_criteria;
	while (arr.length > 1) {
		bit_criteria = get_most_common_bit_at_pos(arr, arr.length, pos, width);
		holder = arr.filter(has_bit_at(bit_criteria, pos, width));
		arr = holder;
		pos++;
	}
	return arr[0];
}

function get_co_scrubber_rating(diagnostics, width) {
	let	arr = [...diagnostics];
	let	holder = [];
	let	pos = 0;
	let	bit_criteria;
	while (arr.length > 1) {
		bit_criteria = get_most_common_bit_at_pos(arr, arr.length, pos, width) ^ 1;
		holder = arr.filter(has_bit_at(bit_criteria, pos, width));
		arr = holder;
		pos++;
	}
	return arr[0];
}

(async function processLineByLine() {
	try {
		const	diagnostics = [];
		let	width = 0;
		rl.on('line', (line) => {
			diagnostics.push(parseInt(line, 2))
			if (line.length > width)
				width = line.length;
		});

		await events.once(rl, 'close');

		let	oxygen_generator_rating = get_oxygen_generator_rating(diagnostics, width);
		console.log("found oxygen rating", oxygen_generator_rating);
		let	co_scrubber_rating = get_co_scrubber_rating(diagnostics, width);
		console.log("found scrubber rating", co_scrubber_rating);
		let	life_support_rating = get_life_support_rating(oxygen_generator_rating, co_scrubber_rating);
		console.log("found life support rating", life_support_rating);
	} catch (err) {
		console.error(err);
	}
})();
