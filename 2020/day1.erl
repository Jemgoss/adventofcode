-module(day1).
-export([runparts/0]).

part1([], _) ->
  invalid;
part1([_E | Tail], []) ->
  part1(Tail, Tail);
part1(Search = [E | _], [A | Rest]) ->
  case E + A of
    2020 ->
      {E, A};
    _ ->
      part1(Search, Rest)
  end.

part2([], _,_) ->
  invalid;
part2([_E | Tail], [], Third) ->
  part2(Tail, Tail, Third);
part2(First, [_ | Tail], []) ->
  part2(First, Tail, Tail);
part2(Search = [E | _], Second = [A | _Rest], [B | BRest]) ->
  case E + A + B of
    2020 ->
      {E, A, B};
    _ ->
      part2(Search, Second, BRest)
    end.

runparts() ->
  {ok, BinaryContents} = file:read_file("1.input"),
  Data = [binary_to_integer(A) || A <- re:split(BinaryContents, <<"\n">>), A =/= <<>>],

  {A1, B1} = part1(Data, Data),
  io:fwrite("~p * ~p = ~p~n", [A1, B1, A1 * B1]),

  {A2, B2, C2} = part2(Data, Data, Data),
  io:fwrite("~p * ~p * ~p = ~p~n", [A2, B2, C2, A2 * B2 * C2]).
