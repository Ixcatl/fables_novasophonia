****************************
Attributes & Pools
****************************
Whether sapient like common rats and oppressive dreadwyrms, or feral like lowly bugs and beasts, almost every spirited being found in this world and beyond features the same basic character statistics.

--------

Primary and Secondary Attributes
================================
*Primary attributes* represent one's raw capabilities, used in the vast majority of rolls and checks. Every primary attribute directly determines the values of its *secondary attributes*.

Primary attributes can also be tracked in half numbers; rather than receiving another die, an attribute with an extra .5 point has +1 reroll when using that attribute.

.. note::
      Each primary attribute and each pool (except for Vitality) is capped at a maximum of 7, the peak of what any mortal creature can attain. The minimum is also 1, though it is still possible to receive attribute damage down to 0.

--------

Might
=====
A measure of strength and physical fitness.

Might determines one's effectiveness at swinging a weapon or parrying incoming blows. For checks, Might may be used for shows of brute force, lifting power, or strenuous athleticism.

Load
----
A character's Load score is equal to their Might rounded down. They may carry Bulk up to their Load without penalty. One may hold up to twice their Load, but they will suffer a -1 :term:`die penalty` to all Might or Grace based rolls and must spend an additional 1 taxed Stamina on any action costing Stamina. A character physically cannot carry more than twice their Load score.

.. Tip::
      An item marked with Light or 'L' weighs 1/3 of a point of Bulk. Every third Light item not rendered weightless by items such as pouches counts as one point of Bulk.

--------
      
Grace
=====
A measure of how fine and swift a creature can be in their movements.

Grace determines one's effectiveness at using ranged weaponry or dodging incoming danger. For checks, Grace may be used for manual dexterity, balance, or finesse.

Footwork
--------
A creature's Footwork is equal to half their Grace without the half-point, then rounded up. Each round, they may move a distance in paces within enemies' threat range equal to their Footwork without provoking an attack of opportunity. Leaving threat range still provokes an attack of opportunity as normal.

--------

Mettle
======
A measure of the thickness of one's skin, metaphorical or otherwise, and the strength of their resolve.

Whenever a physical attack successfully hits, a creature may roll to *soak* the damage, using Mettle to ignore flat damage equal to the successes rolled. For checks, Mettle may be used to endure harsh environments, strain one's body, or shake off mental conditions.

Belt Slots
---------
A character has Belt slots equal to their Mettle score rounded down, which are used to hold various items for quick access in intense situations. They may transfer an item from a hand to an open Belt slot, or vice versa, without spending any Speed.

Any given item takes up Belt slots equal to its Bulk, or 1, whichever is higher. Stowing, drawing, or picking up an item from somewhere other than the Belt all cost Speed equal to its Bulk, also at a minimum of 1.

.. tip::
      Items can be freely dropped out of the hands without spending any Speed, though this comes with the obvious caveat of leaving your item unsecured in the environment.

--------

Insight
=====
A measure of the perception, reasoning, and worldly knowledge of a character.

Insight is used for most aspects of magic and tinkering, in addition to checks using keen senses, sharp intuition, or recalled lore.

Technique Slots
---------------
A character's Technique slots are the staging ground for their arts and spells, assigned for quick and easy use. Characters have Technique slots equal to their Insight rounded down.

--------

Other Attributes
================

Hunger and Belly
----------------
Hunger affects how much food a creature must eat, while Belly is determined by Hunger and is a measure of how sated they are. A creature has maximum Belly equal to their Hunger value.

Every rest, the creature loses Belly equal to their Hunger. This can lower Belly into negative values, and various effects worsen as Belly decreases further.

