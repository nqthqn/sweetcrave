% set up pumps parameters for Chocolate
% this script runs 4 pumps
% 0 = tasteless
% 1 = milkshakeA
% 2 = milkshakeB
% 3 = milkshakeC
% 4 = milkshakeD
% delivers 1 ml over 3 sec
% to calculate rate: rate = (volume divided by sec) multiplied by
% 60 sec. In this case: .5/3 x 60 = 10 (deliver .5 ml over a 3 sec
% duration with a rate of 7.5 mm)
% so in this case we want to deliver max volume over 3 sec. Max rate =
% 15mm, so a/3 x 60 = 15, resolve for a, a = 1 ml.
%to calculate rate: (volume/sec) *60 sec. ex. .2/3 x 60 (deliver .2 ml over a 3 sec duration)

s1=serial('com4','baudrate',19200,'databits',8,'terminator',13);
fopen(s1);
i=0;
    fprintf(s1,([num2str(i) 'dia26.59']));  %syringe inner diameter
    wait(100);
    fprintf(s1,([num2str(i) 'phn01']));  %BEGINNING OF PHASE 1 (before subject receives liquid, infuse to get the liquid to the end of the tube)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat'])); %function pumpint rate
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));   %ml per hour converted into ml per minute (15mm equal to max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.2']));  %volume to be dispensed (takes Xseconds)
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));  %dirinf=pumping direction = infuse
    wait(100);
    fprintf(s1,([num2str(i) 'phn02'])); %BEGINNING OF PHASE 2 (when subject is actually receiving the liquid)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));  %dispenses at a rate of 15 mm (max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.75']));  %volume to be dispensed is .75 (a/3 x 60 = 15, resolve for .75) over 3 seconds
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));
    wait(100);
    fprintf(s1,([num2str(i) 'phn03']));   %BEGINNING OF PHASE 3 (withdraw liquid to prevent any drippage)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm'])); %WITHDRAW AT THE MAXIMUM RATE
    wait(100);
    fprintf(s1,([num2str(i) 'vol.5']));
    wait(100);
    fprintf(s1,([num2str(i) 'dirwdr'])); % direction withdraw
    wait(100);
    fprintf(s1,([num2str(i) 'phn04']));  %  begin phase 4 (stop)
    wait(100);
    fprintf(s1,([num2str(i) 'funstp'])); % stop pump
i=1;
    fprintf(s1,([num2str(i) 'dia26.59']));  %syringe inner diameter
    wait(100);
    fprintf(s1,([num2str(i) 'phn01']));  %BEGINNING OF PHASE 1 (before subject receives liquid, infuse to get the liquid to the end of the tube)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat'])); %function pumpint rate
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));   %ml per hour converted into ml per minute (15mm equal to max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.2']));  %volume to be dispensed (takes Xseconds)
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));  %dirinf=pumping direction = infuse
    wait(100);
    fprintf(s1,([num2str(i) 'phn02'])); %BEGINNING OF PHASE 2 (when subject is actually receiving the liquid)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));  %dispenses at a rate of 15 mm (max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.75']));  %volume to be dispensed is .75 (a/3 x 60 = 15, resolve for .75) over 3 seconds
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));
    wait(100);
    fprintf(s1,([num2str(i) 'phn03']));   %BEGINNING OF PHASE 3 (withdraw liquid to prevent any drippage)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm'])); %WITHDRAW AT THE MAXIMUM RATE
    wait(100);
    fprintf(s1,([num2str(i) 'vol.5']));
    wait(100);
    fprintf(s1,([num2str(i) 'dirwdr'])); % direction withdraw
    wait(100);
    fprintf(s1,([num2str(i) 'phn04']));  %  begin phase 4 (stop)
    wait(100);
    fprintf(s1,([num2str(i) 'funstp'])); % stop pump
