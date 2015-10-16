%Crustcrawler Group 7

%First of kind V1.0

%Use Denavit-Hartenberg convention to establish coordinate frames for the robot
clear %% ALWAYS clear before running new script to verify we have the correct values

name = 'Crustcrawler';
%%n = 4; % # of joints
L(1) = Link([0 4.1 0 pi/2]);
L(2) = Link([0 0 12.2 0]); %%Orginial L(2) change to L(1) to get Matrix-A for 2-3     
L(3) = Link([0 0 0 pi/2]); %%Orginial L(3) change to L(1) to get Matrix-A for 3-4 
L(4) = Link([0 23.8 0 0]); %%Orginial L(4) change to L(2) to get Matrix-A for 3-4 
L
%% Starting the toolbox
mydir = pwd;
cd('C:\Users\Mads\Desktop\ITROB\rvctools')
startup_rvc
cd('C:\Users\Mads\Desktop\ITROB\Week 4')

%% Extract the DH parameters from the model and Create a serial link between the toolbox and our robot 
Crustcrawler = SerialLink(L, 'name', 'Crustcrawler');
%%Crustcrawler.n = 2;
%Run the command "Test1"
Crustcrawler
Crustcrawler.teach([0 0 0 0])

L.RP %Test to see which kind of links we got: R = Revolute P = Prismatic

%% Calculate the transformation A-matrices between frames

%% Crustcrawler.fkine([0 0]) with only the two required frames as input for the SerialLink.

%% fkine([L1 L2 L3 L4]) -> Use number of links defined

Crustcrawler.fkine([0 0 0 0])

% Plot
%%

