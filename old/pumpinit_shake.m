% set up pumps parameters
% there are three phases that are specified:
% phase 1: push liquid to end of tube
% phase 2: dispense liquid in specfic rate and volume
% phase 3: pull liquid back up
% the liquid is pulled back up (phase 3) so that it won't drip from the manifold, and
% so the subject can't suck it out. As such, phase 1 is needed to push the
% liquid back to the outflow point.
% volume and dispense rate can be changed. Use the following formula:
% rate= volume/sec * 60
% example: .5/4 x 60 (deliver .5 ml over a 4 sec duration)=7.5


s1=serial('com1','baudrate',19200,'databits',8,'terminator',13);
fopen(s1);
%for i=0:1
i=0;
    fprintf(s1,([num2str(i) 'dia26.59']));
	wait(100);
	fprintf(s1,([num2str(i) 'phn01'])); % specify phase 1 parameters
	wait(100);
	fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm'])); %rate
    wait(100);
    fprintf(s1,([num2str(i) 'vol0.7'])); %volume
	wait(100);
	fprintf(s1,([num2str(i) 'dirinf'])); %push out
	wait(100);
	fprintf(s1,([num2str(i) 'phn02'])); %specify phase 2 parameters
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
	fprintf(s1,([num2str(i) 'rat7.5mm'])); %dispensing .5mm over 4 seconds
	wait(100);
    fprintf(s1,([num2str(i) 'vol.5']));
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf'])); % push out
    wait(100);
    fprintf(s1,([num2str(i) 'phn03'])); %specify phase 3 parameters
    wait(100);
	fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
	fprintf(s1,([num2str(i) 'rat15mm']));
    wait(100);
	fprintf(s1,([num2str(i) 'vol0.7']));
    wait(100);
	fprintf(s1,([num2str(i) 'dirwdr'])); % retract
    wait(100);
	fprintf(s1,([num2str(i) 'phn04']));
    wait(100);
	fprintf(s1,([num2str(i) 'funstp']));

i=1;
    fprintf(s1,([num2str(i) 'dia26.59']));
	wait(100);
	fprintf(s1,([num2str(i) 'phn01'])); % specify phase 1 parameters
	wait(100);
	fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
    fprintf(s1,([num2str(i) 'rat15mm'])); %rate
    wait(100);
    fprintf(s1,([num2str(i) 'vol1.0'])); %volume
	wait(100);
	fprintf(s1,([num2str(i) 'dirinf'])); %push out
	wait(100);
	fprintf(s1,([num2str(i) 'phn02'])); %specify phase 2 parameters
    wait(100);
    fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
	fprintf(s1,([num2str(i) 'rat7.5mm'])); %dispensing .5mm over 4 seconds
	wait(100);
    fprintf(s1,([num2str(i) 'vol.5']));
    wait(100);
    fprintf(s1,([num2str(i) 'dirinf'])); % push out
    wait(100);
    fprintf(s1,([num2str(i) 'phn03'])); %specify phase 3 parameters
    wait(100);
	fprintf(s1,([num2str(i) 'funrat']));
    wait(100);
	fprintf(s1,([num2str(i) 'rat15mm']));
    wait(100);
	fprintf(s1,([num2str(i) 'vol1.0']));
    wait(100);
	fprintf(s1,([num2str(i) 'dirwdr'])); % retract
    wait(100);
	fprintf(s1,([num2str(i) 'phn04']));
    wait(100);
	fprintf(s1,([num2str(i) 'funstp']));
%end;
fclose(s1);