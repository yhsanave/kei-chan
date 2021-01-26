# Kei-chan
UL Anime Club Discord Bot

---

# Cogs/Features

## Activity

Set Kei-chan's activity.

## Anti-Light Mode

Convert light mode screenshots into dark mode by reacting to a message with `⬜`.

## Avatar

Set Kei-chan's avatar manually, from a premade collection (in the avatar folder), randomly. Also allows automatic avatar updating every hour.

## Ballot

Make and edit ballots for meetings.

## Cogs

Manage loaded and unloaded cogs.

## Deep Fry

Deep fry an image by reacting to the message with `🍟` or by posting in a designated channel.

## Edit

Edit messages sent by Kei-chan.

## Jojo

Reacts to messages containing Jojo's references.

## Level 

Automatically react to Tatsumaki level-up messages.

## Say

Send messages as Kei-chan

## Someone

Jank implementation of the @someone april fools feature

---

# Commands

Command Prefix: `.`

| Cog | Command | Arugments | Description |
| --- | ------- | --------- | ----------- |
| activity | activity | type:*Int* activity:*String* | Sets Kei-chan's activity. Types: 0: Playing, 1: Steaming, 2: Listening, 3: Watching.|
| avatar | avatar | *none* | Sets Kei-chan's avatar to the first image attached to the messsage |
| avatar | cavatar | *none* | Toggles the automatic avatar cycle |
| avatar | lavatar | id:*Int* | Manually set Kei-chan's avatar by id |
| avatar | ravatar | *none* |  Switch Kei-chan to a random avatar |
| avatar | savatar | id:*Int* | Kei-chan posts the selected avatar |
| ballot | editballot | channel:*Channel* id:*Int* | Begins the edit process for a ballot |
| ballot | makeballot | channel:*Channel* | Begins the process of making a ballot to post in the selected channel |
| cogs | load | cog:*String* | Load the selected cog |
| cogs | reload | cog:*String* | Reload the selected cog |
| cogs | unload | cog:*String* | Unload the selected cog |
| edit | edit | channel:*Channel* id:*Int* message:*String* | Edits the selected message in the selected channel. Must be a message sent by Kei-chan |
| say | say | channel:*Channel* message:*String* | Kei-chan sends the message in the selected channel |
| *none* | help | *none* | Help Command |
| *none* | ping | *none* | Pong! |