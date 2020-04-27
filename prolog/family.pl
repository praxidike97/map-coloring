:- discontiguous male/1, female/1, parent/2.

male(henry).

male(dick).
female(mary).

male(michael).

parent(michael, mary).
parent(michael, dick).
parent(dick, henry).


father(X, Y) :- male(Y), parent(X, Y).
mother(X, Y) :- female(Y), parent(X, Y).

grandfather(X, Z) :- male(Y), parent(X, Y), male(Z), parent(Y, Z).