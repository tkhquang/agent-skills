# Polish audit

Contents: what polish is for, kinds of polish, the audit table, how to steer, when to stop.

## What polish is for

Polish is any effect that enhances an interaction without changing the simulation. Remove all of it and the game functions the same and feels dead. Every effect is a clue about a physical property: weight, mass, material, friction, force, fragility. Players assemble those clues into a model of the game's physical world, and anything that contradicts the model stands out.

Levels to review:

1. Individual effects: their motion, size, shape and timing.
2. The impressions they add up to.
3. The physical properties players infer.

Keep in mind:

- Realism is not the efficient route to belief. A ball that squashes on impact and stretches as it rebounds reads as more ball-like than an accurate rigid sphere. A burst of colored stars when a block is hit makes no physical sense and sells the impact perfectly.
- Perception fuses senses. Sight, sound and touch for the same event should arrive together and agree. When they disagree, motion wins over appearance and sound, and the mismatch breaks the illusion.

## Kinds of polish

### Animation

Layered on top of the simulated object, and to the player it is the object. A run cycle with squash, stretch and overlapping action gives weight and personality to what is, underneath, a sliding capsule. The classic principles of animation apply nearly unchanged, apart from staging, which assumes a controlled camera.

- Drive animation from the simulation, never the reverse. Let run-cycle playback speed follow actual movement speed.
- Anticipation and follow-through add weight and cost responsiveness. Keep the first visible response immediate and put the flourish afterward.
- Blends into physics (a tackled character going limp) keep the principle: animation leads until a force takes over.

### Visual effects

Brief, caused by an object and not part of it. They mark the moment and place of an interaction.

- Dust at the feet when starting, stopping and landing.
- Sparks on scraping contact, shifting from white to yellow to red as they fly.
- Trails behind fast-moving things, tracing the arc.
- Debris and splinters on destruction.
- Marks left behind: skid marks, scorch marks, holes.

The motion of a particle matters more than its picture. Burst outward convincingly, then fade.

### Sound

- Impacts: one event, one sound. The character of the sound says what both objects are made of. Reverb says what kind of space it happened in.
- Grinds: a short loop that is modulated continuously so sustained contact never sounds identical.
- Loops: engines, wind, hums.

- Keep several variants of frequent sounds and pick among them, so repetition does not grate.
- Sound changes what the player believes happened. Two balls whose paths cross appear to pass through each other in silence and to bounce when a contact sound plays.
- An attack that feels weak can often be fixed with a better sound and no animation change.
- Sounds do not need to be realistic to work.

### Camera effects

Applied to the view, borrowed from film, and read instantly.

- Screen shake: concussive force. Scale it to the event and keep it short.
- Hit pause: freezing the action on a hit. Values in use run from about 20 ms, one frame, to about 8 frames for a heavy hit in a fighting game. Scale it with the weight of the hit.
- Slow motion and zoom on a decisive moment.
- Field of view widening and motion blur for speed.
- Camera bob in time with footsteps. Camera rearing back in anticipation and snapping forward on a big action.

### Tactile

Controller vibration. It is a blunt instrument that works when it fits the metaphor: continuous rumble for automatic fire, a single pulse for one heavy shot, a low hum for grinding. Use sparingly. Resistance-based force feedback mostly adds fatigue.

## The audit table

Fill in one row per player action and per important world event. Empty cells are either opportunities or deliberate silence. The last column is the test: what should a player infer?

| Action or event | Animation | Visual effect | Sound | Camera | Tactile | What it should say |
|---|---|---|---|---|---|---|
| Start moving | | | | | | |
| Stop or turn sharply | | | | | | |
| Jump | | | | | | |
| Land | | | | | | |
| Attack starts | | | | | | |
| Attack connects | | | | | | |
| Take damage | | | | | | |
| Collect an item | | | | | | |
| Destroy an object | | | | | | |
| Fail or die | | | | | | |

Filled rows from a heavy third-person shooter:

| Action | Animation | Visual effect | Sound | Camera | Tactile | What it says |
|---|---|---|---|---|---|---|
| Enter cover | Tackle-like slam | Dust shaken from the wall | Crunch and thud | Reframes to put the character to one side | | This person is enormous and armored |
| Fire | Braced stance absorbing recoil | Muzzle flash, smoke, chips flying from the target | Deep report, ricochets, falling casings | Shakes in time with shots | Continuous rumble | The weapon is powerful and so is its user |

## How to steer

- Choose one overall impression before adding anything: heavy and brutal, light and springy, crisp and electric. Judge every effect by whether it supports that impression.
- Keep the level of abstraction consistent across look, sound and motion. A cartoon character can stretch and make comic noises. A photorealistic one cannot.
- A stylized treatment lowers what players expect and makes consistency achievable. Photorealism raises expectations for every interaction, including the ones the player invents.
- Make failure appealing too. Players spend much of their time failing. Varied, satisfying crashes reduce frustration and make people watching want to play.
- Exaggerate the result of each input enough that the player can see what happened and repeat it on purpose.
- Tie every effect to a real state change. Decoration that means nothing is read as feedback and confuses.

## When to stop

Polish expands to fill any schedule. Limits:

- Do not start until the motion feels right with plain shapes. Effects cannot rescue a core that is not fun, and a month of juice can hide that for a while.
- In a prototype, add only the minimum needed to judge the feel when the feel depends on it.
- Stop adding when new effects no longer change what players infer.
- Remove any effect that hides information the player needs.
- Offer options to reduce shake, flashes and blur.
