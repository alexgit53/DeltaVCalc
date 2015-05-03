# Delta V Calculator for Kerbal Space Program #

Simple Python program to calculate the delta v of a rocket stage in the game [Kerbal Space Program](https://kerbalspaceprogram.com/).

## Use ##

Enter the start and end masses of the stage - the end mass can easily be found in the VAB by draining the fuel you will burn. These should be entered in tonnes, which is the unit the Engineer's Report uses.

Then enter the vacuum ISP of the engine you're using (mouse over the engine in the parts menu), and the total thrust of the stage - which is `engine thrust * number of engines`.

The program will output your delta v; your acceleration at the start/end of the stage; and your TWRs on Kerbin, the Mun and Minmus at the start/end of the stage.
