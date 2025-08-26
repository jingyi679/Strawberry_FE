WRO 2025 Future Engineers

Team information: 
Team name: Strawberry
Team ID: FE-25-295-01
Team members: Ge Jingyi (in charge of software) and Katelyn Kang (in charge of hardware)

Contents: 
/t-photos contains our team photo

/v-photos contains photos of our robot 
  top.jpg
  bottom.jpg
  left.jpg
  right.jpg
  front.jpg
  back.jpg

/video contains both the .mp4 file of our video and the link to it on YouTube 
  videos.mp4
  videos.md

/schemes contains wiring diagrams for our robot

/src contains the source code used

/models contains all the .stl files for all of the 3D-printed parts of our robot and the technical drawings for each part 
  HMC5883L mount and technical drawing
  OpenMV H7 mount and technical drawing
  VL53L0X mount and technical drawing

/doc contains our documentation in pdf form 

Overview: 
Welcome to Team Strawberry’s github repository for WRO Future Engineers 2025. This README provides a simple overview of our robot. For more information, please refer to our documentation which can be found under /doc or can be accessed via this pdf: https://drive.google.com/file/d/1Vhu3sat-Zx_eqKWrcASS5R9QDsB3pyeH/view?usp=sharing   

Challenge overview: 
For WRO FE, the challenge is split into two rounds – the open round and the obstacle round. In the open round, the robot is required to drive 3 rounds around the game field before coming to a stop in the starting area. For the obstacle round, the robot also has to navigate through the green and red obstacles – turning to the left to go around the obstacle when it is green and to the right when it is red. 

Robot photos
They are in the /v-photos folder. They can also be accessed here: 
https://drive.google.com/drive/folders/1iPZja8Sno2P24jc1DyQ11vu2lhnCgzWN?usp=sharing 

Demo videos
The videos can be found on both this github repository and on YouTube. For the github, we have uploaded the .mp4 video of our robot runs under the /videos folder. For YouTube, we have uploaded the videos and they can be accessed using the following link: https://youtu.be/RUq1AFjBJ5Y 

Hardware overview: 
Parts used: 
1x EVN Alpha
2x 18650 Lithium ion batteries
2x LEGO EV3 Medium motors (45503)
2x VL52L0X ToF distance sensors 
1x OpenMV H7 Camera
1x HMC5883L Compass/ Magnetometer
Female to female jumper wires 
3D printed parts 
Various lego pieces 

For our robot chassis, we primarily used lego to build it. Our robot uses rear-wheel drive. The front wheels are used to control the robot’s direction while the back wheels are powered by a motor. This is because rear-wheel drive would provide better stability and control as compared to front-wheel drive. 
The back wheels are both connected to the same motor but using a lego differential gear, due to the rule that the 2 back wheels cannot be connected to different motors. Using a differential gear would allow each of the back wheels to turn at different speeds despite being connected to the same motor, hence allowing the robot to turn. 
The front wheels, which are used to control the robot’s steering, uses Ackermann steering. This would reduce the front wheel slipping. If the 2 front wheels were to be parallel when turning, the wheels would slip because the center of rotation for each wheel would be different. Hence, Ackermann steering was used to allow the inner wheel to turn more, preventing the wheels from slipping. 
For the sensors, our robot uses various non-lego sensors, such as VL53L0X ToFs, a camera etc. Hence, to securely connect these non-lego sensors to our robot chassis made up of lego, we have designed and 3D-printed our own mounts for each sensor. The mounts have holes to screw the non-lego sensors into and for lego technic pegs so that we could attach them to the robot using lego. The stl files for each mount can be found on our github under the /models folder.

Software overview: 
All of our source code has been uploaded to this github repository and can be found under the /src folder. 

Open round: 
For the open round, we initially wanted the robot to use the robot’s ToFs to find the robot’s distance from the outer and inner walls. From there, we would use PID (Proportional Integral Derivative) to ensure that the robot would stay a fixed distance away from the inner wall, hence allowing the robot to follow the inner wall and go around the field. However, we found that this could lead to some problems, such as the robot starting to spin due to an awkward position of the ToF sensor causing it to detect a much larger distance from the wall. 

Hence, we decided to also use a compass, which would allow us to also know the robot’s orientation. A PID controller was then applied to the compass readings to stabilise orientation, while the ToFs provided corrective adjustments to ensure the robot maintained an appropriate trajectory. 

Obstacle round: 
For the detection of the obstacles, we used our OpenMV camera. We used the ‘find_blobs()’ function to detect the red and green pillars as blobs. The camera would then be able to find the positions of the red and green pillars, and would hence send this information to the EVN via serial. This would then be used to determine how much the robot is supposed to turn to avoid the obstacle. 