+-----------------------+------------------------------------------------------------------------------------------------------------+
| Belly Value           | Effects                                                                                                    |
+=======================+============================================================================================================+
| 0 or above            | Taking a sleep with 0 or higher Belly fully replenishes a creature's Anima, and restores 1 extra Vitality  |
|                       | for each sleep camp action. They also recover from 1 attribute damage per attribute.                       |
+-----------------------+------------------------------------------------------------------------------------------------------------+
| Below 0               | A creature with this much Belly or lower gains half as much Anima, rounded up, from rest.                  |
+-----------------------+------------------------------------------------------------------------------------------------------------+
| Below -5 * Hunger     | In addition to the effect above, a creature with this much Belly or lower suffers -1 to all                |
|                       | primary attributes, but may roll to spot food twice and take the better result.                            |
+-----------------------+------------------------------------------------------------------------------------------------------------+
| Below -10 * Hunger    | The creature is dead, having succumbed to starvation.                                                      |
+-----------------------+------------------------------------------------------------------------------------------------------------+

At GM discretion, prolonged exertion without rest can cost additional Belly.

Charm, Fright, & Style
--------------
These three attributes affect how a character interacts socially with others. According to roleplay preferences, they can represent their appearance, how they act, or even how they smell. Unlike other secondary or miscellaneous attributes, these are used in associated social checks, and follow similar rules to primary attributes, including the maximum of 7. See Social for more information.

.. tip::
      When distributing your bonus starting points for Charm/Fright, they may be broken up into half points (0.5) if desired.

Speed
-----
Speed determines how quickly a creature can move about or interact with their environment. They may move a number of spaces per turn equal to their Speed.

Attunement Points
-------
A character has a base of 3 Attunement points plus their total Path ranks. These are allocated to bear magical items, granting unusual and potentially powerful effects.

Absorption
----------
Some creatures have an Absorption score. After all DR has reduced the damage risked, and soaking has reduced the damage taken, Absorption applies. Absorption reduces the damage taken to 1, plus 1 for every time the damage meets the score. Absorption even reduces unusual sources, such as DoT effects or unsoakable damage, but never :term:`true damage <damage type: true>`.

.. admonition:: Example...
      :class: note

      A creature has an Absorption of 3, and receives a devastating 7 damage after all other sources damage reduction. This damage would be reduced to a base of 1, and since their Absorption value fits into 7 twice, an additional 2 would be stacked on top, ending in a total of 3 damage received.

Bulk
----
Bulk is how much a creature weighs, should another wish to carry them. If a creature carries more Bulk than they weigh themselves, that is treated as the greater of the two.

Size
----
Every creature has a size, varying from small, average, or large. Small and average creatures occupy one square, while large ones occupy a space of 2 squares cubed.

Even larger creatures exist, and their sizes can vary heavily. Such huge creatures are often immune to effects such as grapples and stuns.

--------

Pools
=====
Unlike attributes, which usually remain static beyond debuffs, *pools* are active resources which fluctuate regularly as actions are taken and consequences endured. Only Vitality, Stamina, and Anima are common between all creatures; several others are available to those with the corresponding playstyles or traits.

--------

Vitality
--------
The amount of damage a creature is able to take before dying.

Taking damage reduces Vitality, and a creature reduced to 0 Vitality dies. Particularly driven characters or those controlled by players may enter Death's Door when reduced to 0 Vitality instead.

Stamina
-------
How hard a creature can push themselves in a round of combat.

Most actions taken during combat cost at least 1 Stamina, and additional Stamina can be dedicated to attack and defense rolls. A creature's Stamina replenishes each round at the beginning of their turn.

Each rank taken in a martial path increases maximum Stamina by 1.

Anima
-----
A gauge of how much spiritual power fluctuates within a creature.

All spells and certain special abilities cost Anima, and it is also used while focusing to restore Vitality. Though it is primarily restored by resting, dealing damage to an opponent with a melee attack also grants 1 Anima.

Each rank taken in a mystic path increases maximum Anima by 1.

--------

Temporary Pools
===============
Special abilities and effects can provide an additional temporary, or temp., increase to a creature's pools, tracked separately and not counting towards the pool's maximum. These additional points go away when the creature takes a rest, unless noted otherwise.

Temp. Vitality is always lost first, but the creature can otherwise choose whether to spend their regular pools or temporary pools.
