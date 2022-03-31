## Overall Program loop:
- if __INCLUDE_LEVEL__ == 0:
	+ setup rom.
- if __INCLUDE_LEVEL__ > 12: 
	+ do state transitions .
- else: 
	+ if S != 1: re-include file.
	+ if S != 1: re-include file.
- if __INCLUDE_LEVEL__ == 0:
	+ if S != -1:
		* ERROR: "Failed to execute program".
	+ else:
		* print: "Key valid. Enjoy your program!"

## ROM
- format= 'ROM_' + address + '_' + bit offset[0-7].
- address 00000000_0 to 01011010_7 are random bits.
- address 10000000_0 to 10011010_7 are flag bits.

- _LD and LD are Macro functions and map address + offset to a bit.
- l, _MA and MA are macro functions and calculate address using 8 input bits(l[0-7]).

## After ROM creation:

###  Functions:
- simple toggle.
- double if statements toggle(snake)(deterministic).
- deep if statement toggle(triangle).
- address calculation functions.

### State transitions:

#### **TODO: check which states are deterministic.**
#### **TODO: bundle deterministic states.**

1) S==0:
	1) set S to 24.
2) S==1:
	1) set S to 2.
3) S==2:
	1) set S to 3.
4) S==3:
	1) set S to 4.
5) S==4:
	1) set S to 5.
6) S==5:
	1) set S to 6.
	2) if R[0-7] undefined, set S to 38.
7) S==6:
	1) set S to 7
8) S==7:
	1) set S to 8.
	2) if R[0-7] undefined, set S to 59.
9) S==8:
	1) set S to 9.
10) S==9:
	1) set S to 10.
	2) if R[0-7] undefined, set S to 59.
11) S==10:
	1) set S to 11.
	2) ERROR: "BUG".
12) S==11:
	1) set S to -1.
13) S==12:
	1) set S to 13.
14) S==13:	
	1) set S to 14.
15) S==14:
	1) set S to 15.
	2) if X[0-7] undefined, set S to 22.
16) S==15:
	1) set S to 16.
17) S==16:
	1) set S to 17.
18) S==17:
	1) set S to 18.
	2) if Z[0-7] undefined, set S to 19.
19) S==18:
	1) set S to 19.
20) S==19:
	1) set S to 20.
21) S==20:
	1) set S to 21.
22) S==21:
	1) set S to 14.
23) S==22:
	1) set S to 23.
24) S==23:
	1) set S to 1.
25) S==24:
	1) set S to 25.
26) S==25:
	1) set S to 26.
27) S==26:
	1) set S to 27.
28) S==27:
	1) set S to 28.
29) S==28:
	1) set S to 29.
30) S==29:
	1) set S to 30
31) S==30:
	1) set S to 31
32) S==31:
	1) set S to 32.
	2) if B[0-7] undefined, set S to 56.
33) S==32:
	1) set S to 33.
34) S==33:
	1) set S to 34.
35) S==34:
	1) set S to 35.
	2) CALCULATION STATE.
36) S==35:
	1) set S to 36.
	2) CALCULATION STATE.
37) S==36:
	1) set S to 37.
38) S==37:
	1) set S to 12.
39) S==38:
	1) set S to 39.
40) S==39:
	1) set S to 40.
41) S==40:
	1) set S to 41.
42) S==41:
	1) set S to 42.
43) S==42:
	1) set S to 43.
44) S==43:
	1) set S to 44.
45) S==44:
	1) set S to 45.
46) S==45:
	1) set S to 46.
	2) CALCULATION STATE.
47) S==46:
	1) set S to 47.
48) S==47:
	1) set S to 48.
49) S==48:
	1) set S to 49.
50) S==49:
	1) set S to 50.
51) S==50:
	1) set S to 51.
	2) CALCULATION STATE.
52) S==51:
	1) set S to 52.
53) S==52:
	1) set S to 53.
54) S==53:
	1) set S to 54.
55) S==54:
	1) set S to 55.
56) S==55:
	1) set S to 29.
57) S==56:
	1) set S to 57.
	2) if Q[0-7] undefined, set S to 58.
58) S==57:
	1) set S to 58.
	2) ERROR "INVALID_FLAG".
59) S==58:
	1) set S to -1.
	

