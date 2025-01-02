****************************
Attributes & Pools
****************************
Any being that breathes, walks, or talks features the same basic creature statistics.

--------

Primary and Secondary Attributes
================================
*Primary attributes* represent a creature's raw capabilities, used in the majority of rolls and checks. Every primary attribute directly determines the values of its associated *secondary attributes*.

Primary attributes can also be tracked in half numbers; rather than receiving another die, an attribute with an extra .5 point grants +1 reroll when using that attribute.

.. note::
      Each primary attribute and each pool (except for Vitality) is stopped at a maximum of 7. The minimum is also 1, though it is still possible to be reduced to 0 through effects or attribute damage. Attributes cannot be made negative.

--------

Might
=====
Might determines a creature's effectiveness at swinging a weapon or parrying incoming blows. For checks, Might may be used for acts of brute force, lifting power, or physical fitness.

Load
----
A creature's Load score is equal to its Might rounded down, allowing it to carry Bulk up to its Load score without penalty. Exceeding this limit will impose a -1 :term:`die penalty` to all Might or Grace based rolls, and an additional 1 taxed Stamina on any action costing Stamina. A creature physically cannot carry any more than twice its Load score.

.. Tip::
      An item marked with Light or 'L' weighs 1/3 of a point of Bulk. Every third Light item (when not rendered weightless by items such as pouches) counts as one point of Bulk.

--------
      
Grace
=====
Grace determines a creature's effectiveness at using ranged weaponry or dodging incoming danger. For checks, Grace may be used for manual dexterity, balance, or finesse.

Footwork
--------
A creature's Footwork is equal to half its Grace without a half-point, then rounded up. Each round, it may move a distance in squares within enemies' threat range equal to its Footwork without provoking an attack of opportunity. Leaving threat range still provokes an attack of opportunity as normal.

--------

Mettle
======
Whenever a physical attack successfully hits, a creature may roll to *soak* the damage, using Mettle to ignore flat damage equal to the successes rolled. For checks, Mettle may be used to endure harsh environments, strain one's body, or shake off mental conditions.

Belt Slots
---------
A creature has Belt slots equal to its Mettle score rounded down, which are used to hold various items for quick access in intense situations. Items can be transferred from a hand to an open Belt slot, or vice versa, without spending any Speed.

An item takes up Belt slots equal to its Bulk, or 1, whichever is higher. Stowing, drawing, or picking up an item from somewhere other than the Belt all cost Speed equal to its Bulk, also at a minimum of 1.

.. tip::
      A creature can freely drop items out of its hands without spending any Speed, though this comes with the obvious caveat of leaving that item unsecured in the environment.

--------

Insight
=====
Insight is used for most aspects of magic and tinkering, in addition to checks using perception, reasoning, or worldly knowledge.

Technique Slots
---------------
Creatures have Technique slots equal to their Insight rounded down. These slots are used to prepare weapon arts and spells, for quick use in combat or otherwise.

--------

Other Attributes
================

Hunger and Belly
----------------
Hunger affects how much food a creature must eat, while Belly is determined by Hunger and is a measure of satiation itself. A creature has maximum Belly equal to its Hunger value.

Every rest, the creature loses Belly equal to its Hunger. This can lower Belly into negative values, and various effects worsen as Belly decreases further.

.. list-table::
      :widths: 14 75
      :header-rows: 1

      * - Belly value
        - Effects
      * - 0 or above
        - Sleeping with 0 or higher Belly fully replenishes a creature's Anima, and restores 1 Vitality for every sleep action taken during a rest. 1 attribute damage is also recovered for each attribute.
      * - Below 0
        - A creature with this much Belly or lower gains half as much Anima, rounded up, from rest.
      * - Below -5 * Hunger
        - In addition to the effect above, a creature with this much Belly or lower suffers -1 to all primary attributes, but may roll to spot food twice and take the better result.
      * - Below -10 * Hunger
        - The creature is dead, having succumbed to starvation.

At the GM's discretion, an extended duration without rest may cost additional Belly.

Charm, Fright, & Style
--------------
These three attributes affect how a creature interacts socially with others. According to roleplay preferences, they can represent its appearance, how it acts, or even how it smells. Unlike other secondary or miscellaneous attributes, these are used in associated social checks, and follow similar rules to primary attributes, including the maximum of 7. See Social for more information.

.. tip::
      When distributing your bonus starting points for Charm/Fright, they may be broken up into half points (0.5) if desired.

Speed
-----
Speed determines how quickly a creature can move about or interact with its environment. It may move a number of spaces per turn equal to its Speed.

Attunement Points
-------
A creature has a base of 3 Attunement points plus its total Path ranks. These are allocated to attune with magical items, granting unusual and potentially powerful effects.

Absorption
----------
Some creatures have an Absorption score. After all DR has reduced the damage risked, and soaking has reduced the damage taken, Absorption applies. Absorption reduces the damage taken to 1, plus 1 for every time the damage meets the score and rolls over. Unless specified, Absorption applies to all damage except for :term:`true damage <damage type: true>`.

.. admonition:: Example...
      :class: note

      A creature has an Absorption of 3, and receives a devastating 7 damage after all other sources damage reduction. This damage would be reduced to a base of 1, and since its Absorption value fits into 7 twice, an additional 2 would be stacked on top, ending in a total of 3 damage received.

Bulk
----
Bulk is how much a creature weighs, should another wish to carry it. If a creature carries more Bulk than it weighs itself, that is treated as the greater of the two.

Size
----
Every creature has a set, incremental size. Small and Sverage creatures occupy one square, while Large ones occupy a space of 2 squares cubed. Stranger sizes may exist, such as Huge(3^3) or Colossal(4^4).

.. note::
      A creature cannot grapple or stun a creature more than one size above its own.

--------

Pools
=====
Unlike attributes, which remain static beyond certain effects, *pools* are active resources which fluctuate regularly as actions are taken. Only Vitality, Stamina, and Anima are common between all creatures; unique pools may be available to those with corresponding traits or features.

--------

Vitality
--------
The amount of damage a creature is able to take before dying.

Taking damage reduces Vitality, and a creature reduced to 0 Vitality dies. Particularly driven characters or those controlled by players may enter Death's Door when reduced to 0 Vitality instead.

Stamina
-------
How hard a creature can push itself in a single round of combat.

Most actions taken during combat cost at least 1 Stamina, and additional Stamina can be dedicated to attack and defense rolls. A creature's Stamina replenishes each round at the beginning of its turn.

Each rank taken in a martial path increases maximum Stamina by 1.

Anima
-----
A gauge of how much spiritual power fluctuates within a creature.

All spells and certain special abilities cost Anima, and it is also used while focusing to restore Vitality. Though it is primarily restored by resting, dealing damage to an opponent with a melee attack also grants 1 Anima.

Each rank taken in a mystic path increases maximum Anima by 1.

--------

Temporary Pools
===============
Certain effects may bestow an additional *temporary* increase to a creature's pools, tracked separately and not counting towards the pool's maximum. Unless noted otherwise, these additional points are lost when the creature rests.

Temporary Vitality is always lost first, but a creature may otherwise choose whether to spend its regular pools or temporary pools.
