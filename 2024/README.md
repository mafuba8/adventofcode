# Solutions for Advent of Code 2024

Here are my solutions for the [Advent of Code 2024](https://adventofcode.com/2024) event.

## Short descriptions
In order for me to quickly find certain puzzles, what follows is a
list of short descriptions and tags of each exercise.

- Day 1: **Historian Hysteria**
	- *Compare two lists of numbers.*
	- P1: Pair up one number from each list from smallest to biggest.
	- P2: Figure out how often each number of the first list appears in the second.
	- `parsing`, `sort`, `contain`


- Day 2: **Red-Nosed Reports**
	- *Check lists of numbers if they are monotonicity.*
	- P1: Find lists where all numbers are increasing or decreasing.
	- P2: Now we are allowed to tolerate one pair of consecutive numbers that are not in order.
	- `order`, `monotonicity`


- Day 3: **Mull It Over**
	- *Filter out intact statements out of a heap of garbage symbols.*
	- P1: Find all the intact `mul(X,Y)` instructions.
	- P2: Also parse the `do()` and `don't()` instructions, which enable and disable the `mul(X,Y)` command.
	- `regex`


- Day 4: **Ceres Search**
	- *Word search with the word `XMAS`.*
	- P1: Count all occurrences of the word `XMAS` in the given word puzzle.
	- P2: Find all X-MAS patterns, which are two `MAS` words in the shape of an `X`.
	- `word search`, `crossword`, `2-dimensional`


- Day 5: **Print Queue**
	- *Work with lists of page numbers and before/after rules for their order.*
	- P1: Find all lists where the page numbers adhere the order rules.
	- P2: Put all the incorrectly ordered lists pack in their correct order.
	- `order`, `rules`, `re-arrange`, `inversions`


- Day 6: **Guard Gallivant**
	- *Analyze the path of a guard that walks through an area with obstacles.*
	- P1: Find all the tiles that the guard visits before leaving the mapped area.
	- P2: Find all the positions where you can put down one additional obstacle that forces the guard to
end up in a loop.
	- `2-dimensional`, `simulation`, `favourite`


- Day 7: **Bridge Repair**
	- *Operator search puzzle.*
	- P1: Find the equations that can be made true by inserting `+` and `*` operators.
	- P2: In addition of + and * operators, there is now an additional 'concatenation' operator `||`
	- `operator search`, `evaluation`


- Day 8: **Resonant Collinearity.**
	- *Analyze an integer lattice where each pair of antennas with the same frequency induce two 'Antinode' spots.*
	- P1: Find all unique locations where 'Antinodes' appear.
    - P2: Now each pair of antennas create a full lattice of antinodes (instead of only two).
	- `2-dimensional`, `geometric`


- Day 9: **Disk Fragmenter.**
	- *Simulate moving blocks of contiguous bits into spots of free space.*
	- P1: Create one contiguous block by moving bits into free space.
    - P2: Since this creates a lot of fragmentation, instead compactify while keeping bit blocks together.
	- `encoding`, `disk fragmentation`


- Day 10: **Hoof it.**
	- *Find hiking trails on a topographic map, which have an even, uphill slope.*
	- P1: Find all trailheads (start of a hiking trail) and count how many peaks are reachable from there.
    - P2: For each trailhead, count how many distinct hiking trails begin there.
	- `2-dimensional`, `topographic map`, `graph`


- Day 11: **Plutonian Pebbles.**
	- *Mysterious engraved stones which multiply exponentially according to a given rule set.*
	- P1: Find out how many stones there will be after blinking 25 times.
    - P2: Find out how many stones there will be after blinking 75 times.
	- `transformation ruleset`, `scaling problem`, `memoization`


- Day 12: **Garden Groups.**
	- *Calculate the amount of fences needed to split the garden into plots of the same plant.*
	- P1: Figure out the area and perimeter of each region.
    - P2: Instead of the circumference, find the number of sides each region has.
	- `area`, `circumference`, `flood-fill`


- Day 13: **Claw Contraption.**
	- *Win prizes through a Claw Machine arcade game where button presses cost tokens.*
	- P1: Find the fewest tokens needed to win all actually obtainable prizes.
    - P2: Same as P1, but now the prizes have way higher coordinates, requiring many more button presses.
	- `linear optimization`, `linear algebra`, `numpy`


- Day 14: **Restroom Redoubt.**
	- *Simulate the movements of several robots that each walks in a straight line and wrap at the borders.*
	- P1: Find the robot positions after 100 steps and the quadrant they are in.
    - P2: Find the step at which the robots arrange themselves into a picture of a Christmas tree.
	- `2-dimensional`, `simulation`, `OOP`, `easter-egg`, `curveball`


- Day 15: **Warehouse Woes.**
	- *Simulate a robot moving through a warehouse, pushing boxes around.*
	- P1: Find the positions of the boxes after the robot finishes moving.
    - P2: Similar to P1, but now the warehouse, boxes and walls are twice as wide.
	- `2-dimensional`, `simulation`, `sokoban`, `favourite`


- Day 16: **Reindeer Maze.**
	- *Race through a maze, where moving straight is cheaper than rotating 90 degrees.*
	- P1: Find the lowest possible score a racer could reach. 
    - P2: Find all the paths with the lowest score and the number of unique tiles that are on one of those.
	- `2-dimensional`, `graph`, `shortest path`, `dijkstra algorithm`, `all shortest paths`


- Day 17: **Chronospatial Computer.**
	- *Work with a 3-bit computer through its rudimentary Assembly-like language.*
	- P1: Simulate the 3-bit computer and find out what it is trying to output.
    - P2: Find the value in register A so that the program outputs an exact copy of the program itself.
	- `assembly`, `3-bit computer`, `register`, `instructions`, `curveball`, `pattern analysis`


- Day 18: **RAM Run.**
	- *Walk through a maze that gradually builds up through falling blocks of obstacles.*
	- P1: Find the minimum number of steps needed to reach the exit after 1024 blocks have dropped.
    - P2: Find the first block that will cut off the path to the exit.
	- `2-dimensional`, `graph`, `shortest path`, `dijkstra algorithm`, `path existence`, `binary search`, `favourite`


- Day 19: **Linen Layout.**
	- *Arrange a list of coloured stripes into towel patterns.*
	- P1: For each design, find out if it can be built with the given patterns. 
    - P2: For each possible design, count all the different ways that they can be made from the given patterns.
	- `pattern matching`, `memoization`


- Day 20: **Race Condition.**
	- *Race through a single-path track, where you are allowed to cheat once, disabling collision for a few steps.*
	- P1: Find all 2-step no-collision cheats that would save you at least 100 steps.
    - P2: Find all 20-step no-collision cheats that would save you at least 100 steps.
	- `2-dimensional`, `manhattan metric`, `favourite`


- Day 21: **Keypad Conundrum.**
	- *Recursive shortest path problem where robots control other robots through keypads.*
	- P1: Find the least number of button presses needed to input the code on the final keypad. (Two directional keypad
robots)
    - P2: Same as P1, but now there are 25 directional keypad robots inbetween.
	- `all shortest paths`, `scaling`, `memoization`, `favourite`


- Day 22: **Monkey Market.**
	- *Hashing algorithm to create pseudorandom numbers.*
	- P1: For each entry, find the number created after 2000 runs of the given mix/prune algorithm.
    - P2: Track difference after each algorithm step and find the one that gives the most bananas.
	- `hashing algorithm`, `brute-force`


- Day 23: **LAN Party.**
	- *Graph clique problem: Find fully-connected vertex subsets.*
	- P1: Find all computer-trios in the network that are connected to each other and one of them starts with 't'.
    - P2: Find the largest clique of computers
	- `graph`, `clique problem`


- Day 24: **Crossed Wires.**
	- *Work with a network of logical gates.*
	- P1: Simulate the logical gates and find out what decimal number it produces.
    - P2: Find the four wires that need to be swapped so that the whole contraption acts like a binary Adder.
	- `binary representation`, `binary adder`, `logical gates`, `no good way to automate`


- Day 25: **Code Chronicle.**
	- *Match key patterns to their corresponding lock patterns.*
	- P1: Find the number of unique lock/key pairs.
    - P2: No exercise because it only requires you to have obtained 49 stars.
	- `matching patterns`
