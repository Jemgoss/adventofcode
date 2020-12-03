-module(aoc1).
-export([runparts/0]).

comb(0, _) ->
	[[]];
comb(_, []) ->
	[];
comb(N, [H | T]) ->
	[[H | L] || L <- comb(N-1, T)] ++ comb(N, T).

runparts() ->
	{ok, BinaryContents} = file:read_file("1.input"),
	Data = [binary_to_integer(A) || A <- re:split(BinaryContents, <<"\n">>), A =/= <<>>],

	% Part 1
	{value, [A1, B1]} = lists:search(fun([A,B]) -> A + B =:= 2020 end, comb(2, Data)),
	io:fwrite("~p * ~p = ~p~n", [A1, B1, A1 * B1]),

	% Part 2
	{value, [A2, B2, C2]} = lists:search(fun([A,B,C]) -> A + B + C =:= 2020 end, comb(3, Data)),
	io:fwrite("~p * ~p * ~p = ~p~n", [A2, B2, C2, A2 * B2 * C2]).
