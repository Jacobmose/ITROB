%% Variables

table_to_camera_height = 93.5;
table_width = 68.5; %cm
table_higth = 37.5; %usikker m�ling.

bla_klods_l = 5; %l�ngde
bla_klods_h = 5; %h�jde
bla_klods_b = 5; %bredde

oplosning_billede_width = 605;
oplosning_billede_height = 325;

kant_til_bla_klods = 78.33; %pixels
test = kant_til_bla_klods-11;

kant_til_bla_klods_maling = 11; %cm
top_til_bla_klods_maling = 13; %cm

billede_dpi = 96;

%% Show image
imtool('C:\Users\Jacobmosehansen\Desktop\IKT\6_Semester\ITROB\itrob_repo\Billeder\ALEXJACOB V3.jpg')

%% Calculations

mm_per_pixel_table = ((table_width*10)/oplosning_billede_width)
mm_per_pixel_table*test

