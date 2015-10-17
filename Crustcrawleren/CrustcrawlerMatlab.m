%Crustcrawler Group 7
%Second of kind V2.0
%Use Denavit-Hartenberg convention to establish coordinate frames for the robot
name = 'Crustcrawler';
n = 4; % # of joints
L(1) = Link([0 16.5 0 pi/2]);    
L(2) = Link([0 0 17.5 0]);     
L(3) = Link([0 0 6.5 0]);
L(4) = Link([0 0 18 0]);  %FIX så drejeledet sidder ordentlig på (ikke muligt iflg. læren)
%% Starting the toolbox
mydir = pwd;
cd('C:\Users\Mads\Desktop\ITROB\rvctools')
startup_rvc
cd('C:\Users\Mads\Desktop\ITROB\Week 3') %Change dir to ".\CrustcrawlerMatlab.m"

%% Extract the DH parameters from the model and Create a serial link between the toolbox and our robot 
Crustcrawler = SerialLink(L, 'name', 'Crustcrawler');
%Run the command "Crustcrawler"
Crustcrawler.teach([-0.785 0.266 -0.983 0])%Radianer for hver joint