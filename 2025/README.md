# Solutions for Advent of Code 2025

Here are my solutions for the [Advent of Code 2025](https://adventofcode.com/2025) event.

Starting with 2025, there will only be 12 days of puzzles, instead of the previous 25 days.


## Short descriptions
In order for me to quickly find certain puzzles, what follows is a
list of short descriptions and tags of each exercise.

- Day 1: **Secret Entrance**
	- *Figure out a password by rotating a number dial.*
	- P1: Count the number of times that the dial ends up on 0.
	- P2: Count the number of times that the dial goes past 0.
	- `modulo`


- Day 2: **Gift Shop**
	- *Check IDs within given ranges for invalid numbers.*
	- P1: Find numbers that are made of some sequence of digits repeated twice.
	- P2: Find numbers that are made of some sequence of digits repeated at least twice.
	- `number ranges`, `repeated patterns`


- Day 3: **Lobby**
	- *Connect batteries in series to get enough joltage.*
	- P1: Find the digits that form the largest two-digit integer.
	- P2: Find the digits that form the largest twelve-digit integer.
	- `digit concatenation`, `recursion`


- Day 4: **Printing Department**
	- *Remove paper rolls if they have fewer than four neighbors.*
	- P1: Count the number of accessible paper rolls. 
	- P2: Repeatedly remove all accessible paper rolls until you cannot remove any more.
	- `2-dimensional`, `game of life`


- Day 5: **Cafeteria**
	- *Check ranges of ingredient IDs.*
	- P1: For each ID, find out if they are in a list of fresh ingredients. 
	- P2: Count how many unique ingredients are in the union of all ranged.
	- `number ranges`, `containment`, `interval`, `set intersection`, `set union`


- Day 6: **Trash Compactor**
	- *Parse some math equations written in columns.*
	- P1: Find the solutions of the equation in each column. 
	- P2: The computation is digit-wise and right-to-left.
	- `column-based`, `parse equations`, `digit-wise`, `right-assocative`


- Day 7: **Laboratories**
	- *Simulate a laser through 2D space that splits on some points*
	- P1: Count how many times the laser will split.
	- P2: On every split a new timeline appears, count the number of timelines. 
	- `2-dimensional`, `quantum`, `recursion`, `memoization`


- Day 8: **Playground**
	- *Build circles out of junction boxes, always connecting to the closest box.*
	- P1: Connect 1000 pairs and find the length of the three shortest circles.
	- P2: Continue connecting pairs until all are in the same circuit.
	- `2-dimensional`, `euclidean distance`


- Day 9: **Movie Theater**
	- *Work with rectangles with given corners.*
	- P1: Find the largest rectangle that can be built out of two given corners.
	- P2: Find the largest rectangle that is still within the polygon of all directly connected corners. 
	- `2-dimensional`, `quantum`, `recursion`, `memoization`


- Day 10: **Factory**
	- *Create a boolean and an integer pattern with a certain amount of button presses.*
	- P1: Determine the fewest button presses required to configure all indicator lights.
	- P2: Determine the fewest button presses required to configure all joltage levels.
	- `difficult`, `z3-prover`, `dijkstra-algorithm`, `linear optimization`


- Day 11: **Reactor**
	- *Analyze paths in a network of devices.*
	- P1: Count all paths from device `you` to device `out`.
	- P2: Count all paths from `svr` to `out` that must visit two specific nodes.
	- `directed graph`, `recursion`, `memoization`


- Day 12: **Christmas Tree Farm**
	- *Try to figure out if you can fit a list of shapes into a given area.*
	- P1: Figure out how many regions can fit the given list of presents.
	- P2: No exercise because it only requires you to have obtained 23 stars.
	- `np-hard`, `trick-question`

