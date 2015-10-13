% shortmilk
% modified from milkshake1
% ksb 3/2013

% Soda Event Types:
%    0 - milkshake image + regular soda taste (CS+paired)
%    1 - water image + tasteless solution taste (CS+paired)

% milkshake PUMPS
% 0 = tasteless
% 1 = milkshake

% milkshake soa1 and soa2 are selected from a discrete uniform distribution of 1 to 7
% second

% milkshake order array holds the trial type as event type table above
% the number if examples of each type is as follows
% 0 - 15 trials
% 1 - 15 trials


% -------------Parameter & Initialization Section----------------

%Mindinghealth 
clear;
version = '3/27/13'; 
%outputPath='C:\Documents and Settings\rayv\Kyle\';
%outputPath='D:\Documents and Settings\sticelab\My Documents\shortmilk\';
outputPath='C:\Users\kyleb\Desktop\paradigms\shake\';

initPeriod = 4000;         % blank period to wait.
numTrials=30;              %number of trials
state = 773;               %rand num gen 'seed' so every subject gets the same order



% Set up correct handles for visual and audio cues

regularPic = [outputPath 'shake.jpg'];
waterPic = [outputPath 'water.jpg'];
fixPic = [outputPath 'fixation.bmp'];
noImagePic = [outputPath 'noimage.bmp'];

% ---------------------------------------------------------------

% set up pumps parameters
s1=serial('com1','baudrate',19200,'databits',8,'terminator',13);
fopen(s1);

% set up cogent parameters
config_display(0,3,[1 1 1],[0 0 0],'Arial',48,7,0);
config_keyboard;
config_sound(1,8,22050,1);

% Get user input to configure a results file (but save as .log). This is where 
% stimulus onsets will be stored
[fname, pname] = uiputfile('*.log','Save log file as...'); 

% This line is to remove any extension the user might have
% added to the name.
[pname, fname, ext] = fileparts(fullfile(pname,fname));

config_results(fullfile(pname,[fname,'.log']));

n=2;
for f=1:15
    order(f)=0;
    order(f+15)=1;
    n=n+1;
end;

rand('state', state);
randn('state', state);
order=ShuffleIt(order);                   % mix trial types
soa1 = unidrnd(3,1,numTrials);          % discrete uniform distr for interval 1  (1 to 3 before trigger the pump)
soa2 = unidrnd(8,1,numTrials)          % discrete uniform distr for interval 2  (1 to 7)

soa1=soa1 * 1000;     %convert sec to msec
soa2=soa2 * 1000;

picon=0;                  % init some vars
beginpump=0;
taste_onset=0;
picoff=0;
rinse_onset=0;
swallowRinseTime=0;
endtrial=0;

picDur=2000;      % time picture is on
pumpDur=5000;       % period for pump period after 5000 taste onset (pump period = 10000)
swallowDur=1000;    % how long word "swallow" is on
timeToTaste=4000;   % time after pump on until taste (we calculated it by watching pumps drip)

% Get the subject number
subj = inputdlg('Enter the subject number');
drawnow


% ---------------------Program Run Section----------------------

% ---Start Cogent---
start_cogent;

%prepare visual buffers
loadpict(fixPic,1);       % fixation screen
preparestring('Wait for trigger to begin',2);
preparestring('Swallow',3);
loadpict(regularPic,4);     %regular milkshake
loadpict(waterPic,5);    %water
loadpict(noImagePic,6);    %nothing
preparestring('The End',7);


% Label Results record with subject's #, the date, the script run, and data file used
% Make column headers in Results
addresults('Subject: ', subj{1});
addresults(datestr(now,0));
addresults(mfilename,strcat('version: ', version));   % name of current script
%addresults(reward_antdata);
addresults('');
str = sprintf('ordernum\ttype\tpicon\tpicoff\tbeginpump\tTaste_onset\tswallow\trinse_onset\tswallowRinseTime\tendtrial');
addresults(str);

% Draw preparatory screen and wait for trigger (5) from scanner
clearkeys;
drawpict(2);
waitkeydown(inf, 62);                     % wait for trigger
drawpict(1);    %draw blank screen

t=time;

