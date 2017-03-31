# Scissor-Paper-Rock Game with micro:bit and Bluetooth
The code simulates a popular Scissor-Paper-Rock game using two micro:bit devices communicating via Bluetooth. Full description for the challenge and installation instructions can be found in this [blog post][1].

* On shake the micro:bit should pick a random shape (scissors, paper, or rock) and show it using LED array on the device
* The two devices should connect and send the data over to each other
* The opposite device comperes then its own shape to the one received, and decides weather it won or lost
* Each of the two micro:bits shows then "Won" or "Lost" on the LED array.

**Note**: Make sure to change *group=1* to a number between 0 and 255. Both chips should belong to the same group to connect to each other.

[1]: http://mehmandarov.com/microbit-bluetooth-challenge/
