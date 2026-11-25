# Gate catalog

Contents: code, rules and content, screens and input, speed and size, saves, platform, assets and rights, people, a first set.

Pick by risk. The last column is how the gate passes while the game is wrong.

## Code

| Gate | Proves | Passes wrongly when |
|---|---|---|
| Types or compile | The project builds from clean output | Old compiled files remain. Delete them first |
| Lint | Style and banned constructs, such as engine code in the rules core | A ban has no test that fires it |
| Tooling tests | Contract and code agree. The gates themselves work | It is left out of the normal run |
| Build | Production packages exist, hold what they must and nothing else | A search has no positive control |

## Rules and content

| Gate | Proves | Passes wrongly when |
|---|---|---|
| Unit | Each rule, at its bounds, in the core | Tests restate the implementation |
| Determinism | The same seed and moves give the same state | Only one machine and one build type are used |
| Level solvability | Every shipped level can be finished, and its stored values match | The solver and game use different rules code |
| Difficulty bands | Each level fits its place in the curve | Bands are edited to fit the levels |
| Data rules | Each item, option or unit obeys the rule of its kind | The list is empty or filtered |
| Script sync | Shipped lines equal the approved script | Files outside its scope hold dialogue |
| Route coverage | Every label reached, every option picked, no dead end | Coverage counts test scripts |
| Content review | Each line and image in scope passes the content rules | Nobody keeps the line table |
| Simulation health | Bots finish games, no stall, no repeated impossible order | A turn limit hides stalls. Count them |

## Screens and input

| Gate | Proves | Passes wrongly when |
|---|---|---|
| Smoke | The built game starts, reaches play and completes a level with no error | The run skips the real load path |
| Phone run | The same by touch, at phone sizes, rotated and resized during play | Touch is simulated with mouse events |
| Screens | Every screen opens, closes, and has an exit, also when interrupted | Only the main path is walked |
| Captures | Each screen at each reference size was looked at | Files exist and nobody opened them |
| Text | Every string comes from the string table, fits, and uses shipped glyphs | The font subset is never compared with the strings |
| Accessibility | No information by color or sound alone, reduced motion works, targets and text meet their minimum size | It is a checklist with no owner |

## Speed and size

| Gate | Proves | Passes wrongly when |
|---|---|---|
| Frame budget | Percentiles hold on worst-case scenes under a stated load | Software rendering, or an idle scene |
| Size budget | Download, total, file count and largest file are inside the limits | It measures the development build |
| Soak | Long unattended play shows no growth or crash | The run stays on one screen |

## Saves

| Gate | Proves | Passes wrongly when |
|---|---|---|
| Save fixtures | Every released save version loads, and a corrupt or absent save starts clean | Fixtures are regenerated with the code |
| Storage failure | The game completes a level with storage blocked or full | Only the write is made to fail |
| Round trip | Save, load and continue equals never saved | Only a few fields are compared |

## Platform

| Gate | Proves | Passes wrongly when |
|---|---|---|
| Service adapter | Events in order, no repeats, no event during a break, failures never block play | The mock is kinder than the real service |
| Target split | Each build holds its own service code and content, and no other target's | Compiled or packed files are not unpacked |
| Package | Archive rules of the store, listing text and images complete | The archive is checked before it is written |
| Device smoke | Installs and plays on real hardware: touch, rotate, background, resume | An emulator stands in without saying so |
| Policy check | Each live rule page was read again on a stated date | Old notes are reused |

## Assets and rights

| Gate | Proves | Passes wrongly when |
|---|---|---|
| Asset check | Every shipped file has an entry with source, license and approval | Placeholders count as final |
| Attribution | Every shipped font and library has its notice in the package | Embedded code in a library is missed |

## People

| Gate | Proves | Passes wrongly when |
|---|---|---|
| Owner playtest | A named person played a named build for a named goal | Behavior changed after the play |
| Player test | New players understand and continue | The testers know the game. See `game-concept-prototyping` |

## A first set

For a project with nothing:

1. Compile and lint.
2. Unit tests on whatever rules can run headless.
3. A clean production build, searched for debug tools.
4. One smoke run on that build that completes the smallest full loop.
5. Captures at the smallest and the design size.
6. A size budget.

Add the rest as their subjects appear. Keep slow gates, such as a full frame test, for the release and say so in the contract.
