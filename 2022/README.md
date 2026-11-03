# Solutions for Advent of Code 2022

Here are my solutions for the [Advent of Code 2022](https://adventofcode.com/2022) event.

## Short descriptions
In order for me to quickly find certain puzzles, what follows is a
list of short descriptions and tags of each exercise.

- Day 1: **Calorie Counting**
  - *Combine sets of numbers.*
  - P1: Find the set with the highest combined number.
  - P2: Find the top-three sets.
  - `parsing`, `sort`

- Day 2: **Rock Paper Scissors** 
  - *Follow a strategy for a Rock-Paper-Scissors game.*
  - P1: Calculate score when you play according to the guide.
  - P2: Now you need to pick your shape so that the result is as in the guide.
  - `game`, `matching`

- Day 3: **Rucksack Reorganization** 
  - *Analyze a series of items(characters) in each half of a string.*
  - P1: Find items shared by both compartments, weighted by priority.
  - P2: Find the item shared by sets of three Rucksacks.
  - `partitioning`, `shared item`

- Day 4: **Camp Cleanup** 
  - *Compare overlapping ranges of ID numbers.*
  - P1: Find range pairs where one contains the other.
  - P2: Find range pairs that overlap at all.
  - `bounding box intersection`

- Day 5: **Supply Stacks** 
  - *Tower of Hanoi style Box stacking.*
  - P1: Find crate on top of each stack.
  - P2: Now the crane can move several boxes at once.
  - `Tower of Hanoi`, `Stack`

- Day 6: **Tuning Trouble** 
  - *Parse datastream using packet markers.*
  - P1: Find the first occurrence of four distinct characters. 
  - P2: Find the first occurrence of fourteen distinct characters.
  - `datastream`, `distince characters`

- Day 7: **No Space Left On Device** 
  - *Parse terminal input of a Unix style directory tree.*
  - P1: Find the total size of all directories.
  - P2: Choose the smallest directory to delete that frees up enough space. 
  - `Terminal Input`, `Stack`

- Day 8: **Treetop Tree House** 
  - *Find the idea tree for a tree house.*
  - P1: Count trees that are visible from outside.
  - P2: Find the tree with the highest scenic score.
  - `2-dimensional`

- Day 9: **Rope Bridge** 
  - *Simulate a rope wrigglin through the air.*
  - P1: Find all positions that the 2-segment rope has visited.
  - P2: Same as P1, but now the rope has ten segments.
  - `simulation`

- Day 10: **Cathode-Ray Tube** 
  - *Simulate basic CPU though assembly-like syntax.*
  - P1: Calculate the state after six different cycle lengths.
  - P2: Figure out which words the CPU draws on the screen. 
  - `assembly`, `CPU`, `text solution`

- Day 11: **Monkey in the Middle** 
  - *Simulate a monkey game dictated by some simple rules.*
  - P1: Find the two most active monkeys.
  - P2: No number limiting rule now, simulate 10000 rounds.
  - `simulation`, `residues modulo primes`, `scaling`

- Day 12: **Hill Climbing Algorithm** 
  - *Find climbing paths on a height map.*
  - P1: Find the path with the fewest steps.
  - P2: Find the shortest path from a tile with height 'a' to the end.
  - `2-dimensional`, `shortest path`

- Day 13: **Distress Signal** 
  - *Handle recursively defined packets.*
  - P1: Compare pairs of packets if they are in right order.
  - P2: Organize all packets in the right order.
  - `recursive`, `bubblesort`

- Day 14: **Regolith Reservoir** 
  - *Simulate sand falling on a given height profile.*
  - P1: Count how many units of sand end up resting.
  - P2: Now with a ground, simulate how many units end up before the source is stuck.
  - `2-dimensional`, `simulation`, `physics`, `endless`

- Day 15: **Beacon Exclusion Zone** 
  - *Recover the global structure from a set of local data.*
  - P1: Find how many spots without beacon are in a far row.
  - P2: Find the beacon outside all scanning ranges.
  - `inverse 2-dimensional`, `manhattan distance`

- Day 16: **Proboscidea Volcanium** 
  - *Find the optimal path between valves and caves.*
  - P1: Find the most pressure that can be released in 30 minutes.
  - P2: Find the most pressure that can be released in parallel with an elephant.
  - `graph`, `optimization`, `elephants`, `hard`

- Day 17: **Pyroclastic Flow** 
  - *Simulate falling Tetris blocks.*
  - P1: Find the tower height after 2022 rocks have fallen.
  - P2: Find the tower height after 1 trillion rocks have fallen.
  - `simulation`, `Tetris`, `favourite`, `cycle`

- Day 18: **Boiling Boulders** 
  - *Calculate the surface of a polycube.*
  - P1: Get the total surface of the obsidian blob.
  - P2: Get the total outer surface of the obsidian blob.
  - `3-dimensional`, `surface calculation`, `flood-fill`

- Day 19: **Not Enough Minerals** 
  - *Crack geodes using self-replicating robots built from blueprints.*
  - P1: Find the number of geodes each blueprints can produce in 24 minutes.
  - P2: Same as P1 but for 32 minutes and only for three blueprints.
  - `hard`, `recursive`, `memoization`

- Day 20: **Grove Positioning System** 
  - *Apply a number shuffling algorithm where numbers are moved according to their value.*
  - P1: Apply the mixing algorithm to your input.
  - P2: Longer routine involving 10 mixing steps.
  - `circular`, `self-referencing operation`

- Day 21: **Monkey Math** 
  - *Solve a monkey riddle involving numbers and math operations.*
  - P1: Find the value of the root monkey.
  - P2: Figure out what number yourself need to shout so that it works out.
  - `math operations`, `recursive`, `inverse problem`

- Day 22: **Monkey Map** 
  - *Simulate the path through a given maze with circular boundaries.*
  - P1: Find the final position in the path. 
  - P2: The map turns out to be the net of a cube.
  - `2-dimensional`, `cube net`

- Day 23: **Unstable Diffusion** 
  - *Simulate elfs moving around.*
  - P1: Find the rectangular boundary after 10 steps.
  - P2: Find the rectangular boundary after no elf moves anymore. 
  - `2-dimensional`, `endless`, `rectangle boundary`

- Day 24: **Blizzard Basin** 
  - *Find the path through a valley while dodging roaming blizzards.*
  - P1: Find the fewest number of minutes requires to get through the valley.
  - P2: Fewest numbers to the goal, back to start and then again to the goal.
  - `2-dimensional`, `graph`, `shortest-path`, `dijkstra`

- Day 25: **Full of Hot Air** 
  - *Work with a weird number system.*
  - P1: Add up numbers given in a weird number system. 
  - P2: No exercise because it only requires you to have obtained 49 stars.
  - `number system`
