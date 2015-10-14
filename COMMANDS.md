#Commands 

 ```txt
'dia26.59'         % set diameter to 26.59mm       

'phn01'            % specify phase 1 parameters
'funrat'          
'rat15mm'          % rate
'vol0.7'           % volume
'dirinf'           % push out

'phn02'            % specify phase 2 parameters
'funrat'          
'rat7.5mm'         % dispensing .5mm over 4 seconds
'vol.5'         
'dirinf'           % push out

'phn03'            % specify phase 3 parameters
'funrat'          
'rat15mm'         
'vol0.7'          
'dirwdr'           % retract

'phn04'         
'funstp'         
```

```
    .Settings = "9600,n,8,1"
    .CommPort = 1
    .RThreshold = 1 'read data per char
    .SThreshold = 0 'send all data at once
    .PortOpen = True
```