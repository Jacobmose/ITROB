%% Variables

clear

table_to_camera_height = 93.5;
table_width = 70; %cm
table_height = 39.5; %cm

bla_klods_l = 5; %længde
bla_klods_h = 5; %højde
bla_klods_b = 5; %bredde

resolution_width = 613;
resolution_height = 347;

border_to_object_measured = 31; %cm
top_to_object_measured = 15; %cm

border_to_Bloodobject = 269.5; %pixels

mm_per_pixel_picture_width = (table_width/resolution_width);
mm_per_pixel_picture_height = (table_height/resolution_height);

%% Show image
imtool('C:\Users\Jacobmosehansen\Desktop\IKT\6_Semester\ITROB\itrob_repo\Billeder\Test-Crop.jpg')

%% Calculations
mm_per_pixel = ((70)/611)
actual_distance_to_object = mm_per_pixel*border_to_Bloodobject

%% Calculations yellow object
border_to_object_yellow_measured = 36.5; %cm
top_to_object_yellow_measured = 18; %cm

border_to_object_yellow = 314.5; %pixels
top_to_object_yellow = 18; %pixels

actual_distance_to_object_yellow = mm_per_pixel_picture_width*border_to_object_yellow

%% Calculations blue object
border_to_object_blue_measured = 19; %cm
top_to_object_blue_measured = 18; %cm

border_to_object_blue = 164.3; %pixels
top_to_object_blue = 18; %pixels

actual_distance_to_object_blue = mm_per_pixel_picture_width*border_to_object_blue

%% Calculations red object
border_to_object_red_measured = 3; %cm
top_to_object_red_measured = 18; %cm

border_to_object_top_red = 26.63; %pixels
border_to_object_bottom_red = 28.25; %pixels
top_to_object_red = 18; %pixels

actual_distance_to_object__bottom_red = mm_per_pixel_picture_width*border_to_object_bottom_red
actual_distance_to_object_top_red = mm_per_pixel_picture_width*border_to_object_top_red

%% Calculations green object
border_to_object_green_measured = 36; %cm
top_to_object_green_measured = 3; %cm

border_to_object_green = 36; %pixels
top_to_object_green = 28.75; %pixels

actual_distance_to_object_green = mm_per_pixel_picture_height*top_to_object_green

%% Calculation coin

startup_rvc;

border_to_coin = 513.95;
border_to_coin_measured = 59;
top_to_coin_measured = 9.6;
top_to_coin = 85.09;

resolution_coin_width = 70/611;
resolution_coin_heigth = 39.5/344;

actual_distance_width_coin = resolution_coin_width*border_to_coin
actual_distance_height_coin = resolution_coin_heigth*top_to_coin

robot_frame = se2(34.2, 35, pi)
P_coin_camera_frame = [actual_distance_height_coin ; actual_distance_width_coin]
P_coin_robot_frame = inv(robot_frame)*[P_coin_camera_frame; 1]










