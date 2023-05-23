'''
IN PROGRESS...
'''


import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
Z = np.linspace(-10, 10, 100)

x, y, z = np.meshgrid(X, Y, Z)
print("### Magnetic Dipole in a Constant Vertical Magnetic Field ###")
print("					            @\n                                                   @@@ Z\n                                                  @   @\n                                                    @\n                                                    @\n                                                    @\n                                                    @                @@@@@@@  M\n                                                    @                   @@@@\n                                          ./(.      @                 @   @@\n                                       %        @   @               @      @\n                                    &              %@             @\n                                &                   @ &          @\n                             @                      @     &    @\n                         .,                         @       @\n                      &                             @     &    &\n                    %                               @   %          &                             @\n                  %  &                              @                 %                          @\n                        @                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Y\n                           ./                    @                            %  _                @\n                               (.             @                                     @            @\n                                   &      @                    .                  @\n                                       @                                       (\n                                    @     .*                           &    @\n                                @     @@      #.                        .*\n                             @       #@  @        @                  &\n                         @                            %           (\n                  @   @                                  ,,   #\n                  @ @                                      .\n                 @ @ @ @  X\n")

#Bz = float(input("Input Magnetic Field (in Tesla): "))
#I = float(input("\nInput Electric Current of the circuit (in Ampère): "))
theta = np.pi/4
Bz = 1
I = 1
a = 2
b = 2


