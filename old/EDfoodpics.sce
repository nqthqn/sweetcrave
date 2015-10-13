# EDfoodpics 3/2013 ksb


$EDfoodpicFile="EDfoodpicsNames.txt";

scenario = "EDfoodpics";     
pcl_file = "EDfoodpics.pcl";

#scenario_type = fMRI;
scenario_type = fMRI_emulation;

pulses_per_scan = 1;
pulse_code = 55;
scan_period = 2000;

default_trial_type = fixed;
default_font_size = 12;
default_background_color=192,192,192; # gray

begin;

bitmap {filename = "fixation.bmp";}fixation;     # fixation  
         
array {
   TEMPLATE "EDfoodpics.tem" {
      TEMPLATE $EDfoodpicFile;
   };
} pics; 

picture {    
	bitmap fixation;   
	x = 0;y = 0;              	      	      
} fpic;

picture {    
	bitmap fixation;   
	x = 0;y = 0;              	      	      
} spic;

picture {
#bitmap testbmp;x = 0;y = 0;
} default;

picture {} blank; 

trial {                # wait 5,000 ms before first trial
   trial_type=fixed;
   picture blank;   
   time=0;
   picture default;
   deltat=5000; #5000
}startDelay;

trial {                
   trial_type=fixed;
   trial_duration=5000;
   picture blank;   
   time=0;
}endDelay;

trial {
   trial_type=fixed;
   trial_duration=7000;
   
   picture fpic;
   time=0;
   
   stimulus_event {  
	   picture spic; 		
	   deltat = 3500;    		
	   code=60; 					
	   response_active=false;
   }picevent;

}theTrial;   
