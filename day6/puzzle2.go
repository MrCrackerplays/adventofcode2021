package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
	"strconv"
)

func AizuArray(A string) []uint64 {
	a := strings.Split(A, ",")
	b := make([]uint64, len(a))
	var ed error
	for i, v := range a {
		b[i], ed = strconv.ParseUint(v, 10, 64)
		if ed != nil {
			log.Fatal(ed)
		}
	}
	return b
}

const days = 256

func breed(schools [9]uint64) [9]uint64{
	bred := schools[0]
	copy(schools[:], schools[1:])
	schools[6] += bred
	schools[8] = bred
	return schools
}

func main() {
	content, err := ioutil.ReadFile("input")
	var str string = string(content)
	if err != nil {
		log.Fatal(err)
	}
	var start_fish []uint64
	var schools [9]uint64
	start_fish = AizuArray(str)
	for _, s := range start_fish {
		schools[s]++
	}
	fmt.Println("Initial state:", schools)
	for i := 1; i <= days; i++ {
		schools = breed(schools)
		// fmt.Println("After", i, "days:", schools)
	}
	fmt.Println("After", days, "days:", schools)
	var	total uint64
	total = 0
	for _, s := range schools {
		total += s
	}
	fmt.Println("End Total:", total)
}
