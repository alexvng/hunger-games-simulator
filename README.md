# Hunger Games simulator

## List of core features:

- Input a list of players
- Players have random events with other players
- Players track alive or dead
- Game loops until win

## List of ease of use features:
- Character names can be input with UI
- Character portraits can be uploaded (toggleable options)

## List of special features:

- Game has special functionality on start, cornucopia, and final elimination
- Game tracks status of characters (injury, energy, mental state, basic needs)
- Game tracks social links between characters
- Game tracks items carried and stashed by characters
  - items can break, be used, etc
- Game tracks locations of characters to determine chance of interaction
- Game assigns character traits

## Structure

- Class Player
  - Injury (pain) out of 100
  - Alive if pain != 0, 
  - Specific flags for body parts
  - Specific flags for illnesses
  - Injury (mental) out of 100
  - Sane if mental != 0
  - Specific flags for certain mental states (angry, terrified, vengeful, traumatized)
  - Starvation, thirst, exhaustion
- Class Event
  - int numParticipants
  - event text with $1, $2, etc
  - function to call on each one
- Class Item
  - subclass types of items
  - 