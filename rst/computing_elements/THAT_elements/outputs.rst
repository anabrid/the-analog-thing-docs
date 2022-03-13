Outputs
=======

The **THAT** comes with 5 AUX-output connectors, X,Y,Z,U and a trigger-output called TRIG.

While the TRIG-output is limited in it's use as trigger-output, the other four outputs can also be used as inputs.

X,Y,Z,U
-------

The **X,Y,Z,U** outputs, to be found on top of the THAT next to the MINION-port, are connected with the output panels to be found in the bottom right corner of the patchfield.


While the THAT has a machine unit of 10 volts, the four outputs are realized as voltage divider with a factor of 10 to 1 so when using these outputs plus/minus one volt is to be expected.

TRIG
----

TRIG is used to trigger an oscilloscope and has the ModeOP (operation) signal connected. The signal is 5V TTL logic and the low level indicates operation while the high level indicates halted or initial state. The polarity of the TRIG signal can be changed with additional jumper J14 in case needed (not assembled by default).

In REP or REPF mode the TRIG signal can be used to trigger the regular repeated operation to show a more or less steady curve (depending on OP TIME) on an oscilloscope. 
