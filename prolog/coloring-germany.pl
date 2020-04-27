main(BB, BE, BW, BY, HB, HE, HH, MV, NI, NW, RP, SH, SL, SN, ST, TH) :-
     diffx(BB, BE), diffx(BB, MV), diffx(BB, SN), diffx(BB, NI), diffx(BB, ST), diffx(BW, BY),
     diffx(BW, HE), diffx(BW, RP), diffx(BY, HE), diffx(BY, TH), diffx(BY, SN), diffx(HB, NI),
     diffx(HE, NI), diffx(HE, NW), diffx(HE, RP), diffx(HE, TH), diffx(HH, NI), diffx(HH, SH),
     diffx(MV, SH), diffx(MV, NI), diffx(NI, SH), diffx(NI, NW), diffx(NI, TH), diffx(NI, ST),
     diffx(NW, RP), diffx(RP, SL), diffx(SN, ST), diffx(SN, TH), diffx(ST, TH).

diffx(A, B) :- diff(A, B).
diffx(A, B) :- diff(B, A).

diff(blau, rot).
diff(blau, gruen).
diff(blau, gelb).

diff(gruen, rot).
diff(gruen, gelb).

diff(rot, gelb).