i=2;
    fprintf(s1,([num2str(i) 'dia26.59']));  %syringe inner diameter
    wait(100);
    fprintf(s1,([num2str(i) 'phn01']));  %BEGINNING OF PHASE 1 (before subject receives liquid, infuse to get the liquid to the end of the tube)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat'])); %function pumpint rate
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));   %ml per hour converted into ml per minute (15mm equal to max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.2']));  %volume to be dispensed (takes Xseconds)
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));  %dirinf=pumping direction = infuse
    wait(100);
    fprintf(s1,([num2str(i) 'phn02'])); %BEGINNING OF PHASE 2 (when subject is actually receiving the liquid)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));  %dispenses at a rate of 15 mm (max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.75']));  %volume to be dispensed is .75 (a/3 x 60 = 15, resolve for .75) over 3 seconds
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));
    wait(100);
    fprintf(s1,([num2str(i) 'phn03']));   %BEGINNING OF PHASE 3 (withdraw liquid to prevent any drippage)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm'])); %WITHDRAW AT THE MAXIMUM RATE
    wait(100);
    fprintf(s1,([num2str(i) 'vol.5']));
    wait(100);
    fprintf(s1,([num2str(i) 'dirwdr'])); % direction withdraw
    wait(100);
    fprintf(s1,([num2str(i) 'phn04']));  %  begin phase 4 (stop)
    wait(100);
    fprintf(s1,([num2str(i) 'funstp'])); % stop pump
i=3;
    fprintf(s1,([num2str(i) 'dia26.59']));  %syringe inner diameter
    wait(100);
    fprintf(s1,([num2str(i) 'phn01']));  %BEGINNING OF PHASE 1 (before subject receives liquid, infuse to get the liquid to the end of the tube)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat'])); %function pumpint rate
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));   %ml per hour converted into ml per minute (15mm equal to max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.2']));  %volume to be dispensed (takes Xseconds)
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));  %dirinf=pumping direction = infuse
    wait(100);
    fprintf(s1,([num2str(i) 'phn02'])); %BEGINNING OF PHASE 2 (when subject is actually receiving the liquid)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));  %dispenses at a rate of 15 mm (max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.75']));  %volume to be dispensed is .75 (a/3 x 60 = 15, resolve for .75) over 3 seconds
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));
    wait(100);
    fprintf(s1,([num2str(i) 'phn03']));   %BEGINNING OF PHASE 3 (withdraw liquid to prevent any drippage)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm'])); %WITHDRAW AT THE MAXIMUM RATE
    wait(100);
    fprintf(s1,([num2str(i) 'vol.5']));
    wait(100);
    fprintf(s1,([num2str(i) 'dirwdr'])); % direction withdraw
    wait(100);
    fprintf(s1,([num2str(i) 'phn04']));  %  begin phase 4 (stop)
    wait(100);
    fprintf(s1,([num2str(i) 'funstp'])); % stop pump
i=4;
    fprintf(s1,([num2str(i) 'dia26.59']));  %syringe inner diameter
    wait(100);
    fprintf(s1,([num2str(i) 'phn01']));  %BEGINNING OF PHASE 1 (before subject receives liquid, infuse to get the liquid to the end of the tube)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat'])); %function pumpint rate
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));   %ml per hour converted into ml per minute (15mm equal to max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.2']));  %volume to be dispensed (takes Xseconds)
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));  %dirinf=pumping direction = infuse
    wait(100);
    fprintf(s1,([num2str(i) 'phn02'])); %BEGINNING OF PHASE 2 (when subject is actually receiving the liquid)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm']));  %dispenses at a rate of 15 mm (max rate)
    wait(100);
    fprintf(s1,([num2str(i) 'vol.75']));  %volume to be dispensed is .75 (a/3 x 60 = 15, resolve for .75) over 3 seconds
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf']));
    wait(100);
    fprintf(s1,([num2str(i) 'phn03']));   %BEGINNING OF PHASE 3 (withdraw liquid to prevent any drippage)
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm'])); %WITHDRAW AT THE MAXIMUM RATE
    wait(100);
    fprintf(s1,([num2str(i) 'vol.5']));
    wait(100);
    fprintf(s1,([num2str(i) 'dirwdr'])); % direction withdraw
    wait(100);
    fprintf(s1,([num2str(i) 'phn04']));  %  begin phase 4 (stop)
    wait(100);
    fprintf(s1,([num2str(i) 'funstp'])); % stop pump
%end;
fclose(s1);