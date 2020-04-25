main(WA, NT, SA, NSW, V, Q, T) :-
     diffx(WA, NT), diffx(WA, SA), diffx(NT, SA), diffx(NT, Q), diffx(Q, SA),
     diffx(Q, NSW), diffx(NSW, SA), diffx(NSW, V), diffx(V, SA), diffx(T, V).

diffx(A, B) :- diff(A, B).
diffx(A, B) :- diff(B, A).

diff(blau, rot).
diff(blau, gruen).
diff(blau, gelb).

diff(gruen, rot).
diff(gruen, gelb).

diff(rot, gelb).
