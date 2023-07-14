# 10 PRINT"ASET-B  VERSION 1.0   WRITTEN BY W.D. WALTON  1985"
# 20 PRINT"CONTRIBUTION OF THE NATIONAL BUREAU OF STANDARDS (U.S.)."
# 30 PRINT"NOT SUBJECT TO COPYRIGHT."
print("ASET-B  VERSION 1.0   WRITTEN BY W.D. WALTON  1985")
print("CONTRIBUTION OF THE NATIONAL BUREAU OF STANDARDS (U.S.).")
print("NOT SUBJECT TO COPYRIGHT.")

# 40 DIM TQ(100),Q(100)
# 50 INPUT"ENTER RUN TITLE";TITLE$
# 60 LR=.35
tq = [0]*100
q = [0]*100
lr = 0.35

# 70 INPUT"HEAT LOSS FRACTION";LC
# 80 INPUT"FIRE HEIGHT (ft)";F
# 90 INPUT"ROOM CEILING HEIGHT (ft)";H
# 100 INPUT"ROOM FLOOR AREA (sq ft)";A
title = input("ENTER RUN TITLE: ")
lc = float(input("HEAT LOSS FRACTION: "))
f = float(input("FIRE HEIGHT (ft): "))
h = float(input("ROOM CEILING HEIGHT (ft): "))
a = float(input("ROOM FLOOR AREA (sq ft): "))

# 110 FM=F*.3048
# 120 HM=H*.3048
# 130 AM=A*.0929
fm = f * 0.3048
hm = h * 0.3048
am = a * 0.0929

# 140 INPUT"MAXIMUM TIME (sec)";TL
tl = float(input("MAXIMUM TIME (sec): "))

# 150 Q0=.1
q0 = 0.1

# 160 PRINT"INPUT FIRE TIMES AND HEAT RELEASE RATES (use -9,-9 to end input)"
print("INPUT FIRE TIMES AND HEAT RELEASE RATES (use -9,-9 to end input)")

# 170 FOR N=1 TO 100
for n in range(1, 100):
    # 180 INPUT"TIME (sec), HEAT RELEASE RATE (kW)";TQ(N),QI
    tq[n], qi = map(float, input("TIME (sec), HEAT RELEASE RATE (kW): ").split(","))
    
    # 190 IF TQ(N) < 0 GOTO 240
    if tq[n] < 0:
        break
    
    # 200 IF QI < Q0 THEN Q(N)=Q0
    if qi < q0:
        q[n] = q0
    else:
        # 210 Q(N)=QI/Q0
        q[n] = qi / q0
    
    # End for
    # 220 NEXT N
    
else:
    # 230 PRINT"MAXIMUM OF 100 INPUT VALUES REACHED"
    print("MAXIMUM OF 100 INPUT VALUES REACHED")


# 240 NQ=N-1
nq = n - 1

# 250 IF TQ(1)<.1 THEN TQ(1)=.1
if tq[1] < 0.1:
    tq[1] = 0.1

# 260 PA=530!
# 270 DA=.0735
# 280 CP=.24
pa = 530
da = 0.0735
cp = 0.24

# 290 C1=(1!-LC)*Q0/(DA*CP*PA*A*1.054)
# 300 C2=.21/A*((1!-LR)*Q0*32!/(DA*CP*PA*1.054))^(1!/3!)
c1 = (1 - lc) * q0 / (da * cp * pa * a * 1.054)
c2 = 0.21 / a * ((1 - lr) * q0 * 32 / (da * cp * pa * 1.054))**(1/3)

# 310 DQ0=(Q(1)-1!)/TQ(1)
dq0 = (q[1] - 1) / tq[1]

# 320 Z0=H-F
# 330 Z1=Z0
z0 = h - f
z1 = z0

# 340 DZ1=-C1-C2*Z0^(5!/3!)
# 350 P1=1!+C1/C2*Z0^(-5!/3!)
# 360 DP1=C1/C2*(2!*DQ0+5!*(C1+C2*Z0^(5!/3!)))/(6!*Z0^(8!/3!))
dz1 = -c1 - c2 * z0**(5/3)
p1 = 1 + c1 / c2 * z0**(-5/3)
dp1 = c1 / c2 * (2 * dq0 + 5 * (c1 + c2 * z0**(5/3))) / (6 * z0**(8/3))

# 370 T1=0!
# 380 T2=0!
# 390 DT=1!
# 400 QT=1!
# 410 OI=5!
# 420 OT=0!
t1 = 0
t2 = 0
dt = 1
qt = 1
oi = 5
ot = 0

# 430 PRINT" "
# 440 PRINT"ASET-B  VERSION 1.0"
# 450 PRINT TITLE$
# 460 PRINT"HEAT LOSS FRACTION=";LC
# 470 PRINT"FIRE HEIGHT=";F;"ft   ";FM;"m"
# 480 PRINT"ROOM HEIGHT=";H;"ft   ";HM;"m"
# 490 PRINT"ROOM AREA=";A;"sq ft   ";AM;"sq m"
# 500 PRINT" "
# 510 PRINT"    TIME      TEMP      TEMP     LAYER     LAYER      FIRE      FIRE"
# 520 PRINT"     sec         F         C        ft         m        kW     BTU/s"
print()
print("ASET-B  VERSION 1.0")
print(title)
print(f"HEAT LOSS FRACTION= {lc:1.1f}")
print(f"FIRE HEIGHT= {f:1.0f} ft    {fm:.4f} m")
print(f"ROOM HEIGHT= {h:1.0f} ft    {hm:.4f} m")
print(f"ROOM AREA= {a:1.0f} sq ft   {am:.4f} sq m")
print()
print("    TIME      TEMP      TEMP     LAYER     LAYER      FIRE      FIRE")
print("     sec         F         C        ft         m        kW     BTU/s")

