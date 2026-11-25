# Economy balance

Contents: the plumbing audit, measurements to keep apart, inflation, stagnation, arbitrage, building an economy with tiers, price channels, crafting, fixed versus floating prices, checklist.

## The plumbing audit

Draw the economy as sources, stocks and sinks before tuning any number.

1. List every source of each currency and item: kills, quests, daily rewards, vendor buyback, crafting outputs, starting grants.
2. List every sink: purchases from the game, repairs, fees, upgrades, consumables, wear, taxes, losses on death.
3. Estimate each per hour of play at early, middle and late stages.
4. Compare totals at each stage. The gap is net issuance: currency created minus currency destroyed per hour. It says how fast the supply grows. It is not an inflation rate.
5. Note stocks without limits. Unlimited storage hides a growing supply and never cures it.

Anything the game creates from nothing is a source, even when it looks like a trade. A vendor who buys anything in unlimited quantity is a faucet.

## Measurements to keep apart

| Measure | Unit | Answers |
|---|---|---|
| Net issuance | Currency per hour of play, or per day across all players | Is the supply growing, and how fast? |
| Balances | Currency held: total, and median by player age | Is it piling up, and with whom? |
| Price level | Cost of a fixed basket of goods over time | Is each unit buying less? This is inflation or deflation |

Net issuance and inflation have different units. A game can issue 1,000 net coins per hour while every vendor price stays fixed: a growing supply with no price change.

Reading them together:

- Positive issuance, fixed prices, things still worth buying: healthy. Players are saving toward goals.
- Positive issuance, fixed prices, balances far above the price of anything desirable: the currency has stopped working as a reward. Add things to buy or scaling costs, not a tax.
- Rising basket price in a player-set market: inflation. Check balances to confirm that currency is the cause.
- Prices moving while issuance is flat: look at the goods. A change in how items are made or dropped moves prices with no change in the money supply.

Building the basket: use goods players actually trade, weight them by volume, and keep the basket fixed between comparisons.

A long-running space trading game tracks inflation this way, with indices from eight raw materials up to about 4,000 consumer items. It reports faucets, sinks and money supply apart from those indices.

- In one quarter its money supply grew 11 percent while consumer prices rose 4.7 percent.
- In another, consumer prices fell 2.1 percent because production rules for advanced items changed, not because of the currency.

Before launch, estimate: net issuance from the plumbing audit, balances by simulating a typical player through each stage, and price level from the cost of what a player at that stage wants next.

## Inflation

Cause: sustained net issuance with nothing to absorb it. Each unit buys less wherever prices can move, and eventually players ignore the official currency. In one action role-playing game gold became worthless, so players traded in gems, then a particular ring, then rare runes used like banknotes.

It is nearly universal because rewards must grow to stay exciting. One online game increased the money from a kill more than 750 times between level 1 and level 60. Without sinks growing at the same pace, money stops being a reward.

Countermeasures:

- Sinks that scale with wealth or level: repairs, upgrades, fees proportional to transaction size.
- Wear and breakage, which keeps ordinary items valuable.
- Storage caps, which also create a capacity upgrade path.
- New desirable things to buy at every stage.
- Fewer or rarer sources at higher levels.
- For games built on runaway growth, a reset loop: restart with a permanent multiplier earned from the last run.

Inflation can be used on purpose for a while. Reaching sums that once seemed impossible feels powerful as long as there is still something meaningful to spend them on.

## Stagnation

Cause: supply too tight or upkeep too high. Players hoard, nobody feels a trade is in their favor, and the economy stops moving. It usually comes from fighting inflation too hard, and it is rarer mostly because players leave before it shows.

Countermeasures: raise income, lower upkeep, guarantee a minimum income, make spending visibly worthwhile.

## Arbitrage

Arbitrage is buying in one place and selling for more in another.

In the earliest graphical online world, a vending machine sold dolls for 75 tokens and a pawn machine across town bought them for 100. Players ferried goods overnight and the money supply multiplied by five by morning. No bug was involved.

Rule: for every item, the highest price the game pays must be below the lowest price the game charges, everywhere. Audit all pairs, including through crafting and conversion chains.

## Building an economy with tiers

1. Group items into tiers by power and rarity.
2. Put power on a gentle exponential. With power = 1.2 to the tier, tier eight is about twice tier four.
3. Put rarity on a steep one. With rarity = 3 to the tier, tier eight is 81 times rarer than tier four.
4. Keep the two curves separate. The cost per unit of power then rises sharply, which checks power creep while keeping top items exciting.
5. Tie where items are found to danger or difficulty.

Finding the right bases takes playtesting. Once found, new content slots in without rederiving everything.

## Price channels for player markets

Give the market a floor and a ceiling and let players set prices in between.

- Floor: the game always buys any item at a low price, for example half its rarity value.
- Ceiling: the game always sells almost any item at a high price, for example twice its rarity value.

Effects:

- Everything can always be bought and sold, and nobody can corner a market.
- Temporary price swings do not damage the structure.
- Both bounds follow the same exponential, so the channel is narrow for low tiers (stable prices for beginners) and wide for high tiers (room for trading as gameplay).

The two multipliers are tuning values.

## Crafting

Ingredients should cost somewhat less than what they produce and rise in proportion to it. Check the full chain for arbitrage: buy ingredients, craft, sell to a vendor.

## Fixed versus floating prices

- Fixed prices and bottomless vendors: predictable, with no economic decisions. Right when selling loot is a step and not the point.
- Floating prices: decisions about where and when to sell, and more for the player to track. Right when trading is part of the game.

## Checklist

- Every source and sink listed, with rates at early, middle and late stages.
- Net issuance, balances and basket price tracked separately. No sink added on the strength of issuance alone.
- Sinks grow at least as fast as sources.
- No item can be bought for less than it can be sold, directly or through crafting.
- Every stage has something worth saving for and something worth spending on now.
- Storage limits exist where hoarding would hurt.
- The currency buys several kinds of things.
- A player returning after a long absence is not priced out, and a new player is not flooded.
