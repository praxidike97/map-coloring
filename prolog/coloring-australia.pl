map_coloring(WA, NT, SA, NSW, V, Q, T, ACT) :-
     diffx(WA, NT), diffx(WA, SA), diffx(NT, SA), diffx(NT, Q), diffx(Q, SA),
     diffx(Q, NSW), diffx(NSW, SA), diffx(NSW, V), diffx(V, SA), diffx(T, V), diffx(ACT, NSW).

diffx(A, B) :- diff(A, B).
diffx(A, B) :- diff(B, A).

diff(blue, red).
diff(blue, green).
diff(blue, yellow).

diff(green, red).
diff(green, yellow).

diff(red, yellow).
