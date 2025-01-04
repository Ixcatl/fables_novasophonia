****************************
Attributes & Pools
****************************
Any being that breathes, walks, or talks features the same basic creature statistics.

--------

Primary and Secondary Attributes
================================
*Primary attributes* represent a creature's raw capabilities, used in the majority of rolls and checks. Every primary attribute determines the base value of its associated *secondary attribute*.

Primary attributes can also be tracked in half points; an attribute with an extra .5 point grants +1 reroll when using that attribute, as per basic rules.

Primary attributes peak at a maximum permanent value of 7. Their minimum permanent value is 1, though it is still possible to reduce them to 0 through effects or attribute damage. Attributes cannot be made negative.

--------

Might
=====
Might determines a creature's effectiveness at swinging a weapon or parrying incoming blows. For checks, Might may be used for acts of brute force, lifting power, or physical fitness.

Load
----
A creature's Load score is equal to its Might rounded down, allowing it to carry Bulk up to its Load score without penalty. Exceeding this limit will impose a -1 :term:`die penalty` to all Might or Grace based rolls and an additional 1 taxed Stamina on any action costing Stamina. A creature physically cannot carry any more than twice its Load score.

.. Tip::
      An item marked with Light or 'L' weighs 1/3 of a point of Bulk. Every third Light item (when not rendered weightless by items such as pouches) counts as one point of Bulk.

--------
      
Grace
=====
Grace determines a creature's effectiveness at using ranged weaponry or dodging incoming danger, in addition to its placement in the turn order. For checks, Grace may be used for manual dexterity, balance, or finesse.

Footwork
--------
A creature's Footwork is equal to half its Grace (sans half point, if any) rounded up. Each round, it may move a distance in squares within enemies' threat range equal to its Footwork without provoking an attack of opportunity. Leaving threat range still provokes an attack of opportunity as normal.

--------

Mettle
======
Mettle is a measure of how much physical or mental punishment a creature can take, used primarily to soak up damage taken. For checks, Mettle may be used to endure harsh environments, strain one's body, or shake off mental conditions.

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
Creatures have Technique slots equal to their Insight rounded down. These slots are allocated to prepare weapon arts and spells for regular use.

--------

Other Attributes
================

Hunger and Belly
----------------
Hunger affects how much food a creature must eat, while Belly is determined by Hunger and is a measure of satiation. A creature has maximum Belly equal to its Hunger value.

Every rest, the creature loses Belly equal to its Hunger. This can lower Belly into negative values, and various effects worsen as Belly decreases further.

.. list-table::
      :widths: 14 75
      :header-rows: 1

      * - Belly value
        - Effects
      * - 0 or above
        - Sleeping with 0 or higher Belly fully replenishes a creature's Anima and restores 1 Vitality for every sleep action taken during a rest. 1 attribute damage is also recovered for each attribute.
      * - Below 0
        - A creature with this much Belly or lower gains only half its maximum Anima, rounded up, from sleep. Additional sleep actions in the same rest will not further restore Anima.
      * - Below -5 * Hunger
        - In addition to the effect above, a creature with this much Belly or lower suffers -1 to all primary attributes.
      * - Below -10 * Hunger
        - The creature is dead, having succumbed to starvation.

At the GM's discretion, characters going long periods without rest may burn through additional Belly.

Charm, Fright, & Style
--------------
These three attributes affect how a creature interacts socially with others. According to roleplay preferences, they can represent its appearance, how it acts, or even how it smells. These are used in associated social checks, and follow similar rules to primary attributes, including maximum/minimum values. See Social for more information.

.. tip::
      When distributing your bonus starting points for Charm/Fright, they may be broken up into half points (0.5) if desired.

Speed
-----
Speed determines how quickly a creature can move about or interact with its environment. It may move a number of squares per turn equal to its Speed.

Attunement Points
-------
A creature has a base of 3 Attunement points plus its total Path ranks. These are allocated to attune with magical items, granting unusual and potentially powerful effects.

Absorption
----------
Some creatures have an Absorption score. After all DR has reduced the damage risked, and soaking has reduced the damage taken, Absorption applies. Absorption reduces the damage taken to 1, plus however many times the Absorption score fits into it. Unless specified, Absorption applies to all damage except for :term:`true damage <damage type: true>`.

.. admonition:: Example...
      :class: note

      A creature has an Absorption of 3 and somehow receives 7 damage after all other sources damage reduction. This damage would be reduced to a base of 1, and since its Absorption value fits into 7 twice, 2 is added, ending in a total of 3 damage received.

Bulk
----
Bulk is how much a creature weighs, should another wish to carry it. If a creature carries more Bulk than it weighs itself, that is treated as the greater of the two.

Size
----
Every creature has a specific amount of squares they take up at once. Small and Average creatures occupy one square, while Large ones occupy a space of 2 squares cubed. Certain creatures may be larger, such as Huge(3^3) or Colossal(4^4), or with modified sizes that are asymmetrical entirely. A creature with such will display how many squares it takes up in its character sheet.

.. note::
      A creature cannot grapple or stun another more than one size above its own.

--------

Pools
=====
Unlike attributes which remain static beyond certain effects, *pools* are active resources which fluctuate regularly as actions are taken. Only Vitality, Stamina, and Anima are common between all creatures; unique pools may be available to those with corresponding traits or features.

Pools share the same minimum and maximum values as attributes, except for Vitality, which does not have an upper limit.

--------

Vitality
--------
The amount of damage a creature is able to take before dying.

Taking damage reduces Vitality, and a creature reduced to 0 Vitality dies. Particularly driven characters or those controlled by players may instead enter Death's Door when reduced to 0 Vitality.

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