def sub880():
    global qt
    # 880 IF T2>TQ(1) GOTO 910
    if t2 <= tq[0]:
        # 890 QT=Q(1)-((Q(1)-1!)/TQ(1))*(TQ(1)-T2)
        qt = q[0] - ((q[0] - 1) / tq[0]) * (tq[0] - t2)
        
        # 900 RETURN 
        return
    
    # 910 FOR N=1 TO NQ
    for n in range(0, nq + 1):
        # 920 IF T2>TQ(N) GOTO 950
        if t2 <= tq[n]:
            # 930 QT=Q(N)-((Q(N)-Q(N-1))/(TQ(N)-TQ(N-1)))*(TQ(N)-T2)
            qt = q[n] - ((q[n] - q[n-1]) / (tq[n] - tq[n-1])) * (tq[n] - t2)
            
            # 940 RETURN
            return
    
        # End for
        # 950 NEXT N
    
    # 960 RETURN
    return

def sub970():
    global ot
    # 970 IF T2<OT THEN RETURN
    if t2 < ot:
        return
    
    # 980 OT=OT+OI
    ot += oi
    
    # 990 QK=QT*Q0
    # 1000 QB=QK*.9485
    qk = qt * q0
    qb = qk * 0.9485
    
    # 1010 PF=(P1*PA)-460!
    # 1020 PC=(PF-32!)/1.8
    pf = (p1 * pa) - 460
    pc = (pf - 32) / 1.8
    
    # 1030 RRF=DP1*31800!
    # 1040 RRC=RRF/1.8
    rrf = dp1 * 31800
    rrc = rrf / 1.8
    
    # 1050 X=Z1+F
    # 1060 XM=X*.3048
    x = z1 + f
    xm = x * 0.3048
    
    # 1070 PRINT USING"######.#  ";T2;PF;PC;X;XM;QK;QB
    print(f"{t2:8.1f}  {pf:8.1f}  {pc:8.1f}  {x:8.1f}  {xm:8.1f}  {qk:8.1f}  {qb:8.1f}")
    
    # 1080 RETURN

# 530 GOSUB 970
sub970()

while True:
    # 540 T1=T2
    # 550 T2=T1+DT
    t1 = t2
    t2 = t1 + dt
    
    # 560 IF T2>TL THEN PRINT"RUN COMPLETE":GOTO 870
    if t2 > tl:
        print("RUN COMPLETE")
        break
    
    # 570 IF T2>TQ(NQ) THEN PRINT"END OF INPUT FIRE":GOTO 870
    if t2 > tq[nq]:
        print("END OF INPUT FIRE")
        break
    
    
    
    # 580 GOSUB 880
    sub880()

    # 590 Z2=Z1+DZ1*DT
    # 600 P2=P1+DP1*DT
    # 610 IER=0
    z2 = z1 + dz1 * dt
    p2 = p1 + dp1 * dt
    ier = 0
    
    while True:
        # 620 IF Z2<=0! GOTO 670
        if z2 <= 0:
            # 670 DP2=(P2*C1*QT)/(Z0-Z2)
            dp2 = (p2 * c1 * qt) / (z0 - z2)
            
            # 680 IF Z2<=-F GOTO 710
            if z2 <= -f:
                # 710 DZ2=0!
                dz2 = 0
            else:
                # 690 DZ2=-C1*QT
                dz2 = -c1 * qt
                
                # End if
                # 700 GOTO 720
                
        else:
            # 630 K=C2*QT^(1!/3!)*Z2^(5!/3!)
            # 640 DZ2=-C1*QT-K
            # 650 DP2=P2*(C1*QT-(P2-1!)*K)/(Z0-Z2)
            k = c2 * qt**(1/3) * z2**(5/3)
            dz2 = -c1 * qt - k
            dp2 = p2 * (c1 * qt - (p2 - 1) * k) / (z0 - z2)
            
            # End if
            # 660 GOTO 720
            
        
        # 720 Z2C=Z1+(DZ1+DZ2)/2!*DT
        # 730 P2C=P1+(DP1+DP2)/2!*DT
        z2c = z1 + (dz1 + dz2) / 2 * dt
        p2c = p1 + (dp1 + dp2) / 2 * dt
        
        # 740 IF Z2C<-F THEN Z2=-F:Z2C=-F
        if z2c < -f:
            z2 = -f
            z2c = -f
        
        # 750 IF ABS(Z2C-Z2)<.001 AND ABS(P2C-P2)<.001 GOTO 810
        if abs(z2c - z2) < 0.001 and abs(p2c - p2) < 0.001:
            break
        
        # 760 IF IER>30 THEN PRINT"WARNING! SOLUTION DID NOT CONVERGE":GOTO 810
        if ier > 30:
            print("WARNING! SOLUTION DID NOT CONVERGE")
            break
        
        # 770 Z2=Z2C
        # 780 P2=P2C
        # 790 IER=IER+1
        z2 = z2c
        p2 = p2c
        ier += 1
        
        # End while
        # 800 GOTO 620
        
    # 810 Z1=Z2C
    # 820 P1=P2C
    # 830 DZ1=DZ2
    # 840 DP1=DP2
    z1 = z2c
    p1 = p2c
    dz1 = dz2
    dp1 = dp2
    
    # 850 GOSUB 970
    sub970()
    
    # End while
    # 860 GOTO 540 
    
# End of program
# 870 END


