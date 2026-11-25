# Platform adapter

Contents: shape, start, events, ad breaks, rewarded ads, saves, mute and audio, consent, host layout, the mock and tests.

## Shape

- One adapter object. The game calls it and never a platform library.
- The adapter takes a driver for the target, or none. With none, every call is a safe no-op.
- The build picks the driver. Drivers of other targets are removed from the build.
- The adapter guards every driver call. An exception becomes a log warning and a default value.
- Rules that hold everywhere live in the adapter: no repeated events, no events during a break, time limits. Drivers only translate.

| Driver member | Returns |
|---|---|
| Start | True when the service works |
| Send event | Nothing |
| Show break or rewarded ad, with a callback when it begins to play | Watched, ended early, failed this time, or none for the session |
| Rewarded available | True or false |
| Storage | The platform's storage, or none |
| Device type | A value, or unknown |
| Watch mute | Calls back now and on change |
| Privacy required, open privacy form | Optional |

## Start

- Start during loading, with a time limit. After the limit, the game opens without the service.
- A late start may still enable ads later. It must not reopen the save that the game already uses.
- Some services throw on every call outside their own host. Treat that as a failed start.
- Choose where saves live before the first screen that needs them.

## Events

| Event | When |
|---|---|
| Loading start, loading stop | Around the real load |
| Play start | The first player input in play, and again after a pause or break. Not on load |
| Play stop | Pause, menu, level end, cutscene, before a break |
| Break | At a logical stop only |
| Celebration | Rare, for real achievements |

Keep the mapping as a table in the design document: game event, then the call on each target, or "None".

## Ad breaks

1. Stop play, then request.
2. Block input from the request until the end or the error.
3. Mute when the ad begins to play. Many requests never show one.
4. End on result, on error, or at a time limit.
5. After the break: unmute, accept input, continue.

- Guard against late callbacks. An ad that starts after its break timed out must not mute the game, because nothing will end that mute.
- Count your own frequency limit where the network has none.
- No break before the player has had a fair amount of play, and none on navigation.
- The game must be complete with ads off.

## Rewarded ads

| Case | Do |
|---|---|
| Watched to the end | Grant once |
| Ended early | No reward, no error text |
| Failed this time | Short notice, keep the button |
| None for the session | Remove or disable the offer |
| Reward arrives after the time limit | Grant it once, to the same level or offer, without interrupting play |
| Ad blocker | No reward, no message about blockers |

Never make a level or progress depend on a reward. A press must always do something.

## Saves

- If the platform has storage and it works, use it. Otherwise use local storage, then memory.
- On first use, merge the local save by best result for each identifier. See `game-programming-patterns`.
- Every access is guarded. Private windows and full quotas throw.

## Mute and audio

- Final mute = ad playing, or host asks, or the player's setting.
- A host's mute request wins over the game's toggle.
- Start and resume audio inside a user action. After a phone interruption, a visibility event may not be enough.
- Stop sound when the app goes to the background.

## Consent

- Ask before the first ad request where the law or platform requires it.
- Separate failed from slow. A slow answer continues in the background, and a form that arrives late waits for a pause in play.
- Offer a way back to the choices when the platform requires one.
- Derive age and audience settings from one switch. Check at build time that permissions, request flags and the switch agree, and check the merged result that ships.

## Host layout

- Respect safe areas on every side. Lay out again when they change alone.
- Reserve space for host overlays. If no call tells whether one shows, reserve it on that target.
- Prevent page scroll and text selection in embedded games. Leave the host's keys alone.
- Do not add a fullscreen button or orientation lock where the host provides them.
- On devices with a back button, define what it does on every screen, in loading, in a tutorial step and during an ad.

## The mock and tests

- The mock runs in development and test builds only. Its options: start works, fails or hangs; ads none, unavailable or held until the test ends them; reward on or off; device; mute; privacy.
- It records events, and the test bridge reads the record.
- Test each driver against a fake of its library: event names, error codes, throwing calls, no call before start.
- Test the adapter: no repeats, nothing during a break, time limits, late callbacks, mute sources, failures in every member.
- Test in the built game: play on after each failure, no request to other hosts.