% EXIT ROUTINE. IF ESC KEY IS PRESSED SCRIPT IS ABORTED
waituntil(t);
readkeys;
[key,kt]=getkeydown;
if~isempty(key)
    if key == 52
        stop_cogent
        fprintf('\nSCRIPT ABORTED BY USER !!!!!\n');
       fclose(s1);
        return
    end
end


%reset the global timer at 0 after trigger
cogstd('sgettime',0);  
waituntil(initPeriod);    % wait baseline period


%taste delivery instructions
for i=1:length(order)  %i=the trial you're on, beginning with the first trial and continuing through the rest of the trials
        
    t0=time;    %t0 represents the beginning of each trial not including dummy time

    % deliver taste cue shape    
    if order(i)==0
        drawpict(4); 
        picon=time;
    elseif order(i)==1
        drawpict(5); 
        picon=time;
    elseif order(i)==2
        drawpict(4);
        picon=time;
    elseif order(i)==3
        drawpict(5);
        picon=time;
    elseif order(i)==4
        drawpict(1);
        picon=time;
    end

    waituntil(t0+picDur);                  %wait for pic off time with picture on (picdur)
    drawpict(1);                             %pic off
    picoff=time;                             %keep pic off time
    waituntil(picoff+soa1(i));          %wait first "jitter" time
    
    if order(i)<2                % taste is 0, 1
        if order(i)==0           % 0=image+milkshake 
            pump=1;
        elseif order(i)==1       % 1=image+tasteless 
            pump=0; 
        end
        fprintf(s1,[num2str(pump(1)) 'run']);   % pump on     
        beginpump=time;
        waituntil(beginpump+timeToTaste);          % wait for taste_onset
        taste_onset=time;
        waituntil(taste_onset+pumpDur);           %finish pump period
        drawpict(3);                              %swallow
        swallowtime=time;
        waituntil(swallowtime+swallowDur);
        drawpict(1);                               %fix on
        swallowOffTime=time;
if order(i)==0           % 0=image+milkshake so will give tastless to rinse
 reportit=9999
    pump=0; 
    fprintf(s1,[num2str(pump(1)) 'run']);   % pump on     
    beginRinsepump=time;
    waituntil(beginRinsepump+timeToTaste);          % wait for taste_onset
    rinse_onset=time;
    waituntil(rinse_onset+pumpDur+1000);           %finish pump period
    drawpict(3);                              %swallow
    swallowRinseTime=time;
    waituntil(swallowRinseTime+swallowDur);
    drawpict(1);                               %fix on
    swallowRinseOffTime=time;
    waituntil(swallowRinseOffTime+soa2(i));   %wait 2nd jitter and then end trial 
    endtrial=time;
else
     waituntil(swallowOffTime+soa2(i));   %wait 2nd jitter and then end trial 
     endtrial=time;
end
        
        
    else                                         % no pump no taste is 2 and 3 and 4
        beginpump=time;                     % beginning of pump period
        waituntil(beginpump+timeToTaste);          % wait 1000 ms for taste_onset -- no taste but period is the same
        taste_onset=time;
        waituntil(taste_onset+pumpDur);           %finish pump period
        swallowtime=time;                       % is end of pump period in these condtions
        waituntil(swallowtime+soa2(i));   %wait 2nd jitter and then end trial 
        endtrial=time;
    end
% EXIT ROUTINE. IF ESC KEY IS PRESSED SCRIPT IS ABORTED
readkeys;
[key,kt]=getkeydown;
if~isempty(key)
    if key == 52
        stop_cogent
        fprintf('\nSCRIPT ABORTED BY USER !!!!!\n')
        fclose(s1);
        return
    end
end 
t2=time;
str2=sprintf('%-g\t%-g\t%-g\t%-g\t%-g\t%-g\t%-g\t%-g\t%-g\t%-g',i,order(i),picon,picoff,beginpump,taste_onset,swallowtime,rinse_onset,swallowRinseTime,endtrial);
addresults(str2);
clearkeys;        
end %end for loop

%end
% add pause to end program
% ---The End---
% ---Stop Cogent---

drawpict(7);    %the end
waitkeydown(inf);
stop_cogent;
fclose(s1);


 
