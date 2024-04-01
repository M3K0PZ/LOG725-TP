# LOG725-TP5
what's here : Network code.

In TP5, I had to create a telegraph game with 2 parts:
 -  Host (J1): sends a text message to be encrypted.
 -  Client (J2): tries to encrypt the message in Morse code.

The basic project is in our GitHub repository, in the tp5_base directory. The exchanges between J1 and J2 are described as follows:

- J1 sends J2 a message, for example, "morse". J1 will encrypt this
message and keeps the encrypted version: -----.-....., but does not send it to J2.
-  The J2 receives the "morse" message. J2 starts transmitting the encrypted
of the message to J1, character by character.
-  Each time the J1 receives a character, a "beep" sound is heard in the
J1's computer, just like in a real telegraph.
-  At the same time, the J1's client application checks whether the sequence received up to that point
corresponds to the initial message. This check is carried out automatically
by the client application, not manually by the human player.

    - If there is a perfect match, J1 sends J2 a congratulatory message
congratulations, then J2 is forbidden to continue transmitting.

    - If there is no perfect match after the J2 has sent the same
characters as the encrypted version, J1 sends a failure message
failure message to J2, then J2 is forbidden to continue transmitting.

-  Then, if J1 sends a new message to J2, the game starts again and J2 can transmit again.

Requirements : 
